import pytest

from nltk.tree import MultiParentedTree


@pytest.fixture(scope="session")
def node_with_pairs():
    return MultiParentedTree(
        'NP',
        [
            MultiParentedTree('NP', [MultiParentedTree('JJtrendy', []), MultiParentedTree('NNS', ['bars'])]),
            MultiParentedTree(',', [',']),
            MultiParentedTree('NP', [MultiParentedTree('NNS', ['clubs'])]),
            MultiParentedTree('CC', ['and']),
            MultiParentedTree('NP', [MultiParentedTree('JJ', ['Catalan']), MultiParentedTree('NNSrestaurants', [])])
        ]
    )


@pytest.fixture(scope="session")
def node_without_pairs():
    return  MultiParentedTree(
        'NP',
        [
            MultiParentedTree('NP', [MultiParentedTree('JJtrendy', []), MultiParentedTree('NNS', ['bars'])]),
            MultiParentedTree('NP', [MultiParentedTree('NNS', ['clubs'])]),
            MultiParentedTree(',', [',']),
            MultiParentedTree('CC', ['and']),
            MultiParentedTree('NP', [MultiParentedTree('JJ', ['Catalan']), MultiParentedTree('NNSrestaurants', [])])
        ]
    )


@pytest.fixture(scope="session")
def node_with_pairs_and_wrong_separator():
    return MultiParentedTree(
        'NP',
        [
            MultiParentedTree('NP', [MultiParentedTree('JJtrendy', []), MultiParentedTree('NNS', ['bars'])]),
            MultiParentedTree('JJ', ['Catalan']),
            MultiParentedTree('NP', [MultiParentedTree('NNS', ['clubs'])]),
            MultiParentedTree('NNS', ['clubs']),
            MultiParentedTree('NP', [MultiParentedTree('JJ', ['Catalan']), MultiParentedTree('NNSrestaurants', [])])
        ]
    )

