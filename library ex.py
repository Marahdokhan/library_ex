# option A 2 dictionaries

class LibraryManagementSystem:
    def __init__(self):
        self.books_by_title = {}
        self.books_by_author = {}

    def add_book(self, title, authors, genre, publication_year, isbn=None, copies=1):
        # Create book details dictionary
        book_details = {
            "Title": title,
            "Authors": authors,
            "Genre": genre,
            "Publication Year": publication_year,
            "ISBN": isbn,
            "Copies": copies
        }
        
        # Add to title dictionary
        self.books_by_title[title.lower()] = book_details
        
        # Add to author dictionary
        for author in authors:
            if author.lower() not in self.books_by_author:
                self.books_by_author[author.lower()] = []
            self.books_by_author[author.lower()].append(book_details)

    def find_book_by_title(self, title):
        return self.books_by_title.get(title.lower(), "Book not found.")

    def find_books_by_author(self, author):
        return self.books_by_author.get(author.lower(), "No books found for this author.")

# Example usage
library = LibraryManagementSystem()

# Add books
library.add_book("The Great Gatsby", ["F. Scott Fitzgerald"], "Fiction", 1925, "1234567890", 5)
library.add_book("To Kill a Mockingbird", ["Harper Lee"], "Fiction", 1960, "0987654321", 3)

# Search books
print(library.find_book_by_title("The Great Gatsby"))
print(library.find_books_by_author("Harper Lee"))



# option B 2 tries
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.books = []  # Store book details at the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, book_details):
        current = self.root
        for char in word.lower():
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
        current.books.append(book_details)

    def search(self, prefix):
        current = self.root
        for char in prefix.lower():
            if char not in current.children:
                return []  # No matches found
            current = current.children[char]
        return self._collect_books(current)

    def _collect_books(self, node):
        results = []
        if node.is_end_of_word:
            results.extend(node.books)
        for child in node.children.values():
            results.extend(self._collect_books(child))
        return results

class LibraryManagementSystem:
    def __init__(self):
        self.title_trie = Trie()
        self.author_trie = Trie()

    def add_book(self, title, authors, genre, publication_year, isbn=None, copies=1):
        # Create book details dictionary
        book_details = {
            "Title": title,
            "Authors": authors,
            "Genre": genre,
            "Publication Year": publication_year,
            "ISBN": isbn,
            "Copies": copies,
        }
        
        # Add to title trie
        self.title_trie.insert(title, book_details)
        
        # Add to author trie
        for author in authors:
            self.author_trie.insert(author, book_details)

    def find_books_by_title(self, title_prefix):
        return self.title_trie.search(title_prefix)

    def find_books_by_author(self, author_prefix):
        return self.author_trie.search(author_prefix)

# Example usage
library = LibraryManagementSystem()

# Add books
library.add_book("The Great Gatsby", ["F. Scott Fitzgerald"], "Fiction", 1925, "1234567890", 5)
library.add_book("To Kill a Mockingbird", ["Harper Lee"], "Fiction", 1960, "0987654321", 3)
library.add_book("The Grapes of Wrath", ["John Steinbeck"], "Fiction", 1939, "1122334455", 2)

# Search by title
print("Books matching 'The':", library.find_books_by_title("The"))

# Search by author
print("Books by authors matching 'Harper':", library.find_books_by_author("Harper"))
