import numpy as np

molarmass = np.array([18.998*2, 1.00794*2, 4.0026, 14.00674 + 1.00794*3, 55.845, 26.981])
print(molarmass)
mole = np.reciprocal(molarmass)
print(mole)
r = 8.314
degreeoffreedom = np.array([5,5,3,6,6,6])
multi=degreeoffreedom * mole
print(multi)
C = 0.5 * degreeoffreedom * r * mole

test = np.array([], dtype=float)
print(test)
for i in range(6):
    test = np.append(test, mole[i] * degreeoffreedom[i])

print(test)
print(C)
