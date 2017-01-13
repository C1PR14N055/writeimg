import webbrowser

def read_list():
	f = open("links", "r")
	return f.readlines()

def __init__():
	for link in read_list():
		print "OPENING: " + link
		webbrowser.open(link)
		raw_input("Press Enter to continue\n")

__init__()