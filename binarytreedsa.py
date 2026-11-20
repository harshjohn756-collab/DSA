# class tree:
#     def __init__(self,data):
#         self.left = None
#         self.right = None
#         self.data= data

#     def insertdata(self,data):
#         if self.data is None:
#             self.data = tree(data)
#         else:
#             if data < self.data:
#                 if self.left:
#                     self.left.insertdata(data)
#                 else:
#                     self.left = tree(data)
#             elif data > self.data:
#                 if self.right:
#                     self.right.insertdata(data)
#                 else:
#                     self.right = tree(data)


# def inorder(root):
#     if root is None:
#         return
#     else:
#         inorder(root.left)
#         print(root.data,end=" ")
#         inorder(root.right)

# def preorder(root):
#     if root is None:
#         return
#     else:
#         print(root.data,end=" ")
#         preorder(root.left)
#         preorder(root.right)

# def postorder(root):
#     if root is None:
#         return
#     else:
#         print(root.data,end=" ")
#         postorder(root.right)
#         postorder(root.left)

# def makelist(root):
#     if root is None:
#         return
#     else:
#         d[root.data] = []
#         makelist(root.left)
#         if root.left:
#             d[root.data].append(root.left.data)
#         if root.right:
#             d[root.data].append(root.right.data)
#         makelist(root.right)
#         return d


# d = {}
# if __name__ == "__main__":
#     root = tree("g")
#     root.insertdata("a")
#     root.insertdata("z")
#     # inorder(root)
#     # preorder(root)
#     # postorder(root)
#     print(makelist(root))

