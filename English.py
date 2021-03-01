class EngDic:
    def __init__(self):
        self.Dic=self.GetLib()
    def GetLib(self):
        dic={}
        k=m=0
        with open('ESL6.txt',encoding='utf-8') as f:
            for line in f:
                k=k+1
                if line[0]=='英':
                    dic.setdefault(k)
                    m=k
                if '.' in line[:5]:
                    dic[m]=k
        for x in dic:
            if dic[x]==None:
                dic[x]=x+1

        with open('ESL6.txt', encoding='utf-8') as f:
            ku=f.readlines()

        ku=[ku[x-2:y+1] for x,y in dic.items()]
        return ku