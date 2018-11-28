text = '... «наивный» - <есть> натуральный, природный, не обработанный искусственными условностями цивилизации. Так что если наша культура есть продолжение природы, её язык (по распространенному мнению философов), её заявление о себе, то в наивном человеке и его слове - это прямейше, спонтанно, без опосредованных звеньев...  — Георгий Гачев, «Плюсы и минусы наивного философствования»'
def clear_text(text, trash_tokens):
    text = text.strip(trash_tokens)
    return text
def get_words(text):
    tokens = text.split()
    trash_tokens = '+=_-?/\><@"\'\#\*'
    good_tokens = []
    for token in tokens:
        clean_token = clear_text(token, trash_tokens)
        if clean_token != '':
            clean_token = clean_token.lower()
            good_tokens.append(clean_token)
    return good_tokens

print(get_words(text))

def find_quotes(input_word, all_quotes, all_quotes_words):
    result = []
    for i, quote in enumerate(all_quotes):
        if input_word in all_quotes_words[i]:
            result.append(quote)
    return result

def main():
    filename = 'quotes.txt'
    DASH = '—'
    all_quotes = []
    all_quotes_words = []
    list_of_authors = []
    with open(filename, encoding = 'utf-8') as fid:
        for line in fid:
            parts = line.split(DASH)
            quote = parts[0].strip()
            author = parts[1].strip()
            quote_words = get_words(quote)
            all_quotes.append(quote)
            all_quotes_words.append(quote_words)
    while True:
        input_word = input('Word? ')
        if input_word == '':
            break
        input_word = input_word.strip().lower()
        found = find_quotes(input_word, all_quotes, all_quotes_words)
        if len(found) == 0:
            print('Nothing found')
        else:
            for quote in found:
                print(quote)
if __name__ == '__main__':
    main()
