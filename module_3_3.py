def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [False, '"Что-то там"', 55]
values_dict = {'a': 'one', 'b': 'two', 'c': 'three'}

values_list_2 = [54.32, 'Строка']



print_params()
print_params(1, 2, 3)
print_params(True)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
