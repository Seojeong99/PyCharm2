from wordcloud import WordCloud
import matplotlib.pyplot as plt
#import Utils.FileManager
from konlpy.tag import Twitter, Okt

nlpy = Okt()
#WRITE_FILENAME = fileName
#f = open('C://Users//kopo//Desktop//abc.txt', 'r', encoding='UTF-8')
#lines = f.readlines()
#f.close()
#for i in range(0, len(lines)):
def picknoun(lines):
    nouns = nlpy.nouns(lines[i])
    print(nouns)

with open("inputfinalplease.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
        try:
            picknoun(data)
        except:
            0