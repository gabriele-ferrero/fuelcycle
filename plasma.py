from component import Component
from pulsedSource import PulsedSource

class Plasma(Component, PulsedSource):
    def __init__(self, name, N_burn, TBE, AF, pulse_period, *args, **kwargs):
        """
        Initialize a Plasma object.

        Args:
            name (str): The name of the plasma.
            N_burn (float): The burn rate of the plasma.
            TBE (float): The tritium burnup efficiency of the plasma.
            AF (float): The amplification factor of the pulse.
            pulse_period (float): The period between pulses.
        """
        Component.__init__(self, name, residence_time = 1, *args, **kwargs)
        PulsedSource.__init__(self, amplitude=N_burn, pulse_duration=pulse_period*AF, pulse_period=pulse_period)
        self.N_burn = N_burn
        self.TBE = TBE

    def get_inflow(self):
        """
        Calculate the inflow rate of the plasma.

        Returns:
            float: The inflow rate of the plasma.

        """
        return self.get_pulse()/self.TBE

    def get_outflow(self):
        """
        Calculate the outflow rate of the plasma.

        Returns:
            float: The outflow rate of the plasma.

        """
        return (1 - self.TBE)/self.TBE * self.get_pulse()
    
    def calculate_inventory_derivative(self):
        """
        Calculate the derivative of the plasma inventory.

        Returns:
            float: The derivative of the plasma inventory.

        """
        inflow = self.get_inflow()
        outflow = self.get_outflow()
        dydt = inflow - outflow + self.tritium_source - self.get_pulse()
        return dydt
