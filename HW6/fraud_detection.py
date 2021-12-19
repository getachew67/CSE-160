import utils  # noqa: F401, do not remove if using a Mac
# add your imports BELOW this line
import csv
import matplotlib.pyplot as plt
import random


# Your Set of Functions for this assignment goes in here
def extract_election_vote_counts(filename, column_names):
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        values = []
        for row in csv_reader:
            for each in column_names:
                if each in row:
                    if row[each] is None or len(row[each]) == 0:
                        pass
                    else:
                        values.append(int(row[each].replace(',', '')))
    return values


def ones_and_tens_digit_histogram(numbers):
    frequencies = []
    for i in range(0, 10):
        frequencies.append(0)
    for each in numbers:
        _number = str(each)
        if len(_number) < 2:
            _number = "0" + str(_number)
        ones_place = _number[-1]
        tens_place = _number[-2]
        for i in range(0, 10):
            if str(i) == ones_place:
                frequencies[i] += 1
            if str(i) == tens_place:
                frequencies[i] += 1
    sum_frequencies = 0
    for each in frequencies:
        sum_frequencies += each
    frequency_percentages = []
    for i in range(0, 10):
        frequency_percentages.append(frequencies[i]/sum_frequencies)
    return frequency_percentages


def plot_iran_least_digits_histogram(histogram):
    ideal = []
    for i in range(len(histogram)):
        ideal.append(0.1)
    plt.plot(ideal, label="Ideal")
    plt.plot(histogram, label="Iran")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig("iran-digits.png")
    # plt.show()
    plt.clf()


def plot_distribution_by_sample_size(size):
    data_points = []
    for i in range(size):
        data_points.append(random.randint(0, 99))
    histogram = ones_and_tens_digit_histogram(data_points)
    return histogram


def mean_squared_error(numbers1, numbers2):
    mse = 0
    for i in range(len(numbers1)):
        mse += (numbers1[i] - numbers2[i]) ** 2
    mse /= len(numbers1)
    return mse


def calculate_mse_with_uniform(histogram):
    ideal = []
    for i in range(len(histogram)):
        ideal.append(0.1)
    return mean_squared_error(ideal, histogram)


def generate_frequency_series(array_sizes):
    frequency_series = []
    for each_size in array_sizes:
        series = []
        for i in range(0, each_size):
            series.append(random.randint(0, 99))
        frequency_series.append(ones_and_tens_digit_histogram(series))
    return frequency_series


def compare_country_mse_to_samples(
        country, year, country_mse, number_of_country_data_points):
    total_groups = 10000
    array_sizes = []
    for i in range(0, total_groups):
        array_sizes.append(number_of_country_data_points)
    frequency_series = generate_frequency_series(array_sizes)
    frequency_series_mse_with_uniform = []
    for each_series in frequency_series:
        frequency_series_mse_with_uniform.append(
            calculate_mse_with_uniform(each_series))
    total_greater_than_or_equal_country_mse = 0
    total_less_than_country_mse = 0
    for each in frequency_series_mse_with_uniform:
        if each >= country_mse:
            total_greater_than_or_equal_country_mse += 1
        else:
            total_less_than_country_mse += 1
    print(year, country, "election MSE:", country_mse)
    print("Quantity of MSEs larger than or equal to the", year, country,
          "election MSE:", total_greater_than_or_equal_country_mse)
    print("Quantity of MSEs smaller than the", year, country, "election MSE:",
          total_less_than_country_mse)
    print(year, country, "election null hypothesis rejection level p:",
          total_less_than_country_mse / total_groups)


def compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints):
    compare_country_mse_to_samples(2009, "Iranian", iran_mse,
                                   number_of_iran_datapoints)


def compare_us_mse_to_samples(us_mse, number_of_us_datapoints):
    compare_country_mse_to_samples(2008, "United States", us_mse,
                                   number_of_us_datapoints)


# The code in this function is executed when this
# file is run as a Python program
def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.

    # Iran 2009 election
    iranian_vote_counts = extract_election_vote_counts(
        'election-iran-2009.csv', [
            "Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
    iranian_histogram = ones_and_tens_digit_histogram(iranian_vote_counts)
    plot_iran_least_digits_histogram(iranian_histogram)

    # plot_distribution_by_sample_size()

    iranian_mse = calculate_mse_with_uniform(iranian_histogram)
    compare_iran_mse_to_samples(iranian_mse, len(iranian_vote_counts))

    # US 2008 election
    us_2008_candidates = [
        "Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"]
    us_vote_counts = extract_election_vote_counts(
        'election-us-2008.csv', us_2008_candidates)
    us_histogram = ones_and_tens_digit_histogram(us_vote_counts)
    us_mse = calculate_mse_with_uniform(us_histogram)
    compare_iran_mse_to_samples(us_mse, len(us_vote_counts))

    print("2009 Iranian election MSE: " + str(iranian_mse))
    compare_iran_mse_to_samples(iranian_mse, len(iranian_vote_counts))
    print()
    print("2008 United States election MSE: " + str(us_mse))
    compare_us_mse_to_samples(us_mse, len(us_vote_counts))


if __name__ == "__main__":
    main()
