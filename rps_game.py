import pyttsx3,random
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

options =['rock','paper','scissors']

def checker(computer ,user):
    if computer=='rock' and user=='scissors':
        yield"computer"
    elif computer=='rock' and user=='paper':
        yield"user"
    elif computer=='rock' and user=='rock':
        yield'Tie'
    elif computer=='paper' and user=='paper':
        yield'Tie'
    elif computer=='paper' and user=='scissors':
        yield'user'
    elif computer=='paper' and user=='rock':
        yield'computer'
    elif computer=='scissors' and user=='paper':
        yield'computer'
    elif computer=='scissors' and user=='scissors':
        yield'Tie'
    elif computer=='scissors' and user=='rock':
        yield'user'

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source,duration=0.8)
        r.pause_threshold = 0.5
        audio=r.listen(source)

    try:
        query=r.recognize_google(audio,language='en-in')
        print("recognizing")
        print(f"\nUser Said: {query}\n")

    except Exception as e:
        #print(e)
        speak("say that again please")
        return None
    return query

if __name__=='__main__':
    print("\n \n")
    print("".center(104,"*"))
    print("|","Rock , Paper , Scissors game with Computer".center(100," "),"|")
    print("".center(104,"*"),"\n")
    speak("Rock , Paper , Scissors game with Computer")
    print("The Game is starting please speak your choice : - \n")
    speak("The Game is starting please speak your choice ,")
    ucount,ccount,tcount=0,0,0
    while True:
        speak("Rock , Paper , Scissors")
        user_choice = takeCommand()
        if user_choice!=None:    
            user_choice=user_choice.lower()
            if user_choice=='quit':
                break
            if user_choice in options:  
                computer_choice = random.choice(options*10)
                print(f"Computer choice : {computer_choice}")
                speak(f"Computer choice is , {computer_choice}")
                if next(checker(computer_choice,user_choice))=='computer':
                    print("\ncomputer wins\n")
                    speak("computer wins")
                    ccount+=1
                elif next(checker(computer_choice,user_choice))=='user':
                    print("\nuser wins\n")
                    speak("user wins")
                    ucount+=1
                elif next(checker(computer_choice,user_choice))=='Tie':
                    print("\nTie,No one wins\n")
                    speak("Tie,No one wins")
                tcount+=1
            else:
                speak("Wrong choice Try again !")
    
    print(f"\nTotal games : {tcount} \nUser wins : {ucount} \nComputer Wins : {ccount} \nTie :{tcount-ucount-ccount}")
    input("\nPress enter to close the program ")