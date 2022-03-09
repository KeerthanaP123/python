class publisher():
    def __init__(self,name1):
        self.name=name1
    def display(self):
        pass
class book(publisher):
    def __init__(self,title1,author1,name1):
        self.title=title1
        self.author=author1
        publisher.__init__(self,name1)
    def display(self):
        pass
class python(book):
    def __init__(self,price,no_p,title1,author1,name1):
        self.price=price
        self.no=no_p
        book.__init__(self,title1,author1,name1)
    def display(self):
        print("Book Title",self.title)
        print("Author Name",self.author)
        print("Publisher",self.name)
        print("Price",self.price)
        print("no_p",self.no)
title=input("Enter titile")
author=input("Enter author")
name=input("Enter publisher")
price=int(input("Enter price:"))
no_of_pages=int(input("Enter no of pages"))
p1=python(price,no_of_pages,title,author,name)
p1.display()
