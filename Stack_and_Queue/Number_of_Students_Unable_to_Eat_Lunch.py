"""
Number of Students Unable to Eat Lunch

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]

students = [1,1,0,0,1], sandwiches = [0,0,0,1,1]
students = [1,0,0,1,1], sandwiches = [0,0,0,1,1]
students = [0,0,1,1,1], sandwiches = [0,0,0,1,1]
students = [0,1,1,1], sandwiches = [0,0,1,1]
students = [1,1,1], sandwiches = [0,1,1]
Output: 3

Understand
- first element is always the front of the queue
- if student prefers the sandwich on top of the stack, they will take it and leave the queue
- if student doesn't prefer the sandwich on top of the stack, they will leave it and go to the queue's end
- return the number of students that are unable to eat

Match
- Stack, Queue

Plan
- Create count variables for each type of student preference OR Create a dictionary where key = student preference, value = number of students with that preference 
- Loop through the students and decrement the count for the student preference
    - if the count for the student preference is 0, there are no other students that can eat the sandwich thats currently in the queue so the queue of sanwiches wont be able to be cycled through
- Return the sum of the number of students that have a preference of 0 and 1

Implement

Review

Evaluate
"""
# Count Variables
# Time Complexity: O(n), where n is the length of sandwiches and students
# Space Complexity: O(1), count variables are constant space
def countStudents(students, sandwiches):
        squareStudents = roundStudents = 0

        # Get count of all student preferences
        for student in students:
            if student == 0:
                squareStudents += 1
            else:
                roundStudents += 1
        
        for sandwich in sandwiches:
            if sandwich == 0:
                # if the count of the student preference for the current sanwich is 0, there are no other students that can eat the sandwich thats currently in the queue so the queue of sanwiches wont be able to be cycled through
                if squareStudents == 0:
                    break
                else:
                    # decrement when student able to get their preference
                    squareStudents -= 1
            elif sandwich == 1:
                # if the count of the student preference for the current sanwich is 0, there are no other students that can eat the sandwich thats currently in the queue so the queue of sanwiches wont be able to be cycled through
                if roundStudents == 0:
                    break
                else:
                    # decrement when student able to get their preference
                    roundStudents -= 1
        
        # Return the total number of students without lunch. 
        return roundStudents + squareStudents

# Using Counter
# Time Complexity: O(n), where n is the length of the sandwiches array
# Space Complexity: O(k), where k is the number of unique student preferences
from collections import Counter
def countStudents(students, sandwiches):
    studentPreferenceCount = Counter(students)

    for sandwich in sandwiches:
        # if the count of the student preference for the current sanwich is 0, there are no other students that can eat the sandwich thats currently in the queue so the queue of sanwiches wont be able to be cycled through
        if studentPreferenceCount[sandwich] == 0:
            break
        studentPreferenceCount[sandwich] -= 1

    return studentPreferenceCount[0] + studentPreferenceCount[1]

# Not Using Counter: Have to account for missing key values
# Little bit slower
# Time and Space Complexity: same as above
from collections import Counter
def countStudents(students, sandwiches):

    # Create dictionary where key = student preference, value = number of students with that preference
    studentPreferenceCount = {}
    for student in students:
        if student not in studentPreferenceCount:
            studentPreferenceCount[student] = 1
        else:
            studentPreferenceCount[student] += 1

    for sandwich in sandwiches:
        if sandwich not in studentPreferenceCount.keys():
            break
        # if the count of the student preference for the current sanwich is 0, there are no other students that can eat the sandwich thats currently in the queue so the queue of sanwiches wont be able to be cycled through
        if studentPreferenceCount[sandwich] == 0:
            break
        studentPreferenceCount[sandwich] -= 1

    return sum(studentPreferenceCount.values())

# Testing
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]

print("Expected Output: 3")
print("Actual Output: ", countStudents(students, sandwiches))

students = [1,1,0,0]
sandwiches = [0,1,0,1]

print("Expected Output: 0")
print("Actual Output: ", countStudents(students, sandwiches))

students = [1,1]
sandwiches = [0,1]

print("Expected Output: 2")
print("Actual Output: ", countStudents(students, sandwiches))