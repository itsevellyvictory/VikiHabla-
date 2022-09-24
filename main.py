import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say('oi eu sou a viki e eu hablo mesmo')
maquina.say('o que deseja minha rainha victoria?')
maquina.say('digite o que quer que diga, estou a sua disposissao')
maquina.say('mae o que a senhora quer?')
maquina.runAndWait()

print('Digite o que quer que eu fale: ')
fala = input()
maquina.say(fala)
maquina.runAndWait()
