
my_list = [(2,'d','g'),(2,'f','h',56)]
flat_list = [num for sublist in my_list for num in sublist]

c = [e for e in flat_list if isinstance(e, int)]
print(sum(c))
