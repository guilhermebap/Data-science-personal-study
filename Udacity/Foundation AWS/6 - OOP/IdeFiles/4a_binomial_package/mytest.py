from distributions import Binomial
binomial_one = Binomial(.4, 20)
binomial_two = Binomial(.4, 60)
binomial_sum = binomial_one + binomial_two
binomial = Binomial(0.4, 20)
print(binomial_one)
print(binomial_two)
print(binomial_sum)
print(binomial)
print(round(binomial.pdf(5), 5))