# デューデリジェンス（DD）作業ガイド

## はじめに

このガイドは、投資判断に必要な情報を体系的に整理し、評価を行うための標準的な手順を示しています。

**重要**: このリポジトリでは、**擬似スラッシュコマンドシステム**を使ってCursorに作業を依頼できます。各ステップは、コマンドまたはプロンプトファイルを参照することで実行できます。

### 擬似コマンドシステムとは

Cursorに作業を依頼する際、以下の2つの方法があります：

1. **コマンド形式**: `/dd:init 会社名="XXX" 対象期間="2024-2025"` を実行して
2. **プロンプトファイル参照**: `@agents/prompts/dd_init.md` をこの案件に合わせて実行して

各コマンドの詳細は `agents/cursor/commands.md` を参照してください。

### このガイドの構成

- **概要**: このファイル（`DD手順.md`）で全体像を把握
- **詳細手順**: `agents/cursor/dd_method/` 配下の各ステップファイルを参照
- **実行プロンプト**: `agents/prompts/` 配下のプロンプトファイルを使用

---

## DD作業の全体像

DD作業は、以下の9つのステップで構成されています。各ステップは独立して実行できますが、通常は順番に進めることで効率的に作業を進められます。

### ステップ1: ガイドラインの確認

まず、以下のファイルを確認して全体像を把握してください：

- **全体像**: `agents/cursor/dd_method/00_overview.md`
- **擬似コマンド一覧**: `agents/cursor/commands.md`
- **システム指示書**: `agents/cursor/system.md`

**確認事項**:
- 作業の全体像を理解する
- 各ステップの目的を確認する
- 必要な資料の所在を把握する

---

### ステップ2: 業務整理用資料の分類・配置

**目的**: `業務整理用/` フォルダ内のファイルを、`dd materials/` の各セクションに適切にコピーして分類します。

**コマンド**: `/dd:copy` または `@agents/prompts/dd_copy_materials.md`  
**詳細**: `agents/cursor/dd_method/01_copy_and_classify.md`

**対応表**:

| 業務整理用フォルダ | コピー先（dd materials） |
|------------------|------------------------|
| `01財務　税務申告表/` | `financial/税務申告表/` |
| `02財務　月次試算表/` | `financial/月次試算表/` |
| `03財務　月次資金繰実績・予測表/` | `financial/月次資金繰実績・予測表/` |
| `04事業計画　今後の事業計画・予測表/` | `business/今後の事業計画・予測表/` |
| `05株主名簿　株主名簿/` | `round table/株主名簿/` |
| `06資本政策　資本政策/` | `round table/資本政策表/` |
| `07事業計画　ピッチ資料（事業計画）/` | `dd materials/pitch slide/` |
| `08組織　組織図/` | `corporate/組織図/` |
| `09組織　経営陣プロフィール/` | `corporate/経営陣プロフィール/` |
| `10知財　特許リスト/` | `contract/特許リスト/` |
| `11契約書　当ラウンドのタームシート/` | `round table/当ラウンドのタームシート/` |
| `12契約書　過去の投資契約・株主間契約/` | `round table/過去の投資契約・株主間契約/` |
| `13登記簿　履歴事項全部証明書/` | `contract/履歴事項全部証明書/` |
| `14組織図　主な退職者及び退職理由/` | `corporate/主な退職者及び退職理由/` |
| `15契約書　顧客との契約書/` | `contract/顧客との契約書/` |
| `16契約書　代理店契約書/` | `contract/代理店契約書/` |
| `17契約書　政府補助金契約書/` | `contract/政府補助金契約書/` |
| `18契約書　負債に関する契約/` | `contract/負債に関する契約/` |
| `19契約書　営業資料/` | `business/営業資料/` |

**注意**: 元のファイルは `業務整理用/` フォルダに残しておきます（バックアップとして）。

---

### ステップ2.5: 各フォルダ内のファイルサマリの作成

**目的**: コピーしたファイルのうち、Markdownファイル以外（PDF、Excel、Word、画像等）のサマリを、各フォルダ内の `{フォルダ名}サマリ.md` に記載します。

**コマンド**: `/dd:summarize` または `@agents/prompts/dd_summarize_folder.md`  
**詳細**: `agents/cursor/dd_method/02_summarize_files.md`

**サマリに記載する内容**:
- 基本情報（ファイル名、形式、サイズ、更新日時）
- 内容サマリ
- 主要なポイント
- 投資判断への影響

各ファイル形式（PDF、Excel、Word等）に応じて、適切な情報を抽出して記載します。

---

### ステップ3: 基本情報の更新

**目的**: 事業概要と投資条件を、入手した資料から更新します。

**コマンド**: `/dd:update_basics` または 
- `@agents/prompts/dd_update_business_overview.md`（事業概要）
- `@agents/prompts/dd_update_investment_terms.md`（投資条件）

**詳細**: `agents/cursor/dd_method/03_update_basics.md`

