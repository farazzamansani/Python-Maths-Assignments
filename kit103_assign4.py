#####################################################################
# KIT103/KMA155 Programming Assignment 4: Number Theory part 2
# Submission script
#
# Name: Faraz Zamansani
# ID: 386070
#
# Enter your answers to each question below by completing each
# function. After answering a question run this script and test
# your implementation in the IPython console.


# Question 1: The multiplicative inverse (1.5 marks)

#Define your additional function here


def q1_mod_inverse(a, n):
    g, x, y = egcd(a, n)
    if g != 1:
        return None
    else:
        return x % n

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# Question 2: The Affine Cipher (2 marks)
from string import ascii_lowercase as lowercase

def q2_affine_encrypt(message, k1, k2, symbols):
    '''Encrypts message using an affine cipher with multiplicative
    key k1 and shift key k2; ignores any character not in symbols.
    '''
    ciphertext = ''
    for m in message:
        if m in symbols:
            m_index = symbols.find(m)
            c_index = m_index #<-- You must replace m_index with the encryption expression
            ciphertext += symbols[c_index]
    return ciphertext
    
def q2_affine_encrypt2(message, k1, k2, symbols):
    '''Encrypts message using an affine cipher with multiplicative
    key k1 and shift key k2; ignores any character not in symbols.
    '''
    ciphertext = ''
    for m in message:
        if m in symbols:
            m_index = symbols.find(m)
            c_index = (k1*m_index+k2)%len(symbols)#<-- You must replace m_index with the encryption expression
            ciphertext += symbols[c_index]
    return ciphertext


def q2_affine_decrypt(ciphertext, k1, k2, symbols):
    '''Decrypts ciphertext using an affine cipher with multiplicative
    key k1 and shift key k2; ignores any character not in symbols.
    '''
    message = ''
    for m in ciphertext:
        if m in symbols:
            m_index = symbols.find(m)
            kinvert=q1_mod_inverse(k1,len(symbols))
            c_index =((m_index-k2)*kinvert)%len(symbols)
            message += symbols[c_index]
    return message



# Question 3: base2base (1.5 marks)

from string import ascii_uppercase as capitals
digits = [ str(i) for i in range(0, 10) ] + [ c for c in capitals[:26] ]

#Declare any additional helper function here
def dec2other(d, base):
    n = '' #empty string
    q = d
    while q != 0:
        q, r = divmod(q, base)
        n = digits[r]+n
    return n if len(n) > 0 else '0' #d==0 is special case

def q3_base2base(n, b1, b2):
    '''Converts n, a string representing a number in base b1, to a
    string representing the same value in base b2. 2 <= b1, b2 <= 36.
    '''
    return dec2other(int(n,b1),b2) #only works on base 11 or higher







# End of answers
