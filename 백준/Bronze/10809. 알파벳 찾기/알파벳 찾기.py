# 알파벳 리스트 생성
from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)

s = input()
for i in alphabet_list :
    print(s.find(i),end = ' ')