import csv
import json
from pathlib import Path


def read_csv_rows(csv_path: str) -> list[list[str]]:
    """читает csv с заголовком, ес невер формат, то вал ер"""
    if Path(csv_path).suffix.lower() != ".csv":
        raise ValueError("Нужен файл CSV")

    with open(csv_path, encoding="utf-8", newline="") as file:
        try:
            rows = list(csv.reader(file, strict=True))
        except csv.Error as error:
            raise ValueError("Неверный формат CSV") from error

    if not rows or not rows[0]:
        raise ValueError("CSV пустой или нет заголовка")

    header = rows[0]
    if any(name.strip() == "" for name in header):
        raise ValueError("В заголовке есть пустые названия")
    if len(set(header)) != len(header):
        raise ValueError("Названия столбцов повторяются")

    for row in rows[1:]:
        if len(row) != len(header):
            raise ValueError("Строки должны быть одинаковой длины")

    return rows


def json_to_csv(json_path: str, csv_path: str) -> None:
    """преобраз список словарей в csv, нев данные то вал ер"""
    if Path(json_path).suffix.lower() != ".json":
        raise ValueError("Нужен файл JSON")
    if Path(csv_path).suffix.lower() != ".csv":
        raise ValueError("Результат должен быть CSV")

    with open(json_path, encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    fields = set()
    for row in data:
        if not isinstance(row, dict):
            raise ValueError("JSON должен содержать список словарей")
        for value in row.values():
            if isinstance(value, (list, dict)):
                raise ValueError("Вложенные списки и словари не поддерживаются")
        fields.update(row)

    if not fields or any(name.strip() == "" for name in fields):
        raise ValueError("Нет названий столбцов")

    header = sorted(fields)
    with open(csv_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """преобразует csv в список словарей,а знач остаются строками"""
    if Path(json_path).suffix.lower() != ".json":
        raise ValueError("Результат должен быть JSON")

    rows = read_csv_rows(csv_path)
    header = rows[0]
    result = []

    for row in rows[1:]:
        record = {}
        for i in range(len(header)):
            record[header[i]] = row[i]
        result.append(record)

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)