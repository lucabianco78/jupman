import argparse

def readIDS(f):
    """reads a one column file in and stores
    the ids in a dictionary that is returned at the end"""
    ret = dict()
    with open(f, "r") as file:
        for line in file:
            line = line.strip()
            if(line not in ret):
                ret[line] = 1
    return ret

def filterFasta(inF, outF, ids2keep):
    oF = open(outF, "w")
    
    outputME = False
    with open(inF, "r") as file:
        for line in file:
            line = line.strip()
            if(line.startswith(">")):
                #this is the header
                if ids2keep.get(line[1:],False):
                    oF.write(line +"\n")
                    outputME = True
                    print("Writing contig ", line[1:])
                else:
                    outputME = False
            else:
                if(outputME):
                    oF.write(line +"\n")
        
    oF.close()
    

parser = argparse.ArgumentParser(description="Filters a fasta file")
parser.add_argument("inputFasta", type = str, help = "The input fasta file")
parser.add_argument("inputIDS", type = str, help = "The IDS to keep")
parser.add_argument("outputFasta", type = str, 
                    help = "The output fasta file with filtered entries")
args = parser.parse_args()
idsFile = args.inputIDS
inFasta = args.inputFasta
outFasta = args.outputFasta

ids = readIDS(idsFile)
filterFasta(inFasta,outFasta, ids)