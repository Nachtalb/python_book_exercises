import win32com.client

text = """Hello, my friend.
          Ich muss lachen."""

speaker = win32com.client.Dispatch('Sapi.SpVoice')
voices = speaker.GetVoices()                      #1
for voice in voices:
   print(voice.GetDescription())                  #2
   speaker.Voice = voice                          #3
   speaker.Speak(text)


