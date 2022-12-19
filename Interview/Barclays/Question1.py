def getTown(peopleNames):
	# Write your code here
	prefix = ""
	max_name_length = max(peopleNames)
	print(len(max_name_length))
	for i in range(len(max_name_length)):
		if i < len(peopleNames[0]):
			curr = peopleNames[0][i]

		add_curr = True
		for name in peopleNames:
			if i >= len(name) or name[i] != curr:
				add_curr = False
		prefix += curr if add_curr else ""

	print(prefix)
	return prefix

people_names = ["ram", "rama", "ramesh", "rammohand", "ramanand"]

getTown(people_names)