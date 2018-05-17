true_length = 5
str_ = 'i am '
sc = 0

for i in range(true_length):
    if i == ' ':
        sc = sc + 1

idx = true_length + sc * 2

for i in range(true_length,0,-1):
    if str_[i] == ' ':
        str_[idx - 1] = '0'
        str_[idx - 2] = '2'

