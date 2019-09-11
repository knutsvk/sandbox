#ifndef _ISING_H
#define _ISING_H

#include <chrono>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <random>

const double TEMP_MIN = 0.5;
const double TEMP_RANGE = 2.0;

double temperature(unsigned int j, unsigned int L);
double boltzmann_weight(unsigned int num_pos, double temp);

class Lattice
{
    private: 
        unsigned int L;
        std::vector<std::vector<int> > spins;
        std::vector<std::vector<double> > weights;
        // RNG (use the same one for initialization and probability)

    public: 
        Lattice(unsigned int _L);
        Lattice(const Lattice &twin);
        ~Lattice(){};

        double get_length() const {return L;};
        int get_spin(unsigned int i, unsigned int j) const {return spins[i][j];};
        double get_weight(unsigned int num_pos, unsigned int j) const {return weights[num_pos][j];};

        unsigned int count_positive_neighbours(unsigned int i, unsigned int j);
        void step(unsigned int i, unsigned int j, double r);
        void print();
};

void print_difference(const Lattice &l1, const Lattice &l2);

#endif
