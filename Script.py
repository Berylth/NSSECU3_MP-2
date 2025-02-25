import subprocess
import pandas as pd

def EvtxeCmd(args):
    """Run EvtxECmd to parse EVTX files."""
    filename = "Evtxe_output.csv"
    command = [args[0], '-f', args[1], '--csv', args[2], '--csvf', filename] # Create the command
    subprocess.run(command, check=True) # Run program

    return

def RecentFileCacheParser(args):
    """Run RecentFileCacheParser to parse the .bcf files."""
    filename = "RecentFileCache_output.csv"
    command = [args[0], '-f', args[1], '--csv', args[2], '--csvf', filename] # Create the command
    subprocess.run(command, check=True) # Run program

    return

def SBECmd(args):
    """Run SBECmd to parse Shellbags data."""
    filename = "SBECmd_output.csv"
    command = [args[0], '-d', args[1], '--csv', args[2], '--csvf', filename] # Create the command
    subprocess.run(command, check=True) # Run program

    return

def CombineToolOutputs(output_dir):
    # Load CSV files
    recentfile_logs = pd.read_csv('RecentFileCache_output.csv')
    evtx_logs = pd.read_csv('Evtxe_output.csv')
    sbecmd_logs = pd.read_csv('SBECmd_output.csv')

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

    # Update input file paths
    evtx_file = "C:\\Windows\\System32\\winevt\\Logs\\System.evtx"
    recentcache_file = "C:\\Users\\4n6\\Desktop\\MP2\\Input\\RecentFileCache.bcf"
    sbe_file = ""

    # Update output directory
    output_dir = "C:\\Users\\4n6\\Desktop\\MP2\\Output\\"
    """===================================================================================="""

    # Run the tools
    EvtxeCmd([evtx_path, evtx_file, output_dir])
    RecentFileCacheParser([recentcache_path, recentcache_file, output_dir])
    #SBECmd([sbe_path, sbe_file, output_dir])

    # Combine the output of the tools
    CombineToolOutputs(output_dir)

if __name__ == "__main__":
    main()
