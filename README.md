# cm2-Custom-Compiler

Custom Complier for computers in the Roblox game Circuit Maker 2

## How to use

python main.py -f (src code file) -c (config json that has the replacements) -o (output file)

## how to modify

### instuction.json

In the config folder of this repo, there's a instuction.json file. I have provided a template for my own computer as a guide for you. Simply add a key that means something in your assembly language and a value that means something in your computer.

### main.py

In the src folder, there's the compiler/assember/script. The replacements that happen to each word of your assembly is found in keyIteration(). Simply return whatever you would like in your binary depending on what word is used(or anything else), and you should be good.
