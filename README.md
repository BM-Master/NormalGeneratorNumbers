# NormalGeneratorNumbers
Generator of numbers following the standard normal distribution

This generator follow de Odeh and Evans algorithm
  1. Generate u ~ U(0,1)
  2. If u < 10^-20 or U > 1 - 10^-20 go to step 1
  3. If u < 0.5 then X = g(1-u), otherwise X = -g(u)
  4. Return X

To generate u we use the most basic congruential generator that follows this algorithm
  1. Choose three natural numbers m, c and a such that 0<a<m and 0<=c<m
  2. Choose seed to x0 such that 0<=x0<m
  3. Compute the next formula Xn+1 = (a*Xn + c) mod m for n = 1,2,...
  4. Return Un = Xn/m for n=0,1,...

Choose m, c and a wisely following the Knuth theorem to get a generator of maximum cycle

 1. c and m are coprimes
 2. a-1 is multiple of all prime factors of m
 3. if m es multiple of 4, then a-1 too
                                                                      
                                                                      
