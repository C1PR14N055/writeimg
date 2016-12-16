def read_list():
	f = open("list", "r")
	return f.readlines()

def __init__():
	lines = read_list()
	i = 1
	count = len(lines)
	sql_str = ""
	for line in lines:
		sql_str += "INSERT INTO img (name) VALUES ('" + line.strip() + "');\n"
		print "{0} / {1}".format(i, count)
		i += 1

	f = open("sql", "w")
	f.write(sql_str)


__init__()