from pywikihow import search_wikihow
import speedtest #pip install speedtest-cli
from requests import get
import speech_recognition as sr
import pyjokes
import timefin
import pyttsx3
import random
import datetime
import webbrowser
import os
import json
import requests
from bs4 import BeautifulSoup
import pyautogui
jarvis = pyttsx3.init()
def speak(audio):
    jarvis.say(audio)
    jarvis.runAndWait()
print("hello SIR  WELCOME AGAIN ,, MY NAME IS STURDY,  i am your Virtual assistant !(A.I) ,, right now i am under construction.")
speak("""hello SIR ,
WELCOME AGAIN ,,,
my name is STURDY
i am your Virtual assistance !(A.I) ,, right now i am under construction. """)

print("                                                                                                              ")
print("                         MADE BY HARSHIT KUMAR   //  Created On - 9th SEP 2021                                 ")
print("                                                                                                                ")
anvesha = datetime.datetime.now()
y = datetime.datetime.now().hour
if y>=0 and y<=11:
    print("GOOD MORNING SIR !! WAS WAITING FOR YOU ")
    speak("GOOD MORNING SIR !! WAS WAITING FOR YOU")
    speak("its ")
    print(anvesha.strftime("%I:%M %p"))
    speak(anvesha.strftime("%I:%M %p"))
    speak("today is")
    print(anvesha.strftime("%A"))
    speak(anvesha.strftime("%A"))
    speak("and the date is ")
    print(anvesha.strftime("%x"))
    speak(anvesha.strftime("%x"))
elif y>=12 and y<=16:
    print("GOOD AFTERNOON SIR !!  WAS WAITING FOR YOU ")
    speak("GOOD  AFTERNOON  SIR ... WAS  WAITING  FOR  YOU ")
    speak("its ")
    print(anvesha.strftime("%I:%M %p"))
    speak(anvesha.strftime("%I:%M %p"))
    speak("today is")
    print(anvesha.strftime("%A"))
    speak(anvesha.strftime("%A"))
    speak("and the date is ")
    print(anvesha.strftime("%x"))
    speak(anvesha.strftime("%x"))
elif y>=17 and y<=19:
    print("GOOD  EVENING  SIR .. WAS WAITING FOR YOU")
    speak("GOOD  EVENING  SIR !  WAS  WAITING  FOR  YOU ")
    speak("its ")
    print(anvesha.strftime("%I:%M %p"))
    speak(anvesha.strftime("%I:%M %p"))
    speak("today is")
    print(anvesha.strftime("%A"))
    speak(anvesha.strftime("%A"))
    speak("and the date is ")
    print(anvesha.strftime("%x"))
    speak(anvesha.strftime("%x"))
else:
    print("hellow sir ..")
    speak("hello  sir ....")
    speak("its ")
    print(anvesha.strftime("%I:%M %p"))
    speak(anvesha.strftime("%I:%M %p"))
    speak("today is")
    print(anvesha.strftime("%A"))
    speak(anvesha.strftime("%A"))
    speak("and the date is ")
    print(anvesha.strftime("%x"))
    speak(anvesha.strftime("%x"))
    
#wish me ! 
speak(" ,  how   are   you   > ?")
print(",, how are you > ?")
list=["GOOD  SIR " , "LOVE  YOU  SIR " , "GREAT  SIR " , "NICE  .. I  AM  READY  FOR  YOUR  WORK  SIR" , "WONDERFUL  SIR" , "GOOD  TO  LISTEN  SIR"]
harshit=random.choice(list)
x=input("enter your command ")
if x =="badhiya" or x=="all good" or x=="i am fine" or x=="fine" or x=="theek hai" or x=="acche hai" or x=="achhe hai" or x=="good" or x=="i am good" or x=="badhiya hai":
    print(harshit)
    speak(harshit)
elif x=="BADHIYA" or x=="ALL GOOD" or x=="I AM FINE"  or x=="THEEK HAI" or x=="ACHHE HAI" or x=="ACCHE HAI" or x=="GOOD" or x=="I AM GOOD" or x=="BADHIYA HAI" or x=="FINE":
    print(harshit)
    speak(harshit)
elif x =="badhiya " or x=="all good " or x=="i am fine " or x=="fine " or x=="theek hai " or x=="acche hai " or x=="achhe hai " or x=="good " or x=="i am good " or x=="badhiya hai ":
    print(harshit)
    speak(harshit)
