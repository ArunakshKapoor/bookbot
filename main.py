from stats import get_num_words, get_char_count, get_book_string, dict_sorter
import sys

def main():
    booktext = get_book_string(sys.argv[1])
    x = get_num_words(sys.argv[1])

    y = get_char_count(booktext)

    z = dict_sorter(y)
    # print(y)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {x} total words")
    print("--------- Character Count -------")
    for i in range(len(z)):
        print(f"{z[i]["char"]}: {z[i]["num"]}")
    print("============= END ===============")
    
    return

if len(sys.argv) < 2:
    sys.exit("Usage: python3 main.py <path_to_book>")
else:
    main()