import os
import sys
import speech_recognition as sr
from pydub import AudioSegment

FILENAME = 'sample_ru.ogg'


def convert_ogg_to_wav(input_path: str) -> str:
    output_path = os.path.splitext(input_path)[0]+'.wav'
    song = AudioSegment.from_ogg(input_path)
    song.export(output_path, format="wav")
    return output_path


if __name__ == '__main__':
    sound_path = convert_ogg_to_wav(FILENAME)
    recognizer = sr.Recognizer()
    with sr.AudioFile(sound_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language='ru')
        # text = recognizer.recognize_vosk(audio_data)
        print(text)