#### 3.1 事業概要の更新

- **対象ファイル**: `dd materials/business/事業概要.md`
- **参照資料**: ピッチ資料、事業計画書、営業資料等
- **記載内容**: 事業内容、サービス、ターゲット市場、事業モデル、過去の事業の変化・進化

#### 3.2 投資条件の更新

- **対象ファイル**: `dd materials/round table/投資条件概要.md`
- **参照資料**: タームシート、資本政策表、株主名簿等
- **記載内容**: 調達スケジュール、調達条件、資金使途、評価額、調達額、資金使途の内訳

**確認事項**: 数値の整合性、記載漏れ、日付や期間の正確性

---

### ステップ4: ヒアリングリストの更新

**目的**: 更新した事業概要と投資条件を元に、質問を具体化・重複排除・優先度付けします。

**コマンド**: `/dd:questions` または `@agents/prompts/dd_update_hearing_list.md`  
**詳細**: `agents/cursor/dd_method/04_update_questions.md`

- **対象ファイル**: `review_and_hypothesis/dd question/ヒアリングリスト.md`
- **作業内容**: 
  - 既に把握している情報を反映
  - 不足している情報を特定
  - 優先度の高い質問項目を明確化
  - 事業概要や投資条件に関連する質問を追加・調整

---

### ステップ5: 初期レビューの実践

**目的**: `dd materials/` と `research/` フォルダ内の資料を読み込み、評価結果を `review_and_hypothesis/` フォルダ内に整理します。

**コマンド**: `/dd:review` または領域別に：
- `@agents/prompts/review_business.md`（事業性評価）
- `@agents/prompts/review_contracts.md`（契約書レビュー）
- `@agents/prompts/review_corporate.md`（組織評価）
- `@agents/prompts/review_financial.md`（財務評価）
- `@agents/prompts/review_roundtable.md`（投資条件評価）
- `@agents/prompts/review_market_competitors.md`（市場・競合評価）
- `@agents/prompts/review_market_opportunity.md`（市場機会評価）

**詳細**: `agents/cursor/dd_method/05_initial_review.md`

#### レビュー対象と出力先

| レビュー対象 | 評価結果ファイル | 評価観点 |
|------------|----------------|---------|
| `dd materials/business/` | `review_and_hypothesis/review_results/事業性評価.md` | 事業モデル、市場ポジション、成長性、競合優位性 |
| `dd materials/contract/` | `review_and_hypothesis/review_results/契約書レビュー.md` | 法的リスク、財務的影響、事業リスク |
| `dd materials/corporate/` | `review_and_hypothesis/review_results/組織評価.md` | 経営陣の質、組織体制、人材、継続性 |
| `dd materials/financial/` | `review_and_hypothesis/review_results/財務評価.md` | 財務健全性、収益性、資金繰り、財務リスク |
| `dd materials/round table/` | `review_and_hypothesis/review_results/投資条件評価.md` | 評価額の妥当性、調達条件、資金使途、出口戦略 |
| `research/market and competitors/` | `review_and_hypothesis/review_results/市場・競合評価.md` | 市場規模、成長性、競合ポジション、競争環境 |
| `research/業界課題とソリューション/` | `review_and_hypothesis/review_results/市場機会評価.md` | 業界課題、ソリューションの優位性、市場機会 |

**評価結果の記載内容**: 概要、主要な発見事項、ポジティブ要因、リスク要因、推奨事項、結論、根拠となる資料の参照先

---

### ステップ6: 投資仮説の作成

**目的**: 初期レビューを踏まえ、投資テーゼと複数シナリオ（楽観的・現実的・悲観的）を構築します。

**コマンド**: `/dd:thesis` または `@agents/prompts/dd_build_thesis.md`  
**詳細**: `agents/cursor/dd_method/06_investment_hypotheses.md`

#### 投資仮説の構成要素

- **投資テーゼ**: なぜこの企業に投資するのか
- **成長シナリオ**: どのように成長するか
- **競合優位性（MOAT）**: 持続的な優位性は何か
- **出口戦略**: どのようにリターンを得るか
- **リスク要因**: 想定されるリスクと対策

#### 更新対象ファイル

- `review_and_hypothesis/senario/investment_theory.md`: 投資理論・投資テーゼ
- `review_and_hypothesis/strength/MOAT.md`: 競合優位性
- `review_and_hypothesis/strength/競合優位性.md`: 競合優位性（日本語版）
- `review_and_hypothesis/senario/exit_plan.md`: 出口戦略
- `review_and_hypothesis/senario/m_and_a_candidate.md`: M&A候補企業
- `review_and_hypothesis/risk/リスク項目.md`: リスク要因
- `review_and_hypothesis/synergy/事業シナジー.md`: 事業シナジー
- `review_and_hypothesis/comps/DCF.md`: DCF評価
- `review_and_hypothesis/comps/EV_Sales.md`: EV/Sales評価

---

### ステップ7: リサーチテーマの設定と調査

