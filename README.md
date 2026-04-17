# Audio Transcriber

Simple speech-to-text using OpenAI Whisper.

## Mode 1: File Transcription

### Usage
1. Install: `pip install openai-whisper`
2. Place your audio file as `your_audio.mp3`
3. Run: `python transcribe.py`

## Mode 2: Live Microphone Transcription

### Usage
1. Install: `pip install openai-whisper pyaudio numpy`
2. Run: `python live_transcribe.py`
3. Speak into your microphone
4. Press `Ctrl+C` to stop

## Notes
- First run downloads the model (~140MB)
- CPU is slower but works fine
- Live mode uses tiny model for speed