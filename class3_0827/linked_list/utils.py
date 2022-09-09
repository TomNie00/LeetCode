class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def build_list(node_vals, edges):
    nodes = []
    for v in node_vals:
        nodes.append(ListNode(v))

    for i in range(0, len(node_vals) - 1):
        nodes[i].next = nodes[i + 1]

    for e in edges:
        nodes[e[0]].next = nodes[e[1]]
    return nodes[0]


def display(head):
    cnt = 10
    while head:
        print(head.val)
        head = head.next
        cnt -= 1
        if cnt <= 0:
            break

# 在ide里直接测试结果
# 使用时要在根目录创建  __init__.py 的文件
# from 目录.utils.py 'class'
# from 目录.utils.py 'function'
# 引用 class 和 function 时 要分开写
