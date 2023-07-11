def n(a):
    s = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    }

    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety',
    }

    d, c = map(int, a.split(','))
    r = ''
    if d >= 1000:
        r += f'{s[d // 1000]} thousand '
        d %= 1000
    if d >= 100:
        r += f'{s[d // 100]} hundred '
        d %= 100
    if d >= 20:
        r += f'{s[d // 10]} '
        d %= 10
    if d > 0:
        r += f'{s[d]} '
    r += 'dollars\n'
    if c >= 20:
        r += f'{tens[c // 10]} '
        c %= 10
    if c > 0:
        r += f'{s[c]} '
    return r
amount = (str(input()))
print(n(amount))