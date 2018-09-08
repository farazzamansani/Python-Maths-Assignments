'''
KIT103/KMA155 Programming Assignment 5: Permutations and Combinations
Submission script

Name: 
ID: 

Enter your answers to each question below either by replacing the
value None with a short piece of Python code that will calculate or
generate the answer or, in the case of Question 4, replacing the
body of the two functions with your implementation. After answering
a question run this script and test your implementation in the
IPython console.
'''

from itertools import combinations, permutations, product
from scipy.misc import comb, factorial
def fact(n):
    '''Returns the exact, integer value of n!'''
    return factorial(n, exact=True)

# Answers that can be calculated by single lines of code will be stored in
# this dictionary. Question 4's answers will be in the form of functions.
value_ans = {}

# Question 1: Permutations (1 mark)

value_ans['q1 a'] = pow(4,3)
#we could use q1 b with len() to find size aswell
value_ans['q1 b'] = { ''.join(p) for p in product('AUGC', repeat=3) }
value_ans['q1 c'] = fact(6)/fact(3)
#could use q1 d with len() to find size aswell
value_ans['q1 d'] = { p for p in permutations(['dog','cat','pat','hit','fit','kit'], 3) }

# Question 2: Combinations (1 mark)

# If you use this list then your answers will be in the same order as the test program
weather = [ 'dry', 'wet', 'humid', 'cold', 'hot', 'mild' ]
students = { 'Tech %d' % i for i in range(1, 16) }

value_ans['q2 a'] = comb(6,2,exact=True)
value_ans['q2 b'] = { p for p in combinations(weather,2) }
value_ans['q2 c'] = comb(15,5,exact=True)
value_ans['q2 d'] = { k for k in combinations(students,5) }

# Question 3: You choose which (2 marks)

from string import ascii_uppercase
titles = set( ascii_uppercase[:26] )

value_ans['q3 a'] = { p for p in combinations(titles,4) }
value_ans['q3 b'] = comb(26,4,exact=True)
value_ans['q3 c'] = { p for p in permutations(titles,4) }
value_ans['q3 d'] = fact(26)/fact(26-4)

# Question 4: Words are mighter than the sword (1 mark)

def word_perms(word):
    '''Returns the set of all permutations of the letters in `word`.'''
    return {''.join(p) for p in permutations(word) }

def anagrams(word):
    '''Returns the set of all anagrams of `word` (provided it is
    between 2 and 10 characters in length). Behaviour if it is shorter
    or longer than that is unspecified.
    '''
    i=1#used in loop we have word in list starting at 1
    j=2#this is used for loop as word length, dictionary is words length 2-10
    output=""#output starts as empty string
    perms=word_perms(word)
    while j<10:
        while i<len(word_lists[j]):
            if word_lists[j][i] in perms:
                #print word_lists[j][i]
                #if word exists in both we add it onto the output string
                output=output+word_lists[j][i]+","
            i=i+1
        j=j+1
    return output

# Needed for Question 4

from os.path import isfile

def load_words():
    name = 'words.2-10.txt'
    if isfile(name):
        all_words = [ l.rstrip() for l in open(name, 'r') ]
        as_lists = {}
        for size in range(2, 11):
             as_lists[size] = [ word for word in all_words if len(word) == size ]
        as_sets = { size : (set(words) if words else None) for size, words in as_lists.items() }
        return as_lists, as_sets
    return None, None

word_lists, word_sets = load_words()
# Usage examples (note that you do not necessarily need to use both word_lists and word_sets):
# word_lists[2] is a list of the two-letter words
# word_sets[9] is a set of the nine-letter words

# End of things needed for Question 4
