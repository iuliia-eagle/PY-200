

def load(file):
    catalog = []
    with open(file, 'r') as f:
        for line in f:
            splitline = line.split("; ")
            catalog.append({'author': splitline[0], 'title': splitline[1]})
        print(catalog)
    return catalog


def save(catalog, file):
    with open(file, 'w') as f:
        for entry in catalog:
            f.write(entry['author'] + '; ' + entry['title'] + '\n')
    return


def addbook(catalog, author, title):
    catalog.append({'author': author, 'title': title})
    return


def search(catalog, parameter, value):
    result = []
    for entry in catalog:
        if entry[parameter] == value:
            result.append(entry)
    return result


def delete(catalog, book):
    catalog[:] = [entry for entry in catalog
                  if entry.get('author') != book['author'] and entry.get('title') != book['title']]
    return catalog


def editbook(book, parameter, newvalue):
    book[parameter] = newvalue
    return book