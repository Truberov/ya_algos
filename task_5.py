from queue import Queue


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def dfs(node, visited=None, to_visit=None):
    visited.append(node.value)
    if node.left:
        to_visit.put(node.left)
    if node.right:
        to_visit.put(node.right)
    if to_visit.empty():
        return visited
    dfs(to_visit.get(), visited, to_visit)


def main():
    node = Node(8, Node(5, Node(3), Node(6)), Node(10, Node(9), Node(11)))
    visited = list()
    to_visit = Queue()
    dfs(node, visited=visited, to_visit=to_visit)


if __name__ == "__main__":
    main()
