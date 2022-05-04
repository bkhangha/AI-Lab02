def toNegative(literal):
    if literal[0] == "-":
        return literal[1]
    else:
        return "-" + literal


def toPositive(literal):
    if literal[0] == "-":
        return literal[1]
    else:
        return literal


def insertLiteral(clause, literal):
    index = len(clause)
    for i in range(len(clause)):
      if toPositive(clause[i]) > toPositive(literal):
        index = i
        break

    if index == len(clause):
      clause = clause[:index] + [literal]
    else:
      clause = clause[:index] + [literal] + clause[index:]

    return clause


def clauseToString(clause):
    string = str()
    for i in range(len(clause) - 1):
        string += clause[i]
        string += " OR "
    string += clause[-1]
    string += "\n"
    return string
