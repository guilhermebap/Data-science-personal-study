import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n
    return x, y


def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)
    # Return entry [0,1]
    return corr_mat[0,1]


def bootstrap_replicate_1d(data, func):
    """Generate bootstrap replicate of 1D data"""
    return func(np.random.choice(data, size=len(data)))


def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""
    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)
    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)
    return bs_replicates


def draw_bs_pairs_linreg(x, y, size=1):
    """Perform pairs bootstrap for linear regression."""
    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))
    # Initialize replicates: bs_slope_reps, bs_intercept_reps
    bs_slope_reps = np.empty(size)
    bs_intercept_reps = np.empty(size)
    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, size=len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_slope_reps[i], bs_intercept_reps[i] = np.polyfit(bs_x, bs_y, 1)
    return bs_slope_reps, bs_intercept_reps


def permutation_sample(data1, data2):
    """Generate a permutation sample from two data sets."""

    # Concatenate the data sets: data
    data = np.concatenate((data1, data2))

    # Permute the concatenated array: permuted_data
    permuted_data = np.random.permutation(data)

    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[:len(data1)]
    perm_sample_2 = permuted_data[len(data1):]

    return perm_sample_1, perm_sample_2


def draw_perm_reps(data_1, data_2, func, size=1):
    """Generate multiple permutation replicates."""

    # Initialize array of replicates: perm_replicates
    perm_replicates = np.empty(size)

    for i in range(size):
        # Generate permutation sample
        perm_sample_1, perm_sample_2 = permutation_sample(data_1, data_2)

        # Compute the test statistic
        perm_replicates[i] = func(perm_sample_1, perm_sample_2)

    return perm_replicates


def diff_of_means(data_1, data_2):
    """Difference in means of two arrays."""

    # The difference of means of data_1, data_2: diff
    diff = (np.mean(data_1) - np.mean(data_2))

    return diff





'''
The vote for the Civil Rights Act in 1964

The Civil Rights Act of 1964 was one of the most important pieces of legislation 
ever passed in the USA. Excluding "present" and "abstain" votes, 153 House 
Democrats and 136 Republicans voted yea. However, 91 Democrats and 35 Republicans 
voted nay. Did party affiliation make a difference in the vote?

To answer this question, you will evaluate the hypothesis that the party of a 
House member has no bearing on his or her vote. You will use the fraction of 
Democrats voting in favor as your test statistic and evaluate the probability of 
observing a fraction of Democrats voting in favor at least as small as the observed 
fraction of 153/244. (That's right, at least as small as. In 1964, it was the 
Democrats who were less progressive on civil rights issues.) To do this, permute the 
party labels of the House voters and then arbitrarily divide them into "Democrats" and 
"Republicans" and compute the fraction of Democrats voting yea.
'''

# Construct arrays of data: dems, reps
dems = np.array([True] * 153 + [False] * 91)
reps = np.array([True] * 136 + [False] * 35)

def frac_yea_dems(dems, reps):
    """Compute fraction of Democrat yea votes."""
    frac = np.sum(dems) / len(dems)
    return frac

# Acquire permutation samples: perm_replicates
perm_replicates = draw_perm_reps(dems, reps, frac_yea_dems, size=10000)

# Compute and print p-value: p
p = np.sum(perm_replicates <= 153/244) / len(perm_replicates)
print('p-value =', p)




'''
What is equivalent?
You have experience matching stories to probability distributions. Similarly, 
you use the same procedure for two different A/B tests if their stories match. 
In the Civil Rights Act example you just did, you performed an A/B test on voting 
data, which has a Yes/No type of outcome for each subject (in that case, a voter). 
Which of the following situations involving testing by a web-based company has an 
equivalent set up for an A/B test as the one you just did with the Civil Rights Act of 1964?

1) You measure how much time each customer spends on your website before and after an advertising campaign.

2) You measure the number of people who click on an ad on your company's website before and after changing its color.

3) You measure how many clicks each person has on your company's website before and after changing the header layout.

Answer: 2
'''


'''
A time-on-website analog

We return to the no-hitter data set. In 1920, Major League Baseball implemented important rule changes that ended the 
so-called dead ball era. Importantly, the pitcher was no longer allowed to spit on or scuff the ball, an activity that 
greatly favors pitchers. In this problem you will perform an A/B test to determine if these rule changes resulted in a 
slower rate of no-hitters (i.e., longer average time between no-hitters) using the difference in mean inter-no-hitter 
time as your test statistic. The inter-no-hitter times for the respective eras are stored in the arrays nht_dead and 
nht_live, where "nht" is meant to stand for "no-hitter time."
'''

# Compute the observed difference in mean inter-no-hitter times: nht_diff_obs
nht_diff_obs = diff_of_means(nht_dead, nht_live)

# Acquire 10,000 permutation replicates of difference in mean no-hitter time: perm_replicates
perm_replicates = draw_perm_reps(nht_dead, nht_live, diff_of_means, size=10000)

# Compute and print the p-value: p
p = np.sum(perm_replicates <= nht_diff_obs) / len(perm_replicates)
print('p-val =', p)

# p-val = 0.0001

