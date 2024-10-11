immutable_var = 3, 5, [7, 8], False, 'dog'
print (immutable_var)
immutable_var[2][0] = 6
print(immutable_var)
#мы можем изменить только список, потому что кортежи - не изменяемы, однако список внутри кортежа изменяемы.
#если элементы кортежа объединить в список, то их можно будет изменить.
immutable_var = ([3, 5, 7, 8, False, 'dog'])
immutable_var[-1] = 'cat'
print(immutable_var)
immutable_var[4] = True
print(immutable_var)
mutable_var = [True, 9, 8, 0, 'fanta']
print(mutable_var)
mutable_var[3] = 7
mutable_var[-2] = ('sprite')
mutable_var[0] = False
print(mutable_var)

