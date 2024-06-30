my_dict = {'Mila' : 22, 'Sasha' : 16,'Viktor' : 74}
print(my_dict)
print(my_dict['Sasha'])
my_dict = {'Mila' : 22, 'Sasha' : 16,'Viktor' : [74,65]}
print(my_dict)
my_dict.update({'Oleg' : 43,
                'Misha' : 11})
print(my_dict.pop('Mila'))
print(my_dict)

my_set = {'ser', 22, 'lor', 70, "per", 2, 'gor', 22, 'gor', 22, 45, 'ber', 2, 'arr'}
print(my_set)
my_set.add(3.0 )
my_set.add('rar')
my_set.remove('lor')
print(my_set)