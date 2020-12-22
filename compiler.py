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

            #function to parse slatt file and compile to python
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
            
    os.system("python /tmp/{0}.py".format(slatt_file))
    os.remove("/tmp/{0}.py".format(slatt_file))