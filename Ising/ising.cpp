#ifndef _ISING_CPP
#define _ISING_CPP

#include "ising.h"

double temperature(unsigned int j, unsigned int L)
{
    return TEMP_MIN + TEMP_RANGE * j / (L - 1);
}

double boltzmann_weight(unsigned int num_pos, double temp)
{
    unsigned int num_neg = 4 - num_pos; 
    double pos_weight = exp(- num_pos / temp);
    double neg_weight = exp(- num_neg / temp);
    return pos_weight / (pos_weight + neg_weight);
}

Lattice::Lattice(unsigned int _L)
{
    L = _L;

    std::mt19937 rng(std::chrono::high_resolution_clock::now().time_since_epoch().count());
    std::uniform_int_distribution<int> bool_dist(0, 1);
    auto random_spin_value = std::bind(bool_dist, rng);

    int const_spins_left_side = 2 * random_spin_value() - 1;
    for(unsigned int i = 0; i < L; i++)
    {
        std::vector<int> spin_row;
        spin_row.push_back(const_spins_left_side);
        for(unsigned int j = 1; j < L; j++)
        {
            int s = 2 * random_spin_value() - 1;
            spin_row.push_back(s);
        }
        spins.push_back(spin_row);
    }

    std::vector<double> weight_row;
    for(unsigned int n = 0; n < 5; n++)
    {
        for(unsigned int j = 0; j < L; j++)
            weight_row.push_back(boltzmann_weight(n, temperature(j, L)));
        weights.push_back(weight_row);
    }

}

Lattice::Lattice(const Lattice &twin)
{
    L = twin.get_length();

    for(unsigned int i = 0; i < L; i++)
    {
        std::vector<int> spin_row;
        spin_row.push_back(-twin.get_spin(i, 0));
        for(unsigned int j = 1; j < L; j++)
            spin_row.push_back(twin.get_spin(i, j));
        spins.push_back(spin_row);
    }

    std::vector<double> weight_row;
    for(unsigned int n = 0; n < 5; n++)
    {
        for(unsigned int j = 0; j < L; j++)
            weight_row.push_back(twin.get_weight(n, j));
        weights.push_back(weight_row);
    }
}

unsigned int Lattice::count_positive_neighbours(unsigned int i, unsigned int j)
{
/*
Use the sum of the neighbours to decide how many +'s:
num positives = (sum(neighbours)+4)/2
*/
    int sum = spins[i][j-1] + spins[i][j+1];
    if(i == 0)
        sum += spins[L-1][j] + spins[1][j];
    else if(i == (L-1))
        sum += spins[L-2][j] + spins[0][j];
    else 
        sum += spins[i-1][j] + spins[i+1][j];
    return (sum + 4) / 2;
/*    unsigned int num_neighbours = 3;
    if(i == 0)
    {
        if(j == 0)
            sum = spins[L-1][0] + spins[0][1] + spins[1][0];
        else if(j == L-1)
            sum = spins[L-1][L-1] + spins[1][L-1] + spins[0][L-2];
        else
        {
            sum = spins[L-1][j] + spins[0][j+1] + spins[1][j] + spins[0][j-1];
            num_neighbours = 4;
        }
    }
    else if(i == L-1)
    {
        if(j == 0)
            sum = spins[L-2][0] + spins[L-1][1] + spins[0][0];
        else if(j == L-1)
            sum = spins[L-2][L-1] + spins[0][L-1] + spins[L-1][L-2];
        else
        {
            sum = spins[L-2][j] + spins[L-1][j+1] + spins[0][j] + spins[L-1][j-1];
            num_neighbours = 4;
        }
    }
    else if(j == 0)
        sum = spins[i-1][0] + spins[i][1] + spins[i+1][0];
    else if(j == L-1)
        sum = spins[i-1][L-1] + spins[i+1][L-1] + spins[i][L-2];
    else
    {
        sum = spins[i-1][j] + spins[i][j+1] + spins[i+1][j] + spins[i][j-1];
        num_neighbours = 4;
    }

    return (sum + num_neighbours) / 2;*/
}

void Lattice::step(unsigned int i, unsigned int j, double r)
{
    unsigned int num_pos = count_positive_neighbours(i, j);
    if(r < weights[num_pos][j])
        spins[i][j] = 1;
    else
        spins[i][j] = -1;
}

void Lattice::print()
{
    for(unsigned int i = 0; i < L; i++)
    {
        for(unsigned int j = 0; j < L; j++)
        {
            if(spins[i][j] == 1)
                std::cout << "+1 ";
            else
                std::cout << "-1 ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl; 
}

void print_difference(const Lattice &l1, const Lattice &l2)
{
    for(unsigned int i = 0; i < l1.get_length(); i++)
    {
        for(unsigned int j = 0; j < l1.get_length(); j++)
            std::cout << (l1.get_spin(i,j) != l2.get_spin(i,j)) << " ";
        std::cout << std::endl;
    }
    std::cout << std::endl; 
}

#endif
