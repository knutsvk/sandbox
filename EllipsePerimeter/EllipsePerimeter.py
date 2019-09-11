from math import pi
import numpy as np
from scipy.integrate import quadrature
import sys

def eccentricity_squared(a, b):
    e = 1 - (b / a)**2
    assert(0 <= e <= 1)
    return e


def integrand(theta, e2):
    return np.sqrt(1 - e2 * (np.sin(theta))**2)

def complete_elliptic_integral_2(e2):
    # GSL integration:
    # E(e) = \int_0^{\pi/2} \sqrt{ 1 - e^2 \sin^2 (\theta)} d\theta
    theta_lo = 0
    theta_hi = pi / 2
    abstol = 1e-6
    reltol = 1e-6

    output = quadrature(integrand, theta_lo, theta_hi, args=(e2,), tol=abstol, rtol=reltol)
    res= output[0]
    err= output[1]

    assert(res >= 0)
    assert(err <= 1e-6)
    return res

a = 1
b = 1

if len(sys.argv) > 1:
    if len(sys.argv) == 3:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        assert(a > 0)
        assert(0 <= b <= a)
        print("Ellipse with a = %f, b = %f" % (a, b))
    else:
        print("Need exactly 2 input arguments, a and b.")
        print("Defaulting to ellipse with a = ", a, ", b = ", b)

e2 = eccentricity_squared(a, b)
E = complete_elliptic_integral_2(e2)
L = 4 * a * E

print("The perimeter of the ellipse is %.4f" % L)
