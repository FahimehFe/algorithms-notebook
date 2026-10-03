"""876. Middle of the Linked List  ·  https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node.
If there are two middle nodes, return the second one.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

TWO APPROACHES
--------------
    middleNodeUsingList  — store every node, index the middle.   O(n) space
    middleNode           — two pointers, different speeds.       O(1) space

COMPLEXITY
----------
middleNodeUsingList:  Time O(n), Space O(n) — every node stored once.
middleNode:           Time O(n), Space O(1) — two pointers, nothing else.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNodeUsingList(self, head: ListNode | None) -> ListNode | None:
        """Approach 1 — store every node, index the middle. O(n) space."""
        seen = []
        curr = head

        while curr is not None:
            seen.append(curr)
            curr = curr.next

        return seen[(len(seen) // 2)]

    def middleNode(self, head: ListNode | None) -> ListNode | None:
        """Approach 2 — slow and fast pointers. O(1) space."""
        slow = head

        if head.next is not None:
            fast = head.next
        else:
            return head

        while fast is not None:
            slow = slow.next
            if fast.next is None:
                break
            fast = (fast.next).next

        return slow


# ---------------------------------------------------------------- tests
def build(vals: list[int]) -> tuple[ListNode, list[ListNode]]:
    """Build a list from `vals`; also return the nodes so tests can check
    the exact node object that should come back."""
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0], nodes


def to_list(node: ListNode | None) -> list[int]:
    out = []
    while node is not None:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    import random

    sol = Solution()
    methods = (sol.middleNodeUsingList, sol.middleNode)

    # 1. the examples from the problem
    for method in methods:
        assert to_list(method(build([1, 2, 3, 4, 5])[0])) == [3, 4, 5]
        assert to_list(method(build([1, 2, 3, 4, 5, 6])[0])) == [4, 5, 6]

    # 2. edge cases: 1, 2 and 3 nodes; repeated values (the value is never
    #    used to find the middle, only the position)
    for method in methods:
        assert to_list(method(build([7])[0])) == [7]
        assert to_list(method(build([1, 2])[0])) == [2]
        assert to_list(method(build([1, 2, 3])[0])) == [2, 3]
        head, nodes = build([1, 1, 2])
        assert method(head) is nodes[1]

    # 3. property test: every length allowed by the constraints (1–100),
    #    random values — the answer must be the exact node at index n // 2
    random.seed(0)
    for _ in range(20_000):
        n = random.randint(1, 100)
        head, nodes = build([random.randint(1, 100) for _ in range(n)])
        for method in methods:
            assert method(head) is nodes[n // 2], (n, method.__name__)

    print("all passed")