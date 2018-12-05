with open('test.html') as fobj:
    aset = set(fobj)
    with open('uu.txt') as fobj:
        bset = set(fobj)
        with open('diff.txt', 'w') as fobj:
            print(aset)
            fobj.writelines(bset - aset)

