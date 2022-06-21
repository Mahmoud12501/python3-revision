

def multiple_tables(start,end,ms,mstop):
    
    for i in range(start,end+1):
        for n in range(ms,mstop+1):
            print(f"{i} x {n} = {i*n}")
        print("-------------")


start=int(input("enter start "))
end=int(input("enter end "))
ms=int(input("enter ms "))
mstop=int(input("enter mstop "))

multiple_tables(start,end,ms,mstop)