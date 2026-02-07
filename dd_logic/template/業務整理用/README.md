# 業務整理用（インポート資料の置き場）

このフォルダに、**対応表に従ったフォルダ名**でインポートしたファイルを配置してください。

- **template を `deals/{会社名}/` にコピーしたあと**、各案件の `業務整理用/`（このフォルダのコピー先）に資料を追加・配置する。
- **`/dd:copy` 実行時**（案件ルートを指定して）:
  - **実行されるプログラム**: リポジトリの **`program/run_copy.py`**。PDF→PNG は `program/convert_pdf_to_png.py`、XLSX→CSV は `program/convert_xlsx_to_csv.py` により変換される。
  - **読み取り元**: 当該案件の `業務整理用/`（ここに置いたファイルが対象）。
  - **保存先**: 変換・コピーした資料は **当該案件の `dd materials/` のそれぞれのフォルダ** に保存される（`dd_logic/template/dd materials` と同じフォルダ構成。例: `deals/株式会社ABC/dd materials/financial/税務申告表/`、`deals/株式会社ABC/dd materials/pitch slide/` 等）。詳細は [program/README.md](../../../program/README.md) の「変換結果の保存先」を参照。
  - 元ファイルは `業務整理用/` に残す（バックアップ）。
- **対応表**: [.cursor/skills/dd-copy-classify/SKILL.md](../../../.cursor/skills/dd-copy-classify/SKILL.md) または `program/run_copy.py` 内の COPY_MAP。

例: `01財務　税務申告表/`、`07事業計画　ピッチ資料（事業計画）/` など。
