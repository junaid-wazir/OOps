class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.price:.2f}"
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_price(self):
        return self.price
    def set_title(self, title):
        self.title = title
    def set_author(self, author):
        self.author = author
    def set_price(self, price):
        self.price = price
if __name__ == "__main__":
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    price = float(input("Enter the book price: "))

    book1 = book(title, author, price)
    print("\n--- Book Details ---")
    print(book1)

    new_price = float(input("Enter the new price: "))
    book1.set_price(new_price)
    print("\n--- Updated Book Details ---")
    print(book1)