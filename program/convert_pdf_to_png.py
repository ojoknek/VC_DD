#!/usr/bin/env python3
"""
PDF を 1 ページずつ PNG 画像に変換する。
出力: 同一ディレクトリに {元ファイル名}_page_001.png, _page_002.png, ...
"""
from pathlib import Path
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF が必要です: pip install pymupdf", file=sys.stderr)
    sys.exit(1)


def pdf_to_pngs(pdf_path: Path, out_dir: Path, dpi: int = 150) -> list[Path]:
    """
    PDF の各ページを PNG に変換し out_dir に保存する。
    返り値: 生成した PNG の Path のリスト。
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = pdf_path.stem
    created = []

    doc = fitz.open(pdf_path)
    try:
        for i in range(len(doc)):
            page = doc[i]
            pix = page.get_pixmap(dpi=dpi, alpha=False)
            out_name = f"{stem}_page_{i + 1:03d}.png"
            out_path = out_dir / out_name
            pix.save(str(out_path))
            created.append(out_path)
    finally:
        doc.close()

    return created


def main():
    if len(sys.argv) < 3:
        print("Usage: convert_pdf_to_png.py <input.pdf> <output_dir>", file=sys.stderr)
        sys.exit(2)
    pdf_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    if not pdf_path.is_file() or not pdf_path.suffix.lower() == ".pdf":
        print(f"Not a PDF file: {pdf_path}", file=sys.stderr)
        sys.exit(3)
    paths = pdf_to_pngs(pdf_path, out_dir)
    for p in paths:
        print(p)


if __name__ == "__main__":
    main()
