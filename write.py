# -*- coding: utf-8 -*-
import pipes, random, subprocess, time
from textwrap import wrap

#cleaning regex
#(^.*)(?:SRL-D|SRL|SA|SOCIETATE PE ACTIUNI|PFA|II|INTREPRINDERE INDIVIDUALA|PERSOANA FIZICA AUTORIZATA|S\.R\.O\.|SNC|KFT\s?)$

rand_coords = ["44º39'12\"N 26º12'4\"E", "44º39'12.59\"N 26º12'3.09\"E",
			"44º39'12.20\"N 26º12'2.31\"E", "44º39'11.93\"N 26º12'1.69\"E",
			"44º39'11.60\"N 26º12'0.77\"E", "44º39'11.60\"N 26º12'0.15\"E",
			"44º39'11.49\"N 26º11'59.61\"E", "44º39'10.99\"N 26º11'58.68\"E",
			"44º39'10.44\"N 26º12'57.21\"E", "44º39'9.95\"N 26º12'55.67\"E"]

specs_five = [
	"#2c2012",					#color
	"24",						#<= 14 ch font-size
	"20",						#<= 20 ch font-size
	"16",						#>= 25 ch font-size
	"fonts/BebasNeue.otf",		#font-familly
	"4.5x4.5",					#rotation
	"+87",						#left
	"-10"						#top
]

def write_on_image(text):
	which = random.randint(1, 10)
	coord = rand_coords[which - 1]

	if len(text) <= 14:
		font_size = specs_five[1]
	elif len(text) <= 20:
		font_size = specs_five[2]
	elif len(text) > 20:
		font_size = specs_five[3]

	subprocess.call(["convert source_pics/5.jpg -gravity center -fill '" + specs_five[0] 
		+ "' -pointsize " + font_size 
		+ " -font " + specs_five[4] 
		+ " -annotate " + specs_five[5] + specs_five[6] + specs_five[7] + " " + pipes.quote(text) 
		+ " -fill '#f1f1f1'"
		+ " -pointsize 14"
		+ " -font fonts/MyriadPro.otf"
		+ " -annotate -175+265 " + pipes.quote(coord)
		+ " \"out/" + text + ".jpg\""], shell = True)

def read_list():
	f = open("list_us", "r")
	return f.readlines()

def __init__():
	#write_on_image("X")
	#write_on_image("\n".join(wrap("HOLLEMAN SPECIAL TRANSPORT & PROJECT CARGO", 25)))
	#.strip()

	if not True:
		write_on_image("\n".join(wrap("HANDSOME ADV", 25))) # 12 ch
		write_on_image("\n".join(wrap("HANDSOME ADVSS", 25))) # 14 ch
		write_on_image("\n".join(wrap("HANDSOME ADVSSXXX", 25))) # 18 ch
		write_on_image("\n".join(wrap("LLEMAN SPECIALS SSSS", 25))) #20 ch
		write_on_image("\n".join(wrap("HOLLEMAN SPECIAL TRANSPORT & PROJECT CARGO", 25))) # > 25 ch
		
		return


	lines = read_list()
	i = 1
	count = len(lines)
	for line in lines:
		write_on_image("\n".join(wrap(line.strip(), 25)))
		print "{0} / {1}".format(i, count)
		i += 1


__init__()