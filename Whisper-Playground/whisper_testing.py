import whisper

model = whisper.load_model("small")
result = model.transcribe("harvard.wav")
print(result["text"])
