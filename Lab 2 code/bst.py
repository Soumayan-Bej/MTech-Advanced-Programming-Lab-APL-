import random, time
import matplotlib.pyplot as plt


class Node:
    def __init__(self, x):
        self.key, self.left, self.right = x, None, None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if not self.root:
            self.root = Node(x)
            return
        p, c = None, self.root
        while c:
            p, c = c, c.left if x < c.key else c.right if x > c.key else None
        if x < p.key:
            p.left = Node(x)
        elif x > p.key:
            p.right = Node(x)

    def search(self, x):
        c = self.root
        while c:
            if c.key == x:
                return True
            c = c.left if x < c.key else c.right
        return False

    def delete(self, x):
        p, c = None, self.root
        while c and c.key != x:
            p, c = c, c.left if x < c.key else c.right
        if not c:
            return

        if not c.left or not c.right:
            child = c.left or c.right
            if not p:
                self.root = child
            elif p.left is c:
                p.left = child
            else:
                p.right = child
        else:
            sp, s = c, c.right
            while s.left:
                sp, s = s, s.left
            c.key = s.key
            if sp.left is s:
                sp.left = s.right
            else:
                sp.right = s.right

    def inorder(self, n):
        return self.inorder(n.left) + [n.key] + self.inorder(n.right) if n else []

    def preorder(self, n):
        return [n.key] + self.preorder(n.left) + self.preorder(n.right) if n else []

    def postorder(self, n):
        return self.postorder(n.left) + self.postorder(n.right) + [n.key] if n else []

    def height(self):
        if not self.root:
            return 0
        q, h = [(self.root, 1)], 0
        while q:
            n, d = q.pop()
            h = max(h, d)
            if n.left: q.append((n.left, d + 1))
            if n.right: q.append((n.right, d + 1))
        return h


tree = BST()
for x in [50, 30, 70, 20, 40, 60, 80, 10]:
    tree.insert(x)

ino = tree.inorder(tree.root)

print("PROBLEM 1")
print("Inorder :", ino)
print("Preorder:", tree.preorder(tree.root))
print("Postorder:", tree.postorder(tree.root))
print("Sorted? :", ino == sorted(ino))
print("Search 60 :", "Present" if tree.search(60) else "Absent")
print("Search 100:", "Present" if tree.search(100) else "Absent")


print("\nPROBLEM 2")

for x, case in [(80, "leaf"), (70, "one-child"), (30, "two-child")]:
    tree.delete(x)
    print(f"After deleting {case} {x}:", tree.inorder(tree.root))


results = []

for n in [1000, 5000, 10000]:
    for name, data in [
        ("Random", random.sample(range(n), n)),
        ("Sorted", range(n)),
        ("Reverse", range(n - 1, -1, -1))
    ]:
        tree = BST()

        t = time.perf_counter()
        for x in data:
            tree.insert(x)
        build = time.perf_counter() - t

        h = tree.height()

        t = time.perf_counter()
        for x in random.choices(range(n), k=1000):
            tree.search(x)
        search = time.perf_counter() - t

        t = time.perf_counter()
        for x in random.sample(range(n), 500):
            tree.delete(x)
        delete = time.perf_counter() - t

        results.append((n, name, build, h, search, delete))


print("\nPROBLEM 3")
print("n\tType\t\tBuild\t\tHeight\tSearch\t\tDelete")

for r in results:
    print(f"{r[0]}\t{r[1]:<10}\t{r[2]:.6f}\t{r[3]}\t{r[4]:.6f}\t{r[5]:.6f}")


for col, title, ylabel in [
    (2, "BST Build Time", "Time (seconds)"),
    (3, "BST Height", "Height"),
    (4, "1000 Searches", "Time (seconds)"),
    (5, "500 Deletions", "Time (seconds)")
]:
    for name in ["Random", "Sorted", "Reverse"]:
        a = [r for r in results if r[1] == name]
        plt.plot([r[0] for r in a], [r[col] for r in a], "o-", label=name)

    plt.xlabel("Input Size (n)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()
