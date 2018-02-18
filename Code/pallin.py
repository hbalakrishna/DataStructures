a = "A man a plan a canal Panama"
print(a[::-1].lower() == a.lower())
print(a[::-1].lower())
print(a.lower())

b = ''.join(e for e in a if e.isalnum())
print(b[::-1].lower() == b.lower())