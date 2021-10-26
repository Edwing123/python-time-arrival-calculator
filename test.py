import unittest
from main import main


class FlightArrivalTimeCalculatorTestCase(unittest.TestCase):
    def test_expected_outputs(self) -> None:
        inputs = [
            {"input": [8, 0, 0, 45], "expected": [8, 45]},
            {"input": [8, 30, 2, 30], "expected": [11, 0]},
            {"input": [22, 0, 3, 30], "expected": [1, 30]},
            {"input": [22, 0, 50, 0], "expected": [0, 0]},
            {"input": [22, 0, 0, 3000], "expected": [0, 0]},
            {"input": [12, 34, 0, 0], "expected": [12, 34]},
        ]

        for test_data in inputs:
            data, expected = test_data.values()

            print("Testing output")
            print("Input:", *data)
            print("Expected:", *expected)

            result = main(*data)

            print("Got:", *result)
            print()

            self.assertListEqual(result, expected)
