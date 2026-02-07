# DD 資料コピー・変換プログラム

**案件ルート**内の `業務整理用/` から `dd materials/` へ、対応表に従ってファイルをコピーする際に次の変換を行う。  
擬似コマンド **`/dd:copy`** 実行時、Cursor がこのスクリプトを **案件ルートを引数で指定して** 呼び出す想定。

- **PDF** → 1 ページごとに PNG 画像（`{元ファイル名}_page_001.png` など）
- **XLSX / XLS** → 各シートを CSV（複数シートの場合は `{元ファイル名}_sheet_{シート名}.csv`）
- **上記以外** → そのままコピー

元ファイルは `業務整理用/` に残す（バックアップ）。

## /dd:copy 実行時の流れ

1. Cursor に「案件は deals/株式会社ABC で /dd:copy を実行して」と依頼する。
2. エージェントは **`program/run_copy.py`** を **案件ルートを引数で** 実行する（例: `python program/run_copy.py deals/株式会社ABC`）。
3. `run_copy.py` は当該案件の `業務整理用/` を走査し、対応表（COPY_MAP）に従って各フォルダ内のファイルを処理する。
4. **PDF** は `program/convert_pdf_to_png.py` により 1 ページごとに PNG に変換し、**XLSX/XLS** は `program/convert_xlsx_to_csv.py` によりシートごとに CSV に変換する。その他はそのままコピーする。
5. **変換・コピーしたファイルの保存先**は、次の「変換結果の保存先」のとおり。

## 変換結果の保存先

**変換した資料（PDF→PNG・XLSX→CSV）およびそのままコピーしたファイルは、すべて 案件ルートの `dd materials/` のそれぞれのフォルダに保存される。**

- **基準パス**: `案件ルート/dd materials/`（例: `deals/株式会社ABC/dd materials/`）
- **フォルダ構成**: **`dd_logic/template/dd materials` と同じ構成**（template を deals/{会社名} にコピーしているため）。対応表（COPY_MAP）の「コピー先」に従い、次のようなサブフォルダに保存される。

| 保存先（dd materials 直下） | 例（案件ルートが deals/株式会社ABC の場合） |
|----------------------------|--------------------------------------------|
| financial/税務申告表/ | deals/株式会社ABC/dd materials/financial/税務申告表/ |
| financial/月次試算表/ | deals/株式会社ABC/dd materials/financial/月次試算表/ |
| financial/月次資金繰実績・予測表/ | deals/株式会社ABC/dd materials/financial/月次資金繰実績・予測表/ |
| business/今後の事業計画・予測表/ | deals/株式会社ABC/dd materials/business/今後の事業計画・予測表/ |
| round table/株主名簿/ | deals/株式会社ABC/dd materials/round table/株主名簿/ |
| round table/資本政策表/ | deals/株式会社ABC/dd materials/round table/資本政策表/ |
| pitch slide/ | deals/株式会社ABC/dd materials/pitch slide/ |
| corporate/組織図/ | deals/株式会社ABC/dd materials/corporate/組織図/ |
| corporate/経営陣プロフィール/ | deals/株式会社ABC/dd materials/corporate/経営陣プロフィール/ |
| contract/特許リスト/ | deals/株式会社ABC/dd materials/contract/特許リスト/ |
| …（その他は run_copy.py の COPY_MAP を参照） | … |

- **PDF→PNG**: 該当する業務整理用フォルダに PDF がある場合、上記の対応する `dd materials/` のフォルダに、ページごとの PNG が保存される。
- **XLSX→CSV**: 該当する業務整理用フォルダに XLSX/XLS がある場合、上記の対応する `dd materials/` のフォルダに、シートごとの CSV が保存される。
- **dd_logic/template/dd materials** はひな形のため、**直接書き込まない**。書き込み先は常に **案件ルート（例: deals/株式会社ABC）の `dd materials/`**。

## 案件ルートについて

- 新構成では案件ごとに **案件ルート**（例: `deals/株式会社ABC`）があり、その直下に `業務整理用/` と `dd materials/` がある。
- 本プログラムは **案件ルート** を指定して実行する。指定がなければリポジトリルートを案件ルートとして扱う（後方互換）。

## 使い方

**案件を指定して実行（推奨）** — リポジトリルートで:

```bash
program/.venv/bin/python program/run_copy.py deals/株式会社ABC
```

または `run.sh` で（初回は venv 作成＋インストール）:

```bash
./program/run.sh deals/株式会社ABC
```

**環境変数で指定**:

```bash
export DEAL_ROOT=deals/株式会社ABC
./program/run.sh
```

**案件ルートを省略**（リポジトリ直下に `業務整理用/` と `dd materials/` がある場合の後方互換）:

```bash
./program/run.sh
```

**venv の準備（初回）**:

```bash
python3 -m venv program/.venv
program/.venv/bin/pip install -r program/requirements.txt
```

## 依存

- Python 3.10+
- `pymupdf`（PDF→PNG）
- `pandas`, `openpyxl`（XLSX→CSV）

## 個別変換のみ使う場合

- PDF → PNG: `python program/convert_pdf_to_png.py <input.pdf> <output_dir>`
- XLSX → CSV: `python program/convert_xlsx_to_csv.py <input.xlsx> <output_dir>`
