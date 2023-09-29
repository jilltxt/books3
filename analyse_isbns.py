    """Loads and standardizes ISBNs from a text file.
    The idea is to add functions to filter out ISBNS from specific
    countries, and to fetch book details (author, title), maybe using 
    the Google Books API or something else.
    Currently just prints the valid ISBNs.
    """

def load_isbns_from_file(filename):
    with open(filename, 'r') as file:
        isbns = file.readlines()[5:]
        return isbns
        
def standardize_isbn(isbn):
    """Standardize each ISBN by removing spaces and hyphens and adding 
    "978" prefix if ISBN has only 10 digits."""

    isbn = isbn.replace(' ', '').replace('-', '').strip()
    if len(isbn) == 10:
        isbn = '978' + isbn
    return isbn

def filter_valid_isbns(isbns):
    return [isbn for isbn in isbns if len(isbn) == 13]

def main(filename):
    """Load and standardize ISBNs from text file"""
    isbns = load_isbns_from_file(filename)
    standardized_isbns = [standardize_isbn(isbn) for isbn in isbns]
    valid_isbns = filter_valid_isbns(standardized_isbns)
    return valid_isbns
    
def filter_norwegian_isbns(isbns):
    main(filename)
    return [isbn for isbn in valid_isbns if isbn[3:5] == '82']

if __name__ == "__main__":
    filter_norwegian_isbns("test.txt")
