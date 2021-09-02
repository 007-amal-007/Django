class Teacher():
    College="Luminar"
    def __init__(self,tname,department,tid):
        self.tname=tname
        self.department=department
        self.tid=tid
    def Dis(self):
        print("Teacher name: ",self.tname)
        print("Department: ",self.department)
        print(Teacher.College)
        print("Teacher ID: ",self.tid)
TE=Teacher("Savitha","Commerce","CSD103")
TE=Teacher("kavitha","Biology","BSD105")
TE.Dis()
TE.Dis()