# Recreating the bruteforce algorithm in python
# Discrepancy: In official solution, 160 is counted as having 16 '1's.
# TODO: figure this out


def countDigitOne(n: int):
    c = 0
    for i in range(1, n + 1):
        nstr = str(i)
        occurrences = nstr.count("1", 0, len(nstr))
        c += occurrences
        print(occurrences, i)
    return c


target = input("enter digit 0 < n < 10^9:\n")
print(countDigitOne(int(target)))
