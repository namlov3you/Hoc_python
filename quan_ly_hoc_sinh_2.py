results = []
try:
    with open("students.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            name = parts[0]
            math = float(parts[1])
            lit = float(parts[2])

            avg = (math + lit)/2

            results.append((name, avg))

    print(results)

    # Sắp xếp theo điểm trung bình (vị trí index 1)
    results.sort(key= lambda x : x[1], reverse= True)

    print(results)

    with open("result.txt", "w", encoding="utf-8") as f:
        for name, avg in results:
            f.write(f"{name}: {avg:.2f}\n")
    print("Đâ xử lý xong!")

    print("--- In thông tin result ---")
    try:
        with open("result.txt", "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(": ")
                name = data[0]
                avg = data[1]

                print(f"học sinh: {name} | điểm trung bình: {avg}")
    except FileNotFoundError:
        print("Không tìm thấy file")
except FileNotFoundError:
    print("Không tìm thấy file nguồn")