elif x=="BADHIYA " or x=="ALL GOOD " or x=="I AM FINE "  or x=="THEEK HAI " or x=="ACHHE HAI " or x=="ACCHE HAI " or x=="GOOD " or x=="I AM GOOD " or x=="BADHIYA HAI " or x=="FINE ":
    print(harshit)
    speak(harshit)
else:
    print("ohh !!")
    speak(" oh!!! ")

#take command

if __name__=="_main_":
    wishMe()
    while True:
        query=takeCommand().lower()
    takeCommand()


        
#time , dates , dayS codes!!
while True:
    ss = input("enter your command sir - ")
    list1=["ALL GOOD SIR ,  ... WAS  WAITING  FOR  YOUR  COMMAND", "VERY  WELL  SIR",  "AS  SAME  AS  YOU"]
    sri=random.choice(list1)
    list2 = ["bbye SIR ... I AM DONE HERE" , "BYE SIR.. TAKE CARE" ,  "GOOD BYE SIR ! HOPE WE WILL MEET SOON , TILL THEN TAKE CARE" , "SAYONARA SIR "]
    maa = random.choice(list2)
    if ss == "bye" or ss=="BYE" or ss==" BYE" or ss==" bye" or ss=="good bye" or ss==" good bye" or ss==" GOOD BYE" or ss=="GOOD BYE" or ss=="bbye" or ss==" bbye" or ss=="BBYE" or ss==" BBYE":
        print(maa)
        speak(maa)
        break
    elif ss == "whats the time" or ss=="time right now" or ss=="time" or ss=="TIME RIGHT NOW" or ss=="TIME RIGHT NOW " or ss=="TIME" or ss=="TIME " or ss=="time " or ss=="time right now " or ss=="whats the time " or ss=="WHATS THE TIME" or ss=="WHATS THE TIME " or ss=="whats the time right now" or ss=="whats the time right now " or ss=="WHATS THE TIME RIGHT NOW" or ss=="WHATS THE TIME RIGHT NOW ":
        bhanu = datetime.datetime.now()
        print(bhanu.strftime("%I:%M:%S %p"))
        speak(bhanu.strftime("%I:%M:%S %p"))
    elif ss=="day" or ss=="todays day" or ss=="whats the day today" or ss=="day " or ss=="whats the day today " or ss=="DAY" or ss=="DAY "or ss=="WHATS THE DAY TODAY" or ss=="WHATS THE DAY TODAY "or ss=="todays day " or ss=="TODAYS DAY" or ss=="TODAYS DAY ":
        qwerty = datetime.datetime.now()
        print(qwerty.strftime("%A"))
        speak(qwerty.strftime("%A"))
    elif ss=="whats the date today" or ss=="todays date" or ss=="date" or ss=="whats the date today" or ss=="todays date " or ss=="date " or ss=="DATE" or ss=="DATE " or ss=="WHATS THE DATE TODAY" or ss=="WHATS THE DATE TODAY " or ss=="TODAYS DATE" or ss=="TODAYS DATE ":
        rashi = datetime.datetime.now()
        print(rashi.strftime("%x"))
        speak(rashi.strftime("%x"))
    elif ss=="how are you " or ss=="how are you" or ss=="HOW ARE YOU" or ss=="HOW ARE YOU ":
        print(sri)
        speak(sri)
    elif ss=="thank you" or ss=="thanks" or ss=="thank you " or ss=="thanks " or ss=="THANK YOU" or ss=="THANK YOU " or ss=="THANKS" or ss=="THANKS ":
            print("NO PROBLEM, SIR .. ALWAYS WITH YOU")
            speak("NO  PROBLEM  SIR !!  ALWAYS  WITH  YOU")
    elif ss=="do you believe in god":
        print("Yes sir I do believe in that positive energy")
        speak("Yes sir I do believe in that positive energy")
    elif ss=="what can you do":
        print("NOT MUCH YET!! but as your order sir")
        speak("NOT MUCH YET!!, but as your order sir")
#OPENING TASKS
    elif "open notepad" in ss:
        path="C:\\Windows\\notepad"
        os.startfile(path)
