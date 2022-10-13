"""
Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Understand
- there's a cycle if a node is pointing to a previous node

Match
- Linked List

Plan
- base case: if head doesn't exist, return False
- use Floyd's Cycle Detection algorithm
    - create fast and slow pointer
    - while fast != slow
        - if fast.next or fast.next.next == Null, return False
        - slow = slow.next
        - fast = fast.next
    - return True

Implement

Review
- 3 -> 2 -> 0 -> 4 -> 2 -> 0
- slow = 3, fast = 2
- slow = 2, fast = 4
- slow = 0, fast = 0, return True

Evaluate
- Time Complexity: O(n), going through possibly each node 
- Space Complexity: O(1), not using any data structs
"""

def hasCycle(head):

    if not head:
        return False

    slow, fast = head, head.next

    while slow != fast:
        # if fast.next or fast.next.next is None, no cycle
        if fast.next == None or fast.next.next == None:
            return False

        # move slow pointer one
        slow = slow.next

        # move fast pointer two
        fast = fast.next.next

    return True