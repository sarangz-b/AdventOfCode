import csv
import unittest

class DistanceCalc:
    def __init__(self, input_file):
        self.l1, self.l2 = self.read_csv(input_file)

    def read_csv(self, input_file):
        l1 = []
        l2 = []
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                l1.append(int(row[0]))
                l2.append(int(row[1]))
        return l1, l2

    def calculate_distance(self):
        self.l1.sort()
        self.l2.sort()

        total_distance = 0
        for num1, num2 in zip(self.l1, self.l2):
            total_distance += abs(num1 - num2)

        return total_distance

class Testing(unittest.TestCase):
    def test_day01(self):
        calculator = DistanceCalc('input.csv')
        expected_distance = 11
        self.assertEqual(calculator.calculate_distance(), expected_distance)

if __name__ == '__main__':
    calculator = DistanceCalc('input.csv')
    total_distance = calculator.calculate_distance()
    print("Total distance:", total_distance)
    unittest.main()