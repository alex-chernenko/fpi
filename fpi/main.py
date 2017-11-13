#!/usr/local/bin/python3
"""
fpi - Fixed Point Iteration methods comparison.
"""

# basic imports
from sys import argv
import argparse
import logging
import numpy as np

# import local modules
from jacobi import jacobi
from seidel import seidel
#   import sor
import matreader
import grapher

def print_solution(func, A, b, eps):
    print(func.__name__)
    x = func(A, b, eps)
    print(x)

    print(func.__name__, 'error:')
    error = np.dot(A, x) - b
    print(error)
    return x

if __name__ == '__main__':

    def parse_args():
        """ Parses arguments and returns args object to the main program"""
        parser = argparse.ArgumentParser()
        parser.add_argument("PATH", type=str,
                            help="The PATH to the matrix we want work to.")
        parser.add argument("OPT", type=str, nargs='?', default='all',
                            help="'jacobi', 'seidel' or 'sor' computation only")
        parser.add_argument("EPS", type=float, nargs='?', default=10e-10,
                            help="epsilon, the discrepancy from the precise solution.")
        return parser.parse_args()


    # Enable logging
    LOG = u'{}.log'.format(argv[0])
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] \
    %(message)s', level=logging.DEBUG, filename=LOG)

    # parse arguments
    ARGS = parse_args()
    PATH = ARGS.PATH
    FUNC = ARGS.FUNC
    EPS = ARGS.EPS

    # Ax = b
    # Read A, b
    A, b = matreader.read(PATH)

    func = dict('jacobi':jacobi, 'sor':sor, 'seidel':seidel)

    if OPT == 'all':
        # try jacobi
        x_jacobi = print_solution(jacobi, A, b, EPS)

        # try sor
        x_sor = print_solution(sor, A, b, EPS)

        # try seidel
        x_seidel = print_solution(seidel, A, b, EPS)
    else:
        x = print_solution(func[OPT], A, b, EPS)

    # grapher.makeplot(x_jacobi,0,0)