#open any site
    elif "open youtube" in ss:
        webbrowser.open("www.youtube.com")
    elif "open google" in ss:
        webbrowser.open("www.google.com")
# music
    elif ss=="play music" or ss=="play music" or ss=="PLAY MUSIC" or ss=="PLAY MUSIC":
        music="D:\\Downloads\\Akshat bhaiya"
        songs = os.listdir(music)
        z=len(songs)
        fk=(random.randint(0,z))
        print(songs[fk])
        os.startfile(os.path.join(music,songs[fk]))
# TIMER
    elif "timer" in ss:
          speak("for how  much  seconds  sir  ? ")
          sec = int(input("ENTER THE TIME : "))
          for i in range(sec):
              print(str(sec - i) + ' SECONDS REMAINING')
              speak(sec-i)
              time.sleep(1)
          speak("time  is   up   sir ! ")
          print("TIME IS UP SIR !")
          
# TELL ME A JOKE
    elif "tell me a joke" in ss:
        joke=pyjokes.get_joke()
        print(joke)
        speak(joke)
# SCREENSHOTS
    elif 'take' in ss or "screenshot" in ss or 'screenshot' in ss:
            print("TAKING SCREENSHOT SIR")
            speak("taking   screenshot  sir !")
            print("WHAT SHOULD I KEEP THE NAME OF THE FILE ? ")
            speak("what  should  i  keep  the  name  of  te  file  ?")
            name = input("ENTER THE NAME OF THE FILE :-")
            img = pyautogui.screenshot()
            time.sleep(1)
            img.save(f"{name}.png")
            img.show()
            print("SCREENSHOT TAKEN  SIR ! ")
            speak("screenshot  taken  SIR ")
# WIKIHOW
    elif 'how to' in ss:
        try:
             print("SEARCHNG SIR")
             speak("searching sir ")
             max_results=1
             how=search_wikihow(ss, max_results) 
             assert len(how)==1
             print(how[0].summary)
             speak(how[0].summary)
        except:
            print("CAN'T FOUND IT SIR ")
            speak("can't  found  it  sir ")
# INTERNET SPEED CHECK
    elif ss=="test internet speed" or ss=="check internet speed" or ss=="internet speed ":
        print('CHECKING SIR !! JUST GIVE ME A MINUTE . ')
        speak('checking  sir  !! just  give  me  a  miunte . ')
        st=speedtest.Speedtest()
        dl=st.download()
        up=st.upload()
        print(f'''WE HAVE {dl} Mbps DOWNLAOD
               AND {up} Mbps UPLOAD ''')
        speak(f'''WE   HAVE {dl}   Mbps   DOWNLAOD
               AND   {up}   Mbps   UPLOAD   ''')
        speak("we  have  very  fast  internet  sir!")
        speak("Your  Internet  connection  should  be  able  to  handle  multiple  devices  streaming  HD  videos ,  video  conferencing  and  gaming  at  the  same  time.")
#IP ADDRESS
    elif "ip address" in ss:
        ip=get('https://api.ipify.org').text
        print(f"your I.P - ADDRESS is {ip}")
        speak(f"your  I P - ADDRESS  is  {ip}")
# VOLMUME CONTROL
    elif ss=='volume up':
        pyautogui.press("volumeup")
        print("VOLUME UP SIR !")
        speak("volume  up  sir ")
    elif ss=='volume down':
        pyautogui.press("volumedown")
        print("VOLUME DOWN SIR !")
        speak("volume  down  sir !")
    elif ss=='mute':
        pyautogui.press("volumemute")
        print('DONE SIR')
        speak("done  sir !")
    elif ss=="read the toaday's news" or ss=="today's news" or ss=="news":
            try:
                url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=35d60ad2d3a749368ab8dff8ead5b0a4"
                news = requests.get(url).text
                news_dict = json.loads(news)
                arts = news_dict['articles']
                print("TODAY'S NEWS")
                speak("today's  news ")
                for article in arts:
                     print(article['title'])
                     speak(article['title'])
                print("NEWS COMPLETED ...")
                speak("news completed ...")
            except:
                print(" SIR  I AM NOT ABLE TO GET THE NEWS . !! I THINK I AM NOT CONNECTED TO INTERNET")
                speak("sir I AM NOT ABLE TO  GET THE NEWS !  i  think  i  am  not  connected  to  internet")



else:
    print(ss)