import whisper
import sys
import os

def transcribe_audio(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found")
        return
    
    print(f"Loading model...")
    model = whisper.load_model("base")
    
    print(f"Transcribing {file_path}...")
    result = model.transcribe(file_path)
    
    print("\n" + "="*50)
    print("TRANSCRIPTION:")
    print("="*50)
    print(result["text"])
    print("="*50)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio_file>")
    else:
        transcribe_audio(sys.argv[1])