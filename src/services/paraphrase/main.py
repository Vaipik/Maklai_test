from itertools import permutations
from typing import Union

from nltk.tree import MultiParentedTree

DESIRED_LABEL = "NP"
SEPARATORS = (",", "CC")


def paraphrases(base_tree: str, limit: int):
    ptree = MultiParentedTree.fromstring(base_tree)
    pairs = ptree.subtrees(find_pairs_in_node)  # Finding all subtrees that can satisfy our condition
    results = []
    for pair in pairs:
        if not pair:
            return {
                "paraphrases": []
            }
        make_new_trees(results, pair)

    response = convert_to_response(results, limit)
    return {
        "paraphrases": response
    }


def convert_to_response(results: list, limit: int) -> list[dict[str, str]]:
    """
    Converts founded results in list of dictionaries
    :param results: list where all generated trees are stored
    :param limit: maximal amount of new trees
    """
    return [
        {"tree": result.pformat()} for result in results[:limit]
    ]


def find_pairs_in_node(node: MultiParentedTree) -> Union[list[MultiParentedTree], list, None]:
    """Finding all words that satisfy conditing: DESIRED_LABEL SEPARATOR DESIRED_LABEL"""
    if node.height() <= 2:  # No pairs available
        return
    pairs = []
    for idx in range(2, len(node)):
        prev, sep, next = node[idx - 2: idx + 1]

        if prev.label() == next.label() == DESIRED_LABEL and sep.label() in SEPARATORS:
            pairs.extend([sep, next]) if pairs else pairs.extend([prev, sep, next])

    return pairs


def generate_permutations(base_node: MultiParentedTree) -> list[tuple[MultiParentedTree]]:
    """Generating new combinations for base node"""
    result = []
    base_node_tuple = tuple(base_node)  # itertools.permutations returns tuple
    for pair in permutations(base_node):
        # Check if permutated node is still satisfy our conditions
        if all(
                [
                    pair[idx - 2].label() == pair[idx].label() == "NP" and pair[idx - 1].label() in SEPARATORS
                    and pair[idx - 1] == base_node[idx - 1]  # we don't need to substitute separators
                    for idx in range(2, len(pair), 2)
                ]
        ) and pair != base_node_tuple:  # to prevent duplicating data
            result.append(pair)

    return result


def make_new_trees(results: list, node: MultiParentedTree) -> None:
    """
    Generating new trees for given node
    :param results: list where should be stored new trees
    :param node: node for which new trees will be generated
    :returns: None because results is a list from outer scope
    """
    new_pairs = generate_permutations(node)
    parent_tree: MultiParentedTree = new_pairs[0][0].parents()[0]  # Find parent tree for node
    root = parent_tree.roots()[0]
    parent_tree_idx = list(root.subtrees()).index(parent_tree)  # Find parent idx

    for pair in new_pairs:
        new_tree = list(root.copy(deep=True).subtrees())
        new_pair = MultiParentedTree(parent_tree.label(), pair)
        new_tree[parent_tree_idx] = new_pair
        results.append(new_tree[0])
