from math import pi as PI
from dataclasses import dataclass
from typing import List, Tuple

from IonicGate import Gate


@dataclass
class Branch:
    def __init__(self, ends: Tuple[Tuple[int, int], Tuple[int, int]], gates:  List[Tuple[Gate, int]], crossSection: int, capacitance: int, Resistence: int):
        self.Resistence = Resistence
        self.crossSection = crossSection
        self.gates = gates
        self.ends = ends
        self.capacitance = capacitance

        self.length = ((ends[0][0] - ends[1][0]) ** 2 + (ends[0][1] - ends[1][1]) ** 2) ** 0.5

        self.rm = Resistence / (2 * PI * crossSection)

        self.cm = capacitance * 2 * PI * crossSection



