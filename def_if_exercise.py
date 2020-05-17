def celsius_2_fahrenhit(celsius):
	if celsius < -273.15:
		return "the lowest possibletemperature that physicalmatter can reach is -273.15C not allowed less than"
	else:
		fahrenhit = celsius * (9/5) + 32
		return fahrenhit

#print(celsius_2_fahrenhit(-32433))

temprature_list = [10,-20,-289,100]

for i in temprature_list:
	with open('answers.txt', 'a+') as file:
		
		file.write(str(celsius_2_fahrenhit(i)) + '\n')
	

def string_length(str):
	if type(str) == int:
		return "Sorry integers don't have length"
	elif type(str) == float:
		return "Sorry floats don't have length"


	return len(str)

name = input('what is your name: ')
print(string_length(name))
