class Book:
    def __init__(self, name, price, description, author):
        self.name = name
        self.price = price
        self.description = description
        self.author = author

    def __str__(self):
        return f"Book Name: {self.name}\nAuthor: {self.author}\nPrice: ${self.price}\nDescription: {self.description}\n"


class Library:
    def __init__(self):
        self.books = []
        self.load_sample_books()

    def load_sample_books(self):
        sample_books = [
            Book("Rich Dad Poor Dad", "12.99", "A personal finance classic.", "Robert T. Kiyosaki"),
            Book("Atomic Habits", "16.50", "An easy & proven way to build good habits.", "James Clear"),
            Book("The 48 Laws of Power", "18.00", "A guide to power dynamics.", "Robert Greene"),
            Book("The Subtle Art of Not Giving a F*ck", "15.20", "Counterintuitive self-help.", "Mark Manson"),
            Book("Think and Grow Rich", "11.99", "A timeless motivational book.", "Napoleon Hill"),
            Book("To Kill a Mockingbird", "10.99", "Classic novel on justice and race.", "Harper Lee"),
            Book("Sherlock Holmes Vol. 1", "9.50", "Detective tales with Holmes.", "Arthur Conan Doyle"),
            Book("Sherlock Holmes Vol. 2", "9.50", "More thrilling mysteries.", "Arthur Conan Doyle"),
            Book("Sherlock Holmes Vol. 3", "9.50", "Continued adventures.", "Arthur Conan Doyle"),
            Book("Gone Girl", "13.00", "A psychological thriller.", "Gillian Flynn"),
            Book("The Girl with the Dragon Tattoo", "14.00", "Murder mystery meets tech.", "Stieg Larsson"),
            Book("Educated", "13.75", "A memoir about breaking free from ignorance.", "Tara Westover"),
            Book("Sapiens", "19.90", "A brief history of humankind.", "Yuval Noah Harari")
        ]
        self.books.extend(sample_books)

    def add_book(self):
        name = input("Enter book name: ")
        price = input("Enter book price: ")
        description = input("Enter book description: ")
        author = input("Enter book author: ")
        book = Book(name, price, description, author)
        self.books.append(book)
        print("Book added successfully!\n")

    def view_books(self):
        if not self.books:
            print("No books in the library.\n")
        else:
            print("\nBooks in the library:\n")
            for book in self.books:
                print(book)

    def remove_book(self):
        name = input("Enter the book name to remove: ")
        for book in self.books:
            if book.name.lower() == name.lower():
                self.books.remove(book)
                print("Book removed successfully!\n")
                return
        print("Book not found.\n")

    def search_book(self):
        name = input("Enter the book name to search: ")
        for book in self.books:
            if book.name.lower() == name.lower():
                print("Book found:\n")
                print(book)
                return
        print("Book not found.\n")


def main():
    library = Library()
    while True:
        print("Library Menu:")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Remove a Book")
        print("4. Search a Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.remove_book()
        elif choice == "4":
            library.search_book()
        elif choice == "5":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
