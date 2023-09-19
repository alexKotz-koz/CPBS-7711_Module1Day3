
# README

### Installation Requirements:
- Python version 3.11
- Linux or Unix based Operating System required to run the project using the instructions below.

### Project Info:
- This project was built using Python Conda version 23.5.2 on a unix based operating system.
- This project was also tested in a separate Python virtual environment using python version 3.11.2. 

### Files in Module1Day3 directory:

**Input.gmt.txt**: A list of the 12 known genes associated with Fanconi Anemia with there cooresponding loci.

**STRING 1.txt**: A network of connected genes and thier coorelation measurement.

**main.py**: A python script that generates a sub-network of genes from the Input.gmt.txt file with thier cooresponding coorelation measurement (derived from the network in STRING 1.txt)

### Setup and Configuration:

- Download and extract zip folder containing the two source text files and main.py, into a known directory on host machine.

<hr>

## Run

1. Open an instance of the terminal.

**Note**: If using a conda environment, please activate the conda environment prior to running the main.py file.

2. Navigate to the directory in which the project was extracted to.

    Example: 
        
        cd ~\Desktop\Module1Day3\

3. Run the main.py file using python interpreter.

    **Note**: This project requires python version 3.11 or higher, to run the main.py file, please assure you are using the correct interpreter. 

    Example:

        python3 main.py

<hr>

## Results:

Upon successful execution, you should expect to see a new file "results.txt" in the same directory, generated by the python script. This file contains a sub-network in STRING format. The three columns of this file are:

Source Node Gene | Destination Node Gene | Coorelation

The "results.txt" file can be uploaded to Cytoscape (desktop application) to generate a visual representation of the sub-network. 

For more information about Cytoscape, please follow the link below:

[Cytoscape](https://cytoscape.org/what_is_cytoscape.html)
