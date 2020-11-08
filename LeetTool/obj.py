# -*-coding:GBK -*-

class LeetCodeObject:
    @property
    def attr(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + "{" + "{}".format(self.attr) + "}"


class ListNode(LeetCodeObject):
    """链表节点(ListNode)"""

    def __init__(self, val):
        self.val = val
        self.next = None


class TreeNode(LeetCodeObject):
    """二叉树节点(TreeNode)"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Node(LeetCodeObject):
    """树节点(Node)"""

    def __init__(self, val=None, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children