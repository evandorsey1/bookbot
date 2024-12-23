def print_report(filepath, text):
    print(f"--- Begin report of {filepath} ---\n")
    count_words(text)
    print("")
    format_character_map(get_character_map(text))
    print("--- End report ---")

def format_character_map(character_map):
    for char in character_map:
        print(f"The {char} character was found {character_map.get(char,0)} times")


def get_character_map(text):
    lowercase_text = text.lower()
    char_map = {}

    for char in lowercase_text:
        if char.isalpha():
            char_map[char] = char_map.get(char, 0) + 1

    return char_map 


def count_words(text):
    number_of_words = 0
    lines = text.split()
    number_of_words += len(lines)

    print(f"{number_of_words} words found in the document")



def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    
    print_report(file_path, file_contents)
    


if __name__ == "__main__":
    main()