def USDtoALL(type,amount):
    #Calculations for USD to the different currencies
    #Return amount in correct currency desired

def EURtoALL(type,amount):
    #Calculations for EURO to the different currencies
    #Return amount in correct currency desired
    #Type refers to type of current desired and amount is amount to be converted
    
def JPYtoALL(type,amount):
    #Calculations for JPY to different currencies
    #Return amount in correct currency desired
    #Type refers to type of current desired and amount is amount to be converted
    
def GBPtoALL(type,amount):
    #Calculations for GBP to different currencies
    #Return amount in correct currency desired
    #Type refers to type of current desired and amount is amount to be converted
    
def AUDtoALL(type,amount):
    #Calculations for AUD to different currencies
    #Return amount in correct currency desired
    #Type refers to type of current desired and amount is amount to be converted
    
def CADtoALL(type,amount):
    #Calculations for CAD to different currencies
    #Return amount in correct currency desired
    #Type refers to type of current desired and amount is amount to be converted

def CHFtoALL(type,amount):
    #Calculations for CHF to different currencies
    #Return amount in correct currency desired
    #Type refers to type of current desired and amount is amount to be converted

def complexity(inpt,output,amount):
    if(inpt == 1):
        USDtoALL(output,amount)

    elif(inpt == 2)
        EURtoALL(output,amount)

    elif(inpt == 3):
        JPYtoALL(output,amount)

    elif(inpt == 4):
        GBPtoALL(output,amount)

    elif(inpt == 5):
        AUDtoALL(output,amount)

    elif(inpt == 6):
        CADtoALL(output,amount)

    elif(inpt == 7):
        CHFtoALL(output,amount)

def main():
    print("Welcome to the World Currency Converter")
    print("1) US Dollar (USD)\n"
           "2) Euro (EUR)\n"
           "3) Japanese yen (JPY)\n"
           "4) Pound Sterling (GBP)\n"
           "5) Australian Dollar (AUD)\n"
           "6) Canadian Dollar (CAD)\n"
           "7) Swiss franc (CHF)")
    userinput = input("Select a currency you're using from the above options (1 - 7): ")
    useramount = input("Enter the amount you are using: ")
    useroutput = input("Now select a currency you wish to convert it to: ")

    if(userinput == useroutput):
        return "Error, cannot convert one currency to another"

    complexity(userinput,useroutpout,useramount)
    

if __name__ == "__main__":
    main()
