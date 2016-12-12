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

specs_one = [
	"#2c2012",					#color
	"20",						#<= 14 ch font-size
	"16",						#<= 20 ch font-size
	"12",						#> 20 ch font-size
	"fonts/BebasNeue.otf",		#font-familly
	"0x0",						#rotation
	"+0",						#left
	"-5"						#top
]

specs_two = [
	"#05060b",					#color
	"18",						#<= 14 ch font-size
	"14",						#<= 20 ch font-size
	"10",						#> 20 ch font-size
	"fonts/BebasNeue.otf",		#font-familly
	"2x2",						#rotation
	"-30",						#left
	"+10"						#top
]

specs_three = [
	"#2c2012",					#color
	"16",						#<= 14 ch font-size
	"12",						#<= 20 ch font-size
	"9",						#> 20 ch font-size
	"fonts/BebasNeue.otf",		#font-familly
	"2x2",						#rotation
	"+85",						#left
	"+22"						#top
]

specs_four = [
	"#080c18",					#color
	"20",						#<= 14 ch font-size
	"16",						#<= 20 ch font-size
	"12",						#> 20 ch font-size
	"fonts/BebasNeue.otf",		#font-familly
	"2.7x2.7",					#rotation
	"+30",						#left
	"+17"						#top
]

specs_five = [
	"#2c2012",					#color
	"24",						#<= 14 ch font-size
	"20",						#<= 20 ch font-size
	"16",						#> 20 ch font-size
	"fonts/BebasNeue.otf",		#font-familly
	"4.5x4.5",					#rotation
	"+87",						#left
	"-10"						#top
]

specs_six = [
	"#080c18",					#color
	"24",						#<= 14 ch font-size
	"20",						#<= 20 ch font-size
	"16",						#> 20 ch font-size
	"fonts/BebasNeue.otf",		#font-familly
	"4.5x4.5",					#rotation
	"+142",						#left
	"+9"						#top
]

specs_seven = [
	"#2c2012",					#color
	"23",						#<= 14 ch font-size
	"19",						#<= 20 ch font-size
	"15",						#> 20 ch font-size
	"fonts/BebasNeue.otf",		#font-familly
	"6.5x8.5",					#rotation
	"+7",						#left
	"-4"						#top
]

specs_eight = [
	"#0a090f",					#color
	"18",						#<= 14 ch font-size
	"14",						#<= 20 ch font-size
	"10",						#> 20 ch font-size
	"fonts/BebasNeue.otf",		#font-familly
	"10.5x11",					#rotation
	"-3",						#left
	"-25"						#top
]

specs_nine = [
	"#2c2012",					#color
	"24",						#<= 14 ch font-size
	"20",						#<= 20 ch font-size
	"16",						#> 20 ch font-size
	"fonts/BebasNeue.otf",		#font-familly
	"4.5x4.5",					#rotation
	"+87",						#left
	"-10"						#top
]

specs_ten = [
	"#2c2012",					#color
	"24",						#<= 14 ch font-size
	"20",						#<= 20 ch font-size
	"16",						#> 20 ch font-size
	"fonts/BebasNeue.otf",		#font-familly
	"4.5x4.5",					#rotation
	"+87",						#left
	"-10"						#top
]

specs_list = [specs_one, specs_two, specs_three, specs_four, specs_five, 
			specs_six, specs_seven, specs_eight, specs_nine, specs_ten]

def write_on_image(text):
	which = 8 #random.randint(1, 10)
	coord = rand_coords[which - 1]
	specs = specs_list[which - 1]

	if len(text) <= 14:
		font_size = specs[1]
	elif len(text) <= 20:
		font_size = specs[2]
	elif len(text) > 20:
		font_size = specs[3]

	subprocess.call(["convert source_pics/" + str(which) + ".jpg -gravity center -fill '" + specs[0] 
		+ "' -pointsize " + font_size 
		+ " -font " + specs[4] 
		+ " -annotate " + specs[5] + specs[6] + specs[7] + " " + pipes.quote(text) 
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

	if True:
		write_on_image("\n".join(wrap("x", 25))) # x
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