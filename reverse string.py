

def reverse(s):
    if s == "":
        return s

    else:

        return reverse(s[1:]) + s[0]


s = "abcde"

print(reverse(s))
