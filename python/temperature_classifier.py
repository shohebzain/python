#if else lader tempearature = int(input("Enter the temperature: "))
temperature = int(input("Enter the temperature: "))
if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a nice day.")
elif temperature > 10:
    print("It's a bit cold.")
else:
    print("It's cold.")
    
    