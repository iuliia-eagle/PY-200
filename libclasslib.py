class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return self.author + '; ' + self.title

    def edit(self, parameter, value):
        if parameter == 'author':
            self.author = value
        if parameter == 'title':
            self.title = value


class Catalogue:
    def __init__(self, books=[]):
        self.books = books

    def __str__(self):
        cat = ''
        for book in self.books:
            cat += book.__str__()
            cat += '\n'
        return cat

    def addbook(self, book):
        self.books.append(book)

    def search(self, parameter, value):
        result = []
        for entry in self.books:
            if entry[parameter] == value:
                result.append(entry)
        return result

    def delete(self, book):
        self.books[:] = [entry for entry in self.books
                  if entry.get('author') != book['author'] and entry.get('title') != book['title']]

    def save_to_file(self, file):
        with open(file, 'w') as f:
            f.write(self.__str__())

    def load_from_file(self, file):
        with open(file, 'r') as f:
            for line in f:
                splitline = line.split("; ")
                self.books.append(Book(author=splitline[0], title=splitline[1]))