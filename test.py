def fast(x, y):
    print("="*10)
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)), len(str(y)))
        m = n//2

        a = x//10**m
        print(f"a {a}")
        b = x % 10**m
        print(f"b {b}")
        c = y//10**m
        print(f"c {c}")
        d = y % 10**m
        print(f"d {d}")

        k = fast(a, c)
        print(f"k {k}")
        n = fast((a+b), (c+d))
        print(f"n {n}")
        o = fast(b, d)
        print(f"o {o}")

        return (10**2*m*k) + (10**m*(n-k-o))+(o)


print(fast(10515610, 5651551460))
