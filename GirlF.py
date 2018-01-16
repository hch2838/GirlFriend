class GirlFrd :
    def __init__(self,girlF):
        self.girlF = girlF

    def FoundG(self):
        if(self.girlF == True) :
            return None
        elif(self.girlF == False) :
            return None

class Wife(GirlFrd):
    def __init__(self,Wife):
        self.wife = Wife
    def FoundG(self):    #오버라이딩
        if(self.wife == True) :
            return None
        elif(self.wife == False) :
           return None

gf = GirlFrd(False)
wf = Wife(False)
myGf = gf.FoundG()
print("my girl friend : %s"%gf.FoundG())
print("my Wife : %s"%wf.FoundG())

if(gf.FoundG() == wf.FoundG()) :
    print("\nI'am Solo!!")