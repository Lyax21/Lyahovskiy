class Singleton:
	__instance__ = None

#Конструктор
	def __init__(self):
		if Singleton.__instance__ is None:
			Singleton.__instance__ = self	
		else:
			raise Exception("Невозможно создать другой экземпляр Singleton")
			
#Статический метод
	def get_instance():
		if not Singleton.__instance__:
			Singleton()
		return Singleton.__instance__
		
file = Singleton()
print(file)

same_file = Singleton.get_instance()
print(same_file)

another_file = Singleton.get_instance()
print(another_file)

new_file = Singleton()
print(new_file)
