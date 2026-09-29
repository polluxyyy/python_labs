n = int(input())
in_person = 0
remote = 0
for _ in range(n):
    surname, name, age, attendance = input().split()
    age = int(age)
    if attendance == "True":
        in_person += 1
    elif attendance == "False":
        remote += 1
    else:
        raise ValueError("Формат участия должен быть True или False")
print(in_person, remote)
