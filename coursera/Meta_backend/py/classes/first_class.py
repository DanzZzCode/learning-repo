class MyFirstClass:
    
    index = "Author-Book"
    def __init__(self):
        print("Who wrote this?")


    def hand_list(self, philosopher , book):
        print(MyFirstClass.index)
        print(f"{philosopher} wrote the book: {book}")

whodunnit = MyFirstClass()

whodunnit.hand_list("Sun Tzu", "The Art Of War")