import unittest

class Calculator:
    def __init__(self, input_file):
        self.l1, self.l2 = self.read_text(input_file)

    def read_text(self, input_file):
        l1 = []
        l2 = []
        with open(input_file, 'r') as file:
            for line in file:
                num1, num2 = map(int, line.split())
                l1.append(num1)
                l2.append(num2)
        l1.sort()
        l2.sort()
        return l1, l2

    def calculate_distance(self):
        self.l1.sort()
        self.l2.sort()

        total_distance = 0
        for num1, num2 in zip(self.l1, self.l2):
            total_distance += abs(num1 - num2)

        return total_distance

    def calculate_similarity_score(self):
        right_counts = {}
        for num in self.l2:
            right_counts[num] = right_counts.get(num, 0) + 1

        similarity_score = 0
        for num in self.l1:
            similarity_score += num * right_counts.get(num, 0)

        return similarity_score

class Testing(unittest.TestCase):
    def test_day01(self):
        test_distance = Calculator('./test_input.txt')
        expected_distance = 11
        self.assertEqual(test_distance.calculate_distance(), expected_distance)

    def test_day01_similarity(self):
        test_similarity = Calculator('test_input.txt')
        expected_similarity = 31
        self.assertEqual(test_similarity.calculate_similarity_score(), expected_similarity)


if __name__ == '__main__':
    calculator = Calculator('./live_input.txt')
    total_distance = calculator.calculate_distance()
    print("Total distance:", total_distance)
    similarity_score = calculator.calculate_similarity_score()
    print("Similarity score:", similarity_score)
    unittest.main()