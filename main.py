def main():
    alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    letters = {}
    seen_letters = set()
    with open("/home/misterpiggie/workspace/github.com/MisterPiggie/bookbot/books/frankestein.txt") as f:
        file_contents = f.read()
        count = len(file_contents.split())
        file_contents = file_contents.lower()
    for letter in file_contents:
        if letter in seen_letters:
            letters[letter] += 1
        else:
            letters.update({letter: 1})
            seen_letters.add(letter)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print()
    for letter in letters:
        if letter in alphabet:
            print(f"The '{letter}' character was found {letters[letter]} times")
    print("end report")
main()