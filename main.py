##PRE: Input.gmt.txt: contains the FA associated genes in an unstructured format
##POST: structured list of FA associated genes
def fanconi_anemia_genes(inputFile):
    #using lists for the original data, as we need to manipulate the content in the lists
    faData = []
    faGenes = []

    #open input file and add contents to a row (faData)
    with open(inputFile, 'r') as file:
        for row in file:
            faData.append(row.split('\t'))
    file.close()

    #iterate thru faData and remove newline character from last item in each row
    for itr in range(len(faData)):
        if '\n' in faData[itr][-1]:
            faData[itr][-1] = faData[itr][-1].strip()

    #remove the first two items in each row of faData to isolate the genes
    for itr in range(len(faData)):
        faData[itr].pop(0)
        faData[itr].pop(0)

    #add each gene from faData to a single list (faGenes)
    for row in faData:
        for item in row:
            faGenes.append(item)
    
    return faGenes

##PRE: STRING 1.txt: contains network of gene to gene mapping with edge weight
##POST: subnetwork that contains all FA associated genes, connected using the edge weight (from STRING 1.txt) and gene to gene mapping from faData
def create_subnetwork(inputFile, faGenes):

    #open STRING 1 file, iterate thru each row in file
    with open(inputFile, 'r') as file:
        results = []

        for row in file:
            row = row.split('\t')

            #error check format of STRING 1.txt
            if len(row) != 3:
                print('Data format not consistent with STRING format')
                break
            
            #cross check the genes in each row with the genes in faGenes. if both genes are in the faGenes list, add to results.
            if row[0] in faGenes: 
                if row[1] in faGenes:
                    results.append(row)

    file.close()

    with open('results.txt','w') as outputFile:
        for row in results:
            outputFile.write('\t'.join(row))
    outputFile.close()

##PRE: subnetwork, generated from create_subnetwork()
##POST: subnetwork that only contains unique rows. ***this functionality is to remove the duplicated edge connection between any given node-node pair.
def check_duplicate(resultsFile):
    #using set's, as this functionality is related to uniqueness and speed is crucial for effecient completion of the script. 
    results = set() 
    seen = set()
    duplicates = set()

    with open(resultsFile, 'r') as file:
        for row in file:
            row = row.split('\t')
            #sort each row alphabetically and store as tuple to make membership testing more efficent.
            orderedRow = tuple(sorted(row)) 
            
            #if the row from the results file has already 'seen', indicating the contents of the row [gene1, gene2, edge] are identical to another row (order non-specific), add to dummy set.abs
            #else add to seen and final results set
            if orderedRow in seen:
                duplicates.add(tuple(orderedRow))
            else:
                seen.add(orderedRow)
                results.add(tuple(row))

    file.close()

    #write unique rows to final subnetwork
    with open('results.txt','w') as outputFile:
        for row in results:     
            outputFile.write('\t'.join(row))
    outputFile.close()
       




def main():
    faGenes = fanconi_anemia_genes("Input.gmt.txt")

    create_subnetwork("STRING 1.txt", faGenes=faGenes)
    
    #comment check_duplicate call below, to generate subnetwork that contains double edge connections between any given gene-gene relationship
    check_duplicate("results.txt")
    


if __name__ == "__main__":
    main()