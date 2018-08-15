import unexisted_lib_1
from unexisted_lib_2 import unexisted_class
from unexisted_lib_3 import unexisted_function
from unexisted_lib_4 import unexisted_variable


def return_one_value(number_1, number_2):
    """
    :param number_1: int, double
    :param number_2: int, double
    :return: sum of 2 incremented number
    """
    number_1 += 10
    print ('number 1 is incremented')
    number_2 += 20
    print ('number 2 is incremented')
    return number_1+number_2


def return_multiple_value(string_1, string_2):
    """
    :param string_1: "domain_name_1.com.vn"
    :param string_2: "domain_name_2.com"
    :return:
    """
    print 'string 1: ' + string_1
    print 'string 2: ' + string_2
    return string_1.split('.')[0], string_2.split('.')[0]


def run_unexisted_functions():
    """
    :return:
        None if same name;
        Mew string if not.
    """
    string_1 = unexisted_function(para=1)
    string_2 = unexisted_function(para=2)
    if string_1.split('_')[0] == string_2.split('_')[0]:
        print('-------Same name------')
        return
    string_1 = unexisted_class.get_string_1(para=unexisted_variable)
    string_2 = unexisted_lib_1.get_string_2(para=unexisted_variable)
    return string_1, string_2

def try_and_except_function():
    try:
        print('---This is try---')
        return True
    except:
        print('---This is except---')
        raise Exception('except')
