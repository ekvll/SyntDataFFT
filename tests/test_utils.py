from syntdatafft import (
    generate_anomalies,
    create_plot_dict,
    are_all_floats,
    change_type_to_float,
)
from typing import Dict, Union, List, Any
import pytest


@pytest.fixture
def example_values():
    return {"a": 42, "b": "3.14", "c": "1,000.25", "d": "10,0"}


def test_change_type_to_float(example_values):
    result = change_type_to_float(example_values)

    # Check if the keys are the same
    assert set(result.keys()) == set(example_values.keys())

    # Check if the float conversion is correct
    assert result["a"] == 42.0
    assert result["b"] == 3.14
    assert result["c"] == 1000.25
    assert result["d"] == 10.0


def test_change_type_to_float_warning(capsys):
    values = {"a": "non-numeric"}
    result = change_type_to_float(values)

    # Check if the warning is printed
    captured = capsys.readouterr()
    assert "Cannot convert 'non-numeric' to float" in captured.out

    # Check if the result is as expected (in this case, unchanged)
    assert result == {"a": "non-numeric"}


def test_generate_anomalies():
    plot_dict = {
        "input_1_1": 0.5,
        "input_1_2": 10,
        "input_1_3": 5,
        "input_1_4": 0.1,
        "input_1_5": 0.8,
        "input_2_1": 0.8,
        "input_2_2": 15,
        "input_2_3": 7,
        "input_2_4": 0.05,
        "input_2_5": 0.9,
    }

    result = generate_anomalies(plot_dict)

    expected_result = [
        {
            "amplitude": 0.5,
            "start_time": 10,
            "duration": 5,
            "frequency": 0.1,
            "decay_factor": 0.8,
        },
        {
            "amplitude": 0.8,
            "start_time": 15,
            "duration": 7,
            "frequency": 0.05,
            "decay_factor": 0.9,
        },
    ]

    assert result == expected_result


def test_create_plot_dict():
    values = {"x": 1.0, "y": 2.0, "z": 3.0}

    result = create_plot_dict(values)

    expected_result = {"y": 2.0}

    assert result == expected_result


def test_are_all_floats():
    # Test case with all float or int values
    numeric_values = {"x": 1.0, "y": 2, "z": 3.5}
    assert are_all_floats(numeric_values) is True

    # Test case with mixed types
    mixed_values = {"a": "apple", "b": 2.5, "c": 3}
    assert are_all_floats(mixed_values) is False
