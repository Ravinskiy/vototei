import os
import json
import wave
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer, SetLogLevel

FILENAME = 'sample_ru.ogg'

SetLogLevel(0)


def convert_ogg_to_wav(input_path: str) -> str:
    output_path = os.path.splitext(input_path)[0]+'.wav'
    song = AudioSegment.from_ogg(input_path)
    song.export(output_path, format="wav", parameters=["-ac", "1"])
    return output_path


if __name__ == '__main__':
    sound_path = convert_ogg_to_wav(FILENAME)
    model = Model("vosk-model-ru-0.22")
    rec = KaldiRecognizer(model, 160000)
    # You can also specify the possible word list
    # rec = KaldiRecognizer(model, 16000, "zero oh one two three four five six seven eight nine")
    wf = open(sound_path, "rb")
    wf.read(44)  # skip header
    while True:
        data = wf.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            print(res['text'])
    res = json.loads(rec.FinalResult())
    print(res['text'])
