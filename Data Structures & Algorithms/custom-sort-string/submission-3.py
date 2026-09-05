class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if len(order) == 0:
            return s
        new_order = []
        for ch in order:
            for j in s:
                if ch  == j:
                    new_order.append(ch)
        for j in s:
            if j not in order:
                new_order.append(j)
        orde = "".join(new_order)
        return orde
        