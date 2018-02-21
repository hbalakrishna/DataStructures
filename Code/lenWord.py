s = 'Hi How are'
if not s.strip():
    print("empty")
else:
    a = s.split()
    print(len(a[-1]))