def getDivisors(intVal):
    """returns the integer divisors of intVal"""
    ret = []
    for i in range(1,intVal//2+1):
        if(intVal % i == 0):
            ret.append(i)
    return ret

def checkSum(intList, intVal):
    """checks if the sum of elements in intList equals intVal"""
    s = 0
    for x in intList:
        s += x
    return (s == intVal)

def checkPerfect(intVal):
    divisors = getDivisors(intVal)
    return checkSum(divisors,intVal)

def getFirstNPerfects(N):
    i = 0
    val = 2
    ret = {}
    while(i<N):
        if(checkPerfect(val)):
            i+=1
            ret[val] = getDivisors(val)
            print(val)
            val += 1
        else:
            val += 1
        
    
    return ret
            
        
perfects = getFirstNPerfects(4)

for p in perfects:
    print(str(p), "+".join(perfects[p]))