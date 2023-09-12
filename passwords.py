import csv
import re

#unhash if u need to create a new file
#userid_file = open("user_id.csv","w")

def list_data():
    userid_file = list(csv.reader(open("user_id.csv")))
    csv_list = []
    
    for row in userid_file:
        csv_list.append(row)
    
    return csv_list

def user_id(csv_list):
    stop = False
    while stop == False:
        x = 0
        userID = input("Enter new user ID: ").lower()
        id_inlist = False
    
        for row in csv_list:
            if userID in csv_list[x][0]:
                print("ID already exists")
                print("")
                id_inlist = True
            x += 1
            
        if id_inlist == True:
            stop = True
            main()

        return userID

def pw_new():  
    score = 0
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    special_char = re.compile("[!@#$%^&*()_+{}[]\|=-~`:;/?><.,")
    
    lower_check = False
    upper_check = False
    number_check = False
    special_char_check = False
    
    password = input("Enter new password: ")
           
    if len(password) >= 8:
        score += 1
            
    for x in password:
        if x.islower():
            lower_check = True
        if x.isupper():
            upper_check = True
        if x in numbers:
            number_check = True
        if special_char.search(x) == None:
            special_char_check = True
                        
    if lower_check == True:
        score += 1
    if upper_check == True:
        score += 1
    if number_check == True:
        score += 1
    if special_char_check == True:
        score += 1

    if score <= 2:
        print("Weak password")
        tryagain_confirm = input("Would you like to make another one? ").lower()
        print("")
        if tryagain_confirm == "yes":
            password = pw_new()
                
    elif score == 3 or score == 4:
        print("Password could be improved")
        tryagain_confirm = input("Would you like to make another one? ").lower()
        print("")
        if tryagain_confirm == "yes":
            password = pw_new()
                
    else:
        print("Strong password")
        print("")
               
    return password

def lookfor_id(csv_list):
    csv_list = list_data()
    
    tryagain = True
    userID = ""
    x = 0
    
    while tryagain == True:
        id_inlist = False
        
        search_id = input("Enter your user ID: ").lower()
        for row in csv_list:
            if search_id in csv_list[x][0]:
                id_inlist = True
            x += 1
            
        if id_inlist == True:
            userID = search_id
            tryagain = False
        else:
            print("ID does not exist. Please create one")
            print("")
                
        return userID
    
def overwrite(userID,csv_list):
    id_inlist = False
    x = 0
    
    password = pw_new()
    for row in csv_list:
        if userID == csv_list[x][0]:
            id_inlist = True
            if id_inlist == True:
                csv_list[x][1] = password
        x += 1
    
def pw_change(userID,csv_list):
    x = 0
    
    if userID != "":
        overwrite(userID,csv_list)
        
        userid_file = open("user_id.csv","w")
        for row in csv_list:
            new_record = csv_list[x][0] + ", " + csv_list[x][1] + "\n"
            userid_file.write(str(new_record))
            x += 1
            
        userid_file.close()
        
def user_id_display():
    csv_list = list_data()
    counter = 0
    
    for row in csv_list:
        print(csv_list[counter][0])
        print("")
        counter += 1
        
def main():
    csv_list = list_data()
    
    close_program = False
    
    while close_program == False:
        print("1) Create a new User ID \n2) Change a password \n3) Display all user IDs \n4) Quit")
        selection = input("Enter selection: ")
        print("")
        
        if selection == "1":
            userID = user_id(csv_list)
            password = pw_new()
            
            userid_file = open("user_id.csv","a")
            new_record = userID + "," + password + "\n"
            userid_file.write(str(new_record))
            userid_file.close()
            
        elif selection == "2":
            userID = lookfor_id(csv_list)
            pw_change(userID,csv_list)
        elif selection == "3":
            user_id_display()
        elif selection == "4":
            close_program = True
    
main()