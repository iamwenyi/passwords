# passwords 
code idea from the book Python by Example, by Nichola Lacey.
this code was a pain in the back. i hate csv files. 

Code that stores user IDs and passwords in a csv file. It displays the following menu:
1) Create a new User ID 
2) Change a password 
3) Display all user IDs 
4) Quit
Enter selection: 

If the user enters 1, it asks them for a user ID, and also checks if it already exists. Once a suitable user ID has been entered, it asks for a password. A password scores 1 point for each of the following-

has at least 8 characters;
includes uppercase letters;
includes lower case letters;
includes numbers; and
includes at least one special character.

If the password scores 1 or 2, the code tells them the password is weak, and allows them to make another. If it scores 3 or 4, it displays "Password could be improved" and lets them try for another password. If it scores a 5, the password is strong. Then, the final user ID and the password is added to the .csv file.

If they enter 2, they will have to enter a user ID, and it checks if the user ID is in the file. If it does, it allows the user to change the password. 

If they enter 3, it displays all of the user IDs, but not the passwords.

If they enter 4, the program stops!
