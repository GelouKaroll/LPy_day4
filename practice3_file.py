strlen  = 0
words   = 0
new_text = ''

with open('referat.txt', 'r', encoding='utf-8') as f:
    f = f.read()    
    strlen = len(f)

    words = f.split()
    words = len(words)

    new_text = f.replace(',', '!')

with open('report.txt', 'w', encoding='utf-8') as newf:
    msg = 'total lines is : {}\ntotal words is : {}\nhere is new text:\n{}'.format(strlen, words, new_text)
    newf.write(msg)

