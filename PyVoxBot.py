import osjj
import androidhelper

if __name__ == "__main__":
    print("Welcome to PyVoxBot 2.0 by Sufiyan")
    x = int(input("Enter the operating system you are in:\nPress 1 for iOS\nPress 2 for Windows\nPress 3 for Android: "))

    if x == 1:
        while True:
            os.system("say 'Hello, this is PyVoxBot (FOR MAC) created by Master Sufiyan.'")
            a = input("Enter the text you want me to speak: ")

            if a.lower() == "exit":
                os.system("say 'I am Robospeaker and I am leaving now.'")
                print("Bye bye")
                break

            command = f"say {a}"
            os.system(command)

    elif x == 2:
        def speak_text(text):
            command = f'powershell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"'
            os.system(command)

        print("Welcome to PyVoxBot (FOR WINDOWS) 2.0 by Sufiyan")
        while True:
            text_to_speak = input("Enter the text you want me to speak (or type 'exit' to quit): ")
            if text_to_speak.lower() == "exit":
                speak_text("I am Robospeaker and I am leaving now.")
                print("Bye bye")
                break
            speak_text(text_to_speak)

    elif x == 3:
        def text_to_speech_android(text):
            try:
                droid = androidhelper.Android()
                droid.ttsSpeak(text)
            except FileNotFoundError:
                print("Error: install QPYTHON 3L application. Make sure you've installed it.")

        print("Welcome to PyVoxBot (FOR ANDROID) 2.0 by Sufiyan")
        while True:
            text_speech = input("Enter the text you want me to speak (or type 'exit' to quit): ")
            if text_speech.lower() == "exit":
                text_to_speech_android("I am Robospeaker and I am leaving now.")
                print("Bye bye")
                break
            text_to_speech_android(text_speech)

    else:
        print("Enter the correct option")
		    
