
class QuickFind(object):
    def __init__(self, N):
        self.items = range(N)

    def find(self, p, q):
        return self.items[p] == self.items[q]

    def unite(self, p, q):
        # value_to_put_under = self.items[p]
        # root_value = self.items[q]
        value_to_look_for = self.items[p]
        value_to_change = self.items[q]

        pid = self.items[p];
        for idx, value in enumerate(self.items):
            if value_to_look_for == self.items[idx]:
                self.items[idx] = value_to_change

quick_find = QuickFind(10)

unions = [
    [3, 4],
    [4, 9],
    [8, 0],
    [2, 3],
    [5, 6], [5, 9], [7, 3], [4, 8], [6, 1]
]

for union in unions:
    quick_find.unite(union[0], union[1])

assert [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] == quick_find.items
