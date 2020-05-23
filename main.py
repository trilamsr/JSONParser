import sys, getopt
from parse_json_from_path import parse_JSON_from_path

# parse_JSON_from_path('./input.txt', 3)


def print_intruction():
    print('Valid argument are --path=str(X) and --count=int(Y) or ')
    print('Example: py main.py --path=./input.txt --count=3')

def main(args):
    try:
        opts, args = getopt.getopt(args, 'p:c:', ['path=', 'count='])
    except getopt.error as err:
        print(str(err))
        sys.exit(2)
    info = {k:v for k, v in opts}
    if '--path' not in info or '--count' not in info:
        print_intruction()
        sys.exit(2)
    parse_JSON_from_path(info['--path'], int(info['--count']))

if __name__ == "__main__":
    main(sys.argv[1:])