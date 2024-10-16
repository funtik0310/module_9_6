def all_variants(text):
    w = len(text)
    for i in range(1, w + 1):
        for j in range(w - i + 1):
            yield text[j:j + i]

a = all_variants("abc")
for i in a:
    print(i)