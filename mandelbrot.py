from matplotlib import pyplot as plt
import numpy as np


def f(z, c):
    """
    The Mandelbrot set is defined as the set of complex numbers c which do not diverge in the
    sequence 
    
                z_{n+1} = f_c(z_n) = z_n^2 + c
    
    starting from z = 0.
    """
    return z*z + c


def mandelbrot(n, maxiter):
    """
    Compute the Mandelbrot set
    IN  n:          number of points per unit length
    IN  maxiter:    maximum number of terms in sequence f_c
    OUT m:          bool array with True/False values for point being in Mandelbrot set
    """
    m = np.ones((2*n, 3*n), dtype=bool) # which points are diverged and which are not
    z = np.zeros_like(m, dtype=complex) # sequence f_c

    x = np.linspace(-2, 1, 3*n)         
    y = np.linspace(-1, 1, 2*n)
    X, Y = np.meshgrid(x,y)
    complex_grid = np.vectorize(complex)(X,Y)

    # Find (up to) maxiter first numbers in sequence f_c 
    for iter in range(maxiter):

        # Get next number in seuqnece
        z[m] = f(z[m], complex_grid[m])

        # Check for divergence
        m = abs(z) <= 2

    return ~m


if __name__ == "__main__": 
    m = mandelbrot(200, 100)

    # Plot the results
    plt.matshow(m, fignum=0, cmap=plt.gray())
    plt.show()
