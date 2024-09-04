class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: ListNode) -> bool:

    seen_nodes = set()

    current = head
    while current:

        if current in seen_nodes:
            return True

        seen_nodes.add(current)

        current = current.next

    return False
