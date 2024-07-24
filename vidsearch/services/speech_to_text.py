from pydub import AudioSegment
from pydub.utils import make_chunks
import speech_recognition as sr
import os
import tempfile
import json
import multiprocessing as mp


recognizer = sr.Recognizer()

def read_audio(file_path: str) -> AudioSegment:
    return AudioSegment.from_file(file_path)

def save_audio(audio_segment: AudioSegment, format: str) -> str:
    _, save_path = tempfile.mkstemp()
    audio_segment.export(save_path, format=format)
    return save_path

def speech_to_text(audio_segment: AudioSegment) -> str:
    file_path = save_audio(audio_segment, 'aiff')

    with sr.AudioFile(file_path) as source:
        audio_listened = recognizer.record(source)
        output = recognizer.recognize_vosk(audio_listened)
    
    os.remove(file_path)
    
    return json.loads(output).get('text')

def chunked_speech_to_text(file_path: str, interval_sec: int = 20) -> list[str]:
    audio_segment = read_audio(file_path)
    chunks = make_chunks(audio_segment, interval_sec*1000)

    with mp.get_context('spawn').Pool() as pool:
        texts = pool.map(speech_to_text, chunks)

    return texts
