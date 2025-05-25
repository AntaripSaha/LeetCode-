head = [1,2,3,4,5]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            next_node = current.next  # আগের নোড ধরে রাখছি
            current.next = prev       # বর্তমান নোডের next pointing উল্টো করে দিচ্ছি
            prev = current            # prev কে আপডেট করছি
            current = next_node       # current কে সামনে এগিয়ে নিচ্ছি

        return prev  # prev এখন নতুন head
