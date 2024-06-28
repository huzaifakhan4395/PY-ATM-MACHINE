# STARTING

def atm_simulation():
    import time
    
    print("Enter Your PY Card")
    time.sleep(3)
    print("\nScanning the Card")
    time.sleep(5)

# BALNACE
    balance = 1000000
    
# PIN
    pin = 2662
    pin_max_attempts = 2
    attempts = 0
    
    
    print("\nEnter Your 4 digits PIN")
    pin = int(input())
    
    
    while attempts < pin_max_attempts:    
            if pin == 2662:
            

                print("\nJust a moment")
                time.sleep(2)

    # OPTIONS        
                print("\nChoose the option")
                print("\n1. Withdraw Money")
                print("2. Balance Inquiry")
                print("3. Exit")
            
    # WITHDRAW OPTIONS    
            
                while True:

                    option = int(input())
                    if option == 1:
                        print("\nEnter the amount")
                        print("1.500\t 2.1000\n 3.2000\t 4.3000\n 5.5000\t 6.Other Amount")    

                        while True:
                            amount = int(input())
                            if amount == 1:
                                print(f'\nThe amount of 500 has been withdraw and the remaining balance is', int(balance - 500))
                        
                            elif amount == 2:
                                print(f'\nThe amount of 1000 has been withdraw and the remaining balance is', int(balance - 1000))
                                    
                            elif amount == 3:
                                print(f'\nThe amount of 2000 has been withdraw and the remaining balance is', int(balance - 2000))
                            
                            elif amount == 4:
                                print(f'\nThe amount of 3000 has been withdraw and the remaining balance is', int(balance - 3000))
                            
                            elif amount == 5:
                                print(f'\nThe amount of 5000 has been withdraw and the remaining balance is', int(balance - 5000))
                        
                            elif amount == 6:
                                print("\nEnter the Amount")
                                
                                customer_amount = int(input())
                                if customer_amount < balance:
                                    print(f'\nThe amount of {customer_amount} has been withdraw and the remaining balance is', int(balance - customer_amount))
                                else:
                                    print("\nInsufficent Balance")
                        
                            else:
                                print("\nChoose a valid amount option")
                            print("\nDo you want to make another transaction?t (y/n)")
                            
    # ASKING FOR ANOTHER TRANSACTION
                            
                            another_tranaction = input()
                            if another_tranaction == "y":
                                    print("\nEnter the amount")
                                    print("\n1.500\t 2.1000\n 3.2000\t 4.3000\n 5.5000\t 6.Other Amount")
                            else:
                                time.sleep(2)
                                print("\nCollect the Card")
                                time.sleep(2.5)
                                print("\nThanks for using the PY ATM")
                                return    
                        
    # BALANCE INQUIRY

                    elif option == 2:
                    
                        time.sleep(2)
                        print("\nYour current Balance is:", balance)
                        
                        print("\nDo you want to make another transaction?t (y/n)")
                        another_tranaction = input()
                        if another_tranaction == "y": 
                            print("\nChoose the option")
                            print("\n1. Withdraw Money")
                            print("2. Balance Inquiry")
                            print("3. Exit")
                            
                        else:
                            time.sleep(2)
                            print("\nCollect the Card")
                            time.sleep(2.5)
                            print("\nThanks for using the PY ATM")
                            break                    
                    
                        
    # EXIT OPTION

                    elif option == 3:
                        time.sleep(2)
                        print("\nCollect the Card")
                        time.sleep(2.5)
                        print("\nThanks for using the ATM")
                        break
                
                    else:
                        print("\nEnter a valid Option")
                        print("\n1. Withdraw Money")
                        print("2. Balance Inquiry")
                        print("3. Exit")
                
            else:
                print("\nSorry! The PIN is wrong")
                print("\n Enter valid 4 digits PIN")
                pin = int(input())
                attempts += 1
                if attempts == pin_max_attempts:
                    print("\nYou have used your max attempts")
                    time.sleep(2)
                    print("\nYour card has been blocked for security reasons.")
                    time.sleep(2)
                    print("\nCollect the Card")
                    time.sleep(2.5)
                    print("\nThanks for using the PY ATM")
                    break
                continue
            break
    
atm_simulation()