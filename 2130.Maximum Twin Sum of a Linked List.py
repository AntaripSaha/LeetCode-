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

# ✅ Core Logic
def maxSum(head):
    slow = head
    fast = head
    while fast and fast.next: # we will get mid
        slow = slow.next
        fast = fast.next.next

    prev = None
    next_node = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    first = head
    second = prev
    max_sum = 0
    while second:
        sum = first.val + second.val
        max_sum = max(sum, max_sum)
        first = first.next
        second = second.next
    print(max_sum)


# 🧪 এখন test করো
vals = [5,4,2,1]
head = build_linked_list(vals)
new_head = maxSum(head)
print_list(new_head)
