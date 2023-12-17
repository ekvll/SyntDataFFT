import numpy as np
from typing import List, Dict, Tuple


def gen_1d_test_data(
    duration: float,
    sampling_rate: float,
    noise_level: float,
    anomalies: List[Dict[str, float]],
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate 1D test data with anomalies.

    Parameters:
    - duration (float): Duration of the generated data in seconds.
    - sampling_rate (float): Sampling rate of the generated data.
    - noise_level (float): Level of random noise to be added to the data.
    - anomalies (list of dict): List of dictionaries, each containing parameters for an anomaly.
        Each dictionary should have the following keys:
            - "amplitude" (float): Amplitude of the anomaly.
            - "start_time" (float): Start time of the anomaly.
            - "duration" (float): Duration of the anomaly.
            - "frequency" (float): Frequency of the anomaly.
            - "decay_factor" (float): Decay factor of the anomaly.

    Returns:
    - time (numpy.ndarray): Array of time values.
    - data (numpy.ndarray): Generated 1D test data with anomalies and noise.

    Example:
    >>> duration = 10.0
    >>> sampling_rate = 100.0
    >>> noise_level = 0.1
    >>> anomalies = [
    ...     {"amplitude": 1.0, "start_time": 2.0, "duration": 3.0, "frequency": 0.5, "decay_factor": 0.1},
    ...     {"amplitude": 0.8, "start_time": 6.0, "duration": 2.0, "frequency": 0.8, "decay_factor": 0.05}
    ... ]
    >>> gen_1d_test_data(duration, sampling_rate, noise_level, anomalies)
    (array([0.  , 0.01, 0.02, ..., 9.97, 9.98, 9.99]),
     array([ 0.04267712,  0.19942342,  0.37813247, ..., -0.09125388,
            -0.12258709, -0.08630525]))
    """
    time = np.arange(0, duration, 1 / sampling_rate)
    data = np.zeros(len(time))

    for anomaly_params in anomalies:
        anomaly_amplitude = anomaly_params["amplitude"]
        anomaly_start_time = anomaly_params["start_time"]
        anomaly_duration = anomaly_params["duration"]
        anomaly_frequency = anomaly_params["frequency"]
        decay_factor = anomaly_params["decay_factor"]

        start_index = int(anomaly_start_time * sampling_rate)
        end_index = start_index + int(anomaly_duration * sampling_rate)

        anomaly_time = np.arange(0, anomaly_duration, 1 / sampling_rate)
        anomaly = anomaly_amplitude * np.sin(
            2 * np.pi * anomaly_frequency * anomaly_time
        )

        decay = np.exp(-decay_factor * anomaly_time)
        anomaly *= decay

        # Adjust the start and end indices to correctly add the anomaly to the data array
        data[start_index:end_index] += anomaly[: len(data[start_index:end_index])]

    data += noise_level * np.random.normal(size=len(data))

    return time, data
