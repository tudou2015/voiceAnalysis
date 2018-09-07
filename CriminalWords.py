import psycopg2
from pprint import pprint
from speechToText import *
import requests
from collections import Counter


APP_ACCESS_TOKEN = 'P637HVIWSHN73DKHIB2SPGVTKLVRZWSI'

base_url = 'https://api.wit.ai/speech'


class CriminalWords:

    def read_audio(file_path):
        # function to read audio(wav) file
        with open(file_path, 'rb') as f:
            audio = f.read()
        return audio



    def convert_speech_to_text(self):

        file = "/Users/raneem/Desktop/voice/2.wav"
        audio = read_audio(file)
        headers = {'authorization': 'Bearer ' + APP_ACCESS_TOKEN,
               'Content-Type': 'audio/wav'}
        data_response = requests.post(base_url, headers=headers, data=audio).json()

        return data_response['_text']


    # Connect to the database
    def __init__(self):
        try:
            self.conniction = psycopg2.connect(
                "dbname= 'sample_db' user='raneem' host='localhost' password='123456' port='5432'")
            self.conniction.autocommit = True
            self.cursor = self.conniction.cursor()

        except:
            pprint("Cannot connect to database")


    def find_criminal_words(self):

        text = self.convert_speech_to_text()

        # Spilt text into words
        try:
            print(text)  # print the text
            wordList = text.split(" ")  # split text into words


            for words in wordList:
                print(words)

            # detect the criminal words
            wordfreq = []
            try:
                print("The criminal words were detected are: ...")
                for i in range(len(wordList)):
                    self.cursor.execute("SELECT name FROM pet WHERE name = '%s'" % wordList[i])

                    for row in self.cursor:
                        row == ""
                        print(row)
                        counts = Counter(row).most_common(1)
                        print(counts)

            except:
                print("No criminal words detect...")

        except:
            print("Error")


if __name__ == '__main__':
    criminal_Words = CriminalWords()

    criminal_Words.find_criminal_words()