def Gmean(a:int, b:int):
    mean = (a*b)/(a+b)
    print(mean)

a: int=9
b: int= 8
Gmean(a, b)
c:int = 8
d:int = 7
Gmean(c, d)

print("Bulk Data passing in function")
def average(a: int=9, b: int=8):
    print("Average is" , (a+b)/2)
average() 

def name(fname: str, mname: str = "Charlett", lname: str="Khan"):
    print("Hello, ", fname, mname, lname)
name("Ahsan", "Asuka")