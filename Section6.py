# while and Forloop in python

# while loop

i=1
while i<=10:
    print(i)
    i=i+1

# Forloop 

colors =['red','green','orange','yellow','pink']

for item in colors:
    print("I like "+item)


# infinite loop:-

while True:
    name=input("enter your name: ")
    if name=="raghava":
        break

# A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result

#check the above function

text = input("enter a text :")
s = 4
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text,s))
