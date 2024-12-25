from math import pi as PI, sqrt, exp
from dataclasses import dataclass
from typing import List, Tuple

from IonicGate import Gate, RESTING_VOLTAGE


@dataclass
class Branch:
    ends: Tuple[Tuple[int, int], Tuple[int, int]]
    gates: List[Tuple[Gate, int]]
    crossSection: float
    capacitance: float
    resistivity: float

    def __post_init__(self):


        # Calculate the length of the branch
        self.length = sqrt((self.ends[0][0] - self.ends[1][0]) ** 2 +
                           (self.ends[0][1] - self.ends[1][1]) ** 2)

        # Resistance per unit length
        self.ra = self.resistivity / (PI * (self.crossSection ** 2))  # Axial resistance
        self.rm = self.resistivity * self.length / (2 * PI * self.crossSection)  # Membrane resistance

        # Membrane capacitance
        self.cm = self.capacitance * 2 * PI * self.crossSection

        self.lambd = sqrt(self.rm / self.ra)

        # Time constant and space constant
        self.tau = self.rm * self.cm



    def activate(self, ions: List[float]):
        ion_volt = [y - x for x, y in zip(RESTING_VOLTAGE, ions)]
        total_volt = sum(ion_volt)

        # Initialize a list to accumulate ionic flux changes

        for gate, distance_offset in self.gates:


            # Apply exponential decay for voltage based on the distance
            applied_volt = total_volt * exp(-abs(distance_offset) / self.lambd)

            # Update the gate's conductance
            gate.applyConductenceChange(applied_volt)

            # Calculate ionic currents for each ion
            ionic_current = [(ion_volt[i] * gate.Conductence[i]) for i in range(len(ions))]

            print(ionic_current, distance_offset)

        return total_volt * exp(-abs(self.length) / self.lambd)

