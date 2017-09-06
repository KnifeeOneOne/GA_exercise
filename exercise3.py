import random

N_MAX = 1000


def func(*args):
    return sum(*args)


def ga(mu, f, lamda=1, D=50):
    '''
    Algorithm 1: (mu + 1) - GA
    :param mu: the population size
    :param f: the equation 1
    :param lamda: the number of children
    :param D: the D-dimensional binary vector
    :return: the best-so-far solution x_bsf and its objective function value f(x_bsf)
    '''

    t = 1  # the number of generation
    optimal_solution = f([1]*D)


    # initialize the population randomly
    P = population_initialize(mu, D)

    # Evaluate each individual x in P by func
    func_bsf = 0
    x_bsf = None
    for x in P:
        func_now = f(x)
        if func_now > func_bsf:
            x_bsf = x
            func_bsf = func_now

    while t <= N_MAX and func_bsf < optimal_solution:
        # step1: Mating selection
        ## change to Binary tournament selection
        x_a, x_b = binary_tournament_selection(P, f)

        # step2: Variation operator1: Crossover
        u = uniform_crossover(x_a, x_b, D)

        # step3: Variation operator2: Mutation
        bit_flip_mutation(u, D)

        # step4: Evaluate the child u
        t += 1

        func_now = f(u)

        # step5: Update the best-so-far solution x_bsf
        if func_now > func_bsf:
            x_bsf = u
            func_bsf = func_now

        # step 6: Environmental selection
        rand_index = random.randrange(mu)
        x_c = P[rand_index]
        if f(u) >= f(x_c):
            P[rand_index] = u

    # print(t)
    # return x_bsf, f(x_bsf)
    return t


def binary_tournament_selection(population, evalu_func):
    xd, xe, xf,xg = random.choices(population, k=4)
    if evalu_func(xd) > evalu_func(xe):
        xa = xd
    else:
        xa = xe

    if evalu_func(xf) > evalu_func(xg):
        xb = xf
    else:
        xb = xg

    return xa, xb


def bit_flip_mutation(u, D):
    pm = 1/D
    for j, uj in enumerate(u):
        if random.random() < pm:
            if uj == 0:
                u[j] = 1
            else:
                u[j] = 0


def uniform_crossover(x_a, x_b, D):
    parents = (x_a, x_b)
    u = [None] * D
    for j in range(D):
        u[j] = parents[random.randrange(2)][j]
    return u


def population_initialize(mu, D):
    return [[random.randrange(2) for _ in range(D)] for __ in range(mu)]

# for _ in range(10):
#     print(ga(10, func))

with open('/Users/wankanzhen/Desktop/GithubPage/GA_exercise/exercise3.csv', 'w') as f:
    for _ in range(100):
        f.write(str(ga(10, func)) + '\n')
