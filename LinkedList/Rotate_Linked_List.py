"""
Rotate Linked List

Given the head of a linked list, rotate the list to the right by k places.


Understand
- Rotate the list right k number of times
- 1 -> 2 -> 3, k = 2
    - 2 -> 3 -> 1
- 1 -> 2 -> 3, k = 6
    - 1 -> 2 -> 3

Match
- Circular Linked List

Plan
- make linked list circular
- find the node that we want to cut off from, cut it off
    - k % length of linkedlist - 1

Implement

Review
- 1 -> 2 -> 3
- length = 3
- 1 -> 2 -> 3 -> 1
- cutoffpoint = 3 - (2%3 = 2) - 1 = 0
    - at 1
- answer = 2, remove 1 -> 2 connection
- final linked list: 2 -> 3 -> 1
- return 2

Evaluate
- Time Complexity: O(n) - iterate through entire linkedlist to find length, O(n) - worse case cut off point is length(list) - 1, O(n) + O(n) = O(2n) -> O(n)
- Space Complexity: O(1) - don't use any data structures
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateList(head, k):
    if not head:
        return head

    # Used to find the node to cut off from
    length = 1

    # Store last node
    lastNode = head

    # Traverse linkedlist to get to the end to make a circular linked list
    while lastNode.next:
        lastNode = lastNode.next
        length +=1

    # Connect to head node
    lastNode.next = head

    cutOffPoint = length - (k % length) - 1

    cutOffNode = head

    # Traverse linkedlist to cutoffpoint
    for i in range(cutOffPoint):
        cutOffNode = cutOffNode.next

    # Get new head before cutoff
    answer = cutOffNode.next

    # Cutoff
    cutOffNode.next = None

    return answer
    
# 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print("Expected Output: 2")
print("Actual Output: ", rotateList(head, 2).val)