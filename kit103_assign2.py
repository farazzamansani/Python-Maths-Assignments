#####################################################################
# KIT103/KMA155 Programming Assignment 2: Logic
# Submission script
#
# Name:  Faraz Zamansani
# ID:  386070
#
# Enter your answers to each question below by completing each function
# or, in the case of Question 4a, filling in the Karnaugh map.
# After answering a question run this script and test your implementation.

# Question 1: Riding the Parabola

def q1_parabola_check(height,age,has_adult):
 if height>120 and height<200:
   if age<7:
    return 'Sorry, you cannot ride'
   elif age>=7:
            if has_adult==True:
                return 'You can ride'
            else:
                return 'Find an adult'
   elif age>9:
            return'You can Ride'
 else:
     return 'You cannot Ride'



# Question 2: Implementing predicates as functions


def q2_a(a, b, c, d):
   a = not a or not b or not c
   return a or d

def q2_b(a, b):
    c=a and b
    d=a or b
    return not c or d


def q2_c(a, b, c):
    b = a and b
    c = a and c
    return b or c


def q2_d(a):
    return a and not a


# Question 3: Simplifying predicates

def q3_a(a, b, c, d):
    return not a or not b or not c or d

def q3_b(a, b):
    return a^b

def q3_c(a, b, c):
    b=b and c
    return a and b

def q3_d(a):
    return False


# Question 4: Simplifying a predicate using a Karnaugh map

#Part a: Digit Detector Karnaugh Map --- replace the appropriate 0 entries with 1 (representing True)
q4_kmap = [
#cd\ab
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1]
]

#Part b: The detector function
def q4_acme_digit_detector(a, b, c, d):
    '''Returns True iff the curves present resemble a digit, False otherwise.'''
    #Your task is to replace this with an equivalent but simpler expression.
    # If you wish to split your expression over multiple lines then use a
    # slash \ at the end of each line, as below.
    return (a and d) or \
            (d and not a and b) or \
            (b and c and not d)

#End of answers
