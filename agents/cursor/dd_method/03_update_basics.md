# ステップ3: 基本情報の更新

## 目的
`業務整理用/` フォルダ内の資料を全て読み込み、事業概要と投資条件を更新します。

## 対応コマンド
- `/dd:update_basics` または 
  - `@agents/prompts/dd_update_business_overview.md`（事業概要）
  - `@agents/prompts/dd_update_investment_terms.md`（投資条件）

## 3.1 事業概要の更新

### 対象ファイル
- `dd materials/business/事業概要.md`

### 作業内容
- ピッチ資料、事業計画書、営業資料等を読み込み
- 事業内容、サービス、ターゲット市場、事業モデルを整理
- 過去の事業の変化・進化を記載

## 3.2 投資条件の更新

### 対象ファイル
- `dd materials/round table/投資条件概要.md`

### 作業内容
- タームシート、資本政策表、株主名簿等を読み込み
- 調達スケジュール、調達条件、資金使途を具体的な数値で更新
- 評価額、調達額、資金使途の内訳を記載

## 確認事項

- 数値の整合性を確認
- 記載漏れがないか確認
- 日付や期間が正確か確認

## 次のステップ

- ステップ4: ヒアリングリストの更新
- **コマンド**: `/dd:questions` または `@agents/prompts/dd_update_hearing_list.md`
- **詳細**: `agents/cursor/dd_method/04_update_questions.md`

