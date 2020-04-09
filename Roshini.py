import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import string


print("Installing Sara")


engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
#vv='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
engine.setProperty('voice',voices[0])
'''for voice in voices:
     print(voice.id)

'''
# speaks the string passed to it

def speak(audio):

     engine.say(audio)
     engine.runAndWait()

speak("please enter your name!")


n=input('ENTER YOUR NAME  : ')
MASTER = n


if MASTER=='roshini':
     speak("hello i'm your assistant SARA")
else:
     speak("hello i'm SARA")

#this will wish accroding to time

def wish():
     hour = int(datetime.datetime.now().hour)

     if n=='roshini':
          if hour>=0 and hour<3:
               speak("Not a Good Time To Talk Master"+ MASTER)
          elif hour>=3 and hour<4:
               speak("I Am Your Demon"+MASTER+"HA HA HAA")
          elif hour>=4 and hour<12:
               speak("GOOD Morning Master"+MASTER)
          elif hour>=12 and hour<17:
               speak("GOOD Afternoon Master"+MASTER)
          elif hour>=17 and hour<22:
               speak("Good Evening Master"+MASTER)
          else:
               speak("Probably TIME TO SLEEP Master"+MASTER)
     else:
          if hour>=0 and hour<3:
               speak("Not a Good Time To Talk Master"+ MASTER)
          elif hour>=3 and hour<4:
               speak("I Am Your Demon"+MASTER+"HA HA HAA")
          elif hour>=4 and hour<12:
               speak("GOOD Morning"+MASTER)
          elif hour>=12 and hour<17:
               speak("GOOD Afternoon"+MASTER)
          elif hour>=17 and hour<22:
               speak("Good Evening"+MASTER)
          else:
               speak("Probably TIME TO sleep"+MASTER)

     if hour!=3:
          speak("How May I Help You?")
     else:
          speak("It's Wrong Time Don't Mess With Me")
          


#take command from user
def sendmail(to,content):
     server= smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('mailsjdn@gmail.com','passcode')
     sever.sendmail("hwbdjbr@dnjd.com",to,content)
     server.close()




def takecommand():
     r = sr.Recognizer() 
     with sr.Microphone() as source:
          print("Listening....")
          audio= r.listen(source)
          
     try:
          print("Recognizing...")
          quer = r.recognize_google(audio,language="en-US")
          print(f"user said: {quer}\n")
     except :
          speak("ok")
          #print("...")
          quer = None
          takecommand()
     return quer

def termi():
     exit(0)
#mainnn...


wish()

while(True):
     query = takecommand()
     



     #logic for execting tasks

     
     if 'open youtube' in query.lower():
          speak('opening youtube')
          chrome='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
          webbrowser.get(chrome).open("youtube.com")


          
     elif 'play music' in query.lower():
          speak("playing music..")
          songs_dir = "E:\\audio"
          song=os.listdir(songs_dir)
          #print(song)
          os.startfile(os.path.join(songs_dir,song[10]))

     elif 'play video' in query.lower():
          speak("playing videosong...")
          songs_dir = "E:\\video songs"
          song=os.listdir(songs_dir)
          #print(song)
          os.startfile(os.path.join(songs_dir,song[0]))

     elif 'play movie' in query.lower():
          speak("movie time...")
          songs_dir = "D:\movies"
          song=os.listdir(songs_dir)
          #print(song)
          os.startfile(os.path.join(songs_dir,song[4]))
          


     elif ' time' in query.lower():
          time = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"{MASTER} the time is {time}")

     elif 'send mail to' in query.lower():
          try:
               speak("what shall i send")
               content = takecommand()
               to = "hhfdhg@gmail.com"
               sendmail(to,content)
               speak("mail has been send")
          except Exception as e:
               print(e)
               speak("mail failed")

     elif 'search' in query.lower():
          speak("opening google to search")
          query=query.replace("search",'')
          query=query.strip()
          query=query.split(" ")
          if 'about' in query:
               query.replace('about','')
          #query=''.join(query)
          query=''.join(query)
          
          #print(query)
          chrome='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
          webbrowser.get(chrome).open(f'{query}.')

     elif 'how are you' in query.lower():
          speak("I'm good, hope you are having a good day")


     elif 'close SARA' in query.lower():
          speak("Have a good time "+MASTER)
          termi()          
     
     elif 'picture'  in query.lower():
          speak("Opening camera")
          speak('press qq for taking a picture')
          os.startfile("D:\Software\python\pycam.py")
     

     elif 'camera' in query.lower():
          speak("Opening camera")
          speak('press qq for taking a picture')
          os.startfile("D:\Software\python\py\cam.py")
     
     elif 'bored' in query.lower():
          speak("you can play music ")
          speak("or watch a movie")
          
          speak("that will be awesome ")
     
     elif 'interesting' in query.lower():
          speak("ok do coding you kid")
          os.startfile("C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib\\idle.pyw")

     else :
          speak("operation invalid")
