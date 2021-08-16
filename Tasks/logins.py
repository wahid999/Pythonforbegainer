 if count == 3:
    print("\nThree Username and Password Attempts used. Goodbye") 
        break
         


    elif userName == 'wahid' and password == '1Python@': 
        print("Welcome! ")
        break 

    elif userName != 'wahid' and password != '1Python@': 
        print("Your Username and Password is wrong!") 
        userName = input("\n\nUsername: ") 
        password = input("Password: ") 
        count += 1 
        continue 

    elif userName == 'wahid' and password != '1Python@':
        print("Your Password is wrong!") 
        userName = input("\n\nUsername: ")
        password = input("Password: ")
        count += 1 
        continue 

    elif userName != 'wahid' and password == '1Python@':
        print("Your Username is wrong!") 
        userName = input("\n\nUsername: ") 
        password = input("Password: ") 
        count += 1
        continue 