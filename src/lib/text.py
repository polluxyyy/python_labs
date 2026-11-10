import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Приводит текст к нижнему регистру и убирает лишние пробелы."""
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е")

    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    """Выделяет слова, сохраняя дефисы внутри слов."""
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает количество появлений каждого слова."""
    freq = {}

    for word in tokens:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def sort_key(pair: tuple[str, int]) -> tuple[int, str]:
    """Задаёт сортировку по убыванию частоты, затем по алфавиту."""
    word, count = pair
    return -count, word


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ-N слов. Отрицательное N — ValueError."""
    if n < 0:
        raise ValueError("N не должно быть отрицательным")

    pairs = freq.items()
    result = sorted(pairs, key=sort_key)
    return result[:n]