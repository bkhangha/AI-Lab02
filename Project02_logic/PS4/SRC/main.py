from sys import argv
from file_reader import *
from pl_resolution import *

INPUT_LIST = [  
    # 'INPUT/input_1.txt',
    'INPUT/input_2.txt',
    #   'INPUT/input_3.txt',
    #   'INPUT/input_4.txt',
    #   'INPUT/input_5.txt'
]

OUTPUT_LIST = [
    # 'OUTPUT/output_1.txt',
    'OUTPUT/output_2.txt',
    # 'OUTPUT/output_3.txt',
    # 'OUTPUT/output_4.txt',
    # 'OUTPUT/output_5.txt'
]

TOTAL_TESTCASE = len(INPUT_LIST)


def main():
    for index in range(TOTAL_TESTCASE):
        KB, alpha = readFile(INPUT_LIST[index])
        entail = pl_resolution(KB, alpha, OUTPUT_LIST[index])
        print("Result written in ", OUTPUT_LIST[index], "successfully.")
        print("KB", '{}'.format(
            'entails' if entail else 'does not entail'), "alpha.")
        print('--------------------------------------------------------')


if __name__ == "__main__":
    main()
