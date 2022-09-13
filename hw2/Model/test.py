# from .agent import Tree
import agent

tree = agent.Tree()

tree.insert(2000)
tree.insert(101)
tree.insert(1000)
tree.insert(101)
tree.insert(1)
tree.insert(3)

print(tree.root.value)
print(str(tree.root.left.value))
print(str(tree.root.left.left.value))

print("preorder of the tree")
for node in tree.preorder():
    print(node)