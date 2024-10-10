my_dict = {'Vasya' : 1975 , 'Egor' : 1999 , 'Masha' : 2002}
print(my_dict)
print(my_dict['Masha'])
print(my_dict.get('Vlad'))
my_dict.update({'Sahsa' : 1989,
                'Alex' : 1979})
a = my_dict.pop('Egor')
print(a)
print(my_dict)
my_set = {1, 1, 1, 1, 'Яблоко', 42.314}
print(my_set)
my_set.update({13 , (5, 6, 1.6)})
my_set.discard(1)
print(my_set)