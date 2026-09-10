"""FizzBuzz. Intentionally imperfect — see the repo's open issues."""


def fizzbuzz(n):
    out = []
    # BUG: off-by-one, this stops at n-1 instead of n.
    for i in range(1, n):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


if __name__ == "__main__":
    print("\n".join(fizzbuzz(20)))
