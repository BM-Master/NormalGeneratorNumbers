# NormalGeneratorNumbers
Generator of numbers following the standard normal distribution

This generator follow de Odeh and Evans algorithm
  1. Generate u ~ U(0,1)
  2. If u < 10^-20 or U > 1 - 10^-20 go to step 1
  3. If u < 0.5 then X = g(1-u), otherwise X = -g(u)
  4. Return X

Note: g is 

<img src="https://render.githubusercontent.com/render/math?math=g(v) = \sqrt{-2ln(v)} * \frac{A(\sqrt{-2ln(v)})}{B(\sqrt{-2ln(v)})}">

with A(x) and B(x)

<img src="https://render.githubusercontent.com/render/math?math=\sum_{i=0}^4 a_{i}*x^i"> and <img src="https://render.githubusercontent.com/render/math?math=\sum_{i=0}^4 b_{i}*x^i">

Authors recommend use:

1. a0 = −0. 322232431088 
2. a1 = −1
3. a2 = −0. 342242088547 
4. a3 = −0. 0204231210245
5. a4 = −0. 0000453642210148 
6. b0 = 0. 0993484626060
7. b1 = 0. 588581570495 
8. b2 = 0. 531103462366
9. b3 = 0. 103537752850 
10. b4 = 0. 00385607006

tip: if you want to use this formula for non standard normal distribution just rescale the values using the following formula:

X=z*desvStd + mean

To generate u we use the most basic congruential generator that follows this algorithm
  1. Choose three natural numbers m, c and a such that 0<a<m and 0<=c<m
  2. Choose seed to x0 such that 0<=x0<m
  3. Compute the next formula Xn+1 = (a*Xn + c) mod m for n = 1,2,...
  4. Return Un = Xn/m for n=0,1,...

Choose m, c and a wisely following the Knuth theorem to get a generator of maximum cycle

 1. c and m are coprimes
 2. a-1 is multiple of all prime factors of m
 3. if m es multiple of 4, then a-1 too
                                                                      
                                                                      
