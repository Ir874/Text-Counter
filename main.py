# Define the function to filter out the text

def wordcounter(inp): 
    spaces = 0
    for x in inp:
        if " " in x:
            spaces += 1
    print(f"There are {spaces + 1} words in this sentence.")

def repeater(inp):
    pass




# Ask the user for input 
userin = input("Input a string to be classified: ")

# Take user input and add it as a parameter to the word counting function
wordcounter(userin)
