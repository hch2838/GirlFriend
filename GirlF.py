class GirlFrd :
    def __init__(self,girlF):
        self.girlF = girlF

    def FindG(self):
        if(self.girlF == True) :
            return None
        elif(self.girlF == False) :
            return None

class Wife(GirlFrd):
    def __init__(self,Wife):
        self.wife = Wife
    def FindG(self):    #오버라이딩
        if(self.wife == True) :
            return None
        elif(self.wife == False) :
           return None

gf = GirlFrd(False)
wf = Wife(False)
myGf = gf.FindG()
print("my girl friend : %s"%gf.FindG())
print("my Wife : %s"%wf.FindG())

if(gf.FoundG() == wf.FindG()) :
    print("\nI'am Solo!!")
