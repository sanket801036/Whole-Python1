# print(type(l))
#Dict
E = {'name':"Sham",'company':"TCS",'address':"karvenagar",'city':"pune",'country':"India",'Salary':100000}
print(E)

l = {"one":1, "two":4, "three":9, "four":16, "five":25, "six":36,"seven":49,"eight":64,"nine":81,"ten":100}
print(type(l))
print(l)

B = {"Auther":"Kiran sir", "Topic":"Python", "Book_tyoe":"Theory","Auther":"Vaibhav sir"}
#key => unique and immutable
print(B)
B["Topic"]="java"
print(B)


d={1:89,"name":"rahul",2:[4,8],"name1":"rahul"}
print(d)

#single student details
s = {"name":"ram","Roll_no":50,"ID":59896,"rank":5,"Result":"Pass"}
print(s)
s ={1:{"name":"ram","Roll_no":50,"ID":59896,"rank":5,"Result":"Pass"},2:{"name":"sham","Roll_no":60,"ID":596,"rank":10,"Result":"Fail"}}

print(s)

E={1:{"name":"sam","salary":10000,"compony":"TCS","rank":"5"},2:{"name":"joy","salary":10000,"compony":"Infosis","rank":"7"}}
print(E)

d={"Infinix1":{"display":"HD","Camera":"Three","RAM":8},"Infinix2":{"display":"QLED","Camera":5,"RAM":6}}
print(d)

China_Mobile={"Redmi":{"Redmi1":{"Display":"QLED","RAM":8,"Camera":"60pixel"},"Redmi2":{"Display":"FHD","RAM":4,"Camera":"100pixel"}},"Realme":{"Reamlme1":{"Diaplay":"HD","RAM":2,"Camera":"150pixel"}},"Reamlme2":{"Display":"QLED","RAM":12,"Camera":"200pixel"}}
print(China_Mobile)

supra={"price":900000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6}
print(supra)

tata1={"nexon":{"price":500000,"Engine":"500cc","Fuel":"Disel","Cylender":2},"neno":{"price":250000,"Engine":"400cc","Fuel":"water","Cylender":3}}
print(tata1)


tata={"nexon":{"nexon1":{"price":800000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6},"nexon2":{"price":600000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6}},"neno":{"neno1":{"price":700000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6},"neno2":{"price":900000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6}}}
print(tata)

Laptop = {"lenovo":{"lenovo_V15":{},"Lenovo_V14":{}},"HP":{"HP_Chromebook":{},"HP_Pavillion":{}}}
