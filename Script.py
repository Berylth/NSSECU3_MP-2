import subprocess
import pandas as pd
import os
import glob

def EvtxeCmd(args):
    """Run EvtxECmd to parse EVTX files."""
    filename = "Evtxe_output.csv"
    command = [args[0], '-f', args[1], '--csv', args[2], '--csvf', filename] # Create the command
    subprocess.run(command, check=True) # Run program

    return args[2] + filename # get path of tool output

def RecentFileCacheParser(args):
    """Run RecentFileCacheParser to parse the .bcf files."""
    filename = "RecentFileCache_output.csv"
    command = [args[0], '-f', args[1], '--csv', args[2], '--csvf', filename] # Create the command
    subprocess.run(command, check=True) # Run program

    return args[2] + filename # get path of tool output

def SBECmd(args):
    """Run SBECmd to parse Shellbags data."""
    # --csvf option doesn't work
    command = [args[0], '-d', args[1], '--csv', args[2]] # Create the command
    subprocess.run(command, check=True) # Run program

    """Identify the most recently created CSV file in the output directory."""
    list_of_files = glob.glob(os.path.join(args[2], '*.csv'))  # Get all CSV files in the directory
    if not list_of_files:
        raise FileNotFoundError("No CSV files found in the output directory.")
    latest_file = max(list_of_files, key=os.path.getctime)  # Get the most recently created file

    return latest_file

def CombineToolOutputs(output_dir, files):
    # Load csv files
    evtx_logs = pd.read_csv(files[0])
    recentfile_logs = pd.read_csv(files[1])
    sbecmd_logs = pd.read_csv(files[2])

    # Insert 'Source' column at the FIRST position for each DataFrame
    for df, source_name in zip(
        [recentfile_logs, evtx_logs, sbecmd_logs],
        ['RecentFileCache', 'EvtxCmd', 'SBECmd']
    ):
        df.insert(0, 'Source', source_name)  # Insert at position 0

    # Combine vertically (align columns automatically)
    combined_df = pd.concat([recentfile_logs, evtx_logs, sbecmd_logs], ignore_index=True)

    # Save to CSV with 'Source' as the first column
    combined_df.to_csv(output_dir + 'Combined_Forensic_Data.csv', index=False)
    
    return

def main():
    """============================== Program Configurations =============================="""
    # Update actual path of program
    evtx_path = "C:\\Users\\4n6\\Desktop\\MP2\\EvtxeCmd\\EvtxECmd.exe"
    recentcache_path = "C:\\Users\\4n6\\Desktop\\MP2\\RecentFileCacheParser\\RecentFileCacheParser.exe"
    sbe_path  = "C:\\Users\\4n6\\Desktop\\MP2\\SBECmd\\SBECmd.exe"

    # Update artifact path to be inputted
    evtx_artifact = "C:\\Users\\4n6\\Desktop\\MP2\\Input2\\Application.evtx"
    recentcache_artifact = "C:\\Users\\4n6\\Desktop\\MP2\\Input2\\RecentFileCache.bcf"
    sbe_artifact = "C:\\Users\\4n6\\Desktop\\MP2\\Input2\\"

    # Update output directory
    output_dir = "C:\\Users\\4n6\\Desktop\\MP2\\Output\\"
    """===================================================================================="""

    # Run the tools
    Evtx_output = EvtxeCmd([evtx_path, evtx_artifact, output_dir])
    RecentFile_output = RecentFileCacheParser([recentcache_path, recentcache_artifact, output_dir])
    SBECmd_output = SBECmd([sbe_path, sbe_artifact, output_dir])

    # Combine the output of the tools
    CombineToolOutputs(output_dir, [Evtx_output, RecentFile_output, SBECmd_output])

if __name__ == "__main__":
    main()