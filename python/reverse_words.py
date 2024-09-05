def reverse_words(text):
    l = text.split(' ')
    for i in range(len(l)):
        print(l[i][::-1])
        #print(l[i][::-1])
        l[i] = l[i][::-1]
    #return ' '.join(l)
    return l


print(reverse_words("double  spaced  words"))


