import random
import time
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        cur = self.root

        while True:
            if key < cur.key:
                if cur.left is None:
                    cur.left = Node(key)
                    return
                cur = cur.left

            elif key > cur.key:
                if cur.right is None:
                    cur.right = Node(key)
                    return
                cur = cur.right

            else:
                return

    def delete(self, key):
        parent = None
        cur = self.root

        while cur and cur.key != key:
            parent = cur
            cur = cur.left if key < cur.key else cur.right

        if cur is None:
            return

        if cur.left is None or cur.right is None:
            child = cur.left or cur.right

            if parent is None:
                self.root = child
            elif parent.left == cur:
                parent.left = child
            else:
                parent.right = child

        else:
            sp = cur
            s = cur.right

            while s.left:
                sp = s
                s = s.left

            cur.key = s.key

            if sp.left == s:
                sp.left = s.right
            else:
                sp.right = s.right

    def inorder(self, node):
        if node:
            return self.inorder(node.left) + [node.key] + self.inorder(node.right)
        return []

    def preorder(self, node):
        if node:
            return [node.key] + self.preorder(node.left) + self.preorder(node.right)
        return []

    def postorder(self, node):
        if node:
            return self.postorder(node.left) + self.postorder(node.right) + [node.key]
        return []

    def search(self, key):
        cur = self.root

        while cur:
            if key == cur.key:
                return True
            cur = cur.left if key < cur.key else cur.right

        return False

    def height(self):
        if self.root is None:
            return 0

        stack = [(self.root, 1)]
        height = 0

        while stack:
            cur, level = stack.pop()
            height = max(height, level)

            if cur.left:
                stack.append((cur.left, level + 1))

            if cur.right:
                stack.append((cur.right, level + 1))

        return height



keys = [50, 30, 70, 20, 40, 60, 80, 10]

tree = BST()

for key in keys:
    tree.insert(key)

ino = tree.inorder(tree.root)

print("========== Test Case 1 ==========")
print("Inorder :", ino)
print("Preorder:", tree.preorder(tree.root))
print("Postorder:", tree.postorder(tree.root))
print("Sorted? :", ino == sorted(ino))
print("Search 60 :", "Present" if tree.search(60) else "Absent")
print("Search 100:", "Present" if tree.search(100) else "Absent")



print("\n========== Test Case 2 ==========")

tree.delete(80)
print("After deleting leaf 80:")
print(tree.inorder(tree.root))

tree.delete(70)
print("After deleting one-child 70:")
print(tree.inorder(tree.root))

tree.delete(30)
print("After deleting two-child 30:")
print(tree.inorder(tree.root))



print("\n========== Test Case 3 ==========")

sizes = [1000, 5000, 10000]
results = []

for n in sizes:

    random_data = random.sample(range(n), n)
    sorted_data = list(range(n))
    reverse_data = list(range(n - 1, -1, -1))

    for name, data in [
        ("Random", random_data),
        ("Sorted", sorted_data),
        ("Reverse", reverse_data)
    ]:

        tree = BST()

        start = time.perf_counter()

        for key in data:
            tree.insert(key)

        build_time = time.perf_counter() - start

        height = tree.height()

        search_keys = random.choices(data, k=1000)

        start = time.perf_counter()

        for key in search_keys:
            tree.search(key)

        search_time = time.perf_counter() - start

        delete_keys = random.sample(data, 500)

        start = time.perf_counter()

        for key in delete_keys:
            tree.delete(key)

        delete_time = time.perf_counter() - start

        results.append(
            [n, name, build_time, height, search_time, delete_time]
        )



print("\nN       Type        Build(s)    Height    Search(s)    Delete(s)")
print("-" * 65)

for r in results:
    print(
        f"{r[0]:<8}"
        f"{r[1]:<12}"
        f"{r[2]:<12.6f}"
        f"{r[3]:<10}"
        f"{r[4]:<13.6f}"
        f"{r[5]:<12.6f}"
    )



for name in ["Random", "Sorted", "Reverse"]:
    x = [r[0] for r in results if r[1] == name]
    y = [r[2] for r in results if r[1] == name]
    plt.plot(x, y, marker="o", label=name)

plt.xlabel("Input Size (n)")
plt.ylabel("Build Time (seconds)")
plt.title("BST Build Time")
plt.legend()
plt.grid(True)
plt.show()


for name in ["Random", "Sorted", "Reverse"]:
    x = [r[0] for r in results if r[1] == name]
    y = [r[3] for r in results if r[1] == name]
    plt.plot(x, y, marker="o", label=name)

plt.xlabel("Input Size (n)")
plt.ylabel("Height")
plt.title("BST Height")
plt.legend()
plt.grid(True)
plt.show()


for name in ["Random", "Sorted", "Reverse"]:
    x = [r[0] for r in results if r[1] == name]
    y = [r[4] for r in results if r[1] == name]
    plt.plot(x, y, marker="o", label=name)

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Time for 1000 Searches")
plt.legend()
plt.grid(True)
plt.show()


for name in ["Random", "Sorted", "Reverse"]:
    x = [r[0] for r in results if r[1] == name]
    y = [r[5] for r in results if r[1] == name]
    plt.plot(x, y, marker="o", label=name)

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Time for 500 Deletions")
plt.legend()
plt.grid(True)
plt.show()