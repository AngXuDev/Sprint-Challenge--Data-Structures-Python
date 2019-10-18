import time
from binary_search_tree import BinarySearchTree
from collections import Counter

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

start_time = time.time()

# time complexity for initial code would be O(n^2) due to nested loops

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# O(n)
# duplicates = []
# start_time = time.time()
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)


# BST
# bst = BinarySearchTree(names_1[0])
# for name in names_1[1:]:
#     bst.insert(name)
# duplicates = []
# # start_time = time.time()
# for name in names_2:
#     if bst.contains(name):
#         duplicates.append(name)

# Dictionary
# duplicates = []
# nameObj = {}
# for name in names_1:
#     nameObj[name] = name
# # start_time = time.time()
# for name in names_2:
#     if name in nameObj:
#         duplicates.append(name)

# Counter
counter1 = Counter(names_1)
counter2 = Counter(names_2)
duplicates = []
# start_time = time.time()
for key in counter1:
    if key in counter2:
        duplicates.append(key)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
