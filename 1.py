shares={'IBM':36.6,'Lenovo':23.2,'AAAP':21.2,'ADM':10.2}
s=[]
for i in range(len(shares)):
    if filter(i:shares[i]>20,shares):
        s.append(shares[i])
    else:
        pass
    print (s)