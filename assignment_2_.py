def translate_numeral(number):
	if type(number) == str:  # check type of input
		roman_numeral = number
		list1 = list(roman_numeral) # verwandelt Eingabe in Liste mit einzelnen Einträgen.
		# ======enter code below======
		
		Zuordnung = {'I' : 1,	'X' : 10, 'C' : 100, 'M' : 1000, 'V' : 5, 'L' : 50, 'D' : 500, '0' :0} #Dictionary, welches den römischen Zahlen, die arabischen Zahlen zuweist.

		if len(roman_numeral) % 2 != 0: #Zahl ist ungerade, daher an erster Stelle eine 0.
			list1.insert(0,'0')

		arabic_number = 0	# Variable ist erstmal 0

		for i in range(0,len(list1)-1,2): # Immer in zweier Schritten, d.h. ein "Block" von zwei Zahlen.
			if Zuordnung[list1[i]] >= Zuordnung[list1[i+1]]:	#Wenn die Nachfolgezahl kleiner oder gleich ist, wird zur Variable die Summe der beiden dazu addiert.
				arabic_number += Zuordnung[list1[i]] + Zuordnung[list1[i+1]]
				
			if Zuordnung[list1[i]] < Zuordnung[list1[i+1]]:		#Wenn die Nachfolgezahl größer ist, wird zur Variable die Differenz der beiden dazu addiert.
				arabic_number += Zuordnung[list1[i+1]] - Zuordnung[list1[i]]
				

		
		# ======enter code above======
		print('{0} translated to {1}!'.format(roman_numeral, arabic_number))  # print the result
		return arabic_number 

	else:
		print('Input not valid.')

if __name__ == '__main__':
	input_numerals = ['X', 'XXVIII', 'LXXI', 'XCIX', 'MCMXCIV']
	outputs = [10, 28, 71, 99, 1994]
	results = [True, True, True, True, True]

	for index in range(5):
		if translate_numeral(input_numerals[index]) != outputs[index]:
			results[index] = False

	if False in results:
		print('Not all numerals translated correctly. Try again.')
	else:
		print('Well done! All numerals translated correctly.')


