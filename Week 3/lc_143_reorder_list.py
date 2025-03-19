# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find middle with slow/fast
        if not head or not head.next: return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse everything after slow
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Merge the two linked list according to the question
        # i = i_0, i_1, i_2 ...
        # j = i_n, i_n-1,
        i, j = head, prev
        while j.next:
            i.next, i = j, i.next
            j.next, j = i, j.next