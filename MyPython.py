class Node:
    def __init__(self, data, color='red'):
        self.data = data
        self.color = color  # 节点颜色
        self.left = None    # 左子节点
        self.right = None   # 右子节点
        self.parent = None  # 父节点


class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(data=None, color='black')  # 定义NIL叶子节点
        self.root = self.NIL_LEAF

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF
        
        parent = None
        current = self.root
        
        # 查找插入位置
        while current != self.NIL_LEAF:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        
        if parent is None:  # 树为空
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
            
        new_node.color = 'red'  # 新节点默认是红色
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':  # 情况1：叔叔是红色
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:  # 情况2和情况3
                    if node == node.parent.right:  # 情况2：在右边
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'  # 情况3
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'  # 根节点始终为黑色

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL_LEAF:
            y.left.parent = x
            
        y.parent = x.parent
        if x.parent is None:  # x是根节点
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL_LEAF:
            x.right.parent = y
            
        x.parent = y.parent
        if y.parent is None:  # y是根节点
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
            
        x.right = y
        y.parent = x

    def inorder(self, node):
        if node != self.NIL_LEAF:
            self.inorder(node.left)
            print(node.data, node.color)
            self.inorder(node.right)

# 示例使用
if __name__ == "__main__":
    rbt = RedBlackTree()
    values = [20, 15, 25, 10, 5, 1]
    
    for value in values:
        rbt.insert(value)

    print("红黑树的中序遍历:")
    rbt.inorder(rbt.root)
