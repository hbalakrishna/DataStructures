ret = [0]
str_ = "abcaby"

def patMatch(pattern):
    for i in range(1, len(str_)):
        j = ret[i - 1]
        while j > 0 and str_[i]!=str_[j]:
            j = ret[j-1]
        ret.append(j + 1 if str_[i] == str_[j] else j)
    return ret

def subString():
    string = "abcabxabcaby"
    pattern, result,j = patMatch(str_), [],0

    for i in range(len(string)):
        while j>0 and string[i]!=str_[j]:
            j = pattern[j-1]
        if string[i]==str_[j]:
            j += 1
        if j == len(pattern):
            result.append(i - (j - 1))
    return result

print(subString())


for i in range(4-1,0,-1):
    print(i)