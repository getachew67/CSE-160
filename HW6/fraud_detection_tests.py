import fraud_detection as fd
import math


def test_ones_and_tens_digit_histogram():
    # example from spec
    actual = fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
    expected = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])
    # add more test cases here


def test_calculate_mse_with_uniform():
    iranian_vote_counts = fd.extract_election_vote_counts(
        'election-iran-2009.csv',
        ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
    iranian_histogram = fd.ones_and_tens_digit_histogram(iranian_vote_counts)
    iranian_mse = fd.calculate_mse_with_uniform(iranian_histogram)
    assert math.isclose(iranian_mse, 0.000739583333333)


def main():
    test_ones_and_tens_digit_histogram()
    # call other test functions here
    test_calculate_mse_with_uniform()
    test_calculate_mse_with_uniform()


if __name__ == "__main__":
    main()
