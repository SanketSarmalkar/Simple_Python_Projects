import os
# https://www.codesofinterest.com/2020/05/text-to-speech-windows-10-pywin32.html
if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        x = str(input("Enter what you want me to pronounce: "))
        if x == "q":
            os.system("PowerShell Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('bye bye friend')")
            break
        command = f"PowerShell Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')"
        os.system(command)