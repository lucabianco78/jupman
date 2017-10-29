import argparse
import gzip

parser = argparse.ArgumentParser(description="""Reads and prints a text file""")
parser.add_argument("filename", type=str, help="The file name")
parser.add_argument("-z", "--gzipped", action="store_true", help="If set, input file is assumed gzipped")

args = parser.parse_args()
inputFile = args.filename
fh = ""
if(args.gzipped):
    fh = gzip.open(inputFile, "rt")
else:
    fh = open(inputFile, "r")

for line in fh:
    line = line.strip("\n")
    print(line)

fh.close()
