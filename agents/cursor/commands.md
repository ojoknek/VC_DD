# 擬似スラッシュコマンド設計（DD Template）

このファイルは、`DD方法.md` と `README.md` の作業フローを **“擬似スラッシュコマンド”** として呼び出せるように設計したものです。  
Cursorに依頼する際は、依頼文の先頭にコマンド名を付けてください（実際の機能としてのスラッシュコマンドではなく運用ルールです）。

---

## 使い方（基本形）

### 1) コマンドで呼ぶ

- 例: `/dd:init 会社名="XXX" 対象期間="2024-2025"` を実行して

### 2) 具体プロンプトで呼ぶ（推奨）

- 例: `@agents/prompts/dd_init.md` をこの案件に合わせて実行して

---

## コマンド一覧（DD方法/READMEの流れに対応）

### /dd:init（初期セットアップ一括）

- **目的**: これまで `DD方法.md` を読んで開始していた初期一連（資料配置→サマリ→主要更新→初期レビューのキックオフ）をまとめて進行する
- **入力**: 会社名、対象期間、資料の現状（`業務整理用/` に入っているか等）
- **主な成果物**:
  - `dd materials/*` のサマリ更新
  - `dd materials/business/事業概要.md` 更新（必要に応じて）
  - `dd materials/round table/投資条件概要.md` 更新（必要に応じて）
  - `review_and_hypothesis/dd question/ヒアリングリスト.md` 更新（必要に応じて）
- **実行プロンプト**: `agents/prompts/dd_init.md`

### /dd:copy（業務整理用→dd materials へ配置）

- **目的**: `業務整理用/` の資料を対応表に従い `dd materials/` にコピー（バックアップは残す）
- **入力**: 追加された資料の場所、コピー方針（全件/差分）
- **実行プロンプト**: `agents/prompts/dd_copy_materials.md`
- **参照**: `agents/cursor/dd_method/01_copy_and_classify.md`

### /dd:summarize（非mdファイルのサマリ追記）

- **目的**: 各フォルダ内の **Markdown以外（PDF/Excel/Word/画像等）** を洗い出し、`{フォルダ名}サマリ.md` に追記/新規作成する
- **入力**: 対象フォルダ（例: `dd materials/business/今後の事業計画・予測表/`）
- **実行プロンプト**: `agents/prompts/dd_summarize_folder.md`
- **参照**: `agents/cursor/dd_method/02_summarize_files.md`

### /dd:update_basics（事業概要/投資条件の更新）

- **目的**: DDの核となる「事業概要」「投資条件」を素材から更新する
- **入力**: 会社名、対象期間、参照すべき資料（ピッチ/事業計画/ターム等）
- **実行プロンプト**:
  - 事業: `agents/prompts/dd_update_business_overview.md`
  - 投資条件: `agents/prompts/dd_update_investment_terms.md`
- **参照**: `agents/cursor/dd_method/03_update_basics.md`

### /dd:questions（ヒアリングリスト更新）

- **目的**: 事業概要/投資条件の更新結果を元に、質問を具体化・重複排除・優先度付けする
- **入力**: 既に把握している前提、意思決定で重要な論点
- **実行プロンプト**: `agents/prompts/dd_update_hearing_list.md`
- **参照**: `agents/cursor/dd_method/04_update_questions.md`

### /dd:review（初期レビュー）

- **目的**: `dd materials/` と `research/` を読み、評価結果を `review_and_hypothesis/` に整理する
- **入力**: 対象領域（事業/契約/組織/財務/投資条件/市場）
- **実行プロンプト（領域別）**:
  - 事業: `agents/prompts/review_business.md`
  - 契約: `agents/prompts/review_contracts.md`
  - 組織: `agents/prompts/review_corporate.md`
  - 財務: `agents/prompts/review_financial.md`
  - 投資条件: `agents/prompts/review_roundtable.md`
  - 市場・競合: `agents/prompts/review_market_competitors.md`
  - 市場機会: `agents/prompts/review_market_opportunity.md`
- **参照**: `agents/cursor/dd_method/05_initial_review.md`

### /dd:thesis（投資仮説の作成）

- **目的**: 初期レビューを踏まえ、投資テーゼと複数シナリオ（楽観/現実/悲観）を構築する
- **入力**: 投資方針、期待リターン、制約条件
- **実行プロンプト**: `agents/prompts/dd_build_thesis.md`
- **参照**: `agents/cursor/dd_method/06_investment_hypotheses.md`

### /dd:research（リサーチ追加）

- **目的**: 仮説に紐づくリサーチテーマを追加し、`research/` を更新する
- **入力**: 調査テーマ、対象市場/競合、仮説で埋めたい穴
- **実行プロンプト**: `agents/prompts/dd_research_add.md`
- **参照**: `agents/cursor/dd_method/07_research.md`

### /dd:resource（参考資料の追加：Web/Notion）

- **目的**: 参考になった情報を `dd materials/web resource/` または `research/` に保存し、必要に応じてレビューへ反映する
- **入力**: URL/出典、要点、投資判断との関連
- **実行プロンプト**:
  - Web: `agents/prompts/dd_add_web_resource.md`
  - Notion: `agents/prompts/dd_add_notion_resource.md`
- **参照**: `agents/cursor/dd_method/08_resources.md`

### /dd:ic_slide（投資委員会資料の骨格更新）

- **目的**: `review_and_hypothesis/投資委員会資料作成/スライドスケルトン.md` を他資料からアップデート
- **入力**: 投資委員会で強調したい論点、結論の方向性
- **実行プロンプト**: `agents/prompts/dd_update_ic_slides.md`

### /dd:wrap（完了報告）

- **目的**: チェックリストで完了状態を確認し、次のステップ（追加ヒアリング/追加調査）を明確化する
- **入力**: 現時点の進捗、未解決の論点
- **実行プロンプト**: `agents/prompts/dd_completion_report.md`
- **参照**: `agents/cursor/dd_method/09_completion.md`


