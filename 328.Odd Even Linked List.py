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

# ✅ Core Logic (slow-fast pointer দিয়ে middle delete)
def oddEven(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head



# 🧪 এখন test করো
vals = []
head = build_linked_list(vals)
new_head = oddEven(head)
print_list(new_head)
