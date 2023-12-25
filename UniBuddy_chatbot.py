''' [Case Study] --> Imagine the first day of university for a freshman named Alex. 
    Alex is excited but also overwhelmed by the vast campus, numerous courses, and the sea of new faces. 
    To aid new students like Alex, the university's IT department has developed a personalised chatbot. 
    This chatbot, named "UniBuddy", is designed to make the transition smoother for freshmen.
    Upon accessing the chatbot, Alex is prompted to enter their name, favourite colour, and age. 
    Based on this input, UniBuddy offers a personalised greeting.

    For instance, if Alex's favourite colour is blue, UniBuddy might suggest joining the university's "Blue Art Club".
    If Alex is 18, the chatbot might provide information about freshman-specific events.
    The chatbot also offers a feature where Alex can input specific queries, like "Where is the library?"
    or "How do I join the debate club?", 
    and UniBuddy responds with relevant information, all while adhering to a friendly tone,
    using string transformation methods to ensure the responses feel personalised and engaging.
'''
# Initialise message for first time
print('''------------------------------------------------------------------------- 
Welcome to UniBuddy! I am here to help you through your university journey, 
I am going to ask you a few questions to get to know you better.

Please enter your credentials to get started.''')

while True:
    
    user_name = input("\nPlease enter your name: ").capitalize()
        
    if not user_name.isalpha():
        print("Enter a valid name please")
        continue

    else:
        print(f"Welcome {user_name}!!")
        break

while True:
    try:

        user_age = int(input("\nPlease enter your age: "))
        
        if user_age < 18:
            print("Wow! You are starting university at a young age.")
            break
        elif user_age >= 18 and user_age < 25:
            print("You are in the right track there!")
            break
        else:
            print("That's great! It's never too late to learn and grow")
            break            

    except ValueError:
        print("You have not entered a number for your age. Please try again")        

while True:
    user_colour = input("\nPlease enter your favourite colour: ").capitalize()

    if user_colour == 'Blue' or user_colour == 'Red' or user_colour == 'Yellow' or \
        user_colour == 'Green' or user_colour == 'White' or user_colour == 'Black':
        print(f"{user_colour} is a nice color")
        break        
    else:
        print("Enter a correct colour please")
        
if user_age <= 20:
    print("\nI have noticed that you're a freshman, here are a few suggestions for you.")
    
    print("""
    1.  There is the freshman initiation ceremony, that is happening next Friday in
the auditorium @ 13h00.

    2.  There are several parties happening on campus grounds, go check them out!
            
    3.  The Cinema club is doing a presentation on the campus and it's various
facilities, check it out if you'd like a better lay of the land.
""")
    
if user_colour == "Red":
    print("""I see that your favourite colour is red! Try checking out the
following clubs that might interest you.""")    
    print("""
    1. Join our Red Boxing club!

    2. Join our Clifford the Big Red Dog appreciation society!""")
    
elif user_colour == "Blue":
    print("""I see that your favourite colour is blue! Try checking out the
following clubs that might interest you.""")    
    print("""
    1. Join our aquatic activities club where we partake in:
        - water polo
        - swimming
        - diving

    2. Join our Blues Clues apprieciation society!""")
    
elif user_colour == "Yellow":
    print("""I see that your favourite colour is yellow! Try checking out the
following clubs that might interest you.""")
    
    print("""
    1. Join our Track runners club!

    2. Join our Sunshine Breakfast club!""")

elif user_colour == "Green":
    print("""I see that your favourite colour is green! Try checking out the
following clubs that might interest you.""")    
    print("""
    1. Join our Yoga club!

    2. Join our Trekking club!""")
    
elif user_colour == "White":
    print("""I see that your favourite colour is white! Try checking out the
following clubs that might interest you.""")    
    print("""
    1. Join our Baking club!

    2. Join our Origami club""")
    
elif user_colour == "Black":
    print("""I see that your favourite colour is black! Try checking out the
following clubs that might interest you.""")
    print("""
    1. Join our Chess club!

    2. Join our Drawing club!""")
    
print("""\nWelcome to our FAQ (frequently asked questions) section!
Select one question to learn more.""")

# Open the text file that store the most frequently asked questions
faq_file = open("UnibuddyFAQ.txt","r")
# Decalre a list to store the questions
faq_list = []

for lines in faq_file:
    
    temp = lines.strip('\n')    # Remove the newline at the end of each line
    #temp = temp.split()         # Split each line of the file into a list
    #joined = " ".join(temp)     # Join

    faq_list.append(temp)       # Append each line to a list

faq_check = True
while faq_check:
    # Display the list with enumerate
    print("\nThis is a list of our most frequently asked questions:")
    for count, quest in enumerate(faq_list, start=1):
        print(f"{count}. {quest}")

    choice = int(input("\nPlease enter the number question you'd like to ask: "))
    # We deduct 1 from choice to get the correct index position of the question on the list
    index = choice - 1  

    if index == 0:
        print("""You can usually find a campus map at the university's information desk,
the admissions office, or on the university's website.""")
    elif index == 1:
        print("The library is turning left at the main entrance.")
    elif index == 2:
        print("The gym is at the back of the sport campus, at the end of the corridor on the main entrnace.")
    elif index == 3:
        print("The football field is next to the gym, you can also access it going around the campus building.")
    elif index == 4:
        print("The Cafeteria is next to the library on the second corridor at the left of the main entrance.")
    elif index == 5:
        print("You need to select the 'Python University WiFi' and register with your email to have access.")
    elif index == 6:
        print("The admissions office is located near the main entrance to the right.")

    while True:
        new_quest = input("\nDo you want to check the FAQ again? Select 'Y' to go back or 'N' to end the chat. ").upper()

        if new_quest == 'Y':           
           print("\nShowing the frequently asked questions again.")
           break
        elif new_quest == 'N':
            print("\nHopefully I have been helpful to you.")
            print("See you next time, good bye!!")
            faq_check = False
            break
        else:
            print("\nSorry, I'm not sure what you want to do, try again.")

