# this program is to check if you need to program or not

# ask user for input name ann language of programming 
name = input("What is your name? ")
language = input("What is your favorite programming language? ")

# print out the name and language
print("Hello " + name + ", I see you like " + language + ".")
# ask if the user has to program or not (y/n)
program = input("Do you need to program? (y/n) ")
# if the user has to program
if program == "y":
    # print out the message
    print("I see you need to program.")
    # tell the user a motivational message
    print("I see you need to program. You should try to learn how to program.")
# if the user does not have to program
else:
    # print out the message
    print("I see you do not need to program.")
    # ask if they have to program in the future (y/n)
    future = input("Do you need to program in the future? (y/n) ")
    # if the user has to program in the future
    if future == "y":
        # print then program now
        print("You should program now.")
    # if the user does not have to program in the future
    else:
        # print out the message
        # ask the user if they have some code to improve
        improve = input("Do you have some code to improve? (y/n) ")
        # if the user has some code to improve
        if improve == "y":
            # print out the message"
            # print you should program now
            print("You should program now.")
        # if the user does not have some code to improve
        else:
            # print out the message you should program later so program now
            print("You should program later.")
           


