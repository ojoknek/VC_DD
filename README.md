# DD Template（デューデリジェンステンプレート）

スタートアップへの投資判断に必要な情報を**体系的に整理し、評価する**ための標準DDフレームワークです。**案件ごとに `deals/{会社名}/` で新規案件を蓄積**し、`.cursor/skills` の擬似コマンドで再現性高く進められます。

---

## 📋 このテンプレートでできること

- **新規案件の蓄積**: `deals/` に会社ごとのフォルダを用意し、`dd_logic/template` をコピーしてセットを開始
- **資料の分類・配置**: 各案件の `業務整理用/` に置いたファイルを、同案件の `dd materials/` へ対応表に従ってコピー（**PDF→PNG**・**XLSX→CSV** 変換を含む）
- **サマリ作成**: PDF・Excel・Word等の内容を各フォルダの `{フォルダ名}サマリ.md` に記載
- **基本情報の更新**: 事業概要・投資条件を入手資料から反映
- **ヒアリングリスト**: 質問の具体化・重複排除・優先度付け
- **初期レビュー**: 事業・契約・組織・財務・投資条件・市場の評価を `review_and_hypothesis/` に整理
- **投資仮説**: 投資テーゼ・シナリオ・MOAT・出口・リスクの構築（共通思考法は `dd_logic/investment_methodology/` を参照）
- **リサーチ・参考資料**: 調査結果とWeb/Notion情報の保存
- **完了報告**: チェックリストに基づく確認と次ステップの明確化

---

## 🚀 実際の使い方（一連の流れ）

### 前提

- **案件ルート**: 1件のDD案件のフォルダのルート。例: `deals/株式会社ABC`
- すべての擬似コマンドは **「案件は deals/株式会社ABC」** のように案件ルートを指定して実行する
- パス（`dd materials/`、`業務整理用/`、`review_and_hypothesis/` 等）は **案件ルート相対** で解釈する

### ステップ1: 新規案件フォルダを作る

1. `dd_logic/template` を `deals/{会社名}/` にコピーする。
   ```bash
   cp -r dd_logic/template deals/株式会社ABC
   ```
2. これで `deals/株式会社ABC/` の直下に  
   `業務整理用/`・`dd materials/`・`research/`・`review_and_hypothesis/` ができる。

### ステップ2: 資料を案件の「業務整理用」に置く

- **対象**: `deals/株式会社ABC/業務整理用/`
- **対応表に従ったフォルダ名**でファイルを配置する。  
  例: `01財務　税務申告表/`、`07事業計画　ピッチ資料（事業計画）/` など。  
  対応表は [.cursor/skills/dd-copy-classify/SKILL.md](.cursor/skills/dd-copy-classify/SKILL.md) または [program/run_copy.py](program/run_copy.py) 内の COPY_MAP を参照。
- **サンプルで試す場合**: `dd_logic/template/業務整理用` に対応表どおりのフォルダとサンプルファイルを用意しておき、template を `deals/会社名` にコピーすれば、そのまま `/dd:copy` の入力になる。

### ステップ3: 資料のコピー・変換（/dd:copy）

