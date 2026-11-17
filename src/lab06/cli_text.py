import argparse

from src.lib.text import normalize, tokenize, count_freq, top_n


def main() -> None:
    """Читает аргументы и запускает cat или stats."""
    parser = argparse.ArgumentParser(description="Работа с текстовыми файлами")
    sub = parser.add_subparsers(dest="command", required=True)

    cat_parser = sub.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу UTF-8")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = sub.add_parser("stats", help="Посчитать частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к файлу UTF-8")
    stats_parser.add_argument("--top", type=int, default=5, help="Число слов в топе")

    args = parser.parse_args()

    if args.command == "cat":
        with open(args.input, encoding="utf-8") as file:
            for number, line in enumerate(file, start=1):
                if args.n:
                    print(f"{number}: ", end="")
                print(line, end="")

    elif args.command == "stats":
        if args.top < 0:
            parser.error("--top не может быть отрицательным")

        with open(args.input, encoding="utf-8") as file:
            text = file.read()

        tokens = tokenize(normalize(text))
        freq = count_freq(tokens)

        print("Всего слов:", len(tokens))
        print("Уникальных слов:", len(freq))
        print(f"Топ-{args.top}:")

        for word, count in top_n(freq, args.top):
            print(f"{word}:{count}")


if __name__ == "__main__":
    main()