n = str(input(''))
print('ok' if n[0].isupper() and n[1:].islower() and not any(h.isdigit() for h in n) else 'error')
