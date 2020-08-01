from words import all_words

max_len = 0

for i in all_words:
    if len(i) > max_len:
        max_len = len(i)

print(max_len)

            