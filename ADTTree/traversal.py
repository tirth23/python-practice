def inorderTraversal(root): 
    if root:   
        inorderTraversal(root.left) 
        print(root.data)
  		inorderTraversal(root.right) 
  
def postorderTraversal(root):   
    if root: 
        postorderTraversal(root.left) 
        postorderTraversal(root.right) 
        print(root.data)
  
def preorderTraversal(root): 
    if root:
        print(root.data)
        preorderTraversal(root.left) 
        preorderTraversal(root.right)