from translator import sanscript
from translator.sanscript import transliterate
from gtts import gTTS
from playsound import playsound

text = input('Enter the text you want to convert to speech: ')
to_script = sanscript.ITRANS
roman_text = transliterate(text, sanscript.DEVANAGARI, to_script)
tts = gTTS(text=text, lang='en', tld='co.in')
tts.save('speech.mp3')