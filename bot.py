import speech_recognition as sr
from converter import transcript
from result import output, abort, pause, restart, unpause
import time

def main():
    while True:
        print("Say 'genius' to start recording.")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "genius":
                    abort()
                    print("ready")
                    trans = transcript()
                    #trans = "PLAY|CRUEL|SUMMER|BY|TAYLOR|SWIFT"
                    if trans == "PAUSE|":
                        pause()
                    elif trans == "UNPAUSE|":
                        unpause()
                    elif trans == "RESTART|":
                        restart()
                    else:
                        output(trans)
                    
            except Exception as e:
                print(e)
                time.sleep(1.5)
                continue

if __name__ == "__main__":
    main()
    