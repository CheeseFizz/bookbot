def count_words(text:str):
    words = text.split()
    return len(words)

def count_chars(text:str):
    chars = {}
    for char in text.lower():
        if char.isspace():
            try:
                chars['space'] += 1
            except KeyError:
                chars['space'] = 1
        else:
            try:
                chars[char] += 1
            except KeyError:
                chars[char] = 1
    return chars

def sort_on_Count(dict:dict):
    return dict["count"]

def make_char_list(charCounts:dict):
    charList = []
    for key in charCounts:
        if key.isalpha() and key != 'space':
            charList.append({'char':key, 'count':charCounts[key]})
    charList.sort(key=sort_on_Count, reverse=True)
    return charList