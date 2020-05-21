from array import *
import random



dic = {'A':1 , 'B':2 , 'C':3 , 'D':4 , 'E':5 , 'F':6 , 'G':7 , 'H':8, 'I':9, 'J':10}

def my_battlefield():
	global columns
	global rows

	columns = []

	for j in range(10):
		rows = []

		for i in range(10):
			rows.append(None)
		columns.append(rows)

my_battlefield()


def place_ships_fünfer():
	global fünfer
	len_ship = 4

	fünfer = list(input("Platziere dein fünfer Schiff: (z.B. D5 bis D9 oder A2 bis E2)"))
	fünfer.remove(" ")
	fünfer.remove("b")
	fünfer.remove("i")
	fünfer.remove("s")
	fünfer.remove(" ")

	if len(fünfer) == 5:	#Falls Liste eine doppelzahl enthält, rausfinden wo diese ist und auf 10 setzen.
		del fünfer[-2:]
		fünfer.append('10')
	elif len(fünfer) == 6:	#Falls Liste zwei doppelzahlen enthält, beide auf 10 setzen.
		del fünfer[-2:]
		fünfer.append('10')
		del fünfer[1:3]
		fünfer.insert(1, '10')


	# Anfangs- und Endzahl festlegen
	Zahl_start = int(fünfer[1])
	Zahl_ende = int(fünfer[-1])

	Buchstabe_start = dic[fünfer[0]]  # Buchstabe bei dem gestartet wird
	Buchstabe_ende = dic[fünfer[2]]  # Buchstabe bei dem geendet wird

	if Zahl_ende - Zahl_start == len_ship or Buchstabe_ende - Buchstabe_start == len_ship:
		if Buchstabe_start - Buchstabe_ende == 0:  # Schiff waagerecht
			for j in range(Zahl_start - 1, Zahl_ende):
				columns[Buchstabe_start - 1][j] = 'Schiff'

		if Zahl_start - Zahl_ende == 0:  # Schiff senkrecht
			for i in range(Buchstabe_start - 1, Buchstabe_ende):
				columns[i][Zahl_start - 1] = 'Schiff'



	else:		#Falls Anzahl an Kästchen über- oder unterschritten
		if Zahl_ende - Zahl_start > len_ship:
			print("Du hast mehr Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")

		elif Buchstabe_ende - Buchstabe_start > len_ship:
			print("Du hast mehr Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")


		elif Zahl_ende - Zahl_start < len_ship:
			print ("Du hast weniger Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")


		elif Buchstabe_ende - Buchstabe_start < len_ship:
			print("Du hast weniger Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")


	print(columns)

