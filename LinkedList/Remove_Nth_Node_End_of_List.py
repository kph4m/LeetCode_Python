"""
Remove Nth Node from End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Understand
- remove nth node from the end of the linked list

Match
- Linked List

Plan
- Create dummy node to point to the head for easy return
- Create two pointers in order to move through the linked list
    - Second pointer acts as a runner that moves n steps ahead of the second pointer
    - First pointer will be used to identify the node that needs to be removed
- Move both pointers until second reaches the end, this will maintain n gap between the first and second pointer
- Remove the node that the first pointer is pointing to by assigning the next value to the first pointer
- Return the head of the linked list

Implement

Review

Evaluate
- Time Complexity: O(n), go through each node once by the runner
- Space Complexity: O(1), only needed to add dummy node
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Create a dummy node to point to the head
    dummy = ListNode(0)
    dummy.next = head

    # Create two pointers in order to move through the linked list
    # Second pointer acts as a runner that moves n steps ahead of the second pointer
    # First pointer will be used to identify the node that needs to be removed
    first = dummy
    second = dummy

    # Move the second pointer ahead n steps
    for _ in range(n+1):
        second = second.next
        
    # Move both pointers until second reaches the end, this will maintain n gap between the first and second pointer
    while second.next:
        first = first.next
        second = second.next
    
    # When second reaches the end, first will be pointing to the node that is n nodes before the end
    first.next = first.next.next
    return dummy.next

# Testing

# Create linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Remove the 2nd node from the end
result = removeNthFromEnd(head, 2)

resultList = []
while result:
    resultList.append(result.val)
    result = result.next

print("Expected Output: [1,2,4,5]")
print("Actual Output: ", resultList)