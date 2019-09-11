#include "ising.h"

int main(int argc, char* argv[])
{
    // Get runtime parameters from user
    unsigned int L = atoi(argv[1]);             // Length per dimension
    unsigned int num_sweeps = atoi(argv[2]);    // Number of sweeps to perform
                                                // (TODO: steady-state checker)

    // Initiate lattices
    Lattice lattice1(L);
    Lattice lattice2(lattice1);

    // Set up random number generator for picking row and column indices
    std::mt19937 rng(std::chrono::high_resolution_clock::now().time_since_epoch().count());
    std::uniform_int_distribution<int> row_dist(0, L-1);
    std::uniform_int_distribution<int> col_dist(1, L-2);
    std::uniform_real_distribution<double> unit_dist(0.0, 1.0);
    auto random_row = std::bind(row_dist, rng);
    auto random_col = std::bind(col_dist, rng);
    auto random_unit_interval = std::bind(unit_dist, rng);

    unsigned int i, j;
    double r; 
    for(unsigned int counter = 0; counter < num_sweeps; counter++)
    {
        std::cout << "sweep #" << counter << std::endl; 
        // Pick L*L random spins per sweep
        for(unsigned int subcounter = 0; subcounter < L * L; subcounter++)
        {
//            std::cout << "spin #" << subcounter << ": " << std::endl; 
            i = random_row();
            j = random_col();
            if(j == 1)
                std::cout << "ROW 1!!" << std::endl; 
//            std::cout << "(i,j) = (" << i << "," << j << ") " << std::endl;
            r = random_unit_interval();
//            std::cout << "r = " << r << std::endl; 
            lattice1.step(i, j, r);
            lattice2.step(i, j, r);
        }
    }
    print_difference(lattice1, lattice2);


    return EXIT_SUCCESS;
}
