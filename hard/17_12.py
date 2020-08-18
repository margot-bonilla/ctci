"""
Exercise 17.12 BiNode
Consider a simple data structure called BiNode, which has pointers to two other nodes
public class BiNode {
    public BiNode node1, node2;
    public int data;
}
The data structure BiNode could be used to represent both a binary tree (where node1 is the left and node2
the right node) or a doubly linked list (where node1 is the previous and node2 is the next node). Implement
a method to convert a binary search tree (implemented with BiNode) into a doubly linked list. The values should
be kept in order and the operation should be performed in place (that is, the original data structure)/


"""


class BiNode:
    def __init__(self, data):
        self.n1 = None
        self.n2 = None
        self.data = data


def convert(root: BiNode, left=True):
    if root.n1:
        root.n1 = convert(root.n1, True)
        root.n1.n2 = root
    if root.n2:
        root.n2 = convert(root.n2, False)
        root.n2.n1 = root

    node = root
    if left:
        while node.n2:
            node = node.n2
        return node

    while node.n1:
        node = node.n1
    return node


test_case_number = 1


def printString(string):
    print('[\"', string, '\"]', sep='', end='')


def check(expected, output):
    global test_case_number
    result = True
    node_e = expected
    node_o = output
    while node_e and node_o:
        if node_e.data != node_o.data:
            result = False
        node_e = node_e.n2
        node_o = node_o.n2

    while node_e and node_o:
        if node_e.data != node_o.data:
            result = False
        node_e = node_e.n1
        node_o = node_o.n1

    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


def printList(root):
    node = root
    rev = node
    while node:
        print(node.data, end='->')
        rev = node
        node = node.n2
    node = rev
    print()
    print('reverse list')
    while node:
        print(node.data, end='->')
        node = node.n1
    print()


if __name__ == "__main__":
    tree = BiNode('a')
    tree.n1 = BiNode('b')
    tree.n2 = BiNode('c')
    tree.n1.n1 = BiNode('x')
    tree.n1.n2 = BiNode('y')
    tree.n2.n1 = BiNode('j')
    tree.n2.n2 = BiNode('k')

    expected = BiNode('x')
    expected.n2 = BiNode('b')
    expected.n2.n1 = expected
    expected.n2.n2 = BiNode('y')
    expected.n2.n2.n1 = expected.n2
    expected.n2.n2.n2 = BiNode('a')
    expected.n2.n2.n2.n1 = expected.n2.n2
    expected.n2.n2.n2.n2= BiNode('j')
    expected.n2.n2.n2.n2.n1 = expected.n2.n2.n2
    expected.n2.n2.n2.n2.n2= BiNode('c')
    expected.n2.n2.n2.n2.n2.n1 = expected.n2.n2.n2.n2

    check(expected, convert(tree, False))

    tree = BiNode('4')
    tree.n1 = BiNode('2')
    tree.n2 = BiNode('5')
    tree.n1.n1 = BiNode('1')
    tree.n1.n2 = BiNode('3')
    tree.n1.n1.n1 = BiNode('0')
    tree.n2.n2 = BiNode('6')

    expected = BiNode('0')
    expected.n2 = BiNode('1')
    expected.n2.n1 = expected
    expected.n2.n2 = BiNode('2')
    expected.n2.n2.n1 = expected.n2
    expected.n2.n2.n2 = BiNode('3')
    expected.n2.n2.n2.n1 = expected.n2.n2
    expected.n2.n2.n2.n2 = BiNode('4')
    expected.n2.n2.n2.n2.n1 = expected.n2.n2.n2
    expected.n2.n2.n2.n2.n2 = BiNode('5')
    expected.n2.n2.n2.n2.n2.n1 = expected.n2.n2.n2.n2
    expected.n2.n2.n2.n2.n2.n2 = BiNode('6')
    expected.n2.n2.n2.n2.n2.n2.n1 = expected.n2.n2.n2.n2.n2

    check(expected, convert(tree, False))

