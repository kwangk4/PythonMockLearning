import unittest
import mock
import context
from things_in_class import ClassObject
import sys


class TestThingsInClass(unittest.TestCase):

    @mock.patch.object(ClassObject, '__init__', lambda x, y, z, t: None)         # mock init
    @mock.patch('things_in_class.nonexistent_function')
    def test_first_function(self, mock_nonexistent_function):
        # call class
        call_class = ClassObject('para_1', 'para_2', 'para_3')
        # arrange
        mock_variable = 10
        mock_nonexistent_function.return_value = 100
        # action
        result = call_class.first_function(mock_variable)
        # assert
        self.assertEqual(result, 100)
        mock_nonexistent_function.assert_called_once_with(para=mock_variable)

    @mock.patch('things_in_class.nonexistent_class')
    @mock.patch('things_in_class.function_outside_class')   # mock function outside class
    @mock.patch.object(ClassObject, '__init__', lambda x, y, z, t: None)         # mock init
    def test_run_function_inside_and_outside_class_return_false(self, mock_function_outside_class, mock_nonexistent_class):
        """
        Case 1: return False
        :param mock_function_outside_class:
        assert False
        assert function called:
            self.first_function('any_data'): 1 time
            function_outside_class(): 1 time
            nonexistent_class.unexisted_func(): 0 time
        """
        # call class
        call_class = ClassObject('para_1', 'para_2', 'para_3')
        # arrange
        call_class.first_function = mock.MagicMock(return_value=None)  # mock function in class
        mock_function_outside_class.return_value = None
        # action
        result = call_class.run_function_inside_and_outside_class()
        # assert
        self.assertTrue(~result)
        call_class.first_function.assert_called_once_with('any_data')
        mock_function_outside_class.assert_called_once()
        mock_nonexistent_class.unexisted_func.assert_not_called()

    @mock.patch('things_in_class.nonexistent_class')
    @mock.patch('things_in_class.function_outside_class')  # mock function outside class
    @mock.patch.object(ClassObject, '__init__', lambda x, y, z, t: None)  # mock init
    def test_run_function_inside_and_outside_class_return_true(self, mock_function_outside_class, mock_nonexistent_class):
        # call class
        call_class = ClassObject('para_1', 'para_2', 'para_3')
        with mock.patch.object(ClassObject, '_ClassObject__private_method',
                               return_value="This is return result from mock__private_method") as mock_private_method:
            # arrange
            call_class.first_function = mock.MagicMock(return_value='variable_1')  # mock function in class
            mock_function_outside_class.return_value = 'variable_2'
            # action
            result = call_class.run_function_inside_and_outside_class()
            # assert
            self.assertTrue(result)
            call_class.first_function.assert_called_once_with('any_data')
            mock_function_outside_class.assert_called_once()
            mock_nonexistent_class.unexisted_func.assert_called_once()
            mock_private_method.assert_called_once()

    # def test_unit_test_1(self):
    #     import things_in_class
    #     with mock.patch.object(things_in_class.NonExistentClass, '__bases__', (mock.Mock,)) as mock_NonExistentClass:
    #         import things_in_class
    #         ClassInheritiedFromOtherClass = things_in_class.InheritiedFromOtherClass(mock_NonExistentClass)
    #         ClassInheritiedFromOtherClass.unit_test_1()
    #         pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
