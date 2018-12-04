def fake_file(name, size=None):

    if size is None:
        size = 1073741824
    f = open(name,"wb")
    f.seek(size - 1)
    f.write(b"\0")
    f.close()
