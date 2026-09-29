minutes = int(input("Минуты: "))

hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{hours}:{remaining_minutes:02d}")
