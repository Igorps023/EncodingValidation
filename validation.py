# %%
import os
import chardet
from chardet.universaldetector import UniversalDetector
from pathlib import Path

pathway = os.path.join(os.getcwd(), 'Files') #Relative Path
files = os.listdir(pathway)
bytes_to_read = 1024 * 10


for file in files:
    detector = UniversalDetector()
    detector.reset()
    with open( os.path.join(pathway, file), 'rb') as f:
        content = f.read(bytes_to_read)
        detector.feed(content)
        detector.close()
        print(f'Filename: {file} | Encoding:{detector.result["encoding"]} | Confidence: {detector.result["confidence"]}')
    detector.reset()