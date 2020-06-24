#my_str = input("Please enter your own string: ")
#my_str = 'racecar aIbohPhoBiA racecar'

#my_str = my_str.casefold()

#rev_str = reversed(my_str)

#if list(my_str) == list(rev_str):
#   print("This string is a palindrome.")
#else:
#   print("This string is not a palindrome.")

#for input in my_str:
#    if(my_str == rev_str):
#print('This list item is a palindrome')

# Python Program to Check a Given String is Palindrome or Not

string = input("Please enter your own String : ")

if(string == string[:: - 1]):

  print("String in reverse Order :  ", string)

  print("This is a Palindrome String")

else:
    print("This is Not a Palindrome String")

#print("Do you want to continue?")

#answer = None
#while answer not in ("yes", "no"):
#    answer = input("Enter yes or no: ")
#    if answer == "yes":
#      print("Great, Let's Continue!")

answer = input('Would you like to try again?:')
if answer.lower().startswith("y"):
    print("Wonderbah!")
elif answer.lower().startswith("n"):
    print("Peace Out")
    exit()

string = input("Please enter your own String : ")

if(string == string[:: - 1]):

  print("String in reverse Order :  ", string)

  print("This is a Palindrome String")

else:
    print("This is Not a Palindrome String")

    if answer == "no":
        print("Thank you for letting me string you along!")
        exit()
