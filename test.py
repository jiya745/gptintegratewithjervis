
from typing import Text
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pathlib
import pyttsx3
import speech_recognition as sr
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.svm import SVC
# import nltk
# from sklearn.model_selection import train_test_split
# import random
import warnings
warnings.simplefilter('ignore')

# nltk.download("punkt")

def speak(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice',Id)
    print("")
    print(f"==> Jarvis AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recogizing....")
        query = r.recognize_google(audio,language="en")
        print(f"==> Miss Pakistan : {query}")
        return query.lower()

    except:
        return ""

ScriptDir = pathlib.Path().absolute()

url = "https://flowgpt.com/chat/"
chrome_option = Options()
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_option.add_argument(f"user-agent={user_agent}")
chrome_option.add_argument('--profile-directory=Default')
chrome_option.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
chrome_option.add_argument('--headless=new')
service = Service(ChromeDriverManager().install())  # Invoke the Service constructor
driver = webdriver.Chrome(service=service, options=chrome_option)
driver.maximize_window()
driver.get(url=url)
sleep(10)

chatnumber = 3

def checker():
    global chatnumber
    for i in range(1,1000):
        if i % 2 != 0:
            try:
                chatnumber = str(i)
                Xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[{chatnumber}]/div/div/div/div[1]" 
                driver.find_element(by=By.XPATH,value=Xpath)
            except:    
                print(f"The next chatnumber is : {i}")
                chatnumber = str(i)
                break
            
def websiteopener():
    while True:
        try:
            xPath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea'
            driver.find_element(by=By.XPATH,value=xPath)
            break
        except:
            pass
        
def sendmessage(Query):
                xPath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea'
                driver.find_element(by=By.XPATH,value=xPath).send_keys(Query)
                sleep(0.5)
                XPath2 = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/button'
                driver.find_element(by=By.XPATH,value=XPath2).click()

def waitfooranswer():
      sleep(2)
      xpath3 = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div/button'
      while True:
        try:
            driver.find_element(by=By.XPATH,value=xpath3)     
        except:
            break

def resultscrapper():
    global chatnumber
    chatnumber = str(chatnumber)
    Xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[{chatnumber}]/div/div/div/div[1]"    
    Text = driver.find_element(by=By.XPATH,value=Xpath).text
    chatnumbernew  = int(chatnumber)+2
    chatnumber = chatnumbernew
    return Text




websiteopener()
checker()       
while True:
    Query  = speechrecognition()
    if len(str(Query))<3:
        pass
    elif Query==None:
        pass
    else:
        sendmessage(Query=Query)
        waitfooranswer()
        Text =  resultscrapper()
        speak(Text)





# def popupremover():
#     Xpath = '/html/body/div[3]/div[3]/div/section/div/div[3]/button[2]'
#     driver.find_element(by=By.XPATH,value=Xpath).click()
    
# popupremover()
# sleep(5000)
# print("loaded!")
# sendmessage("hello,how are you")
# resultscrapper()
# sleep(50)
#/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[5]/div/div/div/div[1]
#/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div/div/div/div
#/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[3]/div/div/div/div[1]
#/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[5]/div/div/div/div[1]