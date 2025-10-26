import speech_recognition as sr
import os
import pyttsx3
from datetime import datetime
import pyautogui

# Inicializar el motor de voz
engine = pyttsx3.init()

# Función para hacer que el asistente hable
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def decir_hora_fecha():
    #obtener hora y fecha actuales
    ahora = datetime.now()
    #formatea la hora y fecha en el formato deseado
    formato = "%d-%m-%Y, %H:%M:%S"
    hora_fecha_formateada = ahora.strftime(formato)
    return hora_fecha_formateada

# Función para escuchar y reconocer el comando de voz
def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
    try:
        print("Reconociendo...")
        comando = r.recognize_google(audio, language='es-ES')
        print(f"Has dicho: {comando}\n")
    except Exception as e:
        print("Lo siento, no pude reconocer tu voz")
        return "None"
    return comando

# Función para ejecutar comandos
def ejecutar(comando):
    if comando.startswith('jarvis'):
        comando = comando.replace('jarvis', '', 1)
        if 'hola' in comando:
            hablar("Hola señor")
        elif 'abre discord' in comando:
            os.system('start "" "C:\\Users\\usuario\\AppData\\Local\\Discord\\Update.exe" --processStart Discord.exe')
            hablar("Entendido señor")
        elif 'abre steam' in comando:
            os.system('start "" "C:\\Program Files (x86)\\Steam\\steam.exe"')
            hablar("Entendido señor")
        elif 'abre epic' in comando:
            os.system('start "" "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"')
            hablar("Entendido señor")
        elif 'abre visual studio' in comando:
            os.system('start "" "C:\\Users\\usuario\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
            hablar("Entendido señor")
        elif 'abre firefox' in comando:
            os.system('start "" "C:\\Program Files\\Mozilla Firefox\\firefox.exe"')
            hablar("Entendido señor")
        elif 'abre spotify' in comando:
            os.system('start "" C:\\Users\\usuario\\AppData\\Roaming\\Spotify\\Spotify.exe')
            hablar("Entendido señor")
        elif 'abre google' in comando:
            os.system('start "" "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
            hablar("Entendido señor")
        elif 'cierra' in comando:
            pyautogui.hotkey('alt', 'f4')
            hablar("Entendido señor")
        elif 'qué tal' in comando:
            hablar("señor soy un asistente virtual por lo tanto no puedo estar ni mal ni bien pero si le tengo que responder le responderia que estoy bien")
        elif 'qué eres' in comando:
            hablar("soy un asistente virtual encargado de ayudarle en todo lo posible señor")
        elif 'adiós' in comando:
            hablar("adiós señor que tenga un buen día")
        elif 'abre notas' in comando:
            os.system('start "" %windir%\\system32\\notepad.exe')
            hablar("Entendido señor")
        elif 'apaga' in comando:
            os.system('shutdown /s /t 1')
            hablar("Entendido señor")
        elif 'abre edge' in comando:
            os.system('start "" "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"')
            hablar("Entendido señor")
        elif 'abre word' in comando:
            os.system('start "" "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016"')
            hablar("Entendido señor")
        elif 'hora' in comando or 'fecha' in comando:
            hora_fecha = decir_hora_fecha()
            hablar("La fecha y hora actuales son: " + hora_fecha)
        elif 'cuenta un chiste' in comando:
            hablar("van 3 y se cae del medio, ¿te ha hecho gracia?. pues a el tampoco")
        elif 'cuenta una historia' in comando:
            hablar("un dia un niño llamado pi que vivia en la india se tenia que ir del pais con su familia por tema de dinero y luego el barco se hundio y solo sobrevivio el con un tigle")
        elif 'comandos' in comando:
            hablar("hola. fecha, hora. abre discord. abre word. abre spotify. abre firefox. abre google. abre edge. abre steam. abre epic. abre visual studio. abre notas. que tal. que eres. adios. apaga. cuenta un chiste. cuenta una historia. comandos")
# Bucle principal
while True:
    comando = escuchar().lower()
    ejecutar(comando)