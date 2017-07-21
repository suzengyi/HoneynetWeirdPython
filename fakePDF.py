# encoding = utf-8

with open('./fakePDF.pdf', 'wb') as f:
    for each in range(0xff + 1):
        f.write(bytes([each]))