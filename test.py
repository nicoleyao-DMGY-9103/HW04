import whisper

# Load the Whisper model
model = whisper.load_model("small")  # Options: tiny, base, small, medium, large

# Load an audio file (ensure it's 16kHz sample rate)
audio_path = "test_audio.wav"
result = model.transcribe(audio_path)

# Print the transcription
print("Transcribed Text:\n", result["text"])
