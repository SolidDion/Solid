from random import randint, shuffle 
import random 

#Allowing shuffle command to shuffle strings and lists 
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Declaring punctuations since it's easier than using ASCII 
punctuations = [".", ",", "-", "*", "¨", "#", "!", "?", "¤", "%", "/", "=", "_", ";", ";"]

#Declaring the random letters using the random library's randint command 
uppercaseLetter1 = uppercaseLetter=chr(random.randint(65,90)) 
uppercaseLetter2 = uppercaseLetter=chr(random.randint(65,90))  
lowercaseLetter1 = lowercaseLetter=chr(random.randint(97,122)) 
lowercaseLetter2 = lowercaseLetter=chr(random.randint(97,122)) 
digit1 = random.randint(0, 9) 
digit2 = random.randint(0, 9)  
punctuationSign1 = punctuations[random.randint(0,14)] 
punctuationSign2 = punctuations[random.randint(0,14)]

#Adding all the letters together so they make 1 password
passworduppercaseandsigns = (uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(digit1) + str(digit2) + punctuationSign1 + punctuationSign2)

passworduppercaseandnumbers1 = (uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(digit1) + str(digit2)) 
passworduppercaseandnumbers2 = (uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(digit1) + str(digit2)) 
passworduppercaseandnumbers = (passworduppercaseandnumbers2 + passworduppercaseandnumbers1)

passworduppercaseandlowercase1 = (uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2)
passworduppercaseandlowercase2 = (uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2)
passworduppercaseandlowercase3 = (uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2)
passworduppercaseandlowercase = (passworduppercaseandlowercase1 + passworduppercaseandlowercase2 + passworduppercaseandlowercase3) 

#Shuffling the passwords so they're not in order 
passworduppercaseandsigns = shuffle(passworduppercaseandsigns) 
passworduppercaseandnumbers = shuffle(passworduppercaseandnumbers) 
passworduppercaseandlowercase = shuffle(passworduppercaseandlowercase) 

#Outputting the actual passwords using simple print commands
print (passworduppercaseandsigns, "UPPERCASES AND SIGNS 8")
print (passworduppercaseandnumbers, "UPPERCASE AND NUMBERS 12") 
print (passworduppercaseandlowercase, "UPPERCASE AND LOWERCASE 12") 

#Putting in a space input so the program doesn't automatically close on CMD
input (" ") 

