
from NeuronBranches import Branch

from IonicGate import Gate

if __name__ == '__main__':

    b = Branch(((0, 0), (0, 10)), [(Gate(
        [1, 1],
        [1, 1],
        5,
        5
    ), 1)],
               1, 10, 1)

    b.activate([0, 0])
    b.activate([0, 0])
    b.activate([0, 0])


