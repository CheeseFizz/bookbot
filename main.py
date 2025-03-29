import sys
from pathlib import Path
from stats import count_words, count_chars, make_char_list

def get_book_text(book):
    with open(book,'r') as f:
        content = f.read()

    return content



    

def main():
    root_dir = Path(__file__).resolve().parent
    content = get_book_text(f"{root_dir}/{sys.argv[1]}")
    wordCount = count_words(content)
    charCounts = count_chars(content)
    sortedCharList = make_char_list(charCounts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")
    for charDict in sortedCharList:
        print(f"{charDict['char']}: {charDict['count']}")
    


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()