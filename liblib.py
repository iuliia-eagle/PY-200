import json


def load_json(file):
    catalog = []
    with open(file, 'r') as f:
        catalog = json.load(f)
    return catalog


def save(catalog, file):
    with open(file, 'w') as f:
        json.dump(catalog, f)
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