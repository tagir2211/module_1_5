immutable_var = (22,11,1994, 'Tagir', False)
print(immutable_var)
immutable_var[0]=23
# элементы кортежа неизменяемы, поэтому возникнет ошибка
mutable_list = [22,11,1994, 'Tagir', False]
print(mutable_list)
mutable_list[0]=23
mutable_list.append('Python')
mutable_list.extend([True, 'C++'])
mutable_list[3] = mutable_list[3] + ' Latypov'
print(mutable_list)