from itertools import permutations
from typing import Optional, Union

from nltk.tree import Tree, ParentedTree

DESIRED_LABEL = "NP"
SEPARATORS = (",", "CC")

RESULTS = []


def paraphrase(base_tree: str):
    ptree = ParentedTree.fromstring(base_tree)
    parse_tree(ptree)


def parse_tree(ptree: ParentedTree):
    for node in ptree:
        if isinstance(node, ParentedTree):
            pairs_in_node = find_pairs_in_node(node)
            if pairs_in_node:
                c = generate_permutations(pairs_in_node)
                b = 1

            parse_tree(node)


def find_pairs_in_node(node: ParentedTree) -> Union[list[list[Tree]], list, None]:
    """Finding all words that satisfy conditing: DESIRED_LABEL SEPARATOR DESIRED_LABEL"""
    if node.height() <= 2:  # No pairs available
        return

    pairs = []
    for idx in range(2, len(node)):
        prev, sep, next = node[idx - 2: idx + 1]

        if prev.label() == next.label() == DESIRED_LABEL and sep.label() in SEPARATORS:
            pairs.extend([sep, next]) if pairs else pairs.extend([prev, sep, next])

    return pairs


string = """(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )"""

# Initialize tree:

print(RESULTS)


def generate_permutations(collection: list[ParentedTree]) -> list[tuple[ParentedTree]]:
    result = []
    for pair in permutations(collection):
        if all(
            [
                pair[idx - 2].label() == pair[idx].label() == "NP" and pair[idx - 1].label() in SEPARATORS
                and pair[idx - 1] == collection[idx - 1]
                for idx in range(2, len(pair), 2)
            ]
        ):
            result.append(pair)

    return result

paraphrase(string)
