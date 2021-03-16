import re
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def letcut(string):

    size = len(string)
    final_str = string[size - 1:]
    print(final_str)  #마지막글자 자르기
    sp_list = list(final_str)
    result = []
    for keyword in sp_list:
        if re.match('.*[ㄱ-ㅎ ㅏ-ㅣ 가-힣]+.*',keyword) is not None:
            print("if는 들어감")
            char_code = ord(keyword) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            result.append(CHOSUNG_LIST[char1])
            print('초성 : {}'.format(CHOSUNG_LIST[char1]))#초성

            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            result.append(JUNGSUNG_LIST[char2])
            print('중성 : {}'.format(JUNGSUNG_LIST[char2]))#중성

            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            result.append(JONGSUNG_LIST[char3])
            print('종성 : {}'.format(JONGSUNG_LIST[char3]))

        else:
            print("if안들어감")
            result.append(keyword)

    print("".join(result))

    if JONGSUNG_LIST[char3] == ' ':
        print("없어")
    else:
        print("있어")



#word = ['낄끼빠빠', '아아', '맛있냥', '멀라염', '뻐카충']
#for i in word:
#    letcut(i)


#letcut("안녕하세요")
with open("letscut.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
         try:
             data=data.replace("\n", "")
             letcut(data)
         except:0

