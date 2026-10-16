import speech_recognition as sr         # This module can have ability to recognize speech 
import webbrowser                  # This module can have access search in browser
import subprocess                 
import pyttsx3                    # This module convert text into a speech.
from datetime import datetime    # This module is import the date and time functions/ keywords



def speak(text):          # This function can have access to speak with user
    subprocess.run([
        "powershell",
        "-Command",
        "Add-Type -AssemblyName System.Speech; "
        "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
        "$speak.Speak('" + text.replace("'", "''") + "')"
    ])


def processCommand(command):       # This function is used for accesing and do the given commands
    command = command.lower()

    if "open google" in command:    ## Open Google
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        
    elif "open youtube" in command:    ## Open YouTube
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "play" in command:              ## This block of code play any song in youtube
            search_song = command.replace("play", "").strip()
    
            if search_song:
                speak("Playing the song " + search_song)
                webbrowser.open(
                    "https://www.youtube.com/results?search_query=" + search_song.replace(" ", "+")
                )
            else:
                speak("What should I search for")
    

    elif "open github" in command:   ## Open Github
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "open whatsapp" in command:   ## Open Whats App
            speak("Opening Whats App")
            webbrowser.open("https://web.whatsapp.com/")


    elif "search" in command:              ## This block of code search anything on the google
        search = command.replace("search", "").strip()

        if search:
            speak("Searching for " + search)
            webbrowser.open(
                "https://www.google.com/search?q=" + search.replace(" ", "+")
            )
        else:
            speak("What should I search for")

    elif "time" in command:        ## Time
        current_time = datetime.now().strftime("%I:%M %p")  #(%I = 12-Hour format, %M = Minutes, %p = AM/PM)
        speak("The time is " + current_time)

    elif "date" in command:        ## Date
        current_date = datetime.now().strftime("%d %B %Y")  #(%d = Day, %B = Full month name, %Y = 4-digit year)
        speak("Today's date is " + current_date)

    elif "how are you" in command or "how r u" in command:
        speak("I am Fine Sir. What about you...")

    elif "exit" in command or "quit" in command or "stop" in command or "close" in command:      ## Exit the program
        speak("Goodbye sir, Have a nice day!")
        return False

    else:
        speak("Sorry, I don't understand that command.")

    return True


if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:

        r = sr.Recognizer()      # convert your voice into text

        try:
            with sr.Microphone(device_index=1) as source:
                                                ## This block of code is belongs to listen the word jarvis.
                print("Listening...")
                audio = r.listen(
                    source,
                    timeout=2,
                    phrase_time_limit=3
                )

            word = r.recognize_google(audio)   ## Your voice save in word variable

            print("You said:", word)

            if word.lower() == "jarvis":     ## convert your voice into lower words

                speak("Yes sir, what can I do")     ##if the condition true then jarvis speak.

                with sr.Microphone(device_index=1) as source:
                                                ## This block of code is belongs to listen your commands.
                    print("Jarvis Active...")
                    audio = r.listen(
                        source,
                        timeout=2,
                        phrase_time_limit=3
                    )

                command = r.recognize_google(audio)

                print("Command:", command)

                if processCommand(command) == False:
                    break

        except sr.WaitTimeoutError:      ## Wait time was too long
            print("Listening timed out")

        except sr.UnknownValueError:      ## if you not speak correctly your command
            print("Could not understand")

        except sr.RequestError:      ## If any error occurr in google module / function
            print("Google speech recognition error")

        except Exception as e:     ## If any different errors occurs.
            print("Error:", e)