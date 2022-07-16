
words=input("enter string : ")

def frequency_word(words):
    words= words.split(' ')
    unique_word=list(dict.fromkeys(words))
    for c in  unique_word:
        count_word=words.count(c)

        print(f"the frequency of {c}= {count_word} ")

frequency_word(words)

