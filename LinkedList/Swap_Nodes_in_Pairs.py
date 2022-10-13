"""
Swap Node in Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Understand
Swap adjancent pairs and return head
Even length
  1->2->3->4 = 2->1->4->3, return 2
Odd length
  5->1->3 = 1->5->3, return 1
One node
1, return 1

Match
Linkedlist, Dummy node, traverse linkedlist, swap nodes

Plan
check if head exists, if not return nothing
create dummy node, cur node
while theres a cur node and cur.next node (pairs)
  swap them
  change cur node to next next node

Implement

Review
1->3->2->4
0->1->3->2, dummy = 0, dummy.next = 1, cur = 0
cur.next (1) exists, cur.next.next (3) exists
  (1) 0->3->1->2, first = 1, second = 3, first.next = 2 (1->2), second.next = first (3->1), cur.next = second (3), cur.next.next = first (1), cur = 1
  (2) 0->3->1->4->2, first = 2, second = 4, first.next = None (2->None), second.next = first (4->2), cur.next = second (4), cur.next.next = first (2), cur = 2
  (3) cur.next and cur.next.next doesn't exist, break
Output: 0->3->1->4->2, return 3

Evaluate
Time Complexity: Traversing all nodes in the linked list, O(n)
Space Complexity: Swapping nodes in the linked list, no creation of other data structures, O(1)
"""

def swapPairs(head):

    # check if head exists
    if head == None:
        return None

    # create Dummy Node
    dummy = ListNode(0)

    # set dummy next to head
    dummy.next = head

    # cur node to traverse the linked list
    cur = dummy

    # while pair exists
    while cur.next and cur.next.next:
        # get first node
        first = cur.next

        # get second node
        second = cur.next.next

        # assign first next to second next
        first.next = second.next

        # assign second next to first
        second.next = first

        # assign first node to second
        cur.next = second

        # assign second node to first
        cur.next.next = first

        # move pointer to next first pair node
        cur = cur.next.next

    # return head
    return dummy.next