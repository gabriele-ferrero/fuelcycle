from component import Component
from pulsedSource import PulsedSource

class FuelingSystem(Component, PulsedSource):
    def __init__(self, name, N_burn, TBE, AF, pulse_period, *args, **kwargs):
        """
        Initialize a FuelingSystem object.

        Args:
            name (str): The name of the fueling system.
            N_burn (float): The number of burn cycles.
            TBE (float): The time between each burn cycle.
            **kwargs: Additional keyword arguments.

        Returns:
            None
        """
        Component.__init__(self, name, residence_time = 1, *args, **kwargs)
        PulsedSource.__init__(self, amplitude=N_burn, pulse_duration=pulse_period*AF, pulse_period=pulse_period)      
        self.N_burn = N_burn
        self.TBE = TBE

    # To plasma
    def get_outflow(self):
        """
        Calculate the outflow rate of the fueling system.

        Returns:
            float: The outflow rate.
        """
        return self.get_pulse()/self.TBE
