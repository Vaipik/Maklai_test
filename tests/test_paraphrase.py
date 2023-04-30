from nltk import ParentedTree

from src.services.paraphrase.main import find_pairs_in_node, generate_permutations


def test_find_pairs_in_node_ok():
    """Test to find pairs that can be shuffled among themselves"""
    input_node = ParentedTree(
        'NP',
        [
            ParentedTree('NP', [ParentedTree('JJtrendy', []), ParentedTree('NNS', ['bars'])]),
            ParentedTree(',', [',']),
            ParentedTree('NP', [ParentedTree('NNS', ['clubs'])]),
            ParentedTree('CC', ['and']),
            ParentedTree('NP', [ParentedTree('JJ', ['Catalan']), ParentedTree('NNSrestaurants', [])])
        ]
    )

    expected = list(input_node)

    result = find_pairs_in_node(input_node)
    assert result == expected


def test_find_pairs_in_node_not_exists():
    """If pairs are not exist"""
    input_node = ParentedTree(
        'NP',
        [
            ParentedTree('NP', [ParentedTree('JJtrendy', []), ParentedTree('NNS', ['bars'])]),
            ParentedTree('NP', [ParentedTree('NNS', ['clubs'])]),
            ParentedTree(',', [',']),
            ParentedTree('CC', ['and']),
            ParentedTree('NP', [ParentedTree('JJ', ['Catalan']), ParentedTree('NNSrestaurants', [])])
        ]
    )

    expected = []

    result = find_pairs_in_node(input_node)
    assert result == expected


def test_find_pairs_in_node_wrong_separator():
    """If pairs are exist but with wrong separator"""
    input_node = ParentedTree(
        'NP',
        [
            ParentedTree('NP', [ParentedTree('JJtrendy', []), ParentedTree('NNS', ['bars'])]),
            ParentedTree('JJ', ['Catalan']),
            ParentedTree('NP', [ParentedTree('NNS', ['clubs'])]),
            ParentedTree('NNS', ['clubs']),
            ParentedTree('NP', [ParentedTree('JJ', ['Catalan']), ParentedTree('NNSrestaurants', [])])
        ]
    )
    expected = []

    result = find_pairs_in_node(input_node)
    assert result == expected


def test_generate_permutations():
    """
    Test to generate all possible permutations between pairs.
    In one node possible combinations is n!, where n number of parts than can be mixed.
    In following test there must be 6 possible pairs for input_data node
    """
    input_data = [
        ParentedTree('NP', [ParentedTree('JJtrendy', []), ParentedTree('NNS', ['bars'])]),
        ParentedTree(',', [',']),
        ParentedTree('NP', [ParentedTree('NNS', ['clubs'])]),
        ParentedTree('CC', ['and']),
        ParentedTree('NP', [ParentedTree('JJ', ['Catalan']), ParentedTree('NNSrestaurants', [])])
    ]
    result = generate_permutations(input_data)

    expected = [
        (
            ParentedTree('NP', [ParentedTree('JJtrendy', []), ParentedTree('NNS', ['bars'])]),
            ParentedTree(',', [',']),
            ParentedTree('NP', [ParentedTree('NNS', ['clubs'])]),
            ParentedTree('CC', ['and']),
            ParentedTree('NP', [ParentedTree('JJ', ['Catalan']), ParentedTree('NNSrestaurants', [])])
        ),
        (
            ParentedTree('NP', [ParentedTree('JJtrendy', []), ParentedTree('NNS', ['bars'])]),
            ParentedTree(',', [',']),
            ParentedTree('NP', [ParentedTree('JJ', ['Catalan']), ParentedTree('NNSrestaurants', [])]),
            ParentedTree('CC', ['and']),
            ParentedTree('NP', [ParentedTree('NNS', ['clubs'])])
        ),
        (
            ParentedTree('NP', [ParentedTree('NNS', ['clubs'])]),
            ParentedTree(',', [',']),
            ParentedTree('NP', [ParentedTree('JJtrendy', []), ParentedTree('NNS', ['bars'])]),
            ParentedTree('CC', ['and']),
            ParentedTree('NP', [ParentedTree('JJ', ['Catalan']), ParentedTree('NNSrestaurants', [])])
        ),
        (
            ParentedTree('NP', [ParentedTree('NNS', ['clubs'])]),
            ParentedTree(',', [',']),
            ParentedTree('NP', [ParentedTree('JJ', ['Catalan']), ParentedTree('NNSrestaurants', [])]),
            ParentedTree('CC', ['and']),
            ParentedTree('NP', [ParentedTree('JJtrendy', []), ParentedTree('NNS', ['bars'])])
        ),
        (
            ParentedTree('NP', [ParentedTree('JJ', ['Catalan']), ParentedTree('NNSrestaurants', [])]),
            ParentedTree(',', [',']),
            ParentedTree('NP', [ParentedTree('JJtrendy', []), ParentedTree('NNS', ['bars'])]),
            ParentedTree('CC', ['and']),
            ParentedTree('NP', [ParentedTree('NNS', ['clubs'])])
        ),
        (
            ParentedTree('NP', [ParentedTree('JJ', ['Catalan']), ParentedTree('NNSrestaurants', [])]),
            ParentedTree(',', [',']),
            ParentedTree('NP', [ParentedTree('NNS', ['clubs'])]),
            ParentedTree('CC', ['and']),
            ParentedTree('NP', [ParentedTree('JJtrendy', []), ParentedTree('NNS', ['bars'])])
        )
    ]

    assert len(result) == 6
    assert result == expected
