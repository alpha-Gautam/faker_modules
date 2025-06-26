from faker import Faker
import pandas as pd
import random



faker = Faker('en_IN')

data_list=[]
for _ in range(100):
    data = {
        "name": faker.name(),
        "address": faker.address(),
        "email": faker.email(),
        "website": faker.url(),
        "phone_number": faker.phone_number(),
        "company": faker.company(),
        "job": faker.job(),
        "text": faker.text(),
        "date_time": faker.date_time(),
        "country": faker.country(),
        "state":faker.state(),
        "city": faker.city(),
        "pin_code": faker.postcode()
    }
    data_list.append(data)  
    
    
print(type(data_list))
df=pd.DataFrame(data_list)
num=random.randint(1,5)
df.to_csv(f'Rawdata/data{num}.csv', index=False)
# df.to_excel(f'data{random.randint(1,100)}.xlsx', index=False)
print(f"Data generated and saved to Rawdata/data{num}.csv")

# print(data_list)
