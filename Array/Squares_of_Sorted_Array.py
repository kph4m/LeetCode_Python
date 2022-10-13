"""
Understand: 
-QUESTION: Given an array of integers A sorted in non-decreasing order, return a new array of the squares of each number, also in sorted non-decreasing order 
-Arrays can be of any length 
-Integers may be negative 
-Non-decreasing implies that some ints can be duplicates (i.e [0, 0, 0]) 

Match: 
-Lists 
-Pointers (left and right)

Plan:

-If the array has a length of 1: 
--Return number squared 

-If the array has a length of 0: 
--Return nothing

-If the array has no negative numbers (check array[0] !< 0): 
--Simply step through the array, square values and put them in returning list
[1 , 5, 10] 
[1, 25, 100]  

-If the array has ALL negative numbers (if array[length-1] <= 0):
--Simply step through the array starting from the LAST INDEX, square values and put them in returning list  

-If the array as at least one negative number: 
--Find the center of the array based on array length: 
--- Center: length // 2

--Place left and right at the center index. Move left back one index. 
--If abs(left) < abs(right), left^2 is added to new array. 
---Check if NOT at the end of list, then Left decrements -1. 
---Else, print all remaining right values

--Else if abs(right) < abs(left), right^2 is added to new array. 
---Check if at the end of list, Right increments +1 
---Else, print all remaining Left values 

--Else (if Left and Right are the same): 
---Add left's value twice. Then decrement left and increment right (both 1).

[-4,-1,0, 10, 11 12 ] 
 L         R 
[0, 1, 4 ] 

[-4,0,0, 10] 
    L R 
[] 


[-4, -3, -2, 0] 
[0, 4, 9, 16]
""" 

def sort_square(list): 
    #Edge cases
    if list == None: 
    return;

    length = len(list); 


    if (length == 0): 
    return []; 

    if (length == 1): 
    return [list[0]**2] 

    new_list = [];

    #All pos or negative tests: 
    if (list[length-1] <= 0): #all negative 
    for i in range(length-1, -1, -1):
        new_list.append(list[i]**2) 
    return new_list;

    elif (list[0] >= 0): #all positive
    for i in range(length):  
        new_list.append(list[i]**2) 
    return new_list;

    center = length // 2; #// floors, accounting for index starting at 0 
    left = center-1; 
    right = center;


    while (left != -1 and right != length): #while not out of bounds
    if abs(list[left]) < abs(list[right]): #if left is less
        new_list.append(list[left] **2); 
        left -= 1; 

    elif abs(list[right]) < abs(list[left]): #if right is less
        new_list.append(list[right] **2); 
        right += 1; 

    else: #if left == right
        new_list.append(list[right] **2); 
        new_list.append(list[right] **2); 
        left -= 1; 
        right += 1;

    if (left == -1): #if left is out of bounds
    while (right != length): 
        new_list.append(list[right] **2); #fill from right
        right += 1; 

    if (right == length): #if right is out of bounds
    while (left != -1): 
        new_list.append(list[left] **2); #fill from left 
        left -= 1;

    return new_list
# all positive
# [1,25,100]
print(sort_square([1 , 5, 10]))

# pos and neg
# [0,1,16,100,121,144]
print(sort_square([-4, -1, 0, 10, 11, 12]))

# all negative
# [0,4,9,16]
print(sort_square([-4, -3, -2, 0]))

# dups
# [0,4,4,4,9,16]
print(sort_square([-4, -3, -2, -2, -2, 0]))