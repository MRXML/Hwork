w = {
    'hello': 'привет',
    'goodbye': 'до свидания',
    'cat': 'кошка',
    'dog': 'собака'
}
s = ''
while s != 'stop':
    s = input('')
    if s not in w:
        print('Error')
    else:
        print(w[s])