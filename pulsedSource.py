class PulsedSource:
    def __init__(self, amplitude, pulse_duration, pulse_period):
        """
        Initializes a PulsedSource object.

        Parameters:
        amplitude (float): The amplitude of the pulse.
        pulse_duration (float): The duration of each pulse.
        pulse_period (float): The period between pulses.
        """
        self.amplitude = amplitude
        self.pulse_duration = pulse_duration
        self.pulse_period = pulse_period

    def get_value(self, current_time):
        """
        Returns the value of the pulse at the given time.

        Parameters:
        current_time (float): The current time.

        Returns:
        float: The value of the pulse at the given time.
        """
        pulse_time = current_time % self.pulse_period
        if pulse_time < self.pulse_duration:
            return self.amplitude  # Pulse on
        else:
            return 0.0  # Pulse off
