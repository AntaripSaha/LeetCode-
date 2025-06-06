class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# 🔧 Helper: List থেকে Linked List বানাও
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        next_node = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev



# 🧪 এখন test করো
vals = [1, 3, 4, 7, 1, 2, 6]
head = build_linked_list(vals)
# rv = Solution()
# new_head = rv.reverseList(head)
new_head = Solution().reverseList(head)
print_list(new_head)
