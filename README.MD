### Chardet application (a lib developed for encoding detection)

- The main idea is to show how to use this library for dealing with text files with different kinds of encoding.
- There are 6 .txt files inside the 'Files' folder
- The validation.py script iterates through each file inside the 'Files' folder for detecting the properly encoding.

Expected Output:
> Filename: file_guide.csv | Encoding:utf-8 | Confidence: 0.7525 | 
Filename: yan.txt | Encoding:Big5 | Confidence: 0.99 | 
Filename: die.txt | Encoding:utf-8 | Confidence: 0.99 | 
Filename: olaf.txt | Encoding:windows-1251 | Confidence: 0.99 | 
Filename: portugal.txt | Encoding:ISO-8859-1 | Confidence: 0.73 | 
Filename: shisei.txt | Encoding:UTF-8-SIG | Confidence: 1.0 | 
Filename: harpers.txt | Encoding:ascii | Confidence: 1.0 | 

- The file_guide.csv contains info about the .txt files summarised.
- The requirements.txt is used for importing libraries used in this project.
- The .venv folder contains everything about the virtual enviroment.
- The archive.zip file contains all the .txt files zipped.
- For further information about the files, visit the [Kaggle Repository ](https://www.kaggle.com/datasets/rtatman/character-encoding-examples "Kaggle Repository ")

Further information in [Official Chardet Documentation](https://chardet.readthedocs.io/en/latest/index.html# "Official Chardet Documentation"). 
