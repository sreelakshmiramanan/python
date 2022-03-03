class time:
    def _init_ (self,h,m,s):
        self.hr=h
        self.min=m
        self.sec=s
    def _add_ (self,other):
            tempsec=self.sec+other.sec
            tempmin=tempsec/60
            self.sec=int(tempsec%60)
            self.min=self.min+other.min+tempmin
            temphr=self.min/60;
            self.min=int(self.min%60)
            self.hr=int(self.hr+other.hr+temphr)
            return  time(self.hr,self.min,self.sec)
    def _str_ (self):
             return str(self.hr)+'hr'+str(self.min)+'min'+str(self.sec)+'sec'
a=int(input("enter hour of T1:"))
b=int(input("enter minute of T1:"))
c=int(input("enter second of T1:"))
x=int(input("enter hour of T2:"))
Y=int(input("enter minute of T2:"))
Z=int(input("enter second of T2:"))
t1=time(a,b,c)
t2=time(x,y,z)
print(t1+t2)
