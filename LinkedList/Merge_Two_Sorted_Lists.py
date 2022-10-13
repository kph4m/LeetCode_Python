"""
Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Understand
list1 = 1->3->6->7, list2= 1->4->5->8, mergedList = 1->3->4->5->6->7->8
list1 = null, list2 = 1->2->3, mergedList = 1->2->3
list1 = null, list2 = null, mergedList = null

Match
Linkedlist Traversal, dummy node at head, pointer to keep track of dummy, pointers at each list, compare values

Plan
create dummy node to easily access the head later
create pointer to iterate through that list
while l1 and l2 aren't empty
  Check the current value the pointer is on
      Add the lower one to the mergedList, increase the pointer 1
if a list runs out, add the rest of the other list to the merged list
return the head of the dummy

Implement

Review
list1 = 1->3->4, list2 = 1->4->5->6, mergedList
1=1, mergedList = dummy -> 1
1<4, mergedList = dummy -> 1 -> 1
3<4, mergedList = dummy -> 1 -> 1 -> 3
4=4, mergedList = dummy -> 1 -> 1 -> 3 -> 4
4<5, mergedList = dummy -> 1 -> 1 -> 3 -> 4 -> 4
list1 is empty, move to if statements
add rest of list 2 to list, mergedList = dummy -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 6
return head of new list = dummy.next = 1

Evalaution
Time Complexity: We visit each node of each list once, therefore O(n+m), where n represents the size of list1 and m represents the size of list 2
Space Complexity: We create a new node list that has the sum of the size of list1 and list2, therefore O(n+m)
"""

def mergeTwoLists(list1, list2):

    # create dummy node for head retrieval later
    dummy = ListNode()

    # create new node list tail to traverse and update the values
    tail = dummy

    # list1 + list2 aren't empty
    while list1 and list2:
        # if list1.val less
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        # if list2 less
        else:
            tail.next = list2
            list2 = list2.next
        # move the tail pointer
        tail = tail.next
    
    # if one list is null, add the remaining elements of the non-empty one to the list
    if list1:
        tail.next = list1
    else:
        tail.next = list2
    
    # return the head of the new list
    return dummy.next

