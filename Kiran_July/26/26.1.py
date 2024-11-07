d={"rajesh":100000,"pavan":200000,"umesh":400000,"ishwar":500000,"akshay":700000,"om":250000,"vijay":800000}
# rich>5 lack
# middle 2-5 lakh
# pooor <2 lakh
m={}
r={}
p={}
for i in d:
    if d[i]>500000:
        d[i]=m[i]

    