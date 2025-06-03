from stats import word_count, character_count, get_book_text, sorted_part
import sys


def main():

    input = sys.argv[1]

    book_content = get_book_text(input)

    num_words = word_count(book_content)

    num_char = character_count(input)

    sorted_num_char = sorted_part(input)


    print(f"============ BOOKBOT ============ " 
    f"\n Analyzing book found at {input} " 
    f"\n ----------- Word Count ----------"
    f"\n Found {num_words} total words"
    f"\n --------- Character Count -------"
    )
    for dictionary in sorted_num_char:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: 
    main()