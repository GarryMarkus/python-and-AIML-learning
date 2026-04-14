sample = input("Enter a string with all lower case letters: ")

sample_list = sample.split()

result = ""

for i in sample_list:
    result = result + i[0].upper() + i[1:] + " "

print(result)