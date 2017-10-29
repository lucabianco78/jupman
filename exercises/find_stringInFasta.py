import argparse

def getIndexes(string1,string2):
    """checks if string2 is present in string1 and returns 
    all the positions at which string2 occurs in string1"""
    ret = []
    ind = string1.find(string2)
    
    while (ind > -1 and ind < len(string1)):
        ret.append(ind)
        ind = string1.find(string2,ind + 1)
        
    return ret

def processFasta(file,testStr):
    """reads a fasta file entry by entry checks if the input string
       testStr is present in each sequence. Reporting how many times and where.
    """
    header = ""
    seq = ""
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if(line.startswith(">")):
                if(len(header) == 0 ):
                    #first entry:
                    header = line[1:]
                else:
                    #this is a new entry
                    indexes = getIndexes(seq,testStr)
                    if len(indexes) > 0:
                        print("{} in {}: {} times ({})".format(testStr, header,len(indexes),indexes))
                    seq = ""
                    header = line[1:]
            else:
                seq +=line
    #processing the final entry
    indexes = getIndexes(seq,testStr)
    if len(indexes) > 0:
        print("{} in {}: {} times ({})".format(testStr, header,len(indexes),indexes))
                    
parser = argparse.ArgumentParser(description="""Checks if a sequence is exactly contained in a fasta file""")
parser.add_argument("filename", type=str, help="The fasta file name")
parser.add_argument("query", type=str, help="The query string")

args = parser.parse_args()
inFasta = args.filename
testS = args.query
#inFasta = "file_samples/contigs82.fasta"
#testS = "TAAACAT"
processFasta(inFasta, testS)
