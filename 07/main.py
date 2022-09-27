class VideoPlayer:
    def __init__(self, dados):
        self.dados = dados

    def youtube(self):
        msg = ""
        for i in self.dados:
            msg = msg + chr(i)
        print(msg)

    def face(self):
        msg = ''
        for i in self.dados:
            if i is True:
                msg = msg + '1'
            else:
                msg = msg + "0"
        j = 7
        k = 0
        decimais = []
        for i in msg:
            k = k + (int(i) * pow(2, j))
            j -= 1
            if j == -1:
                decimais.append(k)
                k = 0
                j = 7
        msg = ""
        for i in decimais:
            msg = msg + chr(i)
        print(msg)







V = VideoPlayer([80, 97, 114, 97, 98, 233, 110, 115, 44,
 32, 118, 99, 32, 99, 111, 110, 115, 101,
 103, 117, 105, 117, 46])
V.youtube()

W = VideoPlayer([False, True, False, True, False, False, False, False, False, True,
True, False, False, False, False,
 True, False, True, True, True, False, False, True, False, False,
True, True, False, False, False, False,
 True, False, True, True, False, False, False, True, False, True,
True, True, False, True, False, False,
 True, False, True, True, False, True, True, True, False, False,
True, True, True, False, False, True,
 True, False, False, True, False, True, True, False, False, False,
False, True, False, False, False,
 False, False, False, True, True, True, False, True, True, False,
False, True, True, False, False, False,
 True, True, False, False, True, False, False, False, False, False,
False, True, True, False, False,
 False, True, True, False, True, True, False, True, True, True, True,
False, True, True, False, True,
 True, True, False, False, True, True, True, False, False, True,
True, False, True, True, False, False,
 True, False, True, False, True, True, False, False, True, True,
True, False, True, True, True, False,
 True, False, True, False, True, True, False, True, False, False,
True, False, True, True, True, False,
 True, False, True, False, False, True, False, True, True, True,
False])
W.face()