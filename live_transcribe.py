import whisper
import pyaudio
import numpy as np
import wave
import threading
import queue

model = whisper.load_model("tiny")
audio_queue = queue.Queue()
recording = True

def record_microphone():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    frames = []
    while recording:
        data = stream.read(CHUNK)
        frames.append(data)
        if len(frames) * CHUNK / RATE >= 3:
            audio_queue.put(b''.join(frames))
            frames = []
    
    stream.stop_stream()
    stream.close()
    p.terminate()

def transcribe_loop():
    while recording:
        if not audio_queue.empty():
            audio_data = audio_queue.get()
            audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
            result = model.transcribe(audio_np, fp16=False)
            print(f"\r{result['text']}", end="", flush=True)

threading.Thread(target=record_microphone, daemon=True).start()
transcribe_loop()