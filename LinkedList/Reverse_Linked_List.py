"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Understand
- given only the head, reverse the singly linked list and return the head
- 1->2->3->4 = 4->3->2->1

Match
- LinkedList

Plan
- check if head exists
- create two pointers: prev and cur
- set cur.next to prev
- set prev to cur
- set cur to the original cur.next

Implement

Review
- 1->2->3->None
- prev = None, cur = 1
    - nxt = 2
    - cur.next = None
    - prev = 1
    - cur = 2
    - 1->None
- prev = 1, cur = 2
    - nxt = 3
    - cur.next = 1
    - prev = 2
    - cur = 3
    - 2 -> 1 -> None
- prev = 2, cur = 3
    - nxt = None
    - cur.next = 2
    - prev = 3
    - cur = None
- cur is None, get out of while loop
- return current head = 3

Evaluate
- Time Complexity: O(n) - go through every node in the LinkedList
- Space Complexity: O(1) - didn't create any data structures
"""

def reverseList(head):
    if not head:
        return None
    
    prev, cur = None, head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    
    return prev