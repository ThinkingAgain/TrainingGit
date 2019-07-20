s = "loveleetcode"
a = list(set(s))
a.sort(key=s.index)
for x in a:
    if s.count(x) == 1:
        print(s.index(x))
print(a)
