def kteam():
	print('Hello')
print(type(kteam))
kteam()

def kteam1(text):
	print(text)
kteam1('Hello Kteam!')

def kteam(greating, name):
	print(greating, name + '!')
kteam('Hi', 'Kteam')
kteam('Hello', 'SpaceX')


def kteam(name, greating='Hi'):
	print(greating, name + '!')
kteam('Kteam')
kteam('SpaceX')
kteam('SpaceX', 'Hello')
