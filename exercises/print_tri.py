"""
triangle example
"""

for i in range(1, 10):                      # or without string output
    j = 1                                   # for i in range(1,10):
    output = ""                             #     j = 1
    while j <= i:                           #     while(j<=i):
        output = str(j) + " " + output      #         print(j, end = " ")
        j = j + 1                           #         j = j + 1
    print(output)




a = [4,2,1,5,3]

def mySort(v):
    a = v[:]
    a.sort()
    print(a)

print(a)
mySort(a)
print(a)