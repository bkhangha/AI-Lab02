import sys
import getopt
from pl_resolution import *


def main(argv):
    input_file = 'INPUT/input_1.txt'
    output_file = 'OUTPUT/output_1.txt'
    try:
        opts, args = getopt.getopt(argv, 'hi:o:', ['ifile=', 'ofile='])
    except getopt.GetoptError:
        print('script.py - i <input_file> -o <output_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('script.py -i <input_file> -o <output_file>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            input_file = arg
        elif opt in ('-o', '--ofile'):
            output_file = arg
    alpha, KB = read_input(input_file)
    print('KB: ', KB)
    not_alpha = to_cnf(add_recursive([], alpha))
    print('NOT alpha: ', not_alpha)
    pl_res = PL_resolution(not_alpha, KB, output_file)
    if (pl_res):
        print('KB entails alpha.')
    else:
        print('KB does not entail alpha.')
    print('Success.')


if __name__ == '__main__':
    main(sys.argv[1:])
