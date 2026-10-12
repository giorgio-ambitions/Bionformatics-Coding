
from typing import Dict

import numpy as np
from rdkit import Chem


# Atom feature dimensions:
# atomic number: 11
# degree:         6
# formal charge:  6
# aromatic:       1
# total H count:  5
ATOM_FDIM = 31

# Bond feature dimensions:
# bond type: 4
# conjugated: 1
# in ring:    1
BOND_FDIM = 6

_ATOMIC_NUMBERS = [1, 6, 7, 8, 9, 15, 16, 17, 35, 53]
_DEGREES = list(range(6))
_CHARGES = [-2, -1, 0, 1, 2]
_HYDROGENS = list(range(5))
_BOND_TYPES = [
    Chem.BondType.SINGLE,
    Chem.BondType.DOUBLE,
    Chem.BondType.TRIPLE,
    Chem.BondType.AROMATIC,
]


def one_hot_with_other(value, choices):
    """One-hot encode a value, with a final 'other' category."""
    result = [0.0] * (len(choices) + 1)
    try:
        index = choices.index(value)
    except ValueError:
        index = len(choices)
    result[index] = 1.0
    return result


def atom_features(atom) -> list:
    features = []
    features += one_hot_with_other(
        atom.GetAtomicNum(), _ATOMIC_NUMBERS
    )
    features += one_hot_with_other(
        atom.GetTotalDegree(), _DEGREES
    )
    features += one_hot_with_other(
        atom.GetFormalCharge(), _CHARGES
    )
    features.append(float(atom.GetIsAromatic()))
    features += one_hot_with_other(
        atom.GetTotalNumHs(), _HYDROGENS
    )
    return features


def bond_features(bond) -> list:
    features = [
        float(bond.GetBondType() == bond_type)
        for bond_type in _BOND_TYPES
    ]
    features.append(float(bond.GetIsConjugated()))
    features.append(float(bond.IsInRing()))
    return features


def smiles_to_graph(smiles: str) -> Dict[str, np.ndarray]:
    """Convert a SMILES string to a directed molecular graph."""
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles!r}")

    atoms = [atom_features(atom) for atom in mol.GetAtoms()]

    # Each chemical bond becomes two directed edges.
    edges = []
    edge_features = []
    reverse_edge = []

    for bond in mol.GetBonds():
        source = bond.GetBeginAtomIdx()
        target = bond.GetEndAtomIdx()
        features = bond_features(bond)

        forward = len(edges)
        backward = forward + 1

        edges.extend([
            (source, target),
            (target, source),
        ])
        edge_features.extend([features, features.copy()])
        reverse_edge.extend([backward, forward])

    if edges:
        edge_index = np.asarray(edges, dtype=np.int64).T
        bond_x = np.asarray(edge_features, dtype=np.float32)
    else:
        edge_index = np.empty((2, 0), dtype=np.int64)
        bond_x = np.empty((0, BOND_FDIM), dtype=np.float32)

    return {
        "smiles": smiles,
        "atom_x": np.asarray(atoms, dtype=np.float32).reshape(-1, ATOM_FDIM),
        "edge_index": edge_index,
        "bond_x": bond_x,
        "reverse_edge": np.asarray(reverse_edge, dtype=np.int64),
    }


if __name__ == "__main__":
    graph = smiles_to_graph("CCO")

    for key, value in graph.items():
        if isinstance(value, np.ndarray):
            print(f"{key}: shape={value.shape}")
            print(value)
        else:
            print(f"{key}: {value}")