'''
Your p-value is 0.0001, which means that only one out of your 10,000 replicates had a result as extreme as the 
actual difference between the dead ball and live ball eras. This suggests strong statistical significance. 
Watch out, though, you could very well have gotten zero replicates that were as extreme as the observed value. 
This just means that the p-value is quite small, almost certainly smaller than 0.001.
'''

'''
Simulating a null hypothesis concerning correlation
The observed correlation between female illiteracy and fertility in the data set of 162 countries may just be 
by chance; the fertility of a given country may actually be totally independent of its illiteracy. You will 
test this null hypothesis in the next exercise.

To do the test, you need to simulate the data assuming the null hypothesis is true. Of the following choices, 
which is the best way to do it?

    -> Do a permutation test: Permute the illiteracy values but leave the fertility values fixed to generate a 
    new set of (illiteracy, fertility) data.

 #Yes, this exactly simulates the null hypothesis and does so more efficiently than the last option. It is exact 
  because it uses all data and eliminates any correlation because which illiteracy value pairs to which fertility 
  value is shuffled.
'''

'''
Hypothesis test on Pearson correlation

The observed correlation between female illiteracy and fertility may just be by
chance; the fertility of a given country may actually be totally independent ofits illiteracy. You will test this hypothesis. 
To do so, permute the illiteracy values but leave the fertility values fixed. This simulates the hypothesis that they are 
totally independent of each other. For each permutation, compute the Pearson correlation coefficient and assess how many of 
your permutation replicates have a Pearson correlation coefficient greater than the observed one.
'''

# Compute observed correlation: r_obs
r_obs = pearson_r(illiteracy, fertility)

# Initialize permutation replicates: perm_replicates
perm_replicates = np.empty(10000)

# Draw replicates
for i in range(10000):
    # Permute illiteracy measurments: illiteracy_permuted
    illiteracy_permuted = np.random.permutation(illiteracy)

    # Compute Pearson correlation
    perm_replicates[i] = pearson_r(illiteracy_permuted, fertility)

# Compute p-value: p
p = np.sum(perm_replicates >= r_obs) / len(perm_replicates)
print('p-val =', p)

'''
You got a p-value of zero. In hacker statistics, this means that your p-value is very low, since you never got a 
single replicate in the 10,000 you took that had a Pearson correlation greater than the observed one. You could 
try increasing the number of replicates you take to continue to move the upper bound on your p-value lower and lower.
'''




'''
Do neonicotinoid insecticides have unintended consequences?

As a final exercise in hypothesis testing before we put everything together in our case study in the next chapter, you 
will investigate the effects of neonicotinoid insecticides on bee reproduction. These insecticides are very widely used 
in the United States to combat aphids and other pests that damage plants.

In a recent study, Straub, et al. (Proc. Roy. Soc. B, 2016) investigated the effects of neonicotinoids on the sperm of 
pollinating bees. In this and the next exercise, you will study how the pesticide treatment affected the count of live 
sperm per half milliliter of semen.

First, we will do EDA, as usual. Plot ECDFs of the alive sperm count for untreated bees (stored in the Numpy array control) 
and bees treated with pesticide (stored in the Numpy array treated).
'''

# Compute x,y values for ECDFs
x_control, y_control = ecdf(control)
x_treated, y_treated = ecdf(treated)

# Plot the ECDFs
_ = plt.plot(x_control, y_control, marker='.', linestyle='none')
_ = plt.plot(x_treated, y_treated, marker='.', linestyle='none')

# Set the margins
plt.margins(0.02)

# Add a legend
plt.legend(('control', 'treated'), loc='lower right')

# Label axes and show plot
plt.xlabel('millions of alive sperm per mL')
plt.ylabel('ECDF')
plt.show()

'''
Nice plot! The ECDFs show a pretty clear difference between the treatment and control; treated bees have fewer 
alive sperm. Let's now do a hypothesis test in the next exercise.
'''




'''
Bootstrap hypothesis test on bee sperm counts

Now, you will test the following hypothesis: On average, male bees treated
neonicotinoid insecticide have the same number of active sperm per milliliter
of semen than do untreated male bees. You will use the difference of means as
your test statistic.
'''

# Compute the difference in mean sperm count: diff_means
diff_means = np.mean(control) - np.mean(treated)

# Compute mean of pooled data: mean_count
mean_count = np.mean(np.concatenate((control, treated)))

# Generate shifted data sets
control_shifted = control - np.mean(control) + mean_count
treated_shifted = treated - np.mean(treated) + mean_count

# Generate bootstrap replicates
bs_reps_control = draw_bs_reps(control_shifted,
                       np.mean, size=10000)
bs_reps_treated = draw_bs_reps(treated_shifted,
                       np.mean, size=10000)

# Get replicates of difference of means: bs_replicates
bs_replicates = bs_reps_control - bs_reps_treated

# Compute and print p-value: p
p = np.sum(bs_replicates >= np.mean(control) - np.mean(treated)) \
            / len(bs_replicates)    
print('p-value =', p)

# p-value = 0.0

'''
Nice work! The p-value is small, most likely less than 0.0001, since you never saw a bootstrap 
replicated with a difference of means at least as extreme as what was observed. In fact, when I 
did the calculation with 10 million replicates, I got a p-value of 2e-05.
'''