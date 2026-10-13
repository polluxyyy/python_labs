# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)

---

## Задание 1

В файле **arrays.py** я реализовал поиск минимального и максимального значений, сортировку уникальных чисел и объединение строк в один список. Данные для примеров передаются непосредственно при вызове функций.

---

### Функция **min_max**

В этой функции я сначала проверил, что список не пустой. Первое число присвоил переменным **min** и **max**. Затем перебрал элементы списка: если число меньше текущего минимума или больше максимума, обновлял соответствующую переменную. В конце вернул кортеж из минимального и максимального значений.

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        raise ValueError("пустой список")
    min=max=nums[0]
    for x in nums:
        if x<min:
            min=x
        if x>max:
            max=x
    return(min,max)
```

![1.1](1.1.1.png)

*min_max — пример 1.*

![1.2](1.1.2.png)

*min_max — пример 2.*

![1.3](1.1.3.png)

*min_max — пример 3.*

![1.4](1.1.4.png)

*min_max — пример 4.*

![1.5](1.1.5.png)

*min_max — пример 5.*

---

### Функция **unique_sorted**

Здесь я создал список **result** и добавлял в него только числа, которых там ещё не было. После удаления повторений отсортировал список пузырьком. Во вложенных циклах сравнивал соседние элементы и менял их местами, если левое число было больше правого. После каждого прохода следующее наибольшее число оказывалось в конце проверяемой части списка.

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    result=[]
    for x in nums:
        if x not in result:
            result.append(x)
    for i in range(len(result)):
        for j in range(len(result)-1 -i):
            if result[j]>result[j+1]:
                result[j],result[j+1]=result[j+1],result[j]
    return result
```

![1](1.2.1.png)

*unique_sorted — пример 1.*

![2](1.2.2.png)

*unique_sorted — пример 2.*

![3](1.2.3.png)

*unique_sorted — пример 3.*

![4](1.2.4.png)

*unique_sorted — пример 4.*

---

### Функция **flatten**

В этой функции я перебрал строки исходного списка. С помощью **isinstance** проверил, что каждая строка является списком или кортежем. Если это не так, вызвал ошибку **TypeError**. В остальных случаях добавлял все элементы строки в общий список **result** с помощью **+=**.

```python
def flatten(mat: list[list | tuple]) -> list:
    result=[]
    for row in mat:
        if not isinstance(row,(list,tuple)):
            raise TypeError("подходят только список или кортеж")
        result+=row
    return result
```

![1](1.3.1.png)

*flatten — пример 1.*

![2](1.3.2.png)

*flatten — пример 2.*

![3](1.3.3.png)

*flatten — пример 3.*

![4](1.3.4.png)

*flatten — пример 4.*

---

### Пример запуска задания 1

```python
if __name__=="__main__":
    print("мин и макс",min_max([3,-1,5,5,0]))
    print("уникальные по возраст",unique_sorted([3,1,2,1,3]))
    print("общий список",flatten([[1,2],(3,4,5)]))
```

---

## Задание В

В файле **matrix.py** я реализовал транспонирование матрицы и вычисление сумм по строкам и столбцам.

---

### Функция **check_matrix**

Для проверки матрицы я написал отдельную функцию. Она сравнивает длину каждой строки с длиной первой. Если длины различаются, вызывается **ValueError**. Для пустой матрицы цикл не выполняется.

```python
def check_matrix(mat: list[list[float | int]]) -> None:
    for row in mat:
        if len(row)!=len(mat[0]):
            raise ValueError("не ровная(рваная) матрица")
        
```

---

### Функция **transpoce**

Сначала я вызвал **check_matrix**. Если матрица пустая, вернул пустой список. Затем перебирал индексы столбцов через **j**. Для каждого столбца брал по одному элементу из каждой строки и добавлял его в **new_row**. Полученный список добавлял в результат. Таким образом, столбцы исходной матрицы становились строками новой.

```python
def transpoce(mat: list[list[float | int]]) -> list[list]:
    check_matrix(mat)
    result=[]
    if len(mat)==0:
        return result
    for j in range(len(mat[0])):
        new_row=[]
        for row in mat:
            new_row.append(row[j])
        result.append(new_row)
    return result
```

![1](2.1.1.png)

*transpoce — пример 1.*

![2](2.1.2.png)

*transpoce — пример 2.*

![3](2.1.3.png)

*transpoce — пример 3.*

![4](2.1.4.png)

*transpoce — пример 4.*

![5](2.1.5.png)

*transpoce — пример 5.*

---

### Функция **row_sums**

Тут я проверил одинаковую длину строк и создал список результатов. Затем перебрал строки матрицы и вычислил сумму каждой с помощью **sum**. Начальное значение **0.0** позволяет получать суммы типа **float**. Каждую сумму добавил в **result**.

```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)
    result=[]
    for row in mat:
        result.append(sum(row,0.0))
    return result
```

![1](2.2.1.png)

*row_sums — пример 1.*

![2](2.2.2.png)

*row_sums — пример 2.*

![3](2.2.3.png)

*row_sums — пример 3.*

![4](2.2.4.png)

*row_sums — пример 4.*

---

### Функция **col_sums**

Для вычисления сумм столбцов я использовал уже написанные функции. Сначала **transpoce** превращает столбцы матрицы в строки. Затем **row_sums** вычисляет суммы этих строк. Полученные числа являются суммами столбцов исходной матрицы.

```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    return row_sums(transpoce(mat))
```

![1](2.3.1.png)

*stolb_sums — пример 1.*

![2](2.3.2.png)

*stolb_sums — пример 2.*

![3](2.3.3.png)

*stolb_sums — пример 3.*

![4](2.3.4.png)

*stolb_sums — пример 4.*

---

### Пример запуска задания В

```python
if __name__=="__main__":
    m=[[1,2,3],[4,5,6]]
    print("транспонирование",transpoce(m))
    print("суммы строк", row_sums(m))
    print("суммы столбцов", stolb_sums(m))
```

---

## Задание С

В файле **tuples.py** я реализовал форматирование записи студента.

---

### Функция **format_record**

В этой функции я сначала проверил, что запись является кортежем из трёх элементов. Затем проверил типы ФИО, группы и GPA. С помощью **split** разделил ФИО на слова, а через **join** убрал лишние пробелы в названии группы. После этого проверил количество слов, наличие группы и диапазон GPA от 0 до 5. Инициалы получил из первых букв имени и отчества, переведённых в верхний регистр. Фамилию оформил через **capitalize**, а GPA вывел с двумя знаками после точки с помощью **f-строки**.

```python
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

    return f"{words[0].capitalize()} {initials}, группа: {group}, gpa {gpa:.2f}"
```

### Пример запуска задания С

```python
if __name__=="__main__":
    print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
    print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
    print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```

![1](3.3.1.png)

*format_record — пример 1.*

![2](3.3.2.png)

*format_record — пример 2.*

![3](3.3.3.png)

*format_record — пример 3.*

![4](3.3.4.png)

*format_record — пример 4.*

![5](3.3.5.png)

*format_record — пример 5.*

![6](3.3.6.png)

*format_record — пример 6.*

![7](3.3.7.png)

*format_record — пример 7.*

---
