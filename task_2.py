# TODO Найдите количество книг, которое можно разместить на дискете
capacity = 1.44
number_of_pages = 100
number_of_lines = 50
number_of_characters = 25
capacity_for_one_character = 4

bytes_in_kilobyte = 1024

capacity_per_book = capacity_for_one_character*(number_of_characters *number_of_lines *number_of_pages)/(bytes_in_kilobyte*bytes_in_kilobyte)

number_of_books = round(capacity/capacity_per_book)
print("Количество книг, помещающихся на дискету:", number_of_books)
