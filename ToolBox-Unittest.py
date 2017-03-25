import unittest

def sortnegative(list_numbers):
    """This function sorts a list of numbers and removes the negative numbers
    """
    sorted_numbers = sorted(list_numbers)
    positive_numbers = []
    for number in sorted_numbers:
        if number >= 0:
            positive_numbers.append(number)
    print(positive_numbers)
    return positive_numbers


class TestStringMethods(unittest.TestCase):

    def test_noNegatives(self):
        """Test that the function removes negative numbers"""
        list_numbers = [-4, 5, 12, 0, -2, -8, 9]
        positive_list = [0, 5, 9, 12]
        sortnegative(list_numbers)
        self.assertEqual(sortnegative(list_numbers), positive_list)


    def test_Sorted(self):
        """Test that the function sorts the list"""
        list_numbers =  [-4, 5, 12, 0, -2, -8, 9]
        sorted_list = sorted(list_numbers)
        self.assertEqual(sorted(list_numbers), sorted_list)


if __name__ == '__main__':
    unittest.main()
