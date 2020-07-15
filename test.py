import liblib as lib
import json


def main():
    catalog = []
    command = " "
    print("Print help to list commands")

    while command != "exit":
        command = input("Enter command:")
        if command == "help":
            print("load - to open catalog,\n"
                  "save - to save catalog to file,\n"
                  "add - to add file to catalog,\n"
                  "delete - to delete file from catalog,\n"
                  "search - to search book by author(A) or by title(T) in catalog,\n"
                  "exit - to exit.")


        if command == 'load':
            filename = input("\nEnter filename:")
            catalog = lib.load_json(filename)
        if command == 'save':
            filename = input("\nEnter filename:")
            lib.save(catalog, filename)
        if command == 'add':
            author = input("\nEnter author:")
            title = input("\nEnter book title:")
            lib.addbook(catalog, author, title)
        if command == 'delete':
            author = input("\nEnter author:")
            title = input("\nEnter book title:")
            oldbook = {'author': author,
                       'title': title}
            lib.delete(catalog, oldbook)
        if command == 'search':
            key = input("Enter A to search by author, enter T to search by title:")
            if key == "A":
                result = lib.search(catalog, "author", input("Enter author:"))
                print(result)
            if key == "T":
                result = lib.search(catalog, "title", input("Enter title:"))
                print(result)


if __name__ == "__main__":
    main()


