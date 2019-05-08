import time
global a, balance, fee, free_time, exra_fee, interval, input_time
P1 = [0]; P2 = [0]; P3 = [0]; P4 = [0]; P5 = [0]; P6 = [0]; P7 = [0]; P8 = [0]; P9 = [0]

a = [ P1, P2, P3,
      P4, P5, P6,
      P7, P8, P9 ]

fee = 200 
    
extra_fee = 100 

free_time = 10000 #1 hour 00 minutes 00 seconds

interval = 10000


while(1):
    login = str(input("Please input your login "))

    if login == "admin":
        password = str(input("Please input your password "))

    class System:
    
        def ranks():
    
            global  fee, free_time, extra_fee, interval
    
            if login == "admin" and password == "admin":
    
                fee = int(input("Please input parking new fee "))
    
                extra_fee = int(input("Please input new extra parking fee "))
                
                free_time1 = str(input("Input new free time "))
                
                free_time =  int(free_time1.replace(":", ""))

                interval1 = str(input("Input new interval "))

                interval = int(interval1.replace(":",""))
    
            else:
    
                print("You are logged in as user")

    System.ranks()

    input_time = str(input("Please input time of entry " ))

    a[0][0] =  int(input_time.replace(":", ""))                          #int(input("Please input time of entry " )) #6 digits required 2 for hours, minutes and seconds each

    class Dispencer:
    
           
        def __init__(self, a):

            a[0] = (get_time())    
        
        def get_time(self):
            return (time.strftime("%H%M%S "))

        def gate(a):

            global time_spent 
        
            time_spent = int(time.strftime("%H%M%S"))-a
        
            if time_spent <= free_time:
                return("Have a nice trip!")
            else:
                return("Please proceed to the payment terminal")
    
    print(Dispencer.gate(a[0][0]))
    class Bank:

        def verify():
        
            if Dispencer.gate(a[0][0]) == ("Please proceed to the payment terminal"):

                balance = int(input("Please insert cash or card "))
            
                result = balance - fee - (extra_fee * (time_spent//interval))

                print("Your balance ", balance, "-", "parking fee ", fee, "-", "extra fee", extra_fee * (time_spent//interval)) 

                print("Your remaining balance is ", result)

                if result >= 0:
                    return("Transaction completed. Thank you for your cooperation!")
                    
                elif result < 0:
                    return("Access denied! Please contact the local manager and make way for the next vehicle.")

            else:
                return("Sayanara~")
            
    print(Bank.verify())

    print("Next please!")
    
    print("-----------------------------------------------------")
f.close()
