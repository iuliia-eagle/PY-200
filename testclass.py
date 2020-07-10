import libclasslib as libc

book1 = libc.Book(author='Leo Tolstoy', title='War and Peace')

catalogue = libc.Catalogue()
catalogue.load_from_file('libfile.txt')

catalogue.addbook(book1)

catalogue.save_to_file('newfile.txt')
