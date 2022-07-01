from gtts import gTTS
from playsound import playsound

#Definir o texto que será transformado em áudio
texto = gTTS("Meliante detectado")

#Salva o arquivo, definir o nome do arquivo que será salvo
texto.save('audio.mp3')

#Repoduz o som do arquivo
playsound('audio.mp3')