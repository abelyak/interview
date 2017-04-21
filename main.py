import constants
import utils
import QandA_Reader

def getAQ(path):
    qa = QandA_Reader.qareader(path)
    q = qa.getQ()
    a = qa.getA()
    res = ''
    for i in range(0, len(q)):
        tmp = utils.wraptag(str(i + 1) + ". <br/>" + str(utils.readFile(q[i])), 'pre')

        res += utils.wraptag(tmp, 'h3')
        res += utils.wraptag(str(utils.readFile(a[i])), 'pre')
        res += "<hr/>"

    return res

def createQuestions(path):
    head = utils.wraptag(constants.DEF_HEAD, 'head')

    body = constants.DEF_MAIN_LIST
    body += getAQ(str(path))
    body = utils.wraptag(body, 'body')

    out_html = utils.wraptag("<!DOCTYPE html>" + head + body, 'html')

    utils.createHtml(str(path), out_html)

createQuestions('q1')
createQuestions('q2')
createQuestions('q3')

createQuestions('patterns')
createQuestions('ipc')
createQuestions('smart_pointers')
createQuestions('p_sync')

