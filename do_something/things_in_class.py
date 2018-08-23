import nonexistent_lib_1
from nonexistent_lib_2 import nonexistent_function
from nonexistent_lib_3 import nonexistent_class


class ClassObject(object):
    def __init__(self, param_1, param_2, param_3):
        """
        :param param_1: parameter 1
        :param param_2: parameter 2
        :param param_3: parameter 3
        """
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3

    # private method    - need to mock!
    def __private_method(self):
        print 'This is private method!'
        return 'private_method'

    def first_function(self, variable):
        """
        Function inside class
        :param variable: random
        :return:
        """
        print('...Some code...')
        first_var = nonexistent_function(para=variable)
        return first_var

    def run_function_inside_and_outside_class(self):
        # run function inside class
        variable_1 = self.first_function('any_data')
        result_from_private = self.__private_method()
        # run function outside class
        variable_2 = function_outside_class()
        print variable_1, variable_2, result_from_private
        # To have more test case
        if variable_1 and variable_2:
            # this function for assert condition
            nonexistent_class.unexisted_func()
            return True
        return False


def function_outside_class():
    print('This is function outside the class')
    if nonexistent_lib_1.do_something():
        return True
    return False

################################INHRERITED CLASS##############################################
# --- Problems --- [x]

from nonexistent_lib_4 import NonExistentClass


class InheritiedFromOtherClass(NonExistentClass):
    def unit_test_1(self):
        print 'This is method in Inherited Class'
        pass

