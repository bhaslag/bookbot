def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for char in text:
        if char.lower() not in letters:
            letters[char.lower()] = 1
        else:
            letters[char.lower()] += 1
    
    return letters

def sort_on(dict):
    return dict['num']

def descending(letter_dict):
    list_of_dict =  []
    for letter in letter_dict:
        list_of_dict.append({'char': letter, 'num': letter_dict[letter]})
    # print (list_of_dict.sort(key=sort_on, reverse=True))
    list_of_dict.sort(key=lambda x: x['num'], reverse=True)

    return list_of_dict