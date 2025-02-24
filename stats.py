
def get_book_text(path):
    try:
        with open(path) as f:
            file_contents = f.read()
    except FileNotFoundError:
        return f"{path} not found"
    return file_contents

def get_num_words(path):
    counter = 0
    bookContent = get_book_text(path)
    wordCounter = bookContent.split()
    for i in wordCounter:
        counter += 1
    print(f"Found {counter} total words")

def characterCounter(path):
    char_count={}
    bookSubCounter = get_book_text(path)
    for char in bookSubCounter.lower():
        if char in char_count:
            char_count[char] += 1
        else:
             char_count[char] = 1
    for char, count in char_count.items():
        print(f"{char}: {count}s")