"""155. Min Stack  ·  https://leetcode.com/problems/min-stack/

COMPLEXITY
----------
Time:  O(1)
Space: O(n)

"""


class MinStack:
    def __init__(self):
        self.items = []          # each element: [value, min_so_far]
 
    def push(self, value: int) -> None:
        min_so_far = 0
        if len(self.items) > 0:
            if value < self.items[-1][1]:
                min_so_far = value
            else:
                min_so_far = self.items[-1][1]
        else:
            min_so_far = value
 
        self.items.append([value, min_so_far])
 
    def pop(self) -> None:
        if len(self.items) > 0:
            self.items.pop()
 
    def top(self) -> int:
        if len(self.items) > 0:
            return self.items[-1][0]
 
    def getMin(self) -> int:
        if len(self.items) > 0:
            return self.items[-1][1]
        else:
            return
 
 
# ---------------------------------------------------------------- tests
if __name__ == "__main__":
    import random
 
    # 1. the example from the problem
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    assert obj.getMin() == -3
    obj.pop()
    assert obj.top() == 0
    assert obj.getMin() == -2
 
    # 2. edge cases: single element, repeated minimum, push/pop right at the
    #    minimum
    s = MinStack()
    s.push(7)
    assert s.top() == 7 and s.getMin() == 7
 
    s = MinStack()
    for _ in range(4):
        s.push(5)
    assert s.getMin() == 5
    s.pop()
    assert s.getMin() == 5          # three 5's still on the stack
    s.pop()
    s.pop()
    assert s.getMin() == 5          # one 5 left
 
    s = MinStack()
    s.push(1)
    s.push(1)
    assert s.getMin() == 1
    s.pop()
    assert s.getMin() == 1          # the other 1 is still there
 
    s = MinStack()
    s.push(0)
    s.push(-1)
    s.push(1)
    assert s.getMin() == -1
    s.pop()                         # pop the 1, min unaffected
    assert s.getMin() == -1
    s.pop()                         # pop the -1, min falls back to 0
    assert s.getMin() == 0
 
    # 3. 32-bit range extremes
    s = MinStack()
    s.push(-2**31)
    s.push(2**31 - 1)
    assert s.getMin() == -2**31
    assert s.top() == 2**31 - 1
 
    # 4. property test: replay random push/pop/top/getMin against a
    #    brute-force reference (plain Python list + min())
    random.seed(0)
    for _ in range(20_000):
        ref = []
        sol = MinStack()
        for _ in range(random.randint(1, 40)):
            op = random.choice(["push", "pop", "top", "getMin"])
            if op == "push" or not ref:
                val = random.randint(-10**4, 10**4)
                ref.append(val)
                sol.push(val)
            elif op == "pop":
                ref.pop()
                sol.pop()
            elif op == "top":
                assert sol.top() == ref[-1], (ref, sol.items)
            elif op == "getMin":
                assert sol.getMin() == min(ref), (ref, sol.items)
 
    print("all passed")
 