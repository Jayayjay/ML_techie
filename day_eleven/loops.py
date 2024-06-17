




'''For Loops for iteration over a given sequence using the "range" and 'xrange" functions'''
# primes = [2,3,5,7]
# for i in primes:
#     print(i)

# Range
#prints out the range 
# for x in range(5):
#     print(x)

# # specification of the starting point and end point
# for x in range (3,6):
#     print(x)

# Note: The range function is zero based


#While Loops
'''WHile loops repeat as long as a certain boolean condition is met'''
# count = 0 
# while count < 5:
#     print(count)
#     count += 1 # THis is the same as count = count + 1


#Break and continue statements 
'''Break is used to exit a for or while loop, whereas continue is used to skip the current block and return to the "for" or "while" statement'''

# count = 0 
# while True:
#     print(count)
#     count += 1 
#     if count >= 5: 
#         break

# for x in range(10):
#     # check is x is even 
#     if x % 2 == 0:
#         continue
#     print(x)

# # Nested loops
"""Python sllows the use of one loop. the inner loop will be executed one time for each iteration of the outer loop
Example:"""
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
# groups = [['Jobs', 'Gates'], ["Newton", "Euclid"], ["Enstine", "Feynman"]]
# # this outer loop will iterate over each list in the groups list 
# for group in groups:
#     # THis inner loop will go through each name in each list 
#     for name in group:
#         print(name)

'''Loop Control Statements
Break
This terminates the loop statement and transfers execution to the statement immediately following the loop

continue
theis causes teh loop to skip the remainder of its body and immediately retest its condition prior to reiterating 

Pass
Does nothing'''

# Break
for letter in "Statement":
    if letter == "m":
        break
    print(letter)


# Continue 
for letter in "Un known ":
    if letter ==" ":
        continue
    print(letter)

# Loops with the Else clause
for i in range(5):
    print(i)
else:
    print("Loop finished successfully")

count = 0 
while count < i :
    print(count)
    count += 1 

else:
    print("While loop finished successfully")



# for letter in "Python":
#     print(letter)

# student_scores = {"Alice": 85, "Bob": 78, "Charlie": 92}
# for student in student_scores:
#     print(student, student_scores[student])

# count = 0
# while count < 5:
#     count += 1
#     if count == 3:
#         continue
#     print(count)