import random
majors = ["CNTT", "KHMT", "KTPM", "HTTT", "DAPT"]
N = int(input("Nhập số lượng thành viên N: "))
accounts = {}
for i in range(N):
    student_id = 2023600001 + i 
    username = str(student_id).zfill(10)  
    major = random.choice(majors)  
    password = major + username 
    account_key = f"Account{i+1}"
    accounts[account_key] = {
        "Username": username,
        "Password": password
    }

# In ra kết quả
print(accounts)
