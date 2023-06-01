import termux
import os
import time

from termux import TTS
from os import system
from time import sleep

system("pip install termux")
sleep(0.5)
system("clear")

def banner(versi):
	print(f"""
 _________  _________  ______
/________/\/________/\/_____/\ 
\__.::.__\/\__.::.__\/\::::_\/_
   \::\ \     \::\ \   \:\/___/\ 
    \::\ \     \::\ \   \_::._\:\ 
     \::\ \     \::\ \    /____\:\ 
{versi}  \__\/      \__\/    \_____\/

English only\n""")

def ty():
	print(">>> Thank you for use! :)")

banner("v1.0")

try:
	def tts(teks):
		if teks == "":
			TTS.tts_speak("Why is it empty, stupid?")
			ty()

		else:
			TTS.tts_speak(teks)
			ty()

	tts(teks=input("Masukkan Teks : "))

except KeyboardInterrupt:
	TTS.tts_speak("You're out!")
	ty()
