def amount(x):
    a = ""
    for item in x:
        if item.isdigit() or item == ".":
            a += item
    return float(a)
def c(data):
    c = {}
    for entry in data:
        parts = entry.split(" ")
        name = " ".join(parts[:-2])
        a = amount(entry)
        cat = parts[-2]
        if cat in c:
            c[cat] += a
        else:
            c[cat] = a
    return c
def name():
    for e in data:
        parts = e.split(" ")
        name = " ".join(parts[:-2])
        return name
with open('text 1.py', 'r') as file:
    data = file.readlines()
total = c(data)

print(f"{name(data)}, spent: ${total:.2f}")