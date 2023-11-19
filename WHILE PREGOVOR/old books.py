searched_book = str(input())
books_count = 0
book_name = str(input())
book_found = False
while book_name != "No More Books":
    if book_name == searched_book:
        book_found = True
        break
    books_count += 1
    book_name = input()

if book_found:
    print(f"You checked {books_count} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {books_count} books.")

