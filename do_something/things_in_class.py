import unexisted_lib_1
from unexisted_lib_2 import unexisted_function
from unexisted_lib_3 import unexisted_class


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

    def first_function(self, variable):
        """
        Function inside class
        :param variable: random
        :return:
        """
        first_var = unexisted_function(para=variable)
        return first_var

    def run_function_inside_and_outside_class(self):
        # run function inside class
        variable_1 = self.first_function('any_data')
        # run function outside class
        variable_2 = function_outside_class()
        # To have more test case
        if variable_1 and variable_2:
            # this function for assert condition
            unexisted_class.unexisted_func()
            return True
        return False

def function_outside_class():
    print('This is function outside the class')
    if unexisted_lib_1.do_something():
        return True
    return False
