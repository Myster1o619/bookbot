def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_txt(book_path)
    number_of_words = word_amount(book_contents)
    character_count_dict = char_amount(book_contents)

    list_of_dicts = list_of_dicts_create(character_count_dict)
    modified_list_of_dicts = char_and_amount_list_of_dicts(list_of_dicts)  
    
    modified_list_of_dicts.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print("")
    for val in modified_list_of_dicts:
        print(f"The {val["char"]} character was found {val["amount"]} times")
    print("--- End report ---")


    

def get_book_txt(book_location):
    with open(book_location) as f:
         file_contents = f.read()
    return file_contents

def word_amount(book_contents):
    word_list = book_contents.split()
    return len(word_list)

def char_amount(contents):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    lower_contents = contents.lower()
    char_dict = {}
    for i in ALPHABET:
        char_dict[i] = lower_contents.count(i)
    return char_dict

def list_of_dicts_create(some_dict):
    list_of_dicts = [{key: value} for key, value in some_dict.items()]
    return list_of_dicts

def char_and_amount_list_of_dicts(some_dict):
    result = [{"char": key, "amount": value} for d in some_dict for key, value in d.items()]
    return result

def sort_on(dict):
    return dict["amount"]



main()