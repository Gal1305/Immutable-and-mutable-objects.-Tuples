immutable_var = tuple([50, True, 'string', 15.5])
print(immutable_var)
#tuple_[0] = 123 - если сделать так, то выдаст ошибку, т.к. tuple это кортеж, является не изменяемым типом данных

# - а это список, изменяемый тип данных
mutable_list = [333, False, 4.15, 'string']
print(mutable_list)
mutable_list[0] = 111
mutable_list[1] = True
mutable_list[2] = 15
mutable_list[3] = 'integer'
print(mutable_list)