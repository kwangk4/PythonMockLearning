import unittest
import mock
import context


class TestThingsFunction(unittest.TestCase):
    def test_return_one_value(self):
        """
        test: return_one_value(number_1, number_2)
        Input: (10, 10)
        Output: 50
        assert: 50
        """
        # arrange
        mock_number_1 = 10
        mock_number_2 = 10
        # action
        from things_function import return_one_value
        result = return_one_value(mock_number_1, mock_number_2)
        # assert
        self.assertEqual(result, 50)

    def test_return_multiple_value(self):
        """
        test: return_multiple_value(string_1, string_2)
        Input: ('domain_name_1.com.vn', 'domain_name_2.com.vn')
        Output:  'domain_name_1', 'domain_name_2'
        :return:
        """
        # arrange
        mock_string_1 = 'domain_name_1.com.vn'
        mock_string_2 = 'domain_name_2.com.vn'
        # action
        from things_function import return_multiple_value
        result_1, result_2 = return_multiple_value(mock_string_1, mock_string_2)
        # assert
        self.assertEqual(result_1, 'domain_name_1')
        self.assertEqual(result_2, 'domain_name_2')

    @mock.patch('things_decorator.nonexistent_lib_1')
    @mock.patch('things_decorator.nonexistent_variable', 10)    # nonexistent_variable = 10
    @mock.patch('things_decorator.nonexistent_class')
    @mock.patch('things_decorator.nonexistent_function')
    def run_nonexistent_functions(self, mock_nonexistent_function, mock_nonexistent_class
                                  , mock_nonexistent_lib_1):
        """
        test: run_nonexistent_functions()
        :param mock_nonexistent_function: function in nonexistent_lib_3
        :param mock_nonexistent_class: class in nonexistent_lib_2
        :param mock_nonexistent_lib_1: library
        Case 1: return None
        """
        # arrange
        mock_nonexistent_function.return_value = ['name_mock1', 'name_mock2']
        # action
        from things_function import run_nonexistent_functions
        result = run_nonexistent_functions()
        # assert
        self.assertIsNone(result)



