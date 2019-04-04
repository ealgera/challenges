from collections import defaultdict, namedtuple

Movie = namedtuple('Movie', 'title year score')

movie1 = Movie(title='The Hobbit: The Battle of the Five Armies', year='2014', score='7.5')
movie2 = Movie(title='King Kong', year='2005', score='7.2')
movie3 = Movie(title='The Lovely Bones', year='2009', score='6.7')
movie4 = Movie(title='Heavenly Creatures', year='1994', score='7.4')

movie5 = Movie(title='King Kong', year='2005', score='7.2')

director = "Peter Jackson"
d = defaultdict(list)

print(d, len(d.values()))

d[director].append(movie1) 
print(d, len(d[director]))
print()
#d[director].append(movie2) 
#print(d)
d[director].append(movie3) 
print(d, len(d[director]))
print()

d[director].append(movie3) 
print(d, len(d[director]))
print()

#if movie2 in d[director]:
#    print("Bestaat al!")
#else:
#    print("Bestaat nog niet...")