def place_ships_vierer():
	global vierer
	len_ship = 3

	vierer = list(input("Platziere dein vierer Schiff: (z.B. D5 bis D8 oder A2 bis D2)"))
	vierer.remove(" ")
	vierer.remove("b")
	vierer.remove("i")
	vierer.remove("s")
	vierer.remove(" ")

	if len(vierer) == 5:	#Falls Liste eine doppelzahl enthält, rausfinden wo diese ist und auf 10 setzen.
		del vierer[-2:]
		vierer.append('10')
	elif len(vierer) == 6:	#Falls Liste zwei doppelzahlen enthält, beide auf 10 setzen.
		del vierer[-2:]
		vierer.append('10')
		del vierer[1:3]
		vierer.insert(1, '10')


	# Anfangs- und Endzahl festlegen
	Zahl_start = int(vierer[1])
	Zahl_ende = int(vierer[-1])

	Buchstabe_start = dic[vierer[0]]  # Buchstabe bei dem gestartet wird
	Buchstabe_ende = dic[vierer[2]]  # Buchstabe bei dem geendet wird

	# Überprüfe, ob Feld frei ist
	if Zahl_ende - Zahl_start == len_ship or Buchstabe_ende - Buchstabe_start == len_ship:
		if Buchstabe_start - Buchstabe_ende == 0:  # Schiff waagerecht
			for j in range(Zahl_start - 1, Zahl_ende):
				if columns[Buchstabe_start - 1][j] == None:
					columns[Buchstabe_start - 1][j] = 'Schiff'
				else:
					print("Eins der Felder ist bereits belegt. Bitte wähle erneut")
					return

		if Zahl_start - Zahl_ende == 0:  # Schiff senkrecht
			for i in range(Buchstabe_start - 1, Buchstabe_ende):
				if columns[i][Zahl_start - 1] == None:
					columns[i][Zahl_start - 1] = 'Schiff'
				else:
					print("Eins der Felder ist bereits belegt. Bitte wähle erneut")
					return


	else:		#Falls Anzahl an Kästchen über- oder unterschritten
		if Zahl_ende - Zahl_start > len_ship:
			print("Du hast mehr Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return
		elif Buchstabe_ende - Buchstabe_start > len_ship:
			print("Du hast mehr Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return

		elif Zahl_ende - Zahl_start < len_ship:
			print ("Du hast weniger Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return

		elif Buchstabe_ende - Buchstabe_start < len_ship:
			print("Du hast weniger Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return

	print(columns)

def place_ships_dreier():
	global dreier
	len_ship=2

	dreier = list(input("Platziere dein dreier Schiff: (z.B. D5 bis D7 oder A2 bis C2)"))
	dreier.remove(" ")
	dreier.remove("b")
	dreier.remove("i")
	dreier.remove("s")
	dreier.remove(" ")

	if len(dreier) == 5:	#Falls Liste eine doppelzahl enthält, rausfinden wo diese ist und auf 10 setzen.
		del dreier[-2:]
		dreier.append('10')
	elif len(dreier) == 6:	#Falls Liste zwei doppelzahlen enthält, beide auf 10 setzen.
		del dreier[-2:]
		dreier.append('10')
		del dreier[1:3]
		dreier.insert(1, '10')

	# Anfangs- und Endzahl festlegen
	Zahl_start = int(dreier[1])
	Zahl_ende = int(dreier[-1])

	Buchstabe_start = dic[dreier[0]]  # Buchstabe bei dem gestartet wird
	Buchstabe_ende = dic[dreier[2]]  # Buchstabe bei dem geendet wird

	# Überprüfe, ob Feld frei ist
	if Zahl_ende - Zahl_start == len_ship or Buchstabe_ende - Buchstabe_start == len_ship:
		if Buchstabe_start - Buchstabe_ende == 0:  # Schiff waagerecht
			for j in range(Zahl_start - 1, Zahl_ende):
				if columns[Buchstabe_start - 1][j] == None:
					columns[Buchstabe_start - 1][j] = 'Schiff'
				else:
					print("Eins der Felder ist bereits belegt. Bitte wähle erneut")
					return

		if Zahl_start - Zahl_ende == 0:  # Schiff senkrecht
			for i in range(Buchstabe_start - 1, Buchstabe_ende):
				if columns[i][Zahl_start - 1] == None:
					columns[i][Zahl_start - 1] = 'Schiff'
				else:
					print("Eins der Felder ist bereits belegt. Bitte wähle erneut")
					return


	else:		#Falls Anzahl an Kästchen über- oder unterschritten
		if Zahl_ende - Zahl_start > len_ship:
			print("Du hast mehr Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return
		elif Buchstabe_ende - Buchstabe_start > len_ship:
			print("Du hast mehr Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return

		elif Zahl_ende - Zahl_start < len_ship:
			print ("Du hast weniger Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return

		elif Buchstabe_ende - Buchstabe_start < len_ship:
			print("Du hast weniger Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return

	print(columns)


def place_ships_zweier():
	global zweier
	len_ship = 1

	zweier = list(input("Platziere dein zweier Schiff: (z.B. D5 bis D6 oder A2 bis B2)"))
	zweier.remove(" ")
	zweier.remove("b")
	zweier.remove("i")
	zweier.remove("s")
	zweier.remove(" ")

	if len(zweier) == 5:	#Falls Liste eine doppelzahl enthält, rausfinden wo diese ist und auf 10 setzen.
		del zweier[-2:]
		zweier.append('10')
	elif len(zweier) == 6:	#Falls Liste zwei doppelzahlen enthält, beide auf 10 setzen.
		del zweier[-2:]
		zweier.append('10')
		del zweier[1:3]
		zweier.insert(1, '10')

	# Anfangs- und Endzahl festlegen
	Zahl_start = int(zweier[1])
	Zahl_ende = int(zweier[-1])

	Buchstabe_start = dic[zweier[0]]  # Buchstabe bei dem gestartet wird
	Buchstabe_ende = dic[zweier[2]]  # Buchstabe bei dem geendet wird


#Überprüfe, ob Feld frei ist
	if Zahl_ende - Zahl_start == len_ship or Buchstabe_ende - Buchstabe_start == len_ship:
		if Buchstabe_start - Buchstabe_ende == 0:  # Schiff waagerecht
			for j in range(Zahl_start - 1, Zahl_ende):
				if columns[Buchstabe_start - 1][j] == None:
					columns[Buchstabe_start - 1][j] = 'Schiff'
				else:
					print("Eins der Felder ist bereits belegt. Bitte wähle erneut")
					return

		if Zahl_start - Zahl_ende == 0:  # Schiff senkrecht
			for i in range(Buchstabe_start - 1, Buchstabe_ende):
				if columns[i][Zahl_start - 1] == None:
					columns[i][Zahl_start - 1] = 'Schiff'
				else:
					print("Eins der Felder ist bereits belegt. Bitte wähle erneut")
					return


	else:		#Falls Anzahl an Kästchen über- oder unterschritten
		if Zahl_ende - Zahl_start > len_ship:
			print("Du hast mehr Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return
		elif Buchstabe_ende - Buchstabe_start > len_ship:
			print("Du hast mehr Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return

		elif Zahl_ende - Zahl_start < len_ship:
			print ("Du hast weniger Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return

		elif Buchstabe_ende - Buchstabe_start < len_ship:
			print("Du hast weniger Felder als die Länge des Schiffs gewählt! Bitte wähle erneut.")
			return

	print(columns)




def cpu_battlefield():
	global cpu_columns
	global cpu_rows

	cpu_columns = []

	for j in range(10):
		cpu_rows = []

		for i in range(10):
			cpu_rows.append(None)
		cpu_columns.append(cpu_rows)
	print(cpu_columns)

cpu_battlefield()

def cpu_place_ships_fuenfer():
	len_ship = 4 #Schifflänge vermindert um 1, da Fünferschiff z.B. von D5 bis D9

	global position_found_5

	position_found_5 = None

	while position_found_5 == None: #Solange keine Richtung gefunden wurde.
		#Zufällige Wahl der Startposition
		cpu_buchstabe_start = random.randint(1,10)
		cpu_zahl_start = random.randint(1,10)



		#Ist links frei?
		left_free = 0
		if cpu_zahl_start - len_ship >= 1:
			for i in range(0,len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1][cpu_zahl_start - 1 -i] == None:
					left_free += 1

		# Ist rechts frei?
		right_free = 1
		if cpu_zahl_start + len_ship <= 10:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1][cpu_zahl_start - 1 + i] == None:
					right_free += 1

		# Ist oben frei?
		above_free = 2
		if cpu_buchstabe_start - len_ship >= 1:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1 - i][cpu_zahl_start - 1 ] == None:
					above_free += 1

		# Ist unten frei?
		below_free = 3
		if cpu_buchstabe_start + len_ship <= 10:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1 + i][cpu_zahl_start - 1] == None:
					below_free += 1

		#Wenn alle Positionen in eine Richtung frei, nimmt die Variable einen Maximalen Wert an. Diese werden einer neuen Liste an Möglichkeiten hinzugefügt

		possibilities = []
		possibilities.clear() #brauche ich das? oder macht der die automatisch leer, wegen dem was darüber steht?

		if left_free == len_ship+1: #Maximaler Wert, wenn alle Positionen frei
			possibilities.append(left_free)
		if right_free == len_ship+2: #Maximaler Wert, wenn alle Positionen frei
			possibilities.append(right_free)
		if above_free == len_ship+3: #Maximaler Wert, wenn alle Positionen frei
			possibilities.append(above_free)
		if below_free == len_ship+4: #Maximaler Wert, wenn alle Positionen frei
			possibilities.append(below_free)


		if len(possibilities) != 0: #Wenn freie Richtung gefunden wurde, dann:
			direction = random.choice(possibilities) #Zufällige Wahl einer Variable aus möglichen Richtungen
			position_found_5 = True

			print(direction)

			#Je nachdem welche Richtung zufällig gewählt wurde, wird das Schiff plaziert.

			if direction == left_free:
				cpu_zahl_ende = cpu_zahl_start - len_ship

				for j in range(cpu_zahl_ende -1, cpu_zahl_start):
					if cpu_columns[cpu_buchstabe_start - 1][j] == None:
						cpu_columns[cpu_buchstabe_start - 1][j] = 'Schiff{}'.format(len_ship+1) #Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")

			if direction == right_free:
				cpu_zahl_ende = cpu_zahl_start + len_ship

				for j in range(cpu_zahl_start - 1, cpu_zahl_ende):
					if cpu_columns[cpu_buchstabe_start - 1][j] == None:
						cpu_columns[cpu_buchstabe_start - 1][j] = 'Schiff{}'.format(len_ship+1) #Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")


			if direction == above_free:
				cpu_buchstabe_ende = cpu_buchstabe_start - len_ship

				for i in range(cpu_buchstabe_ende -1, cpu_buchstabe_start):
					if cpu_columns[i][cpu_zahl_start - 1] == None:
						cpu_columns[i][cpu_zahl_start - 1] = 'Schiff{}'.format(len_ship+1) #Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")


			if direction == below_free:
				cpu_buchstabe_ende = cpu_buchstabe_start + len_ship

				for i in range(cpu_buchstabe_start -1 , cpu_buchstabe_ende):
					if cpu_columns[i][cpu_zahl_start - 1] == None:
						cpu_columns[i][cpu_zahl_start - 1] = 'Schiff{}'.format(len_ship+1) #Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")

		break

def cpu_place_ships_vierer():
	len_ship = 3 # Schifflänge vermindert um 1, da Fünferschiff z.B. von D5 bis D9

	global position_found_4

	position_found_4 = None

	while position_found_4 == None:  # Solange keine Richtung gefunden wurde.
		# Zufällige Wahl der Startposition
		cpu_buchstabe_start = random.randint(1, 10)
		cpu_zahl_start = random.randint(1, 10)

		print(cpu_buchstabe_start)
		print(cpu_zahl_start)

		# Ist links frei?
		left_free = 0
		if cpu_zahl_start - len_ship >= 1:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1][cpu_zahl_start - 1 - i] == None:
					left_free += 1

		# Ist rechts frei?
		right_free = 1
		if cpu_zahl_start + len_ship <= 10:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1][cpu_zahl_start - 1 + i] == None:
					right_free += 1

		# Ist oben frei?
		above_free = 2
		if cpu_buchstabe_start - len_ship >= 1:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1 - i][cpu_zahl_start - 1] == None:
					above_free += 1

		# Ist unten frei?
		below_free = 3
		if cpu_buchstabe_start + len_ship <= 10:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1 + i][cpu_zahl_start - 1] == None:
					below_free += 1

		# Wenn alle Positionen in eine Richtung frei, nimmt die Variable einen Maximalen Wert an. Diese werden einer neuen Liste an Möglichkeiten hinzugefügt

		possibilities = []

		if left_free == len_ship + 1:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(left_free)
		if right_free == len_ship + 2:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(right_free)
		if above_free == len_ship + 3:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(above_free)
		if below_free == len_ship + 4:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(below_free)

		if len(possibilities) != 0:  # Wenn freie Richtung gefunden wurde, dann:
			direction = random.choice(possibilities)  # Zufällige Wahl einer Variable aus möglichen Richtungen
			position_found_4 = True

			print(direction)

			# Je nachdem welche Richtung zufällig gewählt wurde, wird das Schiff plaziert.

			if direction == left_free:
				cpu_zahl_ende = cpu_zahl_start - len_ship

				for j in range(cpu_zahl_ende - 1, cpu_zahl_start):
					if cpu_columns[cpu_buchstabe_start - 1][j] == None:
						cpu_columns[cpu_buchstabe_start - 1][j] = 'Schiff{}'.format(
							len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")

			if direction == right_free:
				cpu_zahl_ende = cpu_zahl_start + len_ship

				for j in range(cpu_zahl_start - 1, cpu_zahl_ende):
					if cpu_columns[cpu_buchstabe_start - 1][j] == None:
						cpu_columns[cpu_buchstabe_start - 1][j] = 'Schiff{}'.format(
							len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")

			if direction == above_free:
				cpu_buchstabe_ende = cpu_buchstabe_start - len_ship

				for i in range(cpu_buchstabe_ende - 1, cpu_buchstabe_start):
					if cpu_columns[i][cpu_zahl_start - 1] == None:
						cpu_columns[i][cpu_zahl_start - 1] = 'Schiff{}'.format(
							len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")

			if direction == below_free:
				cpu_buchstabe_ende = cpu_buchstabe_start + len_ship

				for i in range(cpu_buchstabe_start - 1, cpu_buchstabe_ende):
					if cpu_columns[i][cpu_zahl_start - 1] == None:
						cpu_columns[i][cpu_zahl_start - 1] = 'Schiff{}'.format(
							len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")


def cpu_place_ships_dreier():
	len_ship = 2  # Schifflänge vermindert um 1, da Fünferschiff z.B. von D5 bis D9

	global position_found_3

	position_found_3 = None

	while position_found_3 == None:  # Solange keine Richtung gefunden wurde.
		# Zufällige Wahl der Startposition
		cpu_buchstabe_start = random.randint(1, 10)
		cpu_zahl_start = random.randint(1, 10)

		print(cpu_buchstabe_start)
		print(cpu_zahl_start)

		# Ist links frei?
		left_free = 0
		if cpu_zahl_start - len_ship >= 1:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1][cpu_zahl_start - 1 - i] == None:
					left_free += 1

		# Ist rechts frei?
		right_free = 1
		if cpu_zahl_start + len_ship <= 10:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1][cpu_zahl_start - 1 + i] == None:
					right_free += 1

		# Ist oben frei?
		above_free = 2
		if cpu_buchstabe_start - len_ship >= 1:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1 - i][cpu_zahl_start - 1] == None:
					above_free += 1

		# Ist unten frei?
		below_free = 3
		if cpu_buchstabe_start + len_ship <= 10:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1 + i][cpu_zahl_start - 1] == None:
					below_free += 1

		# Wenn alle Positionen in eine Richtung frei, nimmt die Variable einen Maximalen Wert an. Diese werden einer neuen Liste an Möglichkeiten hinzugefügt

		possibilities = []

		if left_free == len_ship + 1:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(left_free)
		if right_free == len_ship + 2:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(right_free)
		if above_free == len_ship + 3:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(above_free)
		if below_free == len_ship + 4:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(below_free)

		if len(possibilities) != 0:  # Wenn freie Richtung gefunden wurde, dann:
			direction = random.choice(possibilities)  # Zufällige Wahl einer Variable aus möglichen Richtungen
			position_found_3 = True

			print(direction)

			# Je nachdem welche Richtung zufällig gewählt wurde, wird das Schiff plaziert.

			if direction == left_free:
				cpu_zahl_ende = cpu_zahl_start - len_ship

				for j in range(cpu_zahl_ende - 1, cpu_zahl_start):
					if cpu_columns[cpu_buchstabe_start - 1][j] == None:
						cpu_columns[cpu_buchstabe_start - 1][j] = 'Schiff{}'.format(len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")

			if direction == right_free:
				cpu_zahl_ende = cpu_zahl_start + len_ship

				for j in range(cpu_zahl_start - 1, cpu_zahl_ende):
					if cpu_columns[cpu_buchstabe_start - 1][j] == None:
						cpu_columns[cpu_buchstabe_start - 1][j] = 'Schiff{}'.format(
							len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")

			if direction == above_free:
				cpu_buchstabe_ende = cpu_buchstabe_start - len_ship

				for i in range(cpu_buchstabe_ende - 1, cpu_buchstabe_start):
					if cpu_columns[i][cpu_zahl_start - 1] == None:
						cpu_columns[i][cpu_zahl_start - 1] = 'Schiff{}'.format(
							len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")

			if direction == below_free:
				cpu_buchstabe_ende = cpu_buchstabe_start + len_ship

				for i in range(cpu_buchstabe_start - 1, cpu_buchstabe_ende):
					if cpu_columns[i][cpu_zahl_start - 1] == None:
						cpu_columns[i][cpu_zahl_start - 1] = 'Schiff{}'.format(
							len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")



def cpu_place_ships_zweier():
	len_ship = 1  # Schifflänge vermindert um 1, da Fünferschiff z.B. von D5 bis D9

	global position_found_2

	position_found_2 = None

	while position_found_2 == None:  # Solange keine Richtung gefunden wurde.
		# Zufällige Wahl der Startposition
		cpu_buchstabe_start = random.randint(1, 10)
		cpu_zahl_start = random.randint(1, 10)

		print(cpu_buchstabe_start)
		print(cpu_zahl_start)

		# Ist links frei?
		left_free = 0
		if cpu_zahl_start - len_ship >= 1:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1][cpu_zahl_start - 1 - i] == None:
					left_free += 1

		# Ist rechts frei?
		right_free = 1
		if cpu_zahl_start + len_ship <= 10:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1][cpu_zahl_start - 1 + i] == None:
					right_free += 1

		# Ist oben frei?
		above_free = 2
		if cpu_buchstabe_start - len_ship >= 1:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1 - i][cpu_zahl_start - 1] == None:
					above_free += 1

		# Ist unten frei?
		below_free = 3
		if cpu_buchstabe_start + len_ship <= 10:
			for i in range(0, len_ship + 1):
				if cpu_columns[cpu_buchstabe_start - 1 + i][cpu_zahl_start - 1] == None:
					below_free += 1

		# Wenn alle Positionen in eine Richtung frei, nimmt die Variable einen Maximalen Wert an. Diese werden einer neuen Liste an Möglichkeiten hinzugefügt

		possibilities = []

		if left_free == len_ship + 1:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(left_free)
		if right_free == len_ship + 2:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(right_free)
		if above_free == len_ship + 3:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(above_free)
		if below_free == len_ship + 4:  # Maximaler Wert, wenn alle Positionen frei
			possibilities.append(below_free)

		if len(possibilities) != 0:  # Wenn freie Richtung gefunden wurde, dann:
			direction = random.choice(possibilities)  # Zufällige Wahl einer Variable aus möglichen Richtungen
			position_found_2 = True

			print(direction)

			# Je nachdem welche Richtung zufällig gewählt wurde, wird das Schiff plaziert.

			if direction == left_free:
				cpu_zahl_ende = cpu_zahl_start - len_ship

				for j in range(cpu_zahl_ende - 1, cpu_zahl_start):
					if cpu_columns[cpu_buchstabe_start - 1][j] == None:
						cpu_columns[cpu_buchstabe_start - 1][j] = 'Schiff{}'.format(
							len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")

			if direction == right_free:
				cpu_zahl_ende = cpu_zahl_start + len_ship

				for j in range(cpu_zahl_start - 1, cpu_zahl_ende):
					if cpu_columns[cpu_buchstabe_start - 1][j] == None:
						cpu_columns[cpu_buchstabe_start - 1][j] = 'Schiff{}'.format(
							len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")

			if direction == above_free:
				cpu_buchstabe_ende = cpu_buchstabe_start - len_ship

				for i in range(cpu_buchstabe_ende - 1, cpu_buchstabe_start):
					if cpu_columns[i][cpu_zahl_start - 1] == None:
						cpu_columns[i][cpu_zahl_start - 1] = 'Schiff{}'.format(
							len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")

			if direction == below_free:
				cpu_buchstabe_ende = cpu_buchstabe_start + len_ship

				for i in range(cpu_buchstabe_start - 1, cpu_buchstabe_ende):
					if cpu_columns[i][cpu_zahl_start - 1] == None:
						cpu_columns[i][cpu_zahl_start - 1] = 'Schiff{}'.format(
							len_ship + 1)  # Schiffname nach Länge zur Unterscheidung
					else:
						print("Eins der Felder ist bereits belegt. Bitte wähle erneut")


#cpu_place_ships_fuenfer()
#if position_found_5 == True:
	#cpu_place_ships_vierer()
	#if position_found_4 == True:
		#cpu_place_ships_dreier()
		#if position_found_3 == True:
			#cpu_place_ships_zweier()

cpu_place_ships_fuenfer()
cpu_place_ships_fuenfer()
cpu_place_ships_fuenfer()
cpu_place_ships_fuenfer()
cpu_place_ships_fuenfer()
cpu_place_ships_fuenfer()



print(cpu_columns)


def player_hit():
	ammo = 1	#Wie oft darf ein Feld gewählt werden.

	while ammo >= 1: #Wenn Munition verfügbar.
		hit = list(input("Wähle ein Feld.")) #Feldwahl durch Spieler
		print(hit)

		buchstabe = dic[hit[0]]

		if len(hit) == 3: #Falls Zahl eine 10
			zahl = 10
		elif len(hit) > 3 or len(hit) < 2: #Eingabeüberprüfung
			print("Ungültige Eingabe, bitte wähle erneut.") #return
		else:
			zahl = int(hit[1])

		for shiplength in range(2,6): # Einträge Schiff2 bis Schiff5 sind möglich.
			if cpu_columns[buchstabe-1][zahl-1] == 'Schiff{}'.format(shiplength): #Wenn Spielfeld vom Bot das Wort Schiff an der Position enthält
				print('Du hast ein Schiff getroffen und bist erneut dran.')
				ammo += 1

		if cpu_columns[buchstabe-1][zahl-1] == None: #Wenn Spielfeld vom Bot das Wort Empty an der Position enthält
			print('Dieser Schuss ging ins leere.')
			ammo -= float('inf')

player_hit()