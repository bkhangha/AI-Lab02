from ultilities import *

def pl_resolve(clause1, clause2):
    clause1 = clause1.copy()
    clause2 = clause2.copy()

    for literal in clause1:
        if toNegative(literal) in clause2:
            for eachC1 in clause1:
                if eachC1 != literal and toNegative(eachC1) in clause2:
                    return None

            resolve = list()
            for eachC1 in clause1:
                if eachC1 != literal:
                    resolve = insertLiteral(resolve, eachC1)
            for eachC2 in clause2:
                if toNegative(eachC2) != literal and eachC2 not in clause1:
                    resolve = insertLiteral(resolve, eachC2)

            return resolve
    return None

def pl_resolution(KB, alpha, outputPath):
    fwrite = open(outputPath, "w")

    clauses = KB.copy()
    for literal in alpha:
        clauses.append([toNegative(literal)])

    while (True):
        newClauses = list()
        clausesToWrite = list()
        areNewClauses = False
        isEmptyClause = False

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = pl_resolve(clauses[i], clauses[j])
                if resolvents is not None:
                    print('Resolve', clauses[i], 'and', clauses[j], 'get', resolvents)
                    newClauses.append(resolvents)

        for clause in newClauses:
            if clause not in clauses:
                areNewClauses = True
                clauses.append(clause)
                clausesToWrite.append(clause)
        if (not areNewClauses):
            fwrite.write("0\nNO")
            fwrite.close()
            return False

        fwrite.write(str(len(clausesToWrite)) + "\n")
        for clause in clausesToWrite:
            if clause:
                fwrite.write(clauseToString(clause))
            else:
                isEmptyClause = True
                fwrite.write("{}\n")
        if (isEmptyClause):
            fwrite.write("YES")
            fwrite.close()
            return True