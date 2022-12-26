infile=open("data.txt")
decode={'=':-2,'-':-1,'0':0,'1':1,'2':2}
val=sum(sum((5**i)*decode[n] for i,n in enumerate(reversed(line.strip()))) for line in infile)
print(val)
encode='012=-'
res=""
while val:
    res+=encode[val%5]
    if val>2: val+=2
    val//=5
print(res[::-1])