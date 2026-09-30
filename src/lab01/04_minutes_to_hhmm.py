min = int(input("Минуты: "))
hours = min // 60
perevod_min = min % 60
print(f"{hours}:{perevod_min:02d}")
