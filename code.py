class Solution:
    def isPalindrome(self, head):
        vals = []
        while head:
            vals += head.val,
            head = head.next
        return vals == vals[::-1]

