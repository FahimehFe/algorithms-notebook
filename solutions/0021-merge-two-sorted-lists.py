"""21. Merge Two Sorted Lists  ·  https://leetcode.com/problems/merge-two-sorted-lists/


COMPLEXITY
----------
Time:  O(n + m) — each node from both lists is visited exactly once.
Space: O(1) extra — `dummy`, `current`
"""


class ListNode:
    """LeetCode provides this; defined here so the tests below can build
    and walk lists on their own."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        current = dummy

        while list1 is not None or list2 is not None:
            if list1 is None:
                current.next = list2
                current = current.next
                list2 = list2.next
            elif list2 is None or list1.val <= list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next

        return dummy.next


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
    """Walk with a step cap so a bug that accidentally creates a cycle
    fails loudly instead of hanging the test run."""
    out = []
    node = head
    steps = 0
    while node is not None:
        steps += 1
        if steps > 100_000:
            raise AssertionError("cycle detected — list did not terminate")
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    import random

    sol = Solution()

    # 1. the examples from the problem
    assert to_list(sol.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(sol.mergeTwoLists(build([]), build([]))) == []
    assert to_list(sol.mergeTwoLists(build([]), build([0]))) == [0]

    # 2. edge cases: one list entirely before/after the other, duplicates,
    #    negatives, single-element lists, one side empty
    assert to_list(sol.mergeTwoLists(build([1, 2, 3]), build([4, 5, 6]))) == [1, 2, 3, 4, 5, 6]
    assert to_list(sol.mergeTwoLists(build([4, 5, 6]), build([1, 2, 3]))) == [1, 2, 3, 4, 5, 6]
    assert to_list(sol.mergeTwoLists(build([1, 1, 1]), build([1, 1]))) == [1, 1, 1, 1, 1]
    assert to_list(sol.mergeTwoLists(build([-5, 0, 5]), build([-3, -1]))) == [-5, -3, -1, 0, 5]
    assert to_list(sol.mergeTwoLists(build([7]), build([]))) == [7]
    assert to_list(sol.mergeTwoLists(build([]), build([7]))) == [7]
    assert to_list(sol.mergeTwoLists(build([7]), build([7]))) == [7, 7]

    # 3. structural check: every node in the result is a node that was
    #    already in list1/list2 -- nothing new was allocated
    l1 = build([2, 4, 6])
    l2 = build([1, 3, 5])
    original_ids = set()
    node = l1
    while node is not None:
        original_ids.add(id(node))
        node = node.next
    node = l2
    while node is not None:
        original_ids.add(id(node))
        node = node.next

    merged = sol.mergeTwoLists(l1, l2)
    merged_ids = set()
    node = merged
    while node is not None:
        merged_ids.add(id(node))
        node = node.next
    assert merged_ids == original_ids, "result should reuse the original nodes, not allocate new ones"

    # 4. property test: random sorted lists, checked against Python's own
    #    sorted() on the combined values (an independent check -- it can't
    #    share a bug with the merge logic above)
    random.seed(0)
    for _ in range(20_000):
        n1 = random.randint(0, 50)
        n2 = random.randint(0, 50)
        vals1 = sorted(random.randint(-10**4, 10**4) for _ in range(n1))
        vals2 = sorted(random.randint(-10**4, 10**4) for _ in range(n2))

        result = to_list(sol.mergeTwoLists(build(vals1), build(vals2)))
        assert result == sorted(vals1 + vals2), (vals1, vals2, result)

    print("all passed")