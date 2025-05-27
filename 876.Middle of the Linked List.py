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
def delete_middle(head):
    if not head.next:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next
    return head

def middleNode(head):
    if not head.next:
        return head
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow




# 🧪 এখন test করো
vals = [1]
head = build_linked_list(vals)
new_head = middleNode(head)
print_list(new_head)
