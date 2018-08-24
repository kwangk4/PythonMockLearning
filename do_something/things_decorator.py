from nonexistent_lib_1 import nonexistent_decorator_1
from nonexistent_lib_2 import nonexistent_decorator_2
from nonexistent_lib_3 import nonexistent_decorator_3


@nonexistent_decorator_3(444)
@nonexistent_decorator_2.function_1(404)
@nonexistent_decorator_1
def unit_test_1(object_id):
    """
    Decorator is nonexistent!
    Method Function using decorator.
    """
    # if run this function!
    print('This is method which needs to be tested!')
    return True


from nonexistent_lib_4 import nonexistent_function
from nonexistent_lib_5 import nonexistent_class
from nonexistent_lib_6 import nonexistent_variable

@nonexistent_decorator_3(444)
@nonexistent_decorator_2.function_1(404)
@nonexistent_decorator_1
def unit_test_2():
    """
    Decorator is nonexistent!
    Method Function using Decorator.
    Run other nonexistent functions.
    """
    mock_return_1 = nonexistent_function(nonexistent_variable)
    mock_return_2 = nonexistent_class.function_x()
    print mock_return_1, mock_return_2, nonexistent_variable
    return mock_return_1, mock_return_2

