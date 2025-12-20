import whisper
import os
import subprocess
import sys
# Encoding fix for Windows
sys.stdout.reconfigure(encoding='utf-8')


files = os.listdir("Course_Videos")
for file in files:
    tutorial_number = file.split('-')[0].strip()
    file_name = file.split('-')[1].strip().split('｜')[0].strip()
    print(tutorial_number,file_name)
    subprocess.run(['ffmpeg', '-i', f"Course_Videos/{file}", f"audio/{tutorial_number}_{file_name}.mp3"])