from pydub import AudioSegment
# sound = AudioSegment.from_mp3("/full/path/filename.mp3")
# sound.export("/full/path/filename.wav", format="wav")
sound = AudioSegment.from_mp3("/Users/hung/Downloads/mp3totext-master/input.mp3")
sound.export("/Users/hung/Downloads/mp3totext-master/output.wav", format="wav")



