from typing import Dict, List, Union, Any


def change_type_to_float(values: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert numeric values in a dictionary to float.

    Args:
    - values (Dict[str, Any]): A dictionary where values of various types may need conversion.

    Returns:
    - Dict[str, Any]: A new dictionary with numeric values converted to float.

    Note:
    - If a value is already a float, it is left unchanged.
    - If a value is an integer, it is converted to a float.
    - If a value is a string, it is converted to a float, with special handling for commas.
    - If a string contains both commas and periods, commas are removed.
    - If a string contains only commas, they are replaced with periods.
    - If a string is not convertible to float, the original value is kept, and a warning is printed.

    Examples:
    ```python
    values = {'a': 42, 'b': '3.14', 'c': '1,000', 'd': 'invalid'}
    result = change_type_to_float(values)
    print(result)
    # Output: {'a': 42.0, 'b': 3.14, 'c': 1000.0, 'd': 'invalid'}
    ```

    Raises:
    - Prints a warning if a value cannot be converted to a float.
    """
    for key, value in values.items():
        if isinstance(value, float):
            pass

        elif isinstance(value, int):
            new_value = float(value)
            values[key] = new_value

        elif isinstance(value, str):
            if "," in value and "." in value:
                new_value = value.replace(",", "")
            elif "," in value:
                new_value = value.replace(",", ".")
            else:
                new_value = value

            try:
                values[key] = float(new_value)
            except ValueError:
                print(f"Cannot convert '{value}' to float. Keeping the original value")

        else:
            print(f"Cannot convert '{value}' to float")

    return values


def are_all_floats(values: dict) -> bool:
    """
    Check if all values in the given dictionary are of numeric type (float or int).

    Parameters:
    - values (dict): A dictionary to be checked.

    Returns:
    - all_floats (bool): True if all values are of numeric type, False otherwise.

    Example:
    >>> numeric_values = {'x': 1.0, 'y': 2, 'z': 3.5}
    >>> are_all_floats(numeric_values)
    True

    >>> mixed_values = {'a': 'apple', 'b': 2.5, 'c': 3}
    >>> are_all_floats(mixed_values)
    False
    """
    return all(isinstance(value, (float, int)) for value in values.values())


def create_plot_dict(values: Dict[str, float]) -> Dict[str, float]:
    """
    Create a dictionary suitable for plotting by excluding the first and last keys.

    Parameters:
    - values (dict): A dictionary containing values for plotting.

    Returns:
    - plot_dict (dict): A new dictionary containing values for plotting, excluding the first and last keys.

    Example:
    >>> values = {'x': 1.0, 'y': 2.0, 'z': 3.0}
    >>> create_plot_dict(values)
    {'y': 2.0}
    """
    keys_list = list(values.keys())
    plot_dict = {key: values[key] for key in keys_list[1:-1]}
    return plot_dict


def generate_anomalies(
    plot_dict: Dict[str, Union[float, int]]
) -> List[Dict[str, Union[float, int]]]:
    """
    Generate a list of anomaly dictionaries based on the input plot parameters.

    Parameters:
    - plot_dict (dict): A dictionary containing input parameters for generating anomalies.

    Returns:
    - anomalies (list): A list of dictionaries, each representing an anomaly with the following keys:
        - "amplitude": Amplitude of the anomaly.
        - "start_time": Start time of the anomaly.
        - "duration": Duration of the anomaly.
        - "frequency": Frequency of the anomaly.
        - "decay_factor": Decay factor of the anomaly.

    Example:
    >>> plot_dict = {
    ...     "input_1_1": 0.5,
    ...     "input_1_2": 10,
    ...     "input_1_3": 5,
    ...     "input_1_4": 0.1,
    ...     "input_1_5": 0.8,
    ...     "input_2_1": 0.8,
    ...     "input_2_2": 15,
    ...     "input_2_3": 7,
    ...     "input_2_4": 0.05,
    ...     "input_2_5": 0.9,
    ... }
    >>> generate_anomalies(plot_dict)
    [
        {'amplitude': 0.5, 'start_time': 10, 'duration': 5, 'frequency': 0.1, 'decay_factor': 0.8},
        {'amplitude': 0.8, 'start_time': 15, 'duration': 7, 'frequency': 0.05, 'decay_factor': 0.9}
    ]
    """
    return [
        {
            "amplitude": plot_dict[f"input_{i}_1"],
            "start_time": plot_dict[f"input_{i}_2"],
            "duration": plot_dict[f"input_{i}_3"],
            "frequency": plot_dict[f"input_{i}_4"],
            "decay_factor": plot_dict[f"input_{i}_5"],
        }
        for i in range(1, 3)
    ]
