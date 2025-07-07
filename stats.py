def get_words_from_text(text):
    return len(text.split())


def count_symbols(text):
    symbols = {}
    for ch in text:
        ch = ch.lower()
        if ch in symbols:
            symbols[ch] += 1
        else:
            symbols[ch] = 1
    return symbols


def sort_on(items):
    return items[1]


def sort_items(items_dict):
    sorted_items = sorted(items_dict.items(), reverse=True, key=sort_on)
    return sorted_items
