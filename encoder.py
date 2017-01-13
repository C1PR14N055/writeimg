import urllib

f = open("list_sorted", "r")
lines =  f.readlines()
f.close()

str = ""

for li in lines:
	str += urllib.quote(li) + "\n"

ff = open("encoded", "w")
ff.write(str)
ff.close()