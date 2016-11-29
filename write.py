import random, subprocess, time

#cleaning regex
#(^.*)(?:SRL-D|SRL|SA|SOCIETATE PE ACTIUNI|PFA|II|INTREPRINDERE INDIVIDUALA|PERSOANA FIZICA AUTORIZATA|S\.R\.O\.|SNC|KFT\s?)$

specs_one = [
	"#2c2012",					#color
	"48",						#font-size
	"fonts/BebasNeue.otf",		#font-familly
	"4.5x4.5",
	"+185",						#left
	"+150"						#top
]

def write_on_image(text):
	subprocess.call(["convert source_pics/5.jpg -gravity center -fill '" + specs_one[0] + "' -pointsize " + specs_one[1] + " -font " + specs_one[2] + " -annotate " + specs_one[3] + specs_one[4] + specs_one[5] + " '" + text + "' out/out.jpg"], shell = True)

def read_list():
	f = open("list", "r")
	return f.readlines()

def __init__():
	write_on_image("NOT HANDSOME ADV.")
	#lines = read_list()
	#for line in lines:
	#	print line

__init__()