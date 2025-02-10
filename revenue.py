def revenues(a,b,p,ls,lb,i,f):
    rev = (a-p)*lb + (p-b)*ls - ((p-a)*f + (b-p)*f)*i
    return rev

