"""
Middle of Linked List

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Understand
- given head, return the middle of the linkedlist
- if two middle nodes, return the second one
- 1->2->3 = 2
- 1->2->3->4 = 3

Match
- Linked List
- Slow and Fast pointer
    - slow will reach the middle when fast reaches the end of the linkedlist

Plan
- create fast and slow pointer
- while fast and fast.next exists
    - move the slow pointer one
    - move the fast pointer two
- return the slow pointer when fast and fast.next cease to exist

Implement

Review
1->2->3->4
- slow = 1, fast = 1
- fast and fast.next exist, slow = 2, fast = 3
- fast amd fast.next exist, slow = 3, fast = null
- fast and fast.next don't exist, return 3

Evaluate
- Time Complexity: O(n) - iterate through the entire linked list
- Space Complexity: O(1) - just traversing the linked list

"""

def middleNode(head):

    if not head:
        return None

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
    