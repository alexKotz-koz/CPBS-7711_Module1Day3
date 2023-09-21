
# README

## Report: [Link to Report](https://docs.google.com/document/d/1WyCkMw5yXGx-AHQtY2_fggWxE8zY7hX2IQHKobqR0ds/edit)

### Installation Requirements:
- Python version 3.11
- Linux or Unix-based Operating System required to run the project using the instructions below.

### Project Info:
- This project was built using Python Conda version 23.5.2 on a Unix-based operating system.
- This project was also tested in a separate Python virtual environment using Python version 3.11.2. 

### Files in Module1Day3 directory:

- **Input.gmt.txt**: A list of the 12 known genes associated with Fanconi Anemia with their corresponding loci.

- **STRING 1.txt**: A network of connected genes and their edge weight.

- **main.py**: A Python script that generates a sub-network of genes from the Input.gmt.txt file with their corresponding edge weight (derived from the network in STRING 1.txt)

### Setup and Configuration:

- Clone the repository into a known directory on the host machine.

<hr>

## Run

1. Open an instance of the terminal.

    **Note**: If using a conda environment, please activate the conda environment prior to running the main.py file.

2. Navigate to the directory in which the project was cloned.

    Example: 
        
        cd ~\Desktop\Module1Day3\

3. Run the main.py file using a Python interpreter.

    **Note**: This project requires Python version 3.11 or higher, to run the main.py file, please ensure you are using the correct interpreter. 

    Example:

        python3 main.py
**Note**: This program should take < 1 minute to run, without any changes to the main.py file.

<hr>

## Results:

Upon successful execution, you should expect to see a new file "results.txt" in the same directory, generated by the Python script. This file contains a sub-network in STRING format. The three columns of this file are:

Source Node Gene | Destination Node Gene | Edge Weight

The "results.txt" file can be uploaded to Cytoscape (desktop application) to generate a visual representation of the sub-network. 

For more information about Cytoscape, please follow the link below:

[Cytoscape](https://cytoscape.org/what_is_cytoscape.html)
