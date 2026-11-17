# ЛР6 — Работа с argparse

В этой лабе я сделал запуск программ через командную строку. Для текста использовал функции из ЛР3, для конвертации файлов — из ЛР5. Через argparse добавил выбор команды и параметры запуска.

Все команды ниже выполняются из папки python_labs.

## Задание А — cli_text.py

### Вывод содержимого файла

Команда cat выводит текст из файла. Путь к нему указывается после --input.

```powershell
py -m src.lab06.cli_text cat --input data/samples/people.csv
```

![Вывод файла](../../images/lab06/cat.png)

Если добавить -n, рядом с каждой строкой появится её номер.

```powershell
py -m src.lab06.cli_text cat --input data/samples/people.csv -n
```

![Вывод с номерами](../../images/lab06/cat_n.png)

### Подсчёт слов

Команда stats считает слова в тексте и показывает самые частые. Для проверки я создал файл data/samples/people.txt:

```text
Привет, мир! Привет!!!
Ёжик и ёжик.
```

Запустил программу:

```powershell
py -m src.lab06.cli_text stats --input data/samples/people.txt
```

Получилось 6 слов, из них 4 уникальных. Буква ё заменяется на е, а все слова приводятся к нижнему регистру. При одинаковой частоте слова выводятся по алфавиту.

![Подсчёт слов](../../images/lab06/stats.png)

По умолчанию выводится топ-5. Через --top можно указать другое количество:

```powershell
py -m src.lab06.cli_text stats --input data/samples/people.txt --top 2
```

Теперь в топе только два слова — ежик и привет.

![Топ-2](../../images/lab06/stats_top2.png)

## Задание Б — cli_convert.py

Здесь я добавил три команды для конвертации файлов. После --in указывается исходный файл, после --out — куда записать результат.

Для проверки взял файлы people.json и people.csv из ЛР5.

### JSON в CSV

```powershell
py -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/lab06_people.csv
Get-Content -Encoding UTF8 data/out/lab06_people.csv
```

Первой командой я создал CSV, второй посмотрел его содержимое. Столбцы идут по алфавиту. У Анны не указан город, поэтому это поле осталось пустым.

![JSON в CSV](../../images/lab06/json2csv.png)

### CSV в JSON

```powershell
py -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/lab06_people.json
Get-Content -Encoding UTF8 data/out/lab06_people.json
```

Из CSV получился список из двух словарей. Значения читаются как строки, поэтому возраст в JSON записан в кавычках.

![CSV в JSON](../../images/lab06/csv2json.png)

### CSV в Excel

```powershell
py -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/lab06_people.xlsx
```

После запуска открыл файл в Excel и проверил таблицу. В ней заголовки и две записи — Богдан и Анна. Конвертер создаёт лист Sheet1 и подбирает ширину столбцов по содержимому, но не меньше 8.

![CSV в Excel](../../images/lab06/csv2xlsx.png)

Для Excel используется openpyxl из ЛР5. Если библиотека ещё не установлена:

```powershell
py -m pip install -r requirements.txt
```

## Справка

У каждой команды есть --help. Он показывает, какие параметры можно передать. Саму справку формирует argparse, в коде я указал названия параметров и их описания.

```powershell
py -m src.lab06.cli_text cat --help
py -m src.lab06.cli_text stats --help
```

![Справка cat и stats](../../images/lab06/help_text.png)

```powershell
py -m src.lab06.cli_convert json2csv --help
py -m src.lab06.cli_convert csv2json --help
py -m src.lab06.cli_convert csv2xlsx --help
```

![Справка конвертеров](../../images/lab06/help_convert.png)

## Проверка ошибок

Проверил три случая.

Сначала передал отрицательное количество слов:

```powershell
py -m src.lab06.cli_text stats --input data/samples/people.txt --top -1
```

Программа сообщила, что --top не может быть отрицательным.

Потом не указал путь к файлу:

```powershell
py -m src.lab06.cli_text cat
```

Появилось сообщение, что требуется --input.

И попробовал открыть файл, которого нет:

```powershell
py -m src.lab06.cli_text cat --input data/samples/no_such_file.txt
```

Получил FileNotFoundError.

![Проверка ошибок](../../images/lab06/errors.png)

## Что нужно учитывать

Файлы с текстом читаются в UTF-8. Для пустого текста stats выводит нулевые счётчики, а при --top 0 не выводит сами слова.

Результаты конвертации сохраняются в data/out/. Эта папка должна существовать. Если файл с таким именем уже есть, он перезаписывается.

Проверки JSON и CSV остались в функциях из ЛР5. Если они вызывают ValueError, cli_convert выводит сообщение через parser.error.