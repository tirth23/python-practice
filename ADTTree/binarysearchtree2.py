class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root==None:
            self.root=node(data)
        else:
            cur_node=self.root
            while(cur_node):
                if data>cur_node.data:
                    if cur_node.right==None:
                        cur_node.right=node(data)
                        break
                    else:
                        cur_node=cur_node.right
                elif data<cur_node.data:
                    if cur_node.left==None:
                        cur_node.left=node(data)
                        break
                    else:
                        cur_node=cur_node.left
                else:
                    print('value is already present in BST')
                    break

                    
            if cur_node==None:
                print('value is already present in tree')
            
    def find(self,data):
        cur_node=self.root
        if  self.root==None:
            print('tree is empty ')
        else:
            while(cur_node):
                if cur_node.data==data:
                    print(' value present in tree')
                    return cur_node
                elif data>cur_node.data:
                    cur_node=cur_node.right
                else :
                    cur_node=cur_node.left
            if cur_node==None:
                print('value not present in tree')
    def delete(self,key):
        cur_node=self.root
        par_=self.root
        if self.root==None:
            print('empty')
        else:
            while(cur_node!=None):
                if key>cur_node.data:
                    par_=cur_node
                    cur_node=cur_node.right

                elif  key<cur_node.data:
                    par_=cur_node
                    cur_node=cur_node.left

                elif key==cur_node.data:
                    if cur_node.right==None and cur_node.left==None:
                        if par_.right==cur_node:
                            par_.right=None
                        else:
                            par_.left=None
                        return
                    
                    elif cur_node.left==None and cur_node.right!=None:
                        par__=cur_node
                        temp=cur_node.right

                        while temp.left!=None:
                            par__=temp
                            temp=temp.left
                        cur_node.data=temp.data
                        if par__.right==temp:
                            par__.right==temp.right
                        else:
                            par__.left=temp.right
                        return
                    elif cur_node.left!=None and cur_node.right==None:
                        par__=cur_node
                        temp=cur_node.left

                        while temp.right!=None:
                            par__=temp
                            temp=temp.right
                        cur_node.data=temp.data
                        if par__.right==temp:
                            par__.right==temp.left
                        else:
                            par__.left=temp.left
                        return
                    elif cur_node.left!=None and cur_node.right!=None:
                        par__=cur_node
                        temp=cur_node.right

                        while temp.left!=None:
                            par__=temp
                            temp=temp.left
                        cur_node.data=temp.data
                        if par__.right==temp:
                            par__.right==temp.right
                        else:
                            par__.left=temp.right
                        return
a=BST()
a.insert(50)
a.insert(40)
a.insert(60)
a.insert(55)
a.insert(70)
a.insert(30)
a.insert(45)
a.insert(42)
a.insert(47)
# a.insert(22)
# a.insert(37)
a.insert(41)
a.insert(43)
# a.insert(33)
# a.insert(39)
a.delete(50)
a.find(42)