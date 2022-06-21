class Game:

    def __init__(self) :
      while True:
            print('''
            welcome
                1) Multiple table game
                2) Words-count game
                3) To exit game
            ''')

            choise=input("choise number: ")
            if choise=='3':
                break

            if int(choise)==1:
                start=int(input("enter start "))
                end=int(input("enter end "))
                ms=int(input("enter ms "))
                mstop=int(input("enter mstop "))
                self.multiple_tables(start,end,ms,mstop)
            elif int(choise)==2:
                Sentence=input("enter Sentence : ")
                print(self.count_words(Sentence))
            play_agin=input("To play agin press any key to exit press 'x': ")
            if play_agin=='x':
                break

    def multiple_tables(self,start,end,ms,mstop):
    
            for i in range(start,end+1):
                for n in range(ms,mstop+1):
                    print(f"{i} x {n} = {i*n}")
                print("-------------")
    
    def count_words(self,Sentence):
        word_count= len(Sentence.split())

        return f" the number of words in Sentence is {word_count}"


# x=Game() delete comment and run code 