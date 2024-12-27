import json
import argparse

parse = argparse.ArgumentParser(description="CM2 Code assembler. Made by KO6BXL")
parse.add_argument('-f', type=open,help="File to convert into assembly")
parse.add_argument('-c', type=open,help="Config for convertion.")
parse.add_argument('-o', type=str,help="Config for convertion.")
args = parse.parse_args()

code_file = args.f
conf_file = args.c
out_file = open(args.o, 'a')



keywords = json.loads(conf_file.read())

print(keywords)

word = ""
outline = ""


def keyIteration(word):
    for key in keywords:
        if key in word:


            print("ADD KEY THINGIE")
            print(word)
            print(keywords[key])
            out = " " + keywords[key]
        
            return out
    out = " " + word
    return out

for char in code_file.read():
    word = word+char
    if char == " " or char == "\n":
        # print(word)
       outline = outline + keyIteration(word)
       word = ""
    if char == "\n":
        outline = outline + "\n"
        word = ""
else:
    outline = outline + keyIteration(word)
    



        #print(key)
        #if key in line:
        #    
        #    outline = "\n"+ line.replace(key, keywords[key])

            
out_file.write(outline)

