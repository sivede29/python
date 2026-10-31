# # Frequency counting with a dictionary
# statuses = [
#     "SUCCESS", "FAILED", "SUCCESS",
#     "PENDING", "FAILED", "SUCCESS"
# ]

# # Explain your approach without writing code first.
# # 1-declared a freq_cnt dict
# # 2-used for loop iterate over the statuses list
# # 3-initial cnt=1 for vistis later incremented the cnt

# freq_cnt={}
# for i in statuses:
#     if i not in freq_cnt:
#         freq_cnt[i]=1
#     else:
#         freq_cnt[i]+=1
# print(freq_cnt)


# # Duplicate detection
# numbers = [5, 3, 8, 5, 2, 3, 9, 8, 8, 1]

# #created two list one seen and other de_dup
# #then using for loop iterated over the numbers list,
# #  using condition like num in seen and not in de_dup list, if it statisfy then added it to the de_dup list
# seen=[]
# de_dup=[]

# for num in numbers:
#     if num  in seen:
#         if num not in de_dup:
#             de_dup.append(num)
#     else:
#         seen.append(num)
# print(de_dup)

# Find values occurring exactly once

# numbers = [5, 3, 8, 5, 2, 3, 9, 8, 8, 1]

# freq_cnt={}

# for num in numbers:
#     if num not in freq_cnt:
#        freq_cnt[num] = 1
#     else:
#        freq_cnt[num]+=1
# uniques = [key for key, count in freq_cnt.items() if count == 1]
# print(uniques)


# numbers = [12, 7, 4, 19, 8, 12]

# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i]<numbers[j]:
#             numbers[i],numbers[j]=numbers[j],numbers[i]
            
# print("Max Number Is:",numbers[0])


# # numbers = [12, 7, 4, 19, 8, 12]

# # max_number=numbers[0]

# # for num in numbers:
# #     if max_number<num:
# #         max_number=num
# # print(max_number)

# numbers = [12, 7, 4, 19, 8, 12]

# # The sum of all numbers.
# # The count of even numbers.
# # The average of all numbers.


# total=0
# even_cnt=0
# total_cnt=0

# if numbers:
#     for num in numbers:
#         total+=num
#         total_cnt+=1
#         if num%2==0:
#             even_cnt+=1
# avg=total/total_cnt
# print("total: ",total)
# print("event_cnt :",even_cnt)
# print("total_cnt :",total_cnt)
# print("avg :", avg)



records = [
    {"customer_id": 105, "name": " Diana ", "amount": 75},
    {"customer_id": 106, "name": None, "amount": 40},
    {"customer_id": 107, "amount": 90},
    {"customer_id": 108, "name": "Evan", "amount": None},
    {"customer_id": 109, "name": "Fiona"},
    {"customer_id": 110, "name": "Grace", "amount": 60},
    {"customer_id": 111, "name": "   ", "amount": 25}
]


# Your task: Write a program that creates two lists: valid_records and rejected_records.

# Requirements:
# 1. A valid record must contain customer_id, name, and amount.
# 2. Reject records with missing keys, None values, or a blank name.
# 3. Normalize valid names by removing surrounding spaces and applying title case.
# 4. Keep each rejected record along with a reason explaining why it was rejected.
# 5. Do not crash when a key is missing or its value is None.
# 6. Do not modify the original records.

# valid_records=[]
# rejected_records=[]
# required_keys=["customer_id","name","amount"]
# reason={}
# for item in records:
#     for key in required_keys:
#         if key not in item:
#             rejected_records.append({'record':item.copy(),'reason':f"{key} is none"})
#             break
#         elif isinstance(item[key],str):
#             if item[key].strip()=='':
#                 rejected_records.append({'record':item.copy(),'reason':f"{key} is blank"})
#                 break
#         elif item[key] is None:
#             rejected_records.append({'record':item.copy(),'reason':f"{key} is None"})
#             break

#     else:
#         item['name']=item['name'].strip().title()
#         valid_records.append(item)


# print("valid_records:\n", valid_records)
# print('\n')
# print("rejected_records:\n", rejected_records)

transactions = [
    {"customer_id": 101, "amount": 120},
    {"customer_id": 102, "amount": 80},
    {"customer_id": 101, "amount": 50},
    {"customer_id": 103, "amount": 200},
    {"customer_id": 102, "amount": 20},
    {"customer_id": 101, "amount": 30}
]
res={}
for item in transactions:
    if item['customer_id'] in res:
        res[item["customer_id"]]+=item["amount"]
    else:
        res[item["customer_id"]]=item["amount"]
    
print(res)




















    

        

























