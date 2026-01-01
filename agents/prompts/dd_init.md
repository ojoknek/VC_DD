# /dd:init - 初期セットアップ一括実行

## 目的
DD作業の初期セットアップを一括で実行します。これまで `DD方法.md` を読んで手動で行っていた初期作業（資料配置→サマリ作成→主要ファイル更新→初期レビューのキックオフ）を自動化します。

## 入力パラメータ
- **会社名**: {会社名}
- **対象期間**: {対象期間、例: 2024-2025}
- **資料の現状**: `業務整理用/` フォルダ内の資料状況

## 実行手順

### 1. 資料の配置確認とコピー
- `業務整理用/` フォルダ内の各フォルダを確認
- 対応表（`agents/cursor/dd_method/01_copy_and_classify.md` 参照）に従って、`dd materials/` の適切なディレクトリにファイルをコピー
- 元のファイルは `業務整理用/` に残す（バックアップとして）

### 2. 各フォルダ内のファイルサマリ作成
- `dd materials/` 配下のすべてのサブフォルダを確認
- 各フォルダ内のMarkdownファイル以外のファイル（PDF、Excel、Word、画像等）をリストアップ
- 各フォルダ内の `{フォルダ名}サマリ.md` に、以下の形式でサマリを記載：
  - 基本情報（ファイル名、形式、サイズ、更新日時）
  - 内容サマリ
  - 主要なポイント
  - 投資判断への影響

### 3. 基本情報の更新
- `dd materials/business/事業概要.md` を更新
  - ピッチ資料、事業計画書、営業資料等を読み込み
  - 事業内容、サービス、ターゲット市場、事業モデルを整理
- `dd materials/round table/投資条件概要.md` を更新
  - タームシート、資本政策表、株主名簿等を読み込み
  - 調達スケジュール、調達条件、資金使途を具体的な数値で更新

### 4. ヒアリングリストの更新
- `review_and_hypothesis/dd question/ヒアリングリスト.md` を更新
  - 既に把握している情報を反映
  - 不足している情報を特定
  - 優先度の高い質問項目を明確化

## 成果物
- `dd materials/*` の各サマリファイルが更新されている
- `dd materials/business/事業概要.md` が更新されている
- `dd materials/round table/投資条件概要.md` が更新されている
- `review_and_hypothesis/dd question/ヒアリングリスト.md` が更新されている

## 確認事項
- すべてのフォルダでサマリファイルが作成・更新されているか
- 重要なファイルのサマリが漏れていないか
- 数値の整合性が確認されているか
- 記載漏れがないか

## 参照ファイル
- `agents/cursor/dd_method/01_copy_and_classify.md`
- `agents/cursor/dd_method/02_summarize_files.md`
- `agents/cursor/dd_method/03_update_basics.md`
- `agents/cursor/dd_method/04_update_questions.md`

