s={100:{"name":"Sanket","City":"Nagpur","Percentage":"60%","math":"42%","Bio":"45%","Chem":"40%","Phy":"47"},101:{"name":"Sanket","City":"Nagar","Percentage":"60%","math":"52%","Bio":"55%","Chem":"50%","Phy":"57"},102:{"name":"Sanket","City":"Amravati","Percentage":"70%","math":"62%","Bio":"65%","Chem":"60%","Phy":"67"}}
print(s)

C={"Redmi":{"Redmi1":{"Display":"QLED","RAM":8,"Camera":"60pixel"},"Redmi2":{"Display":"FHD","RAM":4,"Camera":"100pixel"}},"Realme":{"Reamlme1":{"Diaplay":"HD","RAM":2,"Camera":"150pixel"}},"Reamlme2":{"Display":"QLED","RAM":12,"Camera":"200pixel"}}
print(C)
print(C["Redmi"])
print(C["Redmi"]["Redmi1"])
print(C["Realme"]["Reamlme1"]["RAM"])

tata={"nexon":{"nexon1":{"price":800000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6},"nexon2":{"price":600000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6}},"neno":{"neno1":{"price":700000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6},"neno2":{"price":900000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6}}}

print(tata["neno"]["neno1"])
print(tata["neno"]["neno1"]["price"])
print(tata["nexon"]["nexon1"]["Engine"])

#By using  get() method
tata={"nexon":{"nexon1":{"price":800000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6},"nexon2":{"price":600000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6}},"neno":{"neno1":{"price":700000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6},"neno2":{"price":900000,"Engine":"2000cc","Fuel":"Petrol","Cylenders":6}}}

print(tata.get("neno"))


#How to update dada frm dict
# syntax:
#     var[key]=updatedvalue
tata["neno"]["neno1"]["Engine"]="500cc"
print(tata)



