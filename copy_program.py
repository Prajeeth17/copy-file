# Program to copy a text file
# Developed by: Prajeeth K T
# Reg. No: 22002267
with open('text.txt','r') as firstfile:
    with open('copy.txt','a') as secondfile:
        for line in firstfile:
            secondfile.write(line)