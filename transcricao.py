from pydub import AudioSegment
from pydub.utils import make_chunks
import speech_recognition as sr

# load audio file
audio = AudioSegment.from_mp3(r'./entrevista.mp3')
size = 180000 # pieces of 3 min (miliseconds)

chunks = make_chunks(audio, size)
for i, chunk in enumerate(chunks):
    chunk_name = "audio{0}.wav".format(i)
    chunk.export(chunk_name, format="wav")
    file_audio = sr.AudioFile("./" + chunk_name)

    recognizer = sr.Recognizer()

    # transcribe the audio
    with file_audio as source:
        audio_text = recognizer.record(source)
        transcription = recognizer.recognize_google(audio_text, language="pt-BR")

    file = open(chunk_name.replace('.wav', '') + '.txt','w')
    file.write(transcription)
    file.close()