#!/usr/bin/env python3
"""
XLSX の各シートを CSV に変換する。
出力: 同一ディレクトリに {元ファイル名}_sheet_{シート名}.csv（シート1つの場合は {元ファイル名}.csv）
"""
from pathlib import Path
import re
import sys

try:
    import pandas as pd
except ImportError:
    print("pandas が必要です: pip install pandas openpyxl", file=sys.stderr)
    sys.exit(1)


def sanitize_filename(s: str) -> str:
    """ファイル名に使えない文字をアンダースコアに置換"""
    return re.sub(r'[\\/*?:"<>|]', "_", s).strip() or "sheet"


def xlsx_to_csv(xlsx_path: Path, out_dir: Path) -> list[Path]:
    """
    XLSX の各シートを CSV に変換し out_dir に保存する。
    返り値: 生成した CSV の Path のリスト。
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = xlsx_path.stem
    created = []

    xl = pd.ExcelFile(xlsx_path)
    for i, sheet_name in enumerate(xl.sheet_names):
        df = pd.read_excel(xl, sheet_name=sheet_name)
        safe_name = sanitize_filename(str(sheet_name))
        if len(xl.sheet_names) == 1:
            out_name = f"{stem}.csv"
        else:
            out_name = f"{stem}_sheet_{safe_name}.csv"
        out_path = out_dir / out_name
        df.to_csv(out_path, index=False, encoding="utf-8-sig")
        created.append(out_path)
    return created


def main():
    if len(sys.argv) < 3:
        print("Usage: convert_xlsx_to_csv.py <input.xlsx> <output_dir>", file=sys.stderr)
        sys.exit(2)
    xlsx_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    if not xlsx_path.is_file() or xlsx_path.suffix.lower() not in (".xlsx", ".xls"):
        print(f"Not an Excel file: {xlsx_path}", file=sys.stderr)
        sys.exit(3)
    paths = xlsx_to_csv(xlsx_path, out_dir)
    for p in paths:
        print(p)


if __name__ == "__main__":
    main()
