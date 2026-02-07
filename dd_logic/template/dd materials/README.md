# dd materials（ひな形）

このフォルダは **新規案件の `dd materials/` のひな形**です。template を `deals/{会社名}/` にコピーすると、各案件の `dd materials/` がこの構成で作成されます。

## /dd:copy 実行時の保存先

**`/dd:copy` 実行時、変換した資料（PDF→PNG・XLSX→CSV）およびコピーしたファイルの保存先は、この template の `dd materials` ではなく、当該案件の `dd materials/` です。**

- **保存先**: **案件ルート/dd materials/** のそれぞれのフォルダ（例: `deals/株式会社ABC/dd materials/financial/税務申告表/`、`deals/株式会社ABC/dd materials/pitch slide/` 等）
- **フォルダ構成**: この template の `dd materials` と同じ構成（対応表のコピー先に従う）
- **実行プログラム**: `program/run_copy.py`（PDF→PNG は `program/convert_pdf_to_png.py`、XLSX→CSV は `program/convert_xlsx_to_csv.py` を使用）

詳細は [program/README.md](../../../program/README.md) の「変換結果の保存先」を参照。
