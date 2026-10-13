def format_record(rec: tuple[str,str,float]) -> str:
    if not isinstance(rec,tuple):
        raise TypeError("это не кортеж")
    if len(rec)!=3:
        raise ValueError("введите в формате фио, группа,gpa")

    fio,group,gpa=rec

    if not isinstance(fio,str) or not isinstance(group,str):
        raise TypeError("фио и группа должны быть строками")
    if not isinstance(gpa,float) and not isinstance(gpa,int):
        raise TypeError("gpa должен быть числом")

    words=fio.split()
    group=" ".join(group.split())

    if len(words)<2 or len(words)>3:
        raise ValueError("фио 2-3 слова")
    if group=="":
        raise ValueError("нет группы")
    if not 0<=gpa<=5:
        raise ValueError("знач. gpa от 0 до 5")

    initials=words[1][0].upper()+"."
    if len(words)==3:
        initials+=words[2][0].upper()+"."

    return f"{words[0].capitalize()} {initials}, гр. {group}, GPA {gpa:.2f}"

if __name__=="__main__":
    m=("Иванов Иван Иванович", "BIVT-25", "4.6")
    print(f"ввод:{m}\nвывод:{format_record(m)}")