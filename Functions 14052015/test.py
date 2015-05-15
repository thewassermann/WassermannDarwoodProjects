from Angle3D import Angle3D
from comparisons3D import Comparisons
import numpy as np 

# angle3d TESTS
ang = Angle3D()

a = np.array((1.,0.,0.))
b = np.array((0.,0.,0.))
c = np.array((0.,1.,0.))

ans = ang.angle_calc(a, b, c)

print "%f radians\n" % ans


# 3DComparisons tests
comp = Comparisons()

# euc method 

data_expected = np.array((16, 16, 16, 16, 16, 8))
data_observed = np.array((16, 18, 16, 14, 12, 12))

print "%f difference \n" % comp.euc_comp(data_observed, data_expected)

# chi method

p_val = comp.chi_squared(data_observed, data_expected)

ans = comp.p_val_interp(p_val, 0.5)

print p_val

print ans

