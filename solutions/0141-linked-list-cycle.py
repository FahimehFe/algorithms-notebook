"""141. Linked List Cycle  ·  https://leetcode.com/problems/linked-list-cycle/

TWO APPROACHES
--------------
    hasCycleUsingSet   — remember every node seen.             O(n) space
    hasCycle           — two pointers, different speeds.       O(1) space
                         (Floyd's cycle detection / "tortoise and hare")
"""


class ListNode:
    """LeetCode provides this; defined here with an optional `next` so the
    tests below can build (and, when needed, loop) lists on their own."""

    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycleUsingSet(self, head: ListNode | None) -> bool:
        """Approach 1 — remember every node seen. O(n) space."""
        seen = set()
        temp = head

        while temp is not None:
            if temp in seen:
                return True
            else:
                seen.add(temp)
                temp = temp.next

        return False

    def hasCycle(self, head: ListNode | None) -> bool:
        """Approach 2 — two pointers, different speeds. O(1) space."""
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        while fast is not None:
            if slow == fast:
                return True
            else:
                slow = slow.next
                if fast.next is None:
                    return False
                else:
                    fast = (fast.next).next

        return False


# ---------------------------------------------------------------- tests
def build(vals: list[int], cycle_at: int | None = None) -> ListNode | None:
    """Build a list from `vals`. If `cycle_at` is given, the tail's `.next`
    points back to the node at that index instead of `None` — exactly what
    LeetCode's `pos` describes. The caller always knows the ground truth
    (cycle or not) by construction, so tests never need a second algorithm
    to check against."""
    if not vals:
        return None

    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_at is not None:
        nodes[-1].next = nodes[cycle_at]
    return nodes[0]


if __name__ == "__main__":
    import random

    sol = Solution()
    methods = (sol.hasCycleUsingSet, sol.hasCycle)

    # 1. the examples from the problem
    for method in methods:
        assert method(build([3, 2, 0, -4], cycle_at=1)) is True
        assert method(build([1, 2], cycle_at=0)) is True
        assert method(build([1], cycle_at=None)) is False

    # 2. edge cases: empty list, single node (with and without a self-loop),
    #    two nodes (with and without a cycle)
    for method in methods:
        assert method(build([])) is False
        assert method(build([5])) is False
        assert method(build([5], cycle_at=0)) is True          # node points to itself
        assert method(build([1, 2])) is False
        assert method(build([1, 2], cycle_at=1)) is True        # tail points to itself

    # 3. property test: random lists, cyclic and not, checked against the
    #    ground truth the test itself built (no second algorithm involved)
    random.seed(0)
    for _ in range(20_000):
        n = random.randint(0, 150)
        has_cycle = n > 0 and random.random() < 0.5
        cycle_at = random.randint(0, n - 1) if has_cycle else None
        vals = [random.randint(-10**4, 10**4) for _ in range(n)]

        head = build(vals, cycle_at=cycle_at)
        for method in methods:
            assert method(head) is has_cycle, (n, cycle_at, method.__name__)

    print("all passed")