#include <complex>
#include <iostream>

using namespace std;

/* 
 * The Mandelbrot set is defined as the set of complex numbers c which do not diverge in the
 * sequence 
 *
 *              z_{n+1} = f_c(z_n) = z_n^2 + c
 *
 * starting from z = 0.
 */
complex<double> f(complex<double> z, complex<double> c)
{
    return z*z + c;
}

int main(int argc, char* argv[])
{
    int n = 200;        // number of points per unit length
    int maxiter = 100;  // c is "not diverged" if it survives this many iterations 

    // Command-line input
    if(argc > 1)
    {
        n = atoi(argv[1]);
        if(argc < 2)
        {
            maxiter = atoi(argv[2]);
        }
    }

    bool m[3*n][2*n];   // which points are diverged and not 

    // Loop over grid points
    for(int i = 0; i < 3*n; i++)
    {
        double x = -2 + double(i) / n;

        for(int j = 0; j < 2*n; j++)
        {
            double y = -1 + double(j) / n;

            complex<double> z = 0;
            complex<double> c(x, y);

            // Find (up to) 100 first numbers in sequence f_c 
            for(int iter = 0; iter <= maxiter; iter++)
            {
                // Get next number in seuqnece
                z = f(z, c);

                // Check for divergence
                if(abs(z) > 2)
                {
                    m[i][j] = true;
                    break;
                }
            }
        }
    }

    // Print result to screen
    for(int j = 0; j < 2*n; j++)
    {
        for(int i = 0; i < 3*n; i++)
        {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
}
