import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает файл целиком. Для Windows-1251 укажи encoding="cp1251".

    Если файла нет — FileNotFoundError, неверная кодировка — UnicodeDecodeError.
    """
    return Path(path).read_text(encoding=encoding)


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Записывает CSV в UTF-8. Строки разной длины — ValueError."""
    if rows:
        length = len(rows[0])
        for row in rows:
            if len(row) != length:
                raise ValueError("Строки должны быть одинаковой длины")

    with Path(path).open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)