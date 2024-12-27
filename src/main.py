import json
import argparse
#make the argument parsing for commands
parse = argparse.ArgumentParser(description="CM2 Code assembler. Made by KO6BXL")

#add arguments
parse.add_argument('-f', type=open,help="File to convert into assembly")
parse.add_argument('-c', type=open,help="Config for convertion.")
parse.add_argument('-o', type=str,help="Config for convertion.")

#add arguments into this thingie
args = parse.parse_args()

#code file. Holds the code the user wrote
code_file = args.f
#configuration file w/ all the things the programs needs to work
conf_file = args.c

#output file
out_file = open(args.o, 'a')


#grabs dictionary from json file
keywords = json.loads(conf_file.read())

#declare globals
word = ""
outline = ""

#iterate through keys in aforementioned dictionary given a word, returns "err" if it was not found, otherwise value associated with key
def keyIteration(word):

    #go through keys in dictionary
    for key in keywords:
        #if the word matches a key
        if key in word:
            #add space and replace. return out
            out = " " + keywords[key]
            return out
    #if the word is not found in the dictionary, it's probably an error. blame the user and send error code
    print("KEY NOT FOUND, YOU PROBABLY WROTE IT WRONG")
    print(word)
    return "err"

#iterate through each character in user code
for char in code_file.read():
    #add character to a word
    word = word+char
    #if there's a space, assume the word is finished and call some functions
    if char == " " or char == "\n":
        #if key iteration failed, break
        if keyIteration(word) == "err":
            break
        else:
            #global outline is combined with the output value
            outline = outline + keyIteration(word)
        #reset word
        word = ""
    #if there's a new line, add it!
    if char == "\n":
        outline = outline + "\n"
        word = ""

else:
    #once the end of the for loop is reached, add the last word
    if keyIteration(word) == "err":
        print("error rip bozo")    
    else:
        outline = outline + keyIteration(word)
#write final output         
out_file.write(outline)

out_file.close()
code_file.close()
conf_file.close()