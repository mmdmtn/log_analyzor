def result():
    print("-------- FINAL RESULT --------")
        
    print("--Total lines:" ,total_lines,"--")
    
    print("!!Total info:" ,total_info,"!!")
    
    print("##Total ERROR: " ,error_count,"##")
        
    print("**Total WARNING: " ,warning_count,"**")
        
    print("Total failed login:" ,failed_login)
    
    print("Failed log in by account:")
    for username , count in usernames.items():
        print(username, ":",count )

    highest_count = 0

    for user_n , count in usernames.items():
        if count > highest_count:
            highest_count = count
        




    print("Highest failed login count:", highest_count)
    print("Accounts:")

    for user_name2, count2 in usernames.items():
        if count2 == highest_count:
            print(user_name2)


try:

    usernames = {}


    
    with open("sample.log.txt" , "r" , encoding="utf-8") as file:
        
        error_count = 0
        warning_count = 0
        total_lines = 0
        total_info = 0
        failed_login = 0
    
        for i in file:

            total_lines += 1

            if "INFO" in i:
                total_info += 1
        
            elif "ERROR" in i:
                error_count += 1

            elif "WARNING" in i:
                warning_count += 1

            if "Failed login" in i:
                part = i.split()
                username = part[-1]
                
                if username in usernames:
                    usernames[username] += 1

                else:
                    usernames[username] = 1

                failed_login += 1

    result()

except FileNotFoundError:
    print("FILE NOT FOUND!")