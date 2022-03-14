#Vivek
#14 March 2022

#This code takes in input for the lenght of the password (multiple of 4) and then generates a password using
#alphabets + characters + capital alphabets + numbers 

import random

#function for generating the password
def makingPassword(numIn):
    ch = "_#@"
    num = "1234567890"
    alpha  = "abcdefghijklmnopqrstuvwxyz"
    alphaUp = alpha.upper()
    #boolean variables
    character = False; number = False; alphaSmall = False; alphaBig = False

    #Declaring a string
    password = ""

    while(character != True and number != True and alphaSmall != True and alphaBig != True): 
                    
        #for small alphabets
        if alphaSmall == False:
            alphaSmall = True
            for i in range(0, numIn//4, 1):
                #adding strings
                password += alpha[random.randint(0, len(alpha)-1)]    # -1 so that we dont have out of bound accessing

        #for character
        if character == False: 
            character = True

            #going through the 
            for i in range(0, numIn//4, 1):
                #adding strings
                password += ch[random.randint(0, len(ch)-1)]    # -1 so that we dont have out of bound accessing

        #for capital alphabets
        if alphaBig == False:
            alphaBig = True
            for i in range(0, numIn//4, 1):
                #adding strings
                password += alphaUp[random.randint(0, len(alphaUp)-1)]    # -1 so that we dont have out of bound accessing

        #for numbers
        if number == False:
            number == True
            #
            for i in range(0, numIn//4, 1):
                #adding strings
                password += num[random.randint(0, len(num)-1)]    # -1 so that we dont have out of bound accessing
       
    return password



numInput = int(input("Enter the length of password as multiple of 4: "))
while(numInput % 4 != 0):
    print("Error!! incompatable length of password!!")
    numInput = int(input("Length should be multiple of 4: "))
print(makingPassword(numInput))