def page_count(n, p):
    if p > 1:
        if not(p % 2 == 0):
            p_level = int((p-1)/2)
        else:
            p_level = int(p/2)
    else:
        return 0

    if not(n % 2 == 0):
        n_level = int((n-1)/2)
    else:
        n_level = int(n/2)
    if p_level < n_level - p_level:
        return p_level
    else:
        return n_level - p_level

# HackerRank practice challenge : https://www.hackerrank.com/challenges/drawing-book/problem

numPages = page_count(6,2)
print(numPages)