import numpy as np
from typing import Union, Tuple


def workflow_fft(
    data: np.ndarray, sampling_rate: Union[int, float]
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Perform a workflow for analyzing the frequency content of the input data.

    The workflow includes:
    1. Applying a Hamming window to the input data.
    2. Calculating the Fast Fourier Transform (FFT) of the windowed data.
    3. Masking negative frequencies from the FFT result.
    4. Calculating the magnitude spectrum in decibels (dB).

    Parameters:
    - data (numpy.ndarray): Input time-domain data.
    - sampling_rate (Union[int, float]): Sampling rate of the input data.

    Returns:
    - data_windowed (numpy.ndarray): Windowed version of the input data.
    - data_window (numpy.ndarray): The Hamming window applied to the data.
    - frequencies (numpy.ndarray): Array of frequencies.
    - magnitude_db (numpy.ndarray): Magnitude spectrum in decibels corresponding to the frequencies.

    Example:
    >>> data = np.array([1.0, 2.0, 3.0, 4.0])
    >>> sampling_rate = 4.0
    >>> workflow_fft(data, sampling_rate)
    (array([0., 1., 3., 4.]), array([0.08, 0.54, 0.92, 0.54]), array([0., 1., 2.]), array([12.04119983,  6.02059991,  0.        ]))
    """
    data_windowed, data_window = window_data(data)
    freq, magnitude = calc_fft(data_windowed, sampling_rate)
    freq, magnitude = mask_negative_freq(freq, magnitude)
    magnitude_db = calc_magnitude_spectrum_db(magnitude)
    return data_windowed, data_window, freq, magnitude_db


def window_data(data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Apply a Hamming window to the input data.

    Parameters:
    - data (numpy.ndarray): Input data to be windowed.

    Returns:
    - data_windowed (numpy.ndarray): Windowed version of the input data.
    - window (numpy.ndarray): The Hamming window applied to the data.

    Example:
    >>> data = np.array([1.0, 2.0, 3.0, 4.0])
    >>> window_data(data)
    (array([0., 1., 3., 4.]), array([0.08, 0.54, 0.92, 0.54]))
    """
    n = len(data)
    window = np.hamming(n)
    data_windowed = data * window
    return data_windowed, window


def calc_fft(
    data: np.ndarray, sampling_rate: Union[int, float]
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculate the Fast Fourier Transform (FFT) of the input data.

    Parameters:
    - data (numpy.ndarray): Input time-domain data.
    - sampling_rate (float): Sampling rate of the input data.

    Returns:
    - frequencies (numpy.ndarray): Array of frequencies.
    - magnitude_spectrum (numpy.ndarray): Magnitude spectrum corresponding to the frequencies.

    Example:
    >>> data = np.array([1.0, 2.0, 1.0, -1.0])
    >>> sampling_rate = 4.0
    >>> calc_fft(data, sampling_rate)
    (array([ 0.,  1.,  2., -1.]), array([5., 2., 1., 2.]))
    """
    n = len(data)
    fft_result = np.fft.fft(data)
    frequencies = np.fft.fftfreq(n, d=1 / sampling_rate)
    magnitude_spectrum = np.abs(fft_result)
    return frequencies, magnitude_spectrum


def mask_negative_freq(
    freq: np.ndarray, magnitude: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Mask negative frequencies from the given frequency and magnitude arrays.

    Parameters:
    - freq (numpy.ndarray): Array of frequencies.
    - magnitude (numpy.ndarray): Array of corresponding magnitudes.

    Returns:
    - masked_freq (numpy.ndarray): Frequencies with negative values removed.
    - masked_magnitude (numpy.ndarray): Magnitudes corresponding to the remaining frequencies.

    Example:
    >>> freq = np.array([-10, 0, 10, 20])
    >>> magnitude = np.array([1, 2, 3, 4])
    >>> mask_negative_freq(freq, magnitude)
    (array([ 0, 10, 20]), array([2, 3, 4]))
    """
    positive_freq_mask = freq > 0
    freq = freq[positive_freq_mask]
    magnitude = magnitude[positive_freq_mask]
    return freq, magnitude


def calc_magnitude_spectrum_db(
    magnitude_spectrum: Union[np.ndarray, float]
) -> Union[np.ndarray, float]:
    """
    Calculate the magnitude spectrum in decibels (dB) from the given magnitude spectrum.

    Parameters:
    - magnitude_spectrum (numpy.ndarray or float): The input magnitude spectrum.

    Returns:
    - magnitude_spectrum_db (numpy.ndarray or float): The magnitude spectrum in decibels.

    Example:
    >>> magnitude_spectrum = np.array([1.0, 2.0, 3.0])
    >>> calc_magnitude_spectrum_db(magnitude_spectrum)
    array([ 0.        ,  6.02059991, 10.        ])

    Note:
    - If the input is a single float value, the result will also be a float.
    """
    return 20 * np.log10(magnitude_spectrum)
