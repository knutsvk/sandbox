#include <cassert>
#include <cmath>
#include <iostream>
#include <gsl/gsl_integration.h>

double eccentricity_squared(double a, double b)
{
    double e = 1.0 - pow(b/a, 2.0);
    assert(e >= 0.0 && e <= 1.0);
    return e;
}

struct int_params { 
    double e2; 
};

double integrand(double theta, void *p)
{
    int_params &params = *reinterpret_cast<int_params *>(p);
    return sqrt(1.0 - params.e2 * sin(theta) * sin(theta));
}

double complete_elliptic_integral_2(double e2)
{
    // GSL integration: 
    // E(e) = \int_{0}^{\pi/2} \sqrt{1 - e^2 \sin^2 (\theta)} d\theta
    int_params params;
    params.e2 = e2;
    gsl_function F;
    F.function = &integrand; 
    F.params = reinterpret_cast<void *>(&params);

    const double theta_lo = 0.0;
    const double theta_hi = M_PI_2;
    const double abstol = 1.0e-6;
    const double reltol = 1.0e-6;

    double result, error;
    size_t neval;

    int exit_code = gsl_integration_qng(&F, theta_lo, theta_hi, abstol, reltol, 
                                        &result, &error, &neval); 

    if(exit_code)
        std::cerr << "Integration problem: exit code " << exit_code << std::endl;

    assert(result >= 0.0);
    assert(error <= 1.0e-6);

    return result;
}

int main(int argc, char* argv[])
{
    // Initialise a, b to default values (unit circle)
    double a = 1.0, b = 1.0;

    // Use a, b from command line if specified by user. 
    if(argc > 1)
    {
        if(argc == 3)
        {
            a = atof(argv[1]);
            b = atof(argv[2]);
            assert(a > 0.0);
            assert(b >= 0 && b <= a);
            std::cout << "Ellipse with a = " << a << ", b = " << b << std::endl; 
        }
        else
        {
            std::cout << "Need exactly 2 input arguments, a and b." << std::endl; 
            std::cout << "Defaulting to ellipse with a = " << a << ", b = " << b << std::endl; 
        }
    }

    double e2 = eccentricity_squared(a, b);
    double E = complete_elliptic_integral_2(e2);
    double L = 4 * a * E;

    std::cout << "The perimeter of the ellipse is " << L << std::endl; 

    return 0;
}
