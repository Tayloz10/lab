
class Book:
    def __init__(self, title = "None", author = "None", publisher = " None", copyright = "None"):
        self.title = title
        self.aurthor = author
        self.publisher = publisher
        self.copyright = copyright
    def __srt__(self):
        return ('Title {} \nAuthor {}\nPublisher {}\nCopyright {}' . format(self.title, self.author, self.publisher, self.copyright))

    def library():
        title = []
        author = []
        publisher = []
        copyright = []
        with open('books.txt', 'r') as file:
            i = 0
            for line in file:
                books = line.split('\n')
                return books
            while i < len(books()):
                if i % 1 == 0:
                    title.append(file[i])
                if i % 2 == 0:
                    author.append(file[i])
                if i % 3 == 0:
                    publisher.append(file[i])
                if i % 4 == 0:
                    copyright.append(file[i])
                i =+ 1
        print("The library has {} books" .format(i/4))
        j = 0
        while j < ((len(books)/4)):
            print("Title: {}" .format(title[i]))
            print("Author: {}" .format(author[i]))
            print("Publisher: {}" .format(publisher[i]))
            print("Copyright: {}" .format(copyright[i]))
            print()
            j += 1

if __name__ == "__main__":
   Book.library()


