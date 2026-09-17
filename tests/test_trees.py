from structures.trees.binary_tree import Node


def test_node_creation():
    node = Node(42)
    assert node.value == 42
    assert node.left is None
    assert node.right is None
    assert node.is_leaf is True


def test_node_with_children():
    left_child = Node(20)
    right_child = Node(60)
    root = Node(50, left=left_child, right=right_child)

    assert root.value == 50
    assert root.left is left_child
    assert root.right is right_child
    assert root.is_leaf is False
    assert left_child.is_leaf is True
    assert right_child.is_leaf is True


def test_node_representation():
    node = Node("root")
    assert repr(node) == "Node('root')"
    assert str(node) == "root"
