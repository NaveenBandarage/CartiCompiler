def sl_compile(sl_input):
    #imports
    import sys
    import os

    #set globals for later usage
    global slatt_file
    global line

    slatt_file = sl_input

    #get line list
    with open(slatt_file) as slatt:
        lineList = slatt.readlines()

    #parse the slatt file. 
    with open(slatt_file) as slatt:

        for num, line in enumerate(slatt, 1):
            
            #search for "ok!" at end of file
            if lineList[len(lineList) - 1].split()[0] != "ok!" or num == 1 and "**slatt!**" not in line:
                if lineList[len(lineList) - 1].split()[0] != "ok!":
                    print('Error in {0}: Non-valid slatt file (error 1: require "ok!" on last line of program file)'.format(slatt_file))
                    #search for "*slatt!*" at beginning of file
                if line.split()[0] != "**slatt!**":
                    print('Error in {0}: Non-valid slatt file (error 2: require "**slatt!**" on line 1 of program file)'.format(slatt_file))
            else:
                line = line.replace("**slatt!**", "")
                line = line.replace("ok!", "")
            #need to end up adding more actions. 
            #function to parse slatt file and compile to python\
            def parse():
                global slatt_file
                global line
                #prints if "+yo pierre()" is in the line
                slatt_file = slatt_file.replace("/", "")
                if "+yo pierre(" in line:
                    line = line.replace("+yo pierre", "print")
                    parse()
                #set variables using "^wholelotta>"
                elif "^wholelotta>" in line:
                    line = line.replace("^wholelotta>", "=")
                    parse()
                #is equal to (==)
                elif "^iswholelotta>" in line:
                    line = line.replace("^iswholelotta>", "==")
                    parse()
                #define functions using "_flex*"
                elif "_flex*" in line:
                    line = line.replace("_flex*", "def ")
                    parse()
                #call function
                elif "_imightcall" in line:
                    line = line.replace("_imightcall ", "")
                    parse()
                #if/else statement
                elif "*!yah" in line:
                    line = line.replace("*!yah", "if")
                    parse()
                elif "*!nah" in line:
                    line = line.replace("*!nah", "else")
                    parse()
                #input statement
                elif "wokeuplike*(" in line:
                    line = line.replace("wokeuplike*", "input")
                    parse()
                else:
                    os.system("echo '{0}' >> /tmp/{1}.py".format(line, slatt_file))
  
            parse()
    
    print("""\n//.............................................................................................................................................
//.................................................................OOOOO...................CCCCC...............................................
//.PPPPPPPPPPP.PLLLL..........AAAAA..AAYYY...YYYYYYYBBBBBBBB.....OOOOOOOOO..OOOII........CCCCCCCC......AAAAAA....AARRRRRRRRR.RRRTTTTTTTTTTIII..
//.PPPPPPPPPPPPPLLLL..........AAAAAA.AAYYY..YYYYYYYYBBBBBBBBB...BOOOOOOOOOO.OOOII....... CCCCCCCCC.....AAAAAA....AARRRRRRRRRRRRRTTTTTTTTTTIII..
//.PPPPPPPPPPPPPLLLL.........AAAAAAA..AYYYY.YYYYY.YYBBBBBBBBBB.BBOOOOOOOOOOOOOOII...... CCCCCCCCCC...AAAAAAA....AARRRRRRRRRRRRRTTTTTTTTTTIII..
//.PPPPP..PPPPPPLLLL.........AAAAAAA..AYYYY.YYYY..YYBB...BBBBB.BBOOO...OOOOOOOOII...... CCC..CCCCC...AAAAAAAA...AARR...RRRRR...TTTTT...TTIII..
//.PPPPP...PPPPPLLLL........AAAAAAAAA..YYYYYYYYY..YYBB.BBBBBBBBBBOO.....OOOOOOOII..... CC....CCCC...AAAAAAAA...AARR....RRRR...TTTTT...TTIII..
//.PPPPPPPPPPPPPLLLL........AAAAAAAAA..YYYYYYYY...YYBBBBBBBBB.BBBOO.....OOOOOOOII..... CC..........CAAAAAAAA...AARRRRRRRRRR...TTTTT...TTIII..
//.PPPPPPPPPPPPPLLLL........AAAA.AAAAA..YYYYYYY...YYBBBBBBBBBBBBBOO.....OOOOOOOII..... CC..........CAAAAAAAAA..AARRRRRRRRR....TTTTT...TTIII..
//.PPPPPPPPPPP.PLLLL.......AAAAAAAAAAA...YYYYY....YYBBBBBBBBBBBBBOO.....OOOOOOOII..... CC..........CAAAAAAAAA..AARRRRRRRRRR...TTTTT...TTIII..
//.PPPPPPPPPP..PLLLL.......AAAAAAAAAAA...YYYYY....YYBB....BBBBBBBOO.....OOOOOOOII..... CC....CCCC.CCAAAAAAAAA..AARRRRRRRRRR...TTTTT...TTIII..
//.PPPPP.......PLLLL.......AAAAAAAAAAAA..YYYYY....YYBB...BBBBB.BBOOO...OOOOOOOOII...... CCC..CCCCC.CCAAAAAAAAAA.AARR...RRRRR...TTTTT...TTIII..
//.PPPPP.......PLLLLLLLLLLLAAAAAAAAAAAA..YYYYY....YYBBBBBBBBBB.BBOOOOOOOOOOOOOOII...... CCCCCCCCCC.CCAAAAAAAAAA.AARR...RRRRR...TTTTT...TTIII..
//.PPPPP.......PLLLLLLLLLLLAAAA...AAAAA..YYYYY....YYBBBBBBBBBB..BOOOOOOOOOO.OOOII....... CCCCCCCCC.CCCAA....AAAAAAARR...RRRRR...TTTTT...TTIII..
//.PPPPP.......PLLLLLLLLLLLAAA.....AAAAY.YYYYY....YYBBBBBBBBB....OOOOOOOOO..OOOII........CCCCCCCC..CCCAA....AAAAAAARR...RRRRR...TTTTT...TTIII..
//.................................................................OOOOO..................CCCCCC...............................................
//.............................................................................................................................................\n""")

    #got this to print out now finally took ages. 
    text = [string.strip('\n') for string in lineList if string != '']
    templist = list(filter(None, text))
    
    for word in templist:
        print(word)

    os.system("python /tmp/{0}.py".format(slatt_file))
    os.remove("/tmp/{0}.py".format(slatt_file))