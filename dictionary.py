#tạo dictionary
person = {
    "name": "Nam",
    "age": 28,
    "city": "Hà Nội"
}

#in từng thông tin
print("Tên:", person["name"])
print("Tuổi:", person["age"])
print("Thành phố:", person["city"])

print("---- cách duyệt khác ----")

for key, value in person.items():
    print(key, ":", value)
    
# thêm sửa xóa dictionary

# thêm
person["job"] = "Student"

# Sửa
person["age"] = 20

# xóa
del person["city"]

print("---In kết quả----")
for a, b in person.items():
    print(a,":", b)