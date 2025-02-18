import random

def simulate(disease_rate, false_positive_rate, n):
    ## Assume: disease_rate is the probability of having a particular disease;
    ##         all people who have the disease test positive;
    ##         false_positive_rate is the probability of testing positive if you don't have the disease.
    
    ## Simulate the testing process in a population of n people.
    ## Return the list of sick people together with the number of positive tests.

    positive_tests = 0
    sick_individuals = []
    
    for i in range(1, n + 1):
        if random.random() < disease_rate:
            positive_tests += 1
            sick_individuals.append(i)
            continue
        
        if random.random() < false_positive_rate:
            positive_tests += 1
        
    return sick_individuals, positive_tests
    
    return [], 0