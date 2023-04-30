from nltk import MultiParentedTree

from src.services.paraphrase.main import find_pairs_in_node, generate_permutations


def test_find_pairs_in_node_with_existing_pairs(node_with_pairs):
    """Test to find pairs that can be shuffled among themselves"""

    expected = list(node_with_pairs)

    result = find_pairs_in_node(node_with_pairs)
    assert result == expected


def test_find_pairs_in_node_without_pairs(node_without_pairs):
    """If pairs are not exist"""
    expected = []

    result = find_pairs_in_node(node_without_pairs)
    assert result == expected


def test_find_pairs_in_node_wrong_separator(node_with_pairs_and_wrong_separator):
    """If pairs are exist but with wrong separator"""
    expected = []

    result = find_pairs_in_node(node_with_pairs_and_wrong_separator)
    assert result == expected


def test_generate_permutations(node_with_pairs):
    """
    Test to generate all possible permutations between pairs.
    In one node possible combinations is n! - 1, where n number of parts than can be mixed.
    In following test there must be 6 possible pairs for input_data node
    """
    input_data = list(node_with_pairs)
    result = generate_permutations(input_data)

    expected = [
        (
            MultiParentedTree('NP', [MultiParentedTree('JJtrendy', []), MultiParentedTree('NNS', ['bars'])]),
            MultiParentedTree(',', [',']),
            MultiParentedTree('NP', [MultiParentedTree('JJ', ['Catalan']), MultiParentedTree('NNSrestaurants', [])]),
            MultiParentedTree('CC', ['and']),
            MultiParentedTree('NP', [MultiParentedTree('NNS', ['clubs'])])
        ),
        (
            MultiParentedTree('NP', [MultiParentedTree('NNS', ['clubs'])]),
            MultiParentedTree(',', [',']),
            MultiParentedTree('NP', [MultiParentedTree('JJtrendy', []), MultiParentedTree('NNS', ['bars'])]),
            MultiParentedTree('CC', ['and']),
            MultiParentedTree('NP', [MultiParentedTree('JJ', ['Catalan']), MultiParentedTree('NNSrestaurants', [])])
        ),
        (
            MultiParentedTree('NP', [MultiParentedTree('NNS', ['clubs'])]),
            MultiParentedTree(',', [',']),
            MultiParentedTree('NP', [MultiParentedTree('JJ', ['Catalan']), MultiParentedTree('NNSrestaurants', [])]),
            MultiParentedTree('CC', ['and']),
            MultiParentedTree('NP', [MultiParentedTree('JJtrendy', []), MultiParentedTree('NNS', ['bars'])])
        ),
        (
            MultiParentedTree('NP', [MultiParentedTree('JJ', ['Catalan']), MultiParentedTree('NNSrestaurants', [])]),
            MultiParentedTree(',', [',']),
            MultiParentedTree('NP', [MultiParentedTree('JJtrendy', []), MultiParentedTree('NNS', ['bars'])]),
            MultiParentedTree('CC', ['and']),
            MultiParentedTree('NP', [MultiParentedTree('NNS', ['clubs'])])
        ),
        (
            MultiParentedTree('NP', [MultiParentedTree('JJ', ['Catalan']), MultiParentedTree('NNSrestaurants', [])]),
            MultiParentedTree(',', [',']),
            MultiParentedTree('NP', [MultiParentedTree('NNS', ['clubs'])]),
            MultiParentedTree('CC', ['and']),
            MultiParentedTree('NP', [MultiParentedTree('JJtrendy', []), MultiParentedTree('NNS', ['bars'])])
        )
    ]

    assert len(result) == 5
    assert result == expected
