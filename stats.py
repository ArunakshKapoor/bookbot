def get_book_string(filepath):
    with open(filepath) as f:
        book_contents = f.read()
        return book_contents

def get_num_words(filepath):
    with open(filepath) as f:
        book_contents = f.read()
        words = book_contents.split()
        return len(words)
    
def get_char_count(book_contents):
    book = book_contents.lower()
    char_counter = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for i in char_counter.keys():
        for j in book:
            if i == j:
                char_counter[i] += 1
    return char_counter

def dict_sorter(dictionary):
    def sort_on(dictionary):
        return dictionary["num"]
    final_dict = []
    for i in dictionary.keys():
        temp_dict = {}
        temp_dict["char"] = i
        temp_dict["num"] = dictionary[i]
        final_dict.append(temp_dict)
    
    final_dict.sort(reverse=True, key=sort_on)
    return final_dict