from nltk import Tree

from src.services.paraphrase.main import parse_node


def test_parse_node_ok():
    input_node = Tree(
        'NP',
        [
            Tree('NP', [Tree('JJtrendy', []), Tree('NNS', ['bars'])]),
            Tree(',', [',']),
            Tree('NP', [Tree('NNS', ['clubs'])]),
            Tree('CC', ['and']),
            Tree('NP', [Tree('JJ', ['Catalan']), Tree('NNSrestaurants', [])])
        ]
    )

    expected = [
        [Tree('NP', [Tree('NNS', ['clubs'])]), Tree(',', [',']), Tree('NP', [Tree('JJtrendy', []), Tree('NNS', ['bars'])])],
        [Tree('NP', [Tree('JJ', ['Catalan']), Tree('NNSrestaurants', [])]), Tree('NP', [Tree('NNS', ['clubs'])])]
    ]

    result = expected
    assert result == expected


def test_parse_node_bad():
    input_node = Tree(
        'NP',
        [
            Tree('NP', [Tree('JJtrendy', []), Tree('NNS', ['bars'])]),
            Tree('NP', [Tree('NNS', ['clubs'])]),
            Tree(',', [',']),
            Tree('CC', ['and']),
            Tree('NP', [Tree('JJ', ['Catalan']), Tree('NNSrestaurants', [])])
        ]
    )

    expected = []

    result = expected
    assert result == expected
