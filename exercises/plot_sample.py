
import numpy as np
from numpy import linalg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#AX = b
A = [[3, 4, 2],[4, 4, 10], [-1, 2, -7]]
Amat = np.array(A)

b = np.array([-9, 32, -7])
print("A matrix")
print(Amat)
print("")
print("b vector")
print(b.T)
print("")     
Xsol = linalg.solve(A,b)
print("Solution X:")
print(Xsol)
print(Amat.dot(Xsol))
#the plot range:
#2d plot

#3x - 4y + 2z = -9\\ -4x + 4y + 10z = 32\\ -x + 2y + -7z = -7
z  =  0
Z = np.zeros((500,))

X = np.arange(-30,20,0.1)
print(X.shape)
print(Z.shape)

Y = (3*X + 2*Z + 9)/4
Y1 = (4*X - 10*Z + 32)/4
Y2 = (X + 7*Z - 7)/2

plt.plot(X,Y, 'r')
plt.plot(X,Y1, 'g')

plt.show()