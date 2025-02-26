# NSSECU3_MP#2
Integrates the functionality of three digital forensic tools—EvtxECmd, RecentFileCacheParser, and SBECmd—into a single, unified python script. This allows all tools to be executed simultaneously, streamlining the process and combining their outputs into a cohesive result. By eliminating the delays associated with running tools individually and merging overlapping outputs, this project aims to provide cybersecurity professionals with a more efficient and user-friendly solution for analyzing digital forensic data.

## Pre-requisites / Dependencies
1) Any Code Editor such as [VSCode](https://code.visualstudio.com/)
2) [Python](https://www.python.org/downloads/)
    - Pandas  
        ```
        pip install pandas
        ```
3) [Eric Zimmerman's Tools (EZTools)](https://ericzimmerman.github.io/#!index.md)
    - EvtxECmd 
    - RecentFileCacheParser
    - SBECmd
4) WinRar or 7-Zip
5) [Microsoft .net](https://dotnet.microsoft.com/en-us/download/dotnet/9.0)

## Setup / How to Run
1) Download EZTools and unzip them using WinRar or 7-Zip.
2) Download the python script.
3) Download Microsoft .net from the website.
4) You may also download the *'Artifacts'* folder as it contains Windows 7 artifacts that can be used to run the script.
5) Open the script via a code editor. Run the code editor as administrator.
6) Modify the *"program configurations"* section.
7) Run the python script using the command:  
    ```
    python ./Script.py
    ```
8) The combined output of the tools is saved at *output_dir/Combined_Forensic_Data.csv* where output_dir is the user configured output directory.

## Members
- Garcia, Ralph Timothy D.
- Lim, Jiro Phoenix G.
- Magura, Bryle Jhone R.
- Tapia, John Lorenzo N.

## Acknowledgements
- The digital forensic tools used in this project is [EZTools](https://ericzimmerman.github.io/#!index.md), created by Eric Zimmerman. 
