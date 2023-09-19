def fanconi_anemia_genes(inputFile):
    anemiaData = []
    anemiaGenes = []

    #Open input file and add contents to a list (anemiaData)
    with open(inputFile, 'r') as file:
        for row in file:
            anemiaData.append(row.split('\t'))
    file.close()

    #Iterate thru anemiaData and remove newline character from last item in each row
    for itr in range(len(anemiaData)):
        if '\n' in anemiaData[itr][-1]:
            anemiaData[itr][-1] = anemiaData[itr][-1].strip()

    #Remove the first two items in each row of anemiaData to isolate the genes
    for itr in range(len(anemiaData)):
        anemiaData[itr].pop(0)
        anemiaData[itr].pop(0)

    #Add each gene from anemiaData to a single list (anemiaGenes)
    for row in anemiaData:
        for item in row:
            anemiaGenes.append(item)
    
    #NOTE: could try to implement a check for duplicate genes in anemiaGenes to conserve space

    return anemiaGenes


def create_subnetwork(inputFile, anemiaGenes):

    #Create sub-network with FA related genes, using STRING 1.txt

    #1)Open STRING 1 file, iterate thru each row in file
    #2)Cross check the genes in each row with the genes in anemiaGenes
    #3)If both genes are in the anemiaGenes list add to results list

    with open(inputFile, 'r') as file:
        results = []

        for row in file:
            row = row.split('\t')

            #Error check format of STRING 1.txt
            if len(row) != 3:
                print('Data format not consistent with STRING format')
                break
            
            #2 & 3 from comment above
            if row[0] in anemiaGenes: 
                if row[1] in anemiaGenes:
                    results.append(row)

    file.close()

    with open('results.txt','w') as outputFile:
        for row in results:
            outputFile.write('\t'.join(row))
    outputFile.close()


def test(resultsFile, anemiaGenes):
    with open(resultsFile, 'r') as f:
        for line in f:
            line = line.split('\t')
            if line[0] not in anemiaGenes:
                print("0" + str(line))
            if line[1] not in anemiaGenes:
                print(line[1])


def main():

    anemiaGenes = fanconi_anemia_genes("Input.gmt.txt")

    create_subnetwork("STRING 1.txt", anemiaGenes=anemiaGenes)
    
    test("results.txt", anemiaGenes=anemiaGenes)


if __name__ == "__main__":
    main()