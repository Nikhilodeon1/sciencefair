from pygame import mixer
import pygame
import os
import urllib.request
import re
import time
from moviepy.editor import AudioFileClip
from gtts import gTTS
from datetime import datetime
from playsound import playsound
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import geocoder
import long_responses as long
import yt_dlp as youtube_dl # client to many multimedia portals
#import openai

def output(transcript2):
    pygame.init()
    list69 = transcript2.split("|")
    a = 0
    b = 0
    c = 0
    d = 0
    for elm in list69:
        if elm == "PLAY" or elm == "PLACE" or elm == "PLEASE" or elm == "PLEAS" or elm == "PLAIN" or elm == "PLANE" or elm == "PLAC" or elm == "PLAY'D" or elm == "PLAI" or elm == "PLAING"  :
            a = 1
        else:
            if elm == "TIME" or elm == "DIME" or elm == "LIME" or elm == "DAY" or elm == "WEEK" or elm == "MONTH" or elm == "DATE" or elm == "THAT":
                b = 1
            else:
                if elm == "WEATHER" or elm == "WETTER" or elm == "WETHER" or elm == "WATER" or elm == "TEMPERATURE" or elm == "TEMP" or elm == "HOT" or elm == "COLD":
                    c = 1
                else:
                    if a == 0 and b == 0 and c == 0 and d == 0:
                        d=1
    if a == 1: #song generator/player 
        str12 = ""
        for counter in range(0, len(list69)):
            if counter > 0:
                str12 += list69[counter] + " "
            counter += 1
        search_keyword = str12.replace(" ", "+") + "+lyrics"
        html = urllib.request.urlopen("http://youtube.com/results?search_query=" + search_keyword)
        videos_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        link = "http://youtube.com/watch?v=" + videos_ids[0]
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'thisfile.mp4',
        }
        video_title = ''
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            info_dict = ydl.extract_info(link, download=False)
            video_title = info_dict.get('title', None)
            print(video_title)
        mytext = 'Sounds Good! Playing {} on Nikky Tunes'.format(video_title)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("response.mp3")
        mixer.init() #Initialzing pyamge mixer
        mixer.music.load('response.mp3') #Loading Music File
        mixer.music.play() #Playing Music with Pygame
        def MP4ToMP3(mp4, mp3):
            FILETOCONVERT = AudioFileClip(mp4)
            FILETOCONVERT.write_audiofile(mp3)
            FILETOCONVERT.close()
        VIDEO_FILE_PATH = "C:\\Users\\nikhi\\Downloads\\Codes\\ScienceFairProject\\thisfile.mp4"
        AUDIO_FILE_PATH = "C:\\Users\\nikhi\\Downloads\\Codes\\ScienceFairProject\\thatfile.mp3"
        MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
        time.sleep(1.6)
        mixer.init() #Initialzing pyamge mixer
        mixer.music.load('thatfile.mp3') #Loading Music File
        mixer.music.play() #Playing Music with Pygame
    if b == 1: #time
        from datetime import datetime
        now = datetime.now()
        timePre = str(now.time()).split(":")
        datePre = str(now.date()).split("-")
        #timePre = timePre1.split(":")
        #datePre = datePre1.split("-")
        suffix = "AM"
        if int(timePre[0]) > 12:
            suffix = "PM"
            timePre[0] = int(timePre[0]) - 12
        elif int(timePre[0]) == 12:
            suffix = "PM"
        monthdict = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December",
        }
        numdict = {"01": "first", "02": "second", "03": "third", "04": "fourth", "05": "fifth", "06": "sixth", "07": "seventh", "08": "eighth", "09": "nineth", "10": "tenth", "11": "eleventh", "12": "twelveth", "13": "thirteenth", "14": "fourteenth", "15": "fifteenth", "16": "sixteenth", "17": "seventeenth", "18": "eighteenth", "19": "nineteenth", "20": "twentieth", "21": "twentyfirst", "22": "twentysecond", "23": "twentythird", "24": "twentyfourth", "25": "twentyfifth", "26": "twentysixth", "27": "twentyseventh", "28": "twentyeighth", "29": "twentynineth", "30": "thirtieth", "31": "thirtyfirst"}
        

        # enter city name
        city = "union city".replace(" ", "+")

        # creating url and requests instance
        url = "https://www.google.com/search?q="+"weather"+city
        html = requests.get(url).content

        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str1 = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

        # formatting data
        data = str1.split('\n')
        time1111 = data[0]
        sky = data[1]

        # getting all div tag
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

        # printing all data
        day = time1111.split(" ")[0]
        timestr = "The time is " + str(timePre[0]) + ":" + timePre[1] + suffix + ". The date is " + day + " " + monthdict[datePre[1]] + " " + numdict[datePre[2]] + " " + datePre[0]
        oooooooooooooooo = timestr
        language = 'en'
        myobj = gTTS(text=timestr, lang=language, slow=False)
        myobj.save("response.mp3")
        playsound("response.mp3", block = False)
    if c == 1: #weather and stuff
        from datetime import datetime
        g = geocoder.ip('me')
        geoLoc = Nominatim(user_agent="GetLoc")
        locname = geoLoc.reverse("{}, {}".format(g.latlng[0], g.latlng[1]))
        city = locname.address.split(", ")[3].replace(" ", "+")
        city1 = locname.address.split(", ")[3]

        # creating url and requests instance
        url = "https://www.google.com/search?q="+"weather"+city
        html = requests.get(url).content

        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str1231231 = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

        # formatting data
        data = str1231231.split('\n')
        sky = data[1]

        # getting all div tag

        str1 = "The temperature in {} is currently {}. The sky is {}. ".format(city1, temp.replace("°F"," degrees fahrenheit"), sky)
        date_string = datetime.now().strftime("%d%m%Y%H%M")
        filename = "audio/voice"+date_string+".mp3"
        language = 'en'
        myobj = gTTS(text=str1, lang=language, slow=False)
        myobj.save(filename)
        playsound(filename, block=True)
    if d == 1: #chatbot exceptions
        str12 = ""
        for counter in range(0, len(list69)):
            str12 += list69[counter]
        def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
            message_certainty = 0
            has_required_words = True
            # Counts how many words are present in each predefined message
            for word in user_message:
                if word in recognised_words:
                    message_certainty += 1

            # Calculates the percent of recognised words in a user message
            percentage = float(message_certainty) / float(len(recognised_words))

            # Checks that the required words are in the string
            for word in required_words:
                if word not in user_message:
                    has_required_words = False
                    break
                
            # Must either have the required words, or be a single response
            if has_required_words or single_response:
                return int(percentage * 100)
            else:
                return 0


        def check_all_messages(message, str1):
            highest_prob_list = {}

            # Simplifies response creation / adds it to the dict
            def response(bot_response, list_of_words, single_response=False, required_words=[]):
                nonlocal highest_prob_list
                highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

            # Responses -------------------------------------------------------------------------------------------------------
            response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo', 'yo', 'hallo', 'high'], single_response=True)
            response('See you!', ['bye', 'goodbye'], single_response=True)
            response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
            response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
            response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
            response('But Wait! I Never Asked You about Yourself.', ['wierd', 'sus', 'ugly', 'cringe', 'bad'], single_response=True)
            response('I am a bot who knows all.', ['who'], single_response=True)
            response('I asked.', ['who asked'], single_response=True)
            response('Elon Musk is a billionaire who owns the companies: Tesla, SpaceX, and more', ['musk', 'must'], single_response=True)

            # Longer responses
            response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
            response(long.R_EATING, ['what', 'eat', 'drink'], single_response=True)
            response(long.internet(str1), ['is', 'many', 'where'], single_response=True)

            best_match = max(highest_prob_list, key=highest_prob_list.get)
            # print(highest_prob_list)
            # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

            return long.unknown() if highest_prob_list[best_match] < 1 else best_match


        # Used to get the response
        def get_response(user_input):
            split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
            response = check_all_messages(split_message, user_input.lower())
            return response


        # Testing the response system
        while True:
            str1 = get_response(str12.lower())
            oooooooooooooooo = str1
            date_string = datetime.now().strftime("%d%m%Y%H%M")
            filename = "audio/voice"+date_string+".mp3"
            language = 'en'
            myobj = gTTS(text=str1, lang=language, slow=False)
            myobj.save(filename)
            playsound(filename, block = False)
            return oooooooooooooooo

        print("beans")
    return
def abort():
    mixer.music.stop()
    try:
        os.remove("C:\\Users\\nikhi\\Downloads\\Codes\\ScienceFairProject\\thatfile.mp3")
    except:
        return

def restart():
    mixer.music.stop()
    mixer.init() #Initialzing pyamge mixer
    mixer.music.load('thatfile.mp3') #Loading Music File
    mixer.music.play() #Playing Music with Pygame

def pause():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()