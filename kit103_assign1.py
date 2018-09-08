#####################################################################
# KIT103/KMA155 Programming Assignment 1: Sets
# Submission script
#
# Name: Faraz Zamansani
# ID: 386070
#
# Enter your answers to each question below, replacing None with the
# code requested. Question 1 part a should be stored in ans['Q1 a']
# and so on. You can use the show_answers() function from inside the
# IPython console to show the result of your answers when you run
# this script to evaluate all your answers.
# A suggestion: Run the script first, then work out the answers in
# the IPython interactive console before pasting them back here.

ans = {} #an empty dictionary of answers
def show_answers(show_all=True):
    '''Prints the calculated answers to all questions.
    This function is included because it may be useful to you in
    checking your answers, but you are not required to use it.
    '''
    for a in sorted(ans):
        if show_all or ans[a] is not None:
            print('%s: %s' % (a, str(ans[a]) if ans[a] is not None else 'unanswered'))


# Question 1: Set literals

ans['Q1 a'] = {2,4,6,8,10} 
ans['Q1 b'] = {'John','Cameron','Connor','James'}
ans['Q1 c'] = {'a','e','i','o','u'}

# Question 2: Set comprehensions

ans['Q2 a'] = {x*7 for x in range(1, 6) }
ans['Q2 b'] = {x^3 for x in range (1,6)}
ans['Q2 c'] = {'m','i','s','s','i','s','s','i','p'}

# Question 3: Relationships

# Given these definitions provide code to answer the questions from the assignment sheet.
animals = {'camel', 'cow', 'crayfish', 'chameleon', 'giraffe', 'horse', 'salmon', 'worm'}
mammals = {'camel', 'cow', 'giraffe', 'horse'}
aquatic = {'crayfish', 'salmon'}
farmed = {'horse', 'salmon', 'worm'}
caught = {'ball', 'camel', 'horse', 'crayfish', 'salmon'}

ans['Q3 a'] = mammals.issubset(animals)
ans['Q3 b'] = farmed.issubset(mammals)
ans['Q3 c'] = caught.issubset(aquatic)


# Question 4: Set membership

ans['Q4 a'] = mammals-farmed
ans['Q4 b'] = animals&farmed
ans['Q4 c'] = farmed&caught-mammals


# Question 5: Combinations

# Given these definitions, generate the combinations requested in the assignment sheet.
intensities = { 'sedate', 'extreme' }
activities = { 'BASE jumping', 'ironing', 'lecture watching', 'skiing' }
clothing = { 'in pyjamas', 'in a wetsuit', 'in a tuxedo' }

ans['Q5 a'] = {(i1,i2) for i1 in intensities for i2 in activities}
ans['Q5 b'] = {(i1,i2) for i1 in activities for i2 in activities}
ans['Q5 c'] = {(i1,i2,i3) for i1 in intensities for i2 in activities for i3 in clothing}

# Question 6: Bags & Bitsets
# When checking these, note that parts (b)-(e) will look like normal decimal numbers, even though you will have entered binary literals in yours answer to (b)-(d). A binary literal is just another way of expressing an integer value.

ans['Q6 a'] = {'dog','mouse''cat','mouse','dog','dog'}
ans['Q6 b'] = 0b00110
ans['Q6 c'] = 0b10101
ans['Q6 d'] = 0b10111
ans['Q6 e'] = ans['Q6 b'] & ans['Q6 c']

#End of answers
