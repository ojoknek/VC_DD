---
name: dd-copy-classify
description: 案件ルート内の 業務整理用 から dd materials への資料分類・配置。ステップ2。コマンド /dd:copy または dd_copy_materials の実行時に適用する。
---

# DD 資料分類・配置（ステップ2）

**案件ルート**内の `業務整理用/` フォルダのファイルを、対応表に従い同案件の `dd materials/` の各セクションにコピーして分類する。

## コマンド・プロンプト

- **コマンド**: `/dd:copy`（対象は指定した案件ルート）
- **実行**: このスキルの手順・対応表に従う

## 作業内容

1. **案件ルート**（例: `deals/株式会社ABC`）を確認する
2. 当該案件の `業務整理用/` フォルダ内の各フォルダを確認する
3. **`program/` を使ってプログラムを実行する**（コピー＋変換を一括実行）:
   - **実行するスクリプト**: `program/run_copy.py`（リポジトリ内の `program/` フォルダ）
   - リポジトリルートで: `pip install -r program/requirements.txt`（初回のみ）
   - **案件ルートを指定して**: `python program/run_copy.py <案件ルート>` を実行する（例: `python program/run_copy.py deals/株式会社ABC`）
   - **変換処理**（`program/` 内で実行）:
     - **PDF** → `program/convert_pdf_to_png.py` により 1 ページごとに PNG 画像（`{元ファイル名}_page_001.png` 等）に変換して配置
     - **XLSX/XLS** → `program/convert_xlsx_to_csv.py` により各シートを CSV（`{元ファイル名}_sheet_{シート名}.csv` 等）に変換して配置
     - 上記以外 → そのままコピー
4. **元のファイルは `業務整理用/` に残す**（バックアップとして）
5. 必要に応じて、対応表に従い手動で不足分を補うか、ファイル名・フォルダ構造を確認する

## 変換した資料の保存先

**変換・コピーした資料は、案件ルートの `dd materials/` のそれぞれのフォルダに保存される。**

- 保存先は **案件ルート/dd materials/** の直下の対応表のとおりのパス（例: `deals/株式会社ABC/dd materials/financial/税務申告表/`、`deals/株式会社ABC/dd materials/pitch slide/` 等）。
- フォルダ構成は **`dd_logic/template/dd materials` と同じ**（template を `deals/{会社名}/` にコピーしたため、各案件の `dd materials/` は template と同構成）。
- PDF→PNG の結果は該当するコピー先フォルダ内に、XLSX→CSV の結果も該当するコピー先フォルダ内に保存される。

## 対応表（業務整理用 → dd materials）

| 業務整理用フォルダ | コピー先（dd materials） |
|-------------------|--------------------------|
| 01財務　税務申告表/ | financial/税務申告表/ |
| 02財務　月次試算表/ | financial/月次試算表/ |
| 03財務　月次資金繰実績・予測表/ | financial/月次資金繰実績・予測表/ |
| 04事業計画　今後の事業計画・予測表/ | business/今後の事業計画・予測表/ |
| 05株主名簿　株主名簿/ | round table/株主名簿/ |
| 06資本政策　資本政策/ | round table/資本政策表/ |
| 07事業計画　ピッチ資料（事業計画）/ | pitch slide/ |
| 08組織　組織図/ | corporate/組織図/ |
| 09組織　経営陣プロフィール/ | corporate/経営陣プロフィール/ |
| 10知財　特許リスト/ | contract/特許リスト/ |
| 11契約書　当ラウンドのタームシート/ | round table/当ラウンドのタームシート/ |
| 12契約書　過去の投資契約・株主間契約/ | round table/過去の投資契約・株主間契約/ |
| 13登記簿　履歴事項全部証明書/ | contract/履歴事項全部証明書/ |
| 14組織図　主な退職者及び退職理由/ | corporate/主な退職者及び退職理由/ |
| 15契約書　顧客との契約書/ | contract/顧客との契約書/ |
| 16契約書　代理店契約書/ | contract/代理店契約書/ |
| 17契約書　政府補助金契約書/ | contract/政府補助金契約書/ |
| 18契約書　負債に関する契約/ | contract/負債に関する契約/ |
| 19契約書　営業資料/ | business/営業資料/ |

## プログラム（`program/`）

- **メイン**: `program/run_copy.py` — 案件ルートを引数で指定し、当該案件の 業務整理用 → dd materials をコピー。その過程で **PDF→PNG**（`convert_pdf_to_png`）・**XLSX→CSV**（`convert_xlsx_to_csv`）を呼び出して変換し、**変換結果は案件ルートの `dd materials/` の各フォルダ**（対応表のコピー先）に保存する。
- **実行例**: `python program/run_copy.py deals/株式会社ABC`
- **依存**: `program/requirements.txt`（pymupdf, openpyxl, pandas）
- **保存先の詳細**: [program/README.md](../../program/README.md) の「変換結果の保存先」を参照

## 注意事項

- コピー後、ファイル名やフォルダ構造が適切か確認する
- 重複ファイルがないか確認する

## 次ステップ

- ステップ2.5: サマリ作成 → dd-summarize スキル / `/dd:summarize`
