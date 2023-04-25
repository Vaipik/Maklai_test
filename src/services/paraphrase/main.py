from typing import Optional

from nltk.tree import Tree

SEPARATORS = (",", "CC")


def base_tree(tree: str) -> Tree:
    tree = Tree.fromstring(tree)
    tree.pretty_print()
    # parse_tree(tree)
    return tree


def parse_tree(tree: Tree):
    pass


def parse_node(tree: Tree) -> Optional[list[list[Tree]]]:
    """"""
    pairs = []

    for idx in range(2, len(tree)):
        prev, sep, next = tree[idx - 2: idx + 1]
        if prev.label() == next.label() == "NP" and sep.label() in SEPARATORS:
            print(tree[idx - 2].label(), tree[idx].label())
            pairs.append([next, sep, prev])

    return pairs
