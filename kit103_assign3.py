# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#####################################################################
# KIT103/KMA155 Programming Assignment 3: Number Theory part 1
# Submission script
#
# Name: faraz zamansani
# ID: 386070
# Enter your answers to each question below by completing each
# function. After answering a question run this script and test
# your implementation in the IPython console.


# Question 1: Divisibility of really, really big integers (2 marks)

def divisible_by_2(s):
    '''Returns True if the number represented by the string s is divisible by 2, False otherwise.'''
    i=s[-1]
    if int(i)%2==0:
        return True
    else:
        return False


def divisible_by_3(s):
    '''Returns True if the number represented by the string s is divisible by 3, False otherwise.'''
    if sum(map(int, str(s))) % 3 == 0:
        return True
    else:
        return False

def divisible_by_4(s):
 '''Returns True if the number represented by the string s is divisible by 4, False otherwise.'''
 i=s[-2:]
 if int(i)%4==0:
    return True
 else:
    return False


def divisible_by_11(s):
    '''Returns True if the number represented by the string s is divisible by 11, False otherwise.'''
    i=s[-1]
    i=int(i)*10
    j=int(s[:-1])
    x=j+i
    if x%11==0:
     return True
    else:
     return False



# Question 2: GCD from a prime factorisations (2 marks)

from collections import Counter


def q2_factor_gcd(a,b):
    c=Counter(factor_list(a))
    d=Counter(factor_list(b))   
    g=(c & d)
    try:
     maxg=max(g)
    except ValueError:
        return 1
        
    sol=1
    for i in range(maxg+1):
        if g[i]!=0:
         k=g[i]
         sol=sol*(i**k)
    return sol
    


# Question 3: Are a and b coprime (i.e., relatively prime)? (1 mark)

#Declare any addtional helper function here

def q3_coprime(a, b):
    '''Returns True if a and b are coprime, False otherwise.'''
    return helper_function(a,b)

def helper_function(a,b):
    for i in range(2, min(a,b)+1):
        if a%i==0 and b%i==0:
            return False
        else:
            return True

# End of answers


# Provided functions

from math import sqrt

def primes(n):
    primes = set(range(2, n+1))
    for k in range(2, int(sqrt(n))+1):
        if k in primes:
            primes.difference_update( range(k**2, n+1, k) )
    return primes

def primes_list(n):
    return sorted(primes(n))

def factor_list(n):
    factors = []
    iprimes = iter( primes_list(n) )
    while n > 1:
        p = next(iprimes)
        while n % p == 0:
            n = n / p
            factors.append(p)
    return factors

# End of provided functions
