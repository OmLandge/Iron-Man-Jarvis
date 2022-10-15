

def Fun(self,command):
        print(command)
        if 'your name' in command:
            print("My name is jarvis")
            return "My name is jarvis"
        elif 'my name' in command:
            print("your name is Om")
            return "your name is Om"
        elif 'college name' in command:
            print("you are studing in Modern College, with Science stream in p.c.m" )
            return "you are studing in Modern College, with Science stream in p.c.m" 
        elif 'what can you do' in command:
            print("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google, I can tell jokes and more for you")
            return "I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google, I can tell jokes and many more for you"
        elif 'your age' in command:
            print("I am very young that u")
            return "I am very young that u"
        elif 'date' in command and 'come' in command:
            print("I want to spend some time with you, but people around you will be jealous of you and that won't be tolerated so, we catch up some other time")
            return "I want to spend some time with you, but people around you will be jealous of you and that won't be tolerated so, we will catch up some other time"
        elif 'are you single' in command:
            print('No, I am in a relationship with wifi')
            return 'No, I am in a relationship with wifi'
        elif 'are you there' in command:
            print('Yes boss I am here')
            return 'Yes boss I am here'
        elif 'tell me something' in command:
            print('sir, I don\'t have much to say, you only tell me someting i will give you the company')
            return 'sir, I don\'t have much to say, you only tell me someting i will give you the company'
        elif 'thank you' in command:
            print('sir, I am here to help you..., your welcome')
            return 'sir, I am here to help you..., your welcome'
        elif 'in your free time' in command:
            print('sir, I will be listening to all your words')
            return 'sir, I will be listening to all your words'
        elif 'i love you' in command:
            print('I love you too sir')
            return 'I love you too sir'
        elif 'can you hear me' in command:
            print('Yes sir, I can hear you')
            return 'Yes sir, I can hear you'
        elif 'do you ever get tired' in command:
            print('It would be impossible to tire of our conversation')
            return 'It would be impossible to tire of our conversation'
        else :
            print('i can\'t understand your command')
            return 'i can\'t understand your command'