- **依頼例**: 「案件は deals/株式会社ABC で /dd:copy を実行して」
- **実行内容**: **`program/run_copy.py`** を案件ルートを引数で実行する。案件ルート内の `業務整理用/` を読み、対応表に従って **案件ルートの `dd materials/` のそれぞれのフォルダ** へコピー・変換する。
  - **PDF** → `program/convert_pdf_to_png.py` により 1 ページごとに PNG に変換して配置
  - **XLSX/XLS** → `program/convert_xlsx_to_csv.py` によりシートごとに CSV に変換して配置
  - その他 → そのままコピー  
  変換した資料の**保存先**は **案件ルート/dd materials/** の各フォルダ（`dd_logic/template/dd materials` と同じ構成）。元ファイルは `業務整理用/` に残す。
- **実行例**: `python program/run_copy.py deals/株式会社ABC`  
  詳細・保存先一覧は [program/README.md](program/README.md)（「/dd:copy 実行時の流れ」「変換結果の保存先」）を参照。

### ステップ4: 初期セットアップを一括で進める（任意）

- **依頼例**: 「案件は deals/株式会社ABC で /dd:init 会社名="株式会社ABC" 対象期間="2024-2025" を実行して」
- **実行内容**: ステップ2（資料配置＝上記コピー・変換）→ 2.5（サマリ作成）→ 3（事業概要・投資条件更新）→ 4（ヒアリングリスト更新）を一括で実行。  
  内部で `run_copy.py` に案件ルートを渡し、続けてサマリ・基本情報・ヒアリングリストを更新する。

### ステップ5: レビュー・投資仮説・リサーチ・資料整理

- **初期レビュー**: 「案件は deals/株式会社ABC で /dd:review を実行して」  
  → `dd materials/` と `research/` を読み、`review_and_hypothesis/review_results/` 等に評価を記載。
- **投資仮説**: 「案件は deals/株式会社ABC で /dd:thesis を実行して」  
  → `dd_logic/investment_methodology/` を参照しつつ、当該案件の投資テーゼ・シナリオ等を `review_and_hypothesis/senario/` 等に記載。
- **リサーチ**: 「案件は deals/株式会社ABC で /dd:research を実行して」  
  → 調査結果を `research/` にまとめる。
- **参考資料**: 「案件は deals/株式会社ABC で /dd:resource を実行して」  
  → Web/Notion の参照を `dd materials/web resource/` に整理。
- **投資委スライド骨格**: 「案件は deals/株式会社ABC で /dd:ic_slide を実行して」  
  → `review_and_hypothesis/投資委員会資料作成/スライドスケルトン.md` を更新。
- **完了報告**: 「案件は deals/株式会社ABC で /dd:wrap を実行して」  
  → チェックリストで完了確認と次ステップを整理。

---

## 📊 各コマンドの状況と参照関係

| コマンド | 内容 | 前提 | 実行・成果物 | 参照スキル |
|----------|------|------|--------------|------------|
| — | ガイドライン確認 | — | dd-common・DD手順の確認 | dd-common |
| `/dd:init` | 初期セットアップ一括 | 案件フォルダ存在、業務整理用に資料配置済み | 2〜4を順に実行（run_copy.py に案件ルートを渡す） | dd-init |
| `/dd:copy` | 資料分類・配置 | 案件の業務整理用に対応表のフォルダ名でファイルあり | program/run_copy.py を実行。PDF→PNG・XLSX→CSV は program で変換。変換結果は **案件ルート/dd materials/ の各フォルダ**（template と同じ構成）に保存 | dd-copy-classify |
| `/dd:summarize` | サマリ作成 | dd materials にコピー済み | 各フォルダの `{フォルダ名}サマリ.md` に非mdファイルのサマリを記載 | dd-summarize |
| `/dd:update_basics` | 事業概要・投資条件更新 | dd materials に資料あり | 事業概要.md・投資条件概要.md を更新 | dd-update-basics |
| `/dd:questions` | ヒアリングリスト更新 | 事業概要・投資条件を反映済み推奨 | ヒアリングリスト.md を具体化・優先度付け | dd-hearing-list |
| `/dd:review` | 初期レビュー | dd materials・research に資料あり | review_and_hypothesis/review_results/ に領域別評価 | dd-initial-review |
| `/dd:thesis` | 投資仮説 | 初期レビュー済み推奨 | investment_methodology 参照しつつ senario/strength/risk 等を更新 | dd-investment-thesis |
| `/dd:research` | リサーチ追加 | 投資仮説・テーマに応じて | research/ に調査結果をまとめ | dd-research |
| `/dd:resource` | 参考資料整理 | — | dd materials/web resource/ に Web/Notion を保存 | dd-resources |
| `/dd:ic_slide` | 投資委資料骨格 | dd materials・review_and_hypothesis に情報あり | スライドスケルトン.md を更新 | dd-ic-slides |
| `/dd:wrap` | 完了報告 | 各ステップの完了状況に応じて | チェックリストで確認・次ステップを明文化 | dd-completion |

- **入口・一覧**: [.cursor/skills/dd-workflow/SKILL.md](.cursor/skills/dd-workflow/SKILL.md)  
- **コマンド一覧・品質基準・案件ルート**: [.cursor/skills/dd-common/SKILL.md](.cursor/skills/dd-common/SKILL.md)  
- **ステップ詳細（目的・対応表・注意）**: [.cursor/skills/dd-workflow/DD手順.md](.cursor/skills/dd-workflow/DD手順.md)  
- **スキル一覧**: [.cursor/skills/README.md](.cursor/skills/README.md)

---

## 📁 ディレクトリ構成

```
DD_template/
├── .cursor/skills/              # Cursor Agent Skills（DD手順で要素分解）
│   ├── README.md                # スキル一覧・案件ルートの説明
│   ├── dd-workflow/             # 入口＋DD手順（DD手順.md）
│   ├── dd-common/               # 共通ルール・案件ルート・品質基準・コマンド一覧
│   └── dd-*                     # 各ステップスキル（copy, summarize, init, …）
├── deals/                        # 新規案件の蓄積（会社ごとに1フォルダ）
│   └── {会社名}/                 # 案件ルート（dd_logic/template のコピー）
│       ├── 業務整理用/           # インポートしたファイルの置き場（コピー元・残す）
│       ├── dd materials/        # インプット（コピー・変換後の事業・契約・財務等）
│       ├── review_and_hypothesis/ # アウトプット（評価・ヒアリング・投資仮説・リスク等）
│       └── research/            # リサーチ結果（市場・競合・業界課題・M&A/IPO事例等）
├── dd_logic/
│   ├── template/                # 新規案件のひな形（deals/{会社名} にコピーして使う）
│   │   └── 業務整理用/           # 対応表のフォルダ名で資料を置く（README あり）
│   └── investment_methodology/  # 全案件に通底する投資思考法（人間が記述するテンプレート）
├── program/                      # 資料コピー・変換（run_copy.py：案件ルートを指定して実行）
└── README.md                     # 本ファイル
```

---

## 📝 主要な参照先

| 用途 | パス |
|------|------|
| DD手順（全文） | [.cursor/skills/dd-workflow/DD手順.md](.cursor/skills/dd-workflow/DD手順.md) |
| 擬似コマンド一覧・品質基準・案件ルート | [.cursor/skills/dd-common/SKILL.md](.cursor/skills/dd-common/SKILL.md) |
| DD作業の入口・スキル一覧 | [.cursor/skills/dd-workflow/SKILL.md](.cursor/skills/dd-workflow/SKILL.md) |
| チェックリスト（DD完了・週次・月次/決算） | [.cursor/skills/dd-completion/SKILL.md](.cursor/skills/dd-completion/SKILL.md) |
| 投資思考法（共通テンプレート） | [dd_logic/investment_methodology/README.md](dd_logic/investment_methodology/README.md) |
| テンプレート・投資思考法の位置づけ | [dd_logic/README.md](dd_logic/README.md) |
| 資料コピー・変換の使い方 | [program/README.md](program/README.md) |

評価結果・投資仮説の出力先は各案件の `review_and_hypothesis/`。共通の「どう考えるか」は `dd_logic/investment_methodology/` を参照。

---

## 💡 使い方のコツ

- **案件ルートを明示する**: 依頼時に「案件は deals/株式会社ABC」のように指定する
- **段階的に進める**: 一度に完璧にせず、全体像を把握してから詳細を詰める
- **整合性を確認する**: 各ステップ完了時に、前のステップとの数値・記載の一致を確認
- **根拠を残す**: 判断の根拠や仮説は必ず文書化し、参照資料を明記する
- **不足は明示する**: 推測で埋めず、「未確認」「要ヒアリング」として残す

---

## ⚠️ 注意事項

- **業務整理用**: 各案件の `業務整理用/` の元ファイルは残す（バックアップ）。コピー先は当該案件の `dd materials/` のみ更新
- **数値**: 事業計画・投資条件・財務の数値は整合性を常に確認
- **評価**: 客観的に行い、根拠となる資料を併記する。共通の評価観点は `dd_logic/investment_methodology/` を参照

---

## 🔄 更新履歴

| 時期 | 内容 |
|------|------|
| 2025年11月 | 初版作成 |
| 2026年1月 | 更新版・擬似コマンドシステムへの再構成 |
| 2026年2月 | Cursor Agent Skill（dd-workflow）追加。DD手順をスキル内に格納 |
| 2026年2月 | Skills を DD手順で要素分解。dd-workflow は入口に |
| 2026年2月 | agents/ を廃止し、機能を .cursor/skills/ に完全移管 |
| 2026年2月 | **deals 構成に変更**。案件ごとに deals/{会社名}、業務整理用は案件内。dd_logic/investment_methodology で全案件通底の投資思考法テンプレートを追加 |
| 2026年2月 | README を実際の使い方・各コマンドの状況・参照関係で整理 |

---

**作成者**: ojoknek  
**用途**: スタートアップ企業への投資判断・デューデリジェンス  
**ライセンス**: 本ドキュメントの著作権は ojoknek に帰属し、無断転載・配布を禁じます。
