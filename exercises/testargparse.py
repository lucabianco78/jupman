import argparse
parser = argparse.ArgumentParser(description="""This script gets a string 
                                 and an integer and repeats the string N times""")
parser.add_argument("string", type=str,
                    help="The string to be repeated")
parser.add_argument("N", type=int,
                    help="The number of time to repeated the string")

parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")

parser.add_argument("-p", "--trailpoints", type = int, default = 1, help="Adds these many trailing points")
parser.add_argument("-s", "--separator", type = str, default = " ", help="The separator between repeated strings")

args = parser.parse_args()
mySTR = args.string+args.separator
trailP = "." * args.trailpoints
answer = mySTR * args.N 
answer = answer[:-len(args.separator)] + trailP #to remove the last separator
if args.verbose:
    print("the string {} repeated {} times is: {}".format(args.string, args.N, answer))
else:
    print(answer)
