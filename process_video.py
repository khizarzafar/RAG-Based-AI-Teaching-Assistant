# import whisper
import sys
sys.stdout.reconfigure(encoding='utf-8') #encoding error fix

import os

files = os.listdir("Course_Videos")
for file in files:
    tutorial_number = file.split('-')[0].strip()
    file_name = file.split('-')[1].strip().split('｜')[0].strip()
    print(tutorial_number,file_name)