# 1. Bypass decorator to test unittest  -[o]
# 2. Mock private method in class       -[o]
# 3. Mock init - [o]


import unittest
import mock
import context

import sys
sys.modules['nonexistent_lib_4'] = mock.Mock()
sys.modules['nonexistent_lib_5'] = mock.Mock()
sys.modules['nonexistent_lib_6'] = mock.Mock()


class TestThingsDecorator(unittest.TestCase):
    @mock.patch('nonexistent_lib_3.nonexistent_decorator_3')
    @mock.patch('nonexistent_lib_2.nonexistent_decorator_2.function_1')
    @mock.patch('nonexistent_lib_1.nonexistent_decorator_1', lambda x: x)
    def test_unit_1(self, mock_nonexistent_decorator_2, mock_nonexistent_decorator_3):
        # arrange
        mock_nonexistent_decorator_2.return_value = lambda x: x
        mock_nonexistent_decorator_3.return_value = lambda x: x
        # action
        import things_decorator
        result = things_decorator.unit_test_1(123456789)
        print result
        # assert
        self.assertTrue(result)

    @mock.patch('nonexistent_lib_3.nonexistent_decorator_3')
    @mock.patch('nonexistent_lib_2.nonexistent_decorator_2.function_1')
    @mock.patch('nonexistent_lib_1.nonexistent_decorator_1', lambda x: x)
    def test_unit_2(self, mock_nonexistent_decorator_2, mock_nonexistent_decorator_3):
        # arrange
        mock_nonexistent_decorator_2.return_value = lambda x: x
        mock_nonexistent_decorator_3.return_value = lambda x: x

        with mock.patch('things_decorator.nonexistent_function') as mock_nonexistent_function, \
                mock.patch('things_decorator.nonexistent_class') as mock_nonexistent_class, \
                mock.patch('things_decorator.nonexistent_variable', 10):

            mock_nonexistent_function.return_value = 'mock_return_1'
            mock_nonexistent_class.function_x.return_value = 'mock_return_2'
            # action
            import things_decorator
            result_1, result_2 = things_decorator.unit_test_2()
            # assert
            self.assertEqual(result_1, 'mock_return_1')
            self.assertEqual(result_2, 'mock_return_2')


if __name__ == "__main__":
    unittest.main()
