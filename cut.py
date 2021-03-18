from main import Jaccard_similarity


def similarity(s):
    if s >= 0.1:
        print("1")
    else:
        print("0")



str1="안녕하세요"
str2="안녕"
sim = Jaccard_similarity(str1, str2)
print(sim)
similarity(sim)