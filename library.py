import os
os.open('books.py', os.O_RDONLY)
class Book:
    def __init__(self, title = "None", author = "None", publisher = " None", copyright = "None"):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.copyright = copyright
    def __str__(self):
        return ('Title {} \nAuthor {}\nPublisher {}\nCopyright {}' . format(self.title, self.author, self.publisher, self.copyright))

    def library():
        title = []
        author = []
        publisher = []
        copyright = []
        with open('books.py', 'r') as file:
            books = file.read()
            split_books = books.split('\n')
            i = 0
            while i < len(split_books()):
                if i % 2 == 0:
                        author.append(file[i])
                if i % 3 == 0:
                        publisher.append(file[i])
                if i % 4 == 0:
                        copyright.append(file[i])
                elif i % 1 == 0:
                    title.append(file[i])
                    i += 1
        print("The library has {} books" .format(i/4))
        j = 0
        while j < ((len(split_books)/4)):
            print("Title: {}" .format(title[j]))
            print("Author: {}" .format(author[j]))
            print("Publisher: {}" .format(publisher[j]))
            print("Copyright: {}" .format(copyright[j]))
            print()
            j += 1

if __name__ == "__main__":
   Book.library()


