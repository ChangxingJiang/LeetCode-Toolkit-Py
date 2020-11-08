# -*-coding:GBK -*-

from . import ListNode
from . import Node
from . import TreeNode


def build_ListNode(val):
    """使用列表构造链表"""
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


def build_ListNode_with_skip(val, list1, list2, skip1, skip2):
    """构造相交链表

    :param val: 相较交点的值
    :param list1: 链表1
    :param list2: 链表2
    :param skip1: 链表1交点位置
    :param skip2: 链表2交点位置
    :return:
    """
    head1 = build_ListNode(list1[0:skip1])
    head2 = build_ListNode(list2[0:skip2])

    if skip1 == len(list1) or skip2 == len(list2):
        return head1, head2

    head3 = build_ListNode(list1[skip1:])

    i1 = head1
    while i1.next:
        i1 = i1.next
    i1.next = head3

    i2 = head2
    while i2.next:
        i2 = i2.next
    i2.next = head3

    return head1, head2


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