**目的**: 投資仮説をベースに、必要なリサーチテーマを追加し、調査結果をまとめます。

**コマンド**: `/dd:research` または `@agents/prompts/dd_research_add.md`  
**詳細**: `agents/cursor/dd_method/07_research.md`

#### リサーチテーマの例

- 市場動向の調査
- 競合企業の分析
- 業界課題とソリューション
- M&A事例の調査
- IPO事例の調査
- 現場調査

#### 調査結果のまとめ方

各リサーチテーマごとにMarkdownファイルを作成し、以下を記載：
- 調査目的
- 調査方法
- 調査結果
- 主要な発見事項
- 投資判断への示唆
- 参考資料・出典

---

### ステップ8: 参考資料の整理

**目的**: リサーチ中に参考になった記事や情報を適切な場所に保存し、必要に応じてレビューへ反映します。

**コマンド**: `/dd:resource` または 
- `@agents/prompts/dd_add_web_resource.md`（Web記事）
- `@agents/prompts/dd_add_notion_resource.md`（Notion情報）

**詳細**: `agents/cursor/dd_method/08_resources.md`

#### 8.1 Web記事の保存

- **保存先**: `dd materials/web resource/Web/`
- **記載内容**: 記事のURL、公開日、主要な内容、投資判断への関連性

#### 8.2 Notion情報の保存

- **保存先**: `dd materials/web resource/Notion/`
- **記載内容**: 情報の出典（NotionページのURL等）、情報の種類、主要な内容、投資判断への関連性

**注意事項**: 著作権に注意し、必要に応じて引用元を明記。情報の信頼性を確認し、日付を記載して情報の鮮度を管理。

---

### ステップ9: 完了報告

**目的**: 全ての作業が完了したら、完了状態を確認し、次のステップを明確化します。

**コマンド**: `/dd:wrap` または `@agents/prompts/dd_completion_report.md`  
**詳細**: `agents/cursor/dd_method/09_completion.md`

#### 完了確認チェックリスト

- [ ] ステップ2: 業務整理用資料の分類・配置が完了
- [ ] ステップ2.5: 各フォルダ内のファイルサマリが作成・更新済み
- [ ] ステップ3: 事業概要.mdと投資条件.mdが更新済み
- [ ] ステップ4: ヒアリングリスト.mdが更新済み
- [ ] ステップ5: 初期レビューが完了し、各評価ファイルが作成・更新済み
- [ ] ステップ6: 投資仮説ファイルが更新済み
- [ ] ステップ7: リサーチ結果がまとめられている
- [ ] ステップ8: 参考資料が適切に保存されている

#### 完了報告の内容

1. **作業完了の確認**: 各ステップの完了状況、作成・更新したファイルの一覧
2. **主要な発見事項**: 重要な評価結果、主要な投資仮説、重要なリスク要因
3. **次のステップ**: 追加で必要な作業、ヒアリングで確認すべき事項、追加調査が必要なテーマ

---

## 一括実行

初期セットアップを一括で実行する場合：

**コマンド**: `/dd:init` または `@agents/prompts/dd_init.md`

このコマンドは、ステップ2からステップ4までを一括で実行します。

---

## 作業の進め方のコツ

1. **段階的に進める**: 一度に全てを完璧にしようとせず、まず全体像を把握してから詳細を詰める
2. **定期的に確認**: 各ステップ完了時に、前のステップとの整合性を確認
3. **記録を残す**: 判断の根拠や仮説を必ず文書化する
4. **擬似コマンドを活用**: 各ステップはコマンドまたはプロンプトファイルを使って効率的に実行する

---

## 参照ファイル一覧

### ガイド・ドキュメント
- **全体像**: `agents/cursor/dd_method/00_overview.md`
- **擬似コマンド一覧**: `agents/cursor/commands.md`
- **システム指示書**: `agents/cursor/system.md`
- **チェックリスト**: `agents/cursor/checklists.md`

### 各ステップの詳細
- `agents/cursor/dd_method/01_copy_and_classify.md` - 資料分類・配置
- `agents/cursor/dd_method/02_summarize_files.md` - サマリ作成
- `agents/cursor/dd_method/03_update_basics.md` - 基本情報更新
- `agents/cursor/dd_method/04_update_questions.md` - ヒアリングリスト更新
- `agents/cursor/dd_method/05_initial_review.md` - 初期レビュー
- `agents/cursor/dd_method/06_investment_hypotheses.md` - 投資仮説作成
- `agents/cursor/dd_method/07_research.md` - リサーチ
- `agents/cursor/dd_method/08_resources.md` - 参考資料整理
- `agents/cursor/dd_method/09_completion.md` - 完了報告

### プロンプトファイル
- `agents/prompts/` 配下の各プロンプトファイル

---

## 更新履歴

- **2025年11月**: 初版作成
- **2026年1月**: 更新版作成
- **2026年1月**: 擬似コマンドシステムへの再構成

---
