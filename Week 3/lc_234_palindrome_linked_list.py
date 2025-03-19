# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find middle with slow/fast
        if not head: return head
        if not head.next: return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse everything after slow
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        i, j = head, prev
        while i and j:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next
        return True