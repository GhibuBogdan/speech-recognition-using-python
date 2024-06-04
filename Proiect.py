# Sursa :https://www.youtube.com/watch?v=sHeJgKBaiAI

import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('Rostiti cuvantul VIDEO, iar apoi spuneti ce doriti sa cautati')
    print('Vorbiti acum')
    audio = r3.listen(source)

if 'video' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('Ce doriti sa cautati')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

