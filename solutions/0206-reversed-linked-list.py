"""206. Reverse Linked List  ·  https://leetcode.com/problems/reverse-linked-list/
TWO APPROACHES | COMPLEXITY
----------
reverseList:        Time O(n), Space O(1) — three references, no matter the
                     list's length.
reverseListValues:  Time O(n), Space O(n) — the `items` list holds every
                     value at once.
"""


class ListNode:
    """LeetCode provides this; defined here so the tests below can build and
    walk lists on their own."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """Approach 1 — flip the pointers. O(1) space."""
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def reverseListValues(self, head: ListNode | None) -> ListNode | None:
        """Approach 2 — copy values only; nodes and links never move."""
        if head is None:
            return None

        items = []
        iteration = head
        while iteration is not None:
            items.append(iteration.val)
            iteration = iteration.next

        iteration = head
        while len(items) > 0:
            iteration.val = items[-1]
            iteration = iteration.next
            items.pop()

        return head


# ---------------------------------------------------------------- tests
def build(vals: list[int]) -> ListNode | None:
    head = None
    tail = None
    for v in vals:
        node = ListNode(v)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def to_list(head: ListNode | None) -> list[int]:
    """Walk with a step cap so a cycle (a real bug we hit) fails loudly
    instead of hanging the test run forever."""
    out = []
    node = head
    steps = 0
    while node is not None:
        steps += 1
        if steps > 10_000:
            raise AssertionError("cycle detected — list did not terminate")
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    import random

    sol = Solution()

    # 1. the examples from the problem
    for method in (sol.reverseList, sol.reverseListValues):
        assert to_list(method(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
        assert to_list(method(build([1, 2]))) == [2, 1]
        assert to_list(method(build([]))) == []

    # 2. edge cases: single node, two nodes, duplicate values
    for method in (sol.reverseList, sol.reverseListValues):
        assert to_list(method(build([7]))) == [7]
        assert to_list(method(build([1, 1, 1]))) == [1, 1, 1]
        assert to_list(method(build([-3, 0, 3]))) == [3, 0, -3]

    # 3. reverseList specifically: check the RETURNED node is really the old
    #    tail, and the old head's .next is really None (not just that the
    #    values print correctly)
    head = build([1, 2, 3])
    old_tail_id = id(head.next.next)          # node holding 3, before reversal
    old_head_id = id(head)                     # node holding 1, before reversal
    new_head = sol.reverseList(head)
    assert id(new_head) == old_tail_id, "returned head should be the old tail node"
    # walk to find the node that used to be the head; it must now be the tail
    node = new_head
    while node.next is not None:
        node = node.next
    assert id(node) == old_head_id, "old head node should now be the tail"
    assert node.next is None

    # 4. property test: random-length lists, reversed values checked against
    #    Python's own reversed(), for both approaches
    random.seed(0)
    for _ in range(20_000):
        vals = [random.randint(-10**4, 10**4) for _ in range(random.randint(0, 60))]
        for method in (sol.reverseList, sol.reverseListValues):
            result = to_list(method(build(vals)))
            assert result == list(reversed(vals)), (vals, result)

    print("all passed")