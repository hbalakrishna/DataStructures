_set = set
row1 = _set('qwertyuiopQWERTYUIOP')
row2 = _set('asdfghjklASDFGHJKL')
row3 = _set('zxcvbnmZXCVBNM')
row_words = []
words = ["Hello", "Alaska", "Dad", "Peace"]
for w in words:
    w_set = _set(w)
    if w_set <= row1 or w_set <= row2 or w_set <= row3:
        print(w_set, row1, row2, row3)
        row_words.append(w)


print(row_words)
