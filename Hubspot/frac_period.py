def convert(numerator, denominator):
    result_lst = [str(numerator // denominator) + "."]
    remainders = [numerator % denominator]
    numerator %= denominator

    # long division
    while numerator != 0:
        numerator *= 10
        quotient, numerator = divmod(numerator, denominator)
        result_lst.append(str(quotient))

        if numerator not in remainders:
            remainders.append(numerator)
        else:
            # period detected
            result_lst.insert(remainders.index(numerator) + 1, "(")
            result_lst.append(")")
            break

    return "".join(result_lst)


if __name__ == '__main__':
    # print(convert(1, 97))
    # exit(0)
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
