"""
Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Understand
- add the two numbers from the linkedlist in reverse order and return the sum as a linked list

Match
- Linked List

Plan
- loop through and add the values
- create new node for the sum
- account for remainder and node value

Implement

Review

Evaluate
- Time Complexity: O(n), where n is the length of the longer linked list
- Space Complexity: O(n), adding a new node for each node in the long linked list

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    cur = dummy
    carry = 0

    while l1 or l2 or carry:
        # get values from each linked list, or 0 if there are no more nodes
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        print(v1, v2, carry)

        # total sum
        sum = v1 + v2 + carry

        # value for the node calculated using modulo
        # ex: 12 % 10 = 2
        nodeVal = sum % 10

        # update carry if any calculated using floor division
        # ex: 12 // 10 = 1
        carry = sum // 10

        # create new node with the sum
        cur.next = ListNode(nodeVal)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

# Testing

# Create first linked list
head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(3)

# Create second linked list
head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)

result = addTwoNumbers(head, head2)

resultList = []
while result:
    resultList.append(result.val)
    result = result.next

print("Expected Output: [7,0,8]")
print("Actual Output: ", resultList)