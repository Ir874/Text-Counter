# Define the function to filter out the text


def wordcounter(inp,search): 
    spaces = 0 # The variable to count all the words
    
    # Counting block
    for x in inp:
        if " " in x:
            spaces += 1
    print(f"There are {spaces + 1} words in this sentence.")
    
    # Searching block
    search_in_x = 0
    
    for x in inp:
        if search in inp:
            search_in_x += 1        
    
    print(f"{search} appears {search_in_x} times in the inputted string.")
    print(type(search))


# Ask the user for input 
userin = input("Input a string to be classified: ")

# Ask user for search word
searchbool = input("Would you like to search for a word? ")
if searchbool == "yes" or "Yes":
    searchword = input("What word? ")
else: print("Goodbye!")

# Take user input and add it as a parameter to the word counting function
wordcounter(userin,searchword)
