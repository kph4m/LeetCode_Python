"""
Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


Understand
- given list of linkedlists, return linkedlist that combines them in sorted order

Match
- Merge 2 linkedlists, Divide and conquer

Plan
Brute force
- use mergeTwoLists alg to go through the lists and merge each list into a bigger one

Divide and conquer
- merge halves, then combine them at the end

Implement

Review
[[1,4,5],[1,3,4],[2,6]]

Merge [1,4,5], [1,3,4]
[1,1,3,4,4,5]

Merge [1,1,3,4,4,5] and [2,6]
[1,1,2,3,4,4,5,6]

Return [1,1,2,3,4,4,5,6]

Evaluate

Brute Force
- Time Complexity: O(n*m), n = length of lists, m = length of merged list
- Space Complexity: O(1), don't use any data structures


Divide and Conquer
- Time Complexity: O(m*logn), n = length of lists, m = length of merged list
- Space Complexity: O(log(n)), recursive calls
"""
def mergeKLists(lists):
    # Brute force
    # if not list:
    #     return None
    # if len(list) == 1:
    #     return lists[0]

    # output = lists[0]

    # for i in range(1, len(lists)):
    #     output = merge2Lists(output, lists[i])

    # return output

    # Divide and conquer
    if not lists:
        return []
    
    if len(lists) == 1:
        return lists[0]
    
    if len(lists) == 2:
        return merge2Lists(lists[0], lists[1])

    mid = len(lists) // 2
    left = self.mergeKLists(lists[0:mid])
    right = self.mergeKLists(lists[mid:])

    return merge2Lists(left,right)
def merge2Lists(list1, list2):

    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1.next = list1
        else:
            current.next = list2
            list2.next = list2
        # move tail pointer
        current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next
    


    
