import copy


def read_input(input_file):
    with open(input_file, 'r') as fin:
        #read clause
        alpha = []
        clause = fin.readline().replace('OR', '')
        clause_lst = []
        for literal in clause.split():
            if literal[0] == '-':
                clause_lst.append(literal[1])
            else:
                clause_lst.append('-' + literal)
        alpha.append(clause_lst)
        #read number of KBs
        n_KB = int(fin.readline())
        KB = []
        for _ in range(n_KB):
            clause = list(filter(None, fin.readline().replace(
                'OR', '').rstrip('\n').split(' ')))
            KB.append(clause)
    return alpha, KB


def neg(literal):
    l = copy.deepcopy(literal)

    if '-' in literal:
        return literal.replace('-', '')
    else:
        return '-' + l


def is_equiv(clause):

    for literal in clause:
        if neg(literal) in clause:
            return True
    return False


def comparator(literal):
    if literal[0] == '-':
        return literal[1:]
    else:
        return literal


def sort_clause(clause):
    # use bubble sort
    i = 0
    while(i < len(clause) - 1):
        j = i + 1
        while(j < len(clause)):
            if clause[i] == clause[j]:
                del clause[j]
                j -= 1
                i -= 1
            j += 1
        i += 1

    for i in range(len(clause) - 1):
        for j in range(i + 1, len(clause)):
            if (comparator(clause[i]) > comparator(clause[j])):
                clause[i], clause[j] = clause[j], clause[i]
    return clause


def to_string(clause):
    str = ''
    for i in range(len(clause) - 1):
        str += clause[i]
        str += ' OR '

    str += clause[-1]
    str += '\n'
    return str


def is_eval_cnf_form(clause, exist):
    for c in exist:
        if set(c).issubset(set(clause)):
            return False
    return True


def to_cnf(alpha_list):
    alpha_cnf = []
    alpha_list.sort(key=lambda x: len(set(x)))
    for i in alpha_list:
        clause = sort_clause(sorted(set(i)))
        if clause not in alpha_cnf and is_eval_cnf_form(clause, alpha_cnf):
            alpha_cnf.append(clause)
    return alpha_cnf


def add_recursive(lst, alpha_list):
    if len(alpha_list) == 0:
        return lst
    if len(lst) == 0:
        for i in alpha_list[0]:
            lst.append([i])
        return add_recursive(lst, alpha_list[1:len(alpha_list)])
    else:
        temp = []
        for i in lst:
            for j in alpha_list[0]:
                if neg(j) not in i:
                    temp.append(i + [j])
        return add_recursive(temp, alpha_list[1:len(alpha_list)])


def PL_resolve(A_clause, B_clause):
    clause_a = copy.deepcopy(A_clause)
    clause_b = copy.deepcopy(B_clause)
    if(len(clause_a) == 1 and len(clause_b) == len(clause_a)):
        if clause_a[0] == neg(clause_b[0]):
            return '{}'

    for literal in A_clause:
        if neg(literal) in B_clause:
            clause_b.remove(neg(literal))
            clause_a.remove(literal)
            return list(set(clause_a + clause_b))
    return []


def PL_resolution(neg_alpha, KB, output_file):
    with open(output_file, 'w') as fout:
        clauses = KB
        for i in neg_alpha:
            clauses.append(i)
        is_entailed = False
        while True:
            new_clauses = []
            num_result = 0
            w_string = ''
            for i in range(len(clauses) - 1):
                for j in range(i + 1, len(clauses)):
                    new_clause = PL_resolve(clauses[i], clauses[j])
                    new_clause = sort_clause(new_clause)
                    if new_clause == [] or (new_clause in clauses) or (new_clause in new_clauses) or (is_equiv(new_clause)):
                        continue
                    #if resolvents contains the empty clause -> is_entailed = True
                    if new_clause == '{}':
                        is_entailed = True
                    w_string += to_string(new_clause) if new_clause != '{}' else '{}\n'
                    print('[->] Resolve', clauses[i], 'and',
                          clauses[j], 'get', new_clause)
                    num_result += 1
                    #new_clauses unions with resolvents
                    new_clauses.append(new_clause)
            w_string = str(num_result) + '\n' + w_string
            fout.write(w_string)
            if new_clauses == []:
                w_string = '0\nNO'
                fout.write('NO')
                fout.close()
                return False
            elif is_entailed:
                w_string += '\nYES'
                fout.write('YES')
                fout.close()
                return True
            clauses += new_clauses
