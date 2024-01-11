import subprocess
import speech_recognition as sr
import os
import split_file
# import mp3towav
from split_file import *
import sys 
import tkinter as tk
from tkinter import messagebox

filename_txt_path = "/Users/hung/Documents/GitHub/AmazonTranscribeApp/texts/filename.txt"

# Hàm chuyển đổi từ MP4 sang WAV
def convert_mp4_to_wav(mp4_file, wav_file):
    subprocess.run(["ffmpeg", "-i", mp4_file, "-ac", "1", "-ar", "16000", wav_file])

# Assume 'counter' is defined somewhere in your code

for x in range(1, counter):
    filenameupload = ""
    # Đọc dữ liệu từ file
    try:
        with open(filename_txt_path, 'r') as file:
            filenameupload = file.read().strip()
            print('Content of filename.txt:', filenameupload)

    except FileNotFoundError:
        print('filename.txt not found.')
    except Exception as e:
        print(f'Error reading filename.txt: {e}')

    mp4_file_path = "/Users/hung/Documents/GitHub/AmazonTranscribeApp/uploads/{filename}".format(filename=filenameupload)
    wav_file_path = "/Users/hung/Documents/GitHub/AmazonTranscribeApp/uploads/input_converted.wav".format(x)

    # Chuyển đổi từ MP4 sang WAV
    convert_mp4_to_wav(mp4_file_path, wav_file_path)

    # Sử dụng thư viện speech_recognition để nhận dạng giọng nói
    r = sr.Recognizer()

    try:
        with sr.AudioFile(wav_file_path) as source:
            audio = r.record(source)
        result = r.recognize_google(audio)

        # Xóa file output.txt cũ nếu tồn tại
        output_file_path = "/Users/hung/Documents/GitHub/AmazonTranscribeApp/texts/output.txt"
        if os.path.exists(output_file_path):
            os.remove(output_file_path)
            print("Old output.txt has been deleted.")

        # Tạo file output.txt mới
        with open(output_file_path, "w") as new_file:
            new_file.write("")  # Ghi một dòng trắng để tạo file mới

        # Tiếp tục với việc ghi dữ liệu vào file mới
        with open(output_file_path, "a") as f:
            f.write(result + '\n')
            print("New output.txt has been created.")
            print("%d. audio file is done." % (x,))

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Xóa tệp WAV đã chuyển đổi
    if os.path.exists(wav_file_path):
        os.remove(wav_file_path)
    else:
        print("The file does not exist")


# print("Files are deleted.")
# Tạo một cửa sổ
root = tk.Tk()
root.withdraw()  # Ẩn cửa sổ chính

# Hiển thị thông báo pop-up
messagebox.showinfo("Thông báo", "Process completed.")

# Đóng cửa sổ chính (nếu không đóng, cửa sổ sẽ hiển thị nhưng ẩn)
root.destroy()
print("Process completed.")