s = "python programiNg"

dem = 0

for ch in s:
    if ch == "n":
        dem = dem + 1

print(dem)

print("---- cách khác --------")
s=s.lower()
so_lan_n = s.count("n")
print(so_lan_n)