from dataclasses import dataclass
from typing import List

# Define the resting voltages for ions
RESTING_VOLTAGE = [-90, -80]  # Can be updated depending on the system


@dataclass
class Gate:
    InSelectivity: List[int]  # Rate at which ions move in
    ExSelectivity: List[int]  # Rate at which ions move out
    InGradienceLength: float  # The gradient length for inward movement
    ExGradienceLength: float  # The gradient length for outward movement

    def getConductenceChange(self, VoltM: float):
        """
        Calculate the conductance change based on the voltage and selectivity for
        both inward and outward ions. The sum of inward and outward selectivity
        should be balanced in terms of ionic flux.
        """

        # Ensure that the sum of InSelectivity matches the sum of ExSelectivity
        if sum(self.InSelectivity) != sum(self.ExSelectivity):
            raise ValueError("Sum of InSelectivity must equal sum of ExSelectivity to maintain ionic balance.")

        # Calculate the driving force for each voltage component
        DrivingForce = [VoltM - x for x in RESTING_VOLTAGE]

        # Initialize ConductenceChange array
        ConductenceChange = [0, 0]

        for i in range(len(DrivingForce)):
            if DrivingForce[i] > 0:
                # When the driving force is positive (depolarization), ions are flowing inward
                ConductenceChange[i] = (DrivingForce[i] / self.InGradienceLength) * self.InSelectivity[i]
            else:
                # When the driving force is negative (hyperpolarization), ions are flowing outward
                ConductenceChange[i] = (DrivingForce[i] / self.ExGradienceLength) * self.ExSelectivity[i]

        return ConductenceChange