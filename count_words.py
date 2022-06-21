
def count_words(Sentence):
   word_count= len(Sentence.split())

   return word_count



Sentence=input("enter Sentence : ")
print(count_words(Sentence))