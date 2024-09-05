
#using a hashmap
def first_diplicated_letter_h(s:str):
    dic = {}

    for i in range(len(s)):
        letter = s[i]

        if letter in dic:
            return letter
        dic[letter] = i

#using a set
def first_diplicated_letter_s(s:str):
    seen =  set()
    for i in range(len(s)) :
        if s[i] in seen:
            return s[i]
        seen.add(s[i])

print(first_diplicated_letter_s("abcdeda"))