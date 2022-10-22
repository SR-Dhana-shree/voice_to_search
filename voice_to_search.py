#imorting essential libraries
import speech_recognition as sr
import webbrowser

#for accessing microphone
sr.Microphone(device_index=1)

#calling recognizer function
q=sr.Recognizer()
q.energy_threshold=5000

#main program
with sr.Microphone() as source:
    print("Speak!")
    audio=q.listen(source)
    try:
        text=q.recognize_google(audio)
        print("You said : {}".format(text))
        url='https://www.google.co.in/search?q='

        #concatenate the url and given audio
        search_url=url+text
        webbrowser.open(search_url)
    except:
        print("Can't recognize")

