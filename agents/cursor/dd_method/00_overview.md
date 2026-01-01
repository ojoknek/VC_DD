# DD作業の全体像

## はじめに

**重要**: DD作業を開始する際は、まずこのファイル（`agents/cursor/dd_method/00_overview.md`）を読み込んで、全体の流れを把握してください。

本ガイドは、投資判断に必要な情報を体系的に整理し、評価を行うための標準的な手順を示しています。

## 初期セットアップ手順の全体像

### ステップ1: ガイドラインの確認
- 作業の全体像を理解する
- 各ステップの目的を確認する
- 必要な資料の所在を把握する

### ステップ2: 業務整理用資料の分類・配置
- `業務整理用/` フォルダ内のファイルを、`dd materials/` の各セクションに適切にコピー
- **コマンド**: `/dd:copy` または `@agents/prompts/dd_copy_materials.md`
- **詳細**: `agents/cursor/dd_method/01_copy_and_classify.md`

### ステップ2.5: 各フォルダ内のファイルサマリの作成
- Markdownファイル以外のファイル（PDF、Excel、Word等）のサマリを作成
- **コマンド**: `/dd:summarize` または `@agents/prompts/dd_summarize_folder.md`
- **詳細**: `agents/cursor/dd_method/02_summarize_files.md`

### ステップ3: 基本情報の更新
- 事業概要と投資条件を更新
- **コマンド**: `/dd:update_basics` または `@agents/prompts/dd_update_business_overview.md`, `@agents/prompts/dd_update_investment_terms.md`
- **詳細**: `agents/cursor/dd_method/03_update_basics.md`

### ステップ4: ヒアリングリストの更新
- 事業概要と投資条件を元に、質問を具体化・重複排除・優先度付け
- **コマンド**: `/dd:questions` または `@agents/prompts/dd_update_hearing_list.md`
- **詳細**: `agents/cursor/dd_method/04_update_questions.md`

### ステップ5: 初期レビューの実践
- `dd materials/` と `research/` を読み、評価結果を `review_and_hypothesis/` に整理
- **コマンド**: `/dd:review` または `@agents/prompts/review_*.md`
- **詳細**: `agents/cursor/dd_method/05_initial_review.md`

### ステップ6: 投資仮説の作成
- 初期レビューを踏まえ、投資テーゼと複数シナリオを構築
- **コマンド**: `/dd:thesis` または `@agents/prompts/dd_build_thesis.md`
- **詳細**: `agents/cursor/dd_method/06_investment_hypotheses.md`

### ステップ7: リサーチテーマの設定と調査
- 仮説に紐づくリサーチテーマを追加
- **コマンド**: `/dd:research` または `@agents/prompts/dd_research_add.md`
- **詳細**: `agents/cursor/dd_method/07_research.md`

### ステップ8: 参考資料の整理
- 参考になった記事や情報を適切な場所に保存
- **コマンド**: `/dd:resource` または `@agents/prompts/dd_add_web_resource.md`, `@agents/prompts/dd_add_notion_resource.md`
- **詳細**: `agents/cursor/dd_method/08_resources.md`

### ステップ9: 完了報告
- チェックリストで完了状態を確認し、次のステップを明確化
- **コマンド**: `/dd:wrap` または `@agents/prompts/dd_completion_report.md`
- **詳細**: `agents/cursor/dd_method/09_completion.md`

## 一括実行

初期セットアップを一括で実行する場合：
- **コマンド**: `/dd:init` または `@agents/prompts/dd_init.md`

## 作業の進め方のコツ

1. **段階的に進める**: 一度に全てを完璧にしようとせず、まず全体像を把握してから詳細を詰める
2. **定期的に確認**: 各ステップ完了時に、前のステップとの整合性を確認
3. **記録を残す**: 判断の根拠や仮説を必ず文書化する

## 参照ファイル

- **擬似コマンド一覧**: `agents/cursor/commands.md`
- **システム指示書**: `agents/cursor/system.md`
- **チェックリスト**: `agents/cursor/checklists.md`

