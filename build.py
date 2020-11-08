from . import ListNode
from . import Node
from . import TreeNode


def build_ListNode(val):
    if val is None:
        return None
    if isinstance(val, list):
        if len(val) == 0:
            return None
        else:
            head = node = ListNode(val[0])
            for i in range(1, len(val)):
                node.next = ListNode(val[i])
                node = node.next
            return head
    else:
        return None


def build_TreeNode(val):
    # 使用列表构造二叉树
    if val is None:
        return None
    elif isinstance(val, list):
        if len(val) == 0:
            return None
        else:
            head = TreeNode(val[0])
            wait_node_list = [head]
            left = False
            for i in range(1, len(val)):
                node = TreeNode(val[i])
                if not left:
                    if val[i] is not None:
                        wait_node_list[0].left = node
                        wait_node_list.append(node)
                    left = True
                else:
                    if val[i] is not None:
                        wait_node_list[0].right = node
                        wait_node_list.append(node)
                    left = False
                    wait_node_list.pop(0)
            return head
    elif isinstance(val, int) or isinstance(val, str):
        return TreeNode(val)
    else:
        return None


def build_Node(val):
    # 使用列表构造树
    if val is None:
        return None
    elif isinstance(val, int) or isinstance(val, str):
        return Node(val=val)
    elif isinstance(val, list):
        if len(val) == 0:
            return None
        head = Node(val[0])
        node_list = [head]
        now_node = None
        for i in range(1, len(val)):
            v = val[i]
            if v is None:
                now_node = node_list.pop(0)
            else:
                node = Node(v)
                now_node.children.append(node)
                node_list.append(node)
        return head
