extra_records = [
    {"customer_id": 105, "name": " Diana ", "amount": 75},
    {"customer_id": 106, "name": None, "amount": 40},
    {"customer_id": 107, "amount": 90},
    {"customer_id": 108, "name": "Evan", "amount": None},
    {"customer_id": 109, "name": "Fiona"},
    {"customer_id": 110, "name": "Grace", "amount": 60},
    {"customer_id": 111, "name": "   ", "amount": 25}
]

required_keys=["customer_id","name","amount"]
rejected_records=[]
vaild_records=[]
for item in extra_records:
    
    for req_key in required_keys:
        if req_key not in item:
            rejected_records.append({"record": item, "reason": "key missing"})
            break  
        elif  item[req_key] is None or item[req_key].strip()=='':
            rejected_records.append({"record": item, "reason": "value missing"})
            break
    else:
        item['name']=item['name'].strip().title()
        vaild_records.append(item)

total_dict={}
for item in vaild_records:
    cust_id=item['customer_id']
    amount=item['amount']
    if cust_id not in total_dict.keys():
        total_dict[cust_id]=amount
    else:
        total_dict[cust_id]+=amount
    


print(rejected_records)
print(vaild_records)
print(total_dict)


