 class book:
    def __init__(self,name,age,author,price,classification):
        self.book_name = name
        self.book_age = age
        self.book_author = author
        self.book_price = price
        self.book_classification = classification
        

        
    def add_book(self):
            print("Name: " + self.book_name)   
            print("Release Date: " + str(self.book_age))   
            print("Author: " + self.book_author)
            print("Price: " + self.book_price)   
            print("Type: " + self.book_classification)
            print("Book Added")
            
            
            
 book1 = book("The Theory of Everything","10-5-2002","Stephen Hawking","200 INR","Science Fiction")
 book1.add_book()
 
 book2 = book("The Diary of A Young Girl","15-7-1995","Anne Frank","450 INR","Autobiography")
 book2.add_book()

 book3 = book("Why","15-7-2015","National Geographic","500 INR","Encyclopedia")
 book3.add_book()
