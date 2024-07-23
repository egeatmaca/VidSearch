from pydub import AudioSegment
import speech_recognition as sr
import os
import tempfile


recognizer = sr.Recognizer()

def read_audio(file_path: str) -> AudioSegment:
    return AudioSegment.from_file(file_path)

def save_audio(audio_segment: AudioSegment, format: str) -> str:
    _, save_path = tempfile.mkstemp()
    audio_segment.export(save_path, format=format)
    return save_path

def speech_to_text(file_path: str, offset=None, duration=None) -> str:
    converted = False
    if not file_path.endswith('.aiff'):
        file_path = save_audio(read_audio(file_path), 'aiff')
        converted = True

    with sr.AudioFile(file_path) as source:
        audio_listened = recognizer.record(source, offset=None, duration=None)
        text = recognizer.recognize_whisper(audio_listened)
    if converted:
        os.remove(file_path)
    
    return text

def chunked_speech_to_text(file_path: str, interval_sec: int = 10) -> list[str]:
    audio_segment = read_audio(file_path)
    length = len(audio_segment)
    offset = 0
    duration = interval_sec * 1000

    converted = False
    if not file_path.endswith('.aiff'):
        file_path = save_audio(read_audio(file_path), 'aiff')
        converted = True

    texts = []
    while offset < length:
        text = speech_to_text(file_path, offset=offset, duration=duration)
        texts.append(text)
        offset += duration

    if converted:
        os.remove(file_path)
    
    return texts



    
    