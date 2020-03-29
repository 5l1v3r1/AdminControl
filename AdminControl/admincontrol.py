

Mainlist = []

class Admin:
    
    

    def addAdmin(self, id):
        
        try:
            Mainlist.append(id)
            print("id add")
        except:
            print("Error")

    def checkList(self):
        
        for x in range(len(Mainlist)): 
            print (Mainlist[x])


    def deleteId(self, delid):
        try:
            Mainlist.remove(delid)
            print("Id remove")
        except ValueError:
            print(" id not in list") 


    def CheckId(self, idforcheck):
        try:
            result = Mainlist.count(idforcheck)
            if result<1:
                print("Id not in list")
                return False

                
            
            elif result>1 or result == 1:
                print("Id in list")
                return True
                
                

        except:
            print("Error")

    
    def clearList(self):
        try:
            Mainlist.clear()
            print("List clear")
        except:
            print("Eror")

    