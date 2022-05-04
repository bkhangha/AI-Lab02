def readFile(fileName):
    fread = open(fileName, "r")

    # Read clauses
    alpha = fread.readline().strip("\n").replace(' ', '').split("OR")
    nClauseInKB = fread.readline()

    # Read KBs
    KB = list()
    for i in range(int(nClauseInKB)):
        clause = fread.readline().strip("\n").replace(' ', '').split("OR")
        KB.append(clause)

    fread.close()
    return KB, alpha
