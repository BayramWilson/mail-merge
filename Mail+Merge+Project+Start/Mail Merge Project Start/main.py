#TODO: Create a letter using starting_letter.txt
names_arr = []
for name in open("../Mail Merge Project Start/Input/Names/invited_names.txt"):
    name = name.replace("\n", '')
    names_arr.append(name)
#print(names_arr)
with open("./Input/Letters/starting_letter.txt") as file:
    first_line = file.readline(100)
    rest_of_letter = ""
    for line in file:
        file.readline(100)

        rest_of_letter += line




    letter = file
    for name in names_arr:
        to_replace = first_line.replace("[name]", f"{name}")

        with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file2:

            file2.write(f"{to_replace}")
            file2.write(f"{rest_of_letter}")


#for name in names_arr:
#
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp