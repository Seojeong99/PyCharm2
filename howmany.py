
count1 = 0
def count():
    global count1
    count1 = count1 + 1



with open("onlynoun.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
            try:
                count(data)
            except: 0

print(count1)