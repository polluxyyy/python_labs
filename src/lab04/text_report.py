import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv


def main() -> None:
    """Читает текстовый файл и сохраняет частоты всех слов в CSV."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_path", default="data/input.txt")
    parser.add_argument("--out", default="data/report.csv")
    parser.add_argument("--encoding", default="utf-8")
    args = parser.parse_args()

    text = read_text(args.input_path, encoding=args.encoding)
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    rows = top_n(freq, len(freq))
    write_csv(rows, args.out, header=("word", "count"))

    print("Всего слов:", len(tokens))
    print("Уникальных слов:", len(freq))
    print("Топ-5:")
    for word, count in top_n(freq):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()