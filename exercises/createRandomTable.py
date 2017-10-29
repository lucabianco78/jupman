import random

oF = open("../file_samples/random.csv","w")
A = list("ABCDEFGHIL")

oF.write(",".join(A)+"\n")

for i in range(0,50):
    vals = []
    for j in range(0,10):
        val = random.randint(0,100)
        vals.append(str(val))
    oF.write(",".join(vals)+"\n")        

oF.close()