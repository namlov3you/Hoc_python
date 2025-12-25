# 1. cấu trúc dữ liệu: sử dụng list chứa các dictionary
danh_sach_hoc_sinh = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Bình", "diem": 9.0},
    {"ten": "Chi", "diem": 7.5},
    {"ten": "Sinh", "diem": 4.5}
]

file_name ="bang_diem.txt"

# 2. Xử lý file: ghi dữ liệu vào file

print("--- Đang ghi dữ liệu vào file ---")
try:
    with open(file_name, "w", encoding="utf-8") as f:
        for hs in danh_sach_hoc_sinh:
            # Ghi theo định dạng tên - điểm
            line = f"{hs['ten']} - {hs['diem']}\n"
            f.write(line)
    print("Lưu file thành công!")
except Exception as e:
    print(f"có lỗi khi ghi file: {e}")

print ("\n" + "="*30 + "\n")

# 3. Xử lý file: đọc dữ liệu từ file và xử lý

print("--- Đọc dữ liệu từ file và hiển thị  ---")

try:
    with open(file_name, "r", encoding="utf-8") as f:
        # Đọc từng dòng trong file
        for line in f:
            # xử lý chuỗi: bỏ ký tự xuống dòng và tách dữ liệu
            data = line.strip().split(" - ")
            print(type(data))
            ten = data[0]
            diem = data[1]
            
            # kiểm tra điều kiện (cấu trúc rẽ nhánh)
            trang_thai = ""
            if float(diem) >= 8.0:
                trang_thai = "Giỏi"
            elif float(diem) >= 5.0:
                trang_thai = "Khá"
            else:
                trang_thai = "Yếu"
                
            print(f"Học sinh: {ten} | Điểm: {diem} | Xếp loại: {trang_thai}")
except FileNotFoundError:
    print("Không tìm thấy file!")


print("------------")
try:
    with open("bang_diem.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Lỗi: file không tồn tại")