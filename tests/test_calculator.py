from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "Data Structure" / "calculator.py"


def _load_calculator_module():
    spec = spec_from_file_location("calculator", MODULE_PATH)
    module = module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_basic_operations():
    calculator = _load_calculator_module()

    assert calculator.add(2, 3) == 5
    assert calculator.subtract(7, 4) == 3
    assert calculator.multiply(3, 5) == 15
    assert calculator.divide(8, 2) == 4


def test_divide_by_zero_message():
    calculator = _load_calculator_module()

    assert calculator.divide(5, 0) == "Error! Division by zero."
