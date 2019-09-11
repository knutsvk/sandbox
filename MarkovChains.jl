using LinearAlgebra

# Define probability matrix for the movement of frog between petals. 
# P[i,j] is the probability of moving from state i to state j. 
P = zeros(7, 7)
P[1,2] = 1.0
P[2,2] = 0.5
P[2,3] = 0.5
P[3,1] = 0.5
P[3,3] = 0.5
P[4,3] = 0.25
P[4,4] = 0.5
P[4,5] = 0.25
P[5,6] = 0.5
P[5,7] = 0.5
P[6,4] = 1.0
P[7,7] = 1.0

# Assert that the matrix is stochastic
for i=1:7, j=1:7
    @assert 0 ≤ P[i,j] ≤ 1
end
@assert isapprox(sum(P, dims=2), ones(7))

# Question (a) 
println("(a) Probability p that we are still in state 1 after n steps is:")
println("n\tp")
for n in [3, 5, 100]
    p = (P^n)[1,1]
    println("$n\t$p")
end

# Question (b) 
println("(b)")
