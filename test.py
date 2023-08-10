class Person(object):
	"""A simple class."""
	species = "Homo Sapiens"

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def rename(self, renamed):
		self.name = renamed
		print("Now my name is {}".format(self.name))


kelly = Person("Kelly")
john_doe = Person("John Doe")
joseph = Person("Joseph")

print("Kelly's species is: " + kelly.species)
print(joseph.name)
john_doe.rename("Johnny")
