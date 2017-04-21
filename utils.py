def readFile(fname):
    f = open(fname, 'r')
    return f.read()

def wraptag(data, tag):
    return '<' + str(tag) + '>' + str(data) + '</' + str(tag) + '>'

def createHtml(filename, data):
    f = open('html/' + str(filename) + '.html', 'w+')
    f.write(str(data))
    f.close()