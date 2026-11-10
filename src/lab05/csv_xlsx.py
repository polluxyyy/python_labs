from pathlib import Path
from openpyxl import Workbook

from .json_csv import read_csv_rows


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """создает xlsx с листом sheet1 и шириной колонок >=8"""
    if Path(xlsx_path).suffix.lower() != ".xlsx":
        raise ValueError("Результат должен быть XLSX")

    rows = read_csv_rows(csv_path)
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Sheet1"

    for row in rows:
        sheet.append(row)

    for column in sheet.columns:
        width = 8
        for cell in column:
            cell.data_type = "s"
            if cell.value is not None:
                width = max(width, len(str(cell.value)) + 2)
        letter = column[0].column_letter
        sheet.column_dimensions[letter].width = width

    workbook.save(xlsx_path)