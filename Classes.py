import json

class Chat():
    def __init__(self,nome):
        try:
            memory = open(nome+'.json',"r")
        except FileNotFoundError:
            memory = open(nome+'.json',"w")
            memory.write('[["////"],{"oi":"olá, qual o seu nome?","tchau":"tchau"}]')
            memory.close()
            memory = open(nome+'.json',"r")
        self.nome = nome
        self.conhecidos, self.fr = json.load(memory)
        memory.close()
        self.historico = [None,]
    def escutar(self,fr=None):
        if (fr == None):
            fr = input("->")
        fr = str(fr)
        fr = fr.lower()
        return fr
    def pensar(self,fr):
        if (fr in self.fr):
            return self.fr[fr]
        if (fr == "/ap"):
            return "Pergunta?"
            #c = str(input("Pergunta ->"))
            #r = str(input("Resposta->"))
            #c = c.lower()
            
            
        ultimafr = self.historico[-1]
        if (ultimafr == "olá, qual o seu nome?"):
            nome = self.peganome(fr)
            resp = self.respondeNome(nome)
            return resp
        if ( ultimafr == "Pergunta?"):
            self.c = fr 
            self.c = self.c.lower()
            return "Resposta"
        if (ultimafr == "Resposta"):
            r = fr
            self.fr[self.c] = r
            self.gm()
            return 'ok'
        try:
            resp = eval(fr)
            return resp
        except:
            pass
        return "Não entendi,você quer que eu aprenda? se sim digite /ap"
            
    def peganome(self,nome):
        nome = nome.title()
        return nome 
        
    def respondeNome(self,nome):
        if nome in self.conhecidos:
            fr = "Eaw "
        else:
            fr = "Muito prazer "
            self.conhecidos.append(nome)
            self.gm()
        return fr+nome
    def gm(self):
        memory = open(self.nome+'.json',"w")
        json.dump([self.conhecidos,self.fr],memory)
        memory.close()

    def falar(self,fr):
        print(fr)
        self.historico.append(fr)