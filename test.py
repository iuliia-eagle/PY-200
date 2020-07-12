import liblib as lib


newbook = {'author': 'Tolstoy',
           'title': 'War and Peace'}

print(newbook)

# loading catalog from file
catalog = lib.load('libfile.txt')

# adding new book
lib.addbook(catalog, 'Dostoevskiy', 'Crime and Punishment')

# deleting book
oldbook = {'author': "Pushkin",
           'title': "Captain's daughter"}
lib.delete(catalog, oldbook)

# search
print('Found: ' + str(lib.search(catalog, 'author', 'Dostoevskiy')))

# writing catalog to file
lib.save(catalog, 'newfile.json')

# loading from json
newcatalog = lib.load_json('newfile.json')
print(newcatalog)