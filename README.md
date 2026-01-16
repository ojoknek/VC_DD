# DD Template（デューデリジェンステンプレート）

投資判断に必要な情報を体系的に整理し、評価を行うための標準的なデューデリジェンス（DD）フレームワークです。

## 📋 概要

本テンプレートは、スタートアップ企業への投資判断を行う際に必要な情報収集・分析・評価のプロセスを標準化し、効率的かつ網羅的なデューデリジェンスを実施するためのものです。

## 🚀 クイックスタート

### 初めて使用する場合

1. **まず `DD手順.md` を読む**
   - DD作業の全体像と手順を把握してください
   - 各ステップの目的と作業内容を確認してください

2. **擬似コマンドシステムの確認**
   - **擬似コマンド一覧**: `agents/cursor/commands.md`
   - **システム指示書**: `agents/cursor/system.md`
   - **全体像**: `agents/cursor/dd_method/00_overview.md`

3. **初期セットアップの実行**
   - **一括実行**: `/dd:init` または `@agents/prompts/dd_init.md` を実行
   - **個別実行**: 各ステップに対応するコマンドを実行（`agents/cursor/commands.md` 参照）

詳細な手順は `DD手順.md` または `agents/cursor/dd_method/` 配下の各ファイルを参照してください。

## 📁 ディレクトリ構成

```
DD_template/
├── DD手順.md                    # DD作業の手順ガイド（必読・概要版）
├── agents/                      # Cursor向けエージェント指示書
│   ├── cursor/                  # Cursor向け指示書
│   │   ├── system.md            # 「このリポジトリでどう働くか」
│   │   ├── commands.md          # 擬似スラッシュコマンド設計
│   │   ├── checklists.md        # 更新チェックリスト（週次/決算）
│   │   └── dd_method/           # DD手順のステップ別詳細
│   │       ├── 00_overview.md   # 全体像
│   │       ├── 01_copy_and_classify.md
│   │       ├── 02_summarize_files.md
│   │       └── ... (各ステップ)
│   └── prompts/                 # 個別プロンプト（用途別）
│       ├── dd_init.md           # 初期セットアップ一括
│       ├── dd_copy_materials.md  # 資料コピー
│       ├── dd_summarize_folder.md
│       └── ... (各コマンド用プロンプト)
├── dd materials/                # デューデリジェンス資料
│   ├── business/                # 事業関連資料
│   ├── contract/                # 契約書関連資料
│   ├── corporate/               # 組織・経営陣関連資料
│   ├── financial/               # 財務関連資料
│   ├── pitch slide/             # ピッチ資料
│   ├── round table/             # 資本政策・株主関連資料
│   └── web resource/            # 参考資料（Notion、Web記事）
├── review_and_hypothesis/        # レビュー結果と投資仮説
│   ├── comps/                   # 企業価値評価（DCF、EV/Sales等）
│   ├── dd question/             # ヒアリングリスト
│   ├── review_results/          # 評価結果
│   ├── risk/                    # リスク分析
│   ├── senario/                 # シナリオ分析（投資理論、出口戦略等）
│   ├── strength/                # 競合優位性（MOAT）
│   ├── synergy/                 # 事業シナジー
│   ├── 投資委員会資料作成/      # 投資委員会資料
│   └── 現場調査記録/            # 現場調査結果
├── research/                    # リサーチ結果
│   ├── deep research/           # 詳細リサーチ（M&A事例、IPO事例等）
│   ├── market and competitors/  # 市場・競合分析
│   └── 業界課題とソリューション/
└── 業務整理用/                  # 初期資料整理用フォルダ
```

## 🔄 作業フロー

### 擬似コマンドシステムの使い方

このリポジトリでは、**擬似スラッシュコマンド**を使ってCursorに作業を依頼できます。

#### 基本的な使い方

1. **コマンドで呼ぶ**
   - 例: `/dd:init 会社名="XXX" 対象期間="2024-2025"` を実行して

2. **プロンプトファイルで呼ぶ（推奨）**
   - 例: `@agents/prompts/dd_init.md` をこの案件に合わせて実行して

#### 主要なコマンド一覧

- **`/dd:init`**: 初期セットアップ一括実行
- **`/dd:copy`**: 業務整理用→dd materials へ配置
- **`/dd:summarize`**: 非mdファイルのサマリ追記
- **`/dd:update_basics`**: 事業概要/投資条件の更新
- **`/dd:questions`**: ヒアリングリスト更新
- **`/dd:review`**: 初期レビュー（領域別に実行）
- **`/dd:thesis`**: 投資仮説の作成
- **`/dd:research`**: リサーチ追加
- **`/dd:resource`**: 参考資料の追加（Web/Notion）
- **`/dd:ic_slide`**: 投資委員会資料の骨格更新
- **`/dd:wrap`**: 完了報告

詳細は `agents/cursor/commands.md` を参照してください。

### 標準的なDD作業プロセス

`DD手順.md` または `agents/cursor/dd_method/00_overview.md` に記載されている標準的なDD作業プロセスは以下の通りです：

1. **`業務整理用/` にあるファイルを `dd materials/` にコピー** (`/dd:copy`)
2. **`dd materials/` の各ディレクトリ内のファイル内容をサマリに記録** (`/dd:summarize`)
3. **基本情報の更新** (`/dd:update_basics`)
4. **ヒアリングリストの更新** (`/dd:questions`)
5. **初期レビューの実践** (`/dd:review`)
6. **投資仮説の作成** (`/dd:thesis`)
7. **リサーチテーマの設定と調査** (`/dd:research`)
8. **参考資料の整理** (`/dd:resource`)
9. **完了報告** (`/dd:wrap`)

### 一括実行

初期セットアップを一括で実行する場合：
- **`/dd:init`** または `@agents/prompts/dd_init.md` を実行

## 📝 主要ファイル

### ガイドファイル
- **`DD手順.md`**: DD作業の全体手順と各ステップの概要（詳細は `agents/cursor/dd_method/` 参照）
- **`agents/cursor/commands.md`**: 擬似スラッシュコマンド一覧
- **`agents/cursor/system.md`**: Cursor向けシステム指示書
- **`agents/cursor/dd_method/00_overview.md`**: DD作業の全体像
- **`review_and_hypothesis/投資委員会資料作成/スライドスケルトン.md`**: 投資委員会資料のスライド構成テンプレート

### 評価結果ファイル
- `review_and_hypothesis/review_results/事業性評価.md`
- `review_and_hypothesis/review_results/契約書レビュー.md`
- `review_and_hypothesis/review_results/財務状況評価.md`
- `review_and_hypothesis/review_results/投資条件評価.md`
- `review_and_hypothesis/dd question/ヒアリング回答.md`

### 投資仮説ファイル
- `review_and_hypothesis/senario/investment_theory.md`: 投資理論・投資テーゼ
- `review_and_hypothesis/strength/MOAT.md`: 競合優位性
- `review_and_hypothesis/senario/exit_plan.md`: 出口戦略
- `review_and_hypothesis/risk/リスク項目.md`: リスク要因

## 💡 使い方のコツ

1. **段階的に進める**: 一度に全てを完璧にしようとせず、まず全体像を把握してから詳細を詰める
2. **定期的に確認**: 各ステップ完了時に、前のステップとの整合性を確認
3. **記録を残す**: 判断の根拠や仮説を必ず文書化する
4. **参照ファイルを活用**: 各ファイルで参照すべきファイルを明記しているので、情報の出典を確認しながら作業する

## ⚠️ 注意事項

- 元のファイルは `業務整理用/` フォルダに残しておく（バックアップとして）
- 数値データの整合性を常に確認する
- 客観的な評価を心がける
- 根拠となる資料を明記する

## 📚 関連リソース

### ガイド・ドキュメント
- **DD手順ガイド**: `DD手順.md`（概要版）
- **DD手順詳細**: `agents/cursor/dd_method/00_overview.md` 以降
- **擬似コマンド一覧**: `agents/cursor/commands.md`
- **システム指示書**: `agents/cursor/system.md`
- **チェックリスト**: `agents/cursor/checklists.md`

### プロンプトファイル
- **初期セットアップ**: `agents/prompts/dd_init.md`
- **各コマンド用プロンプト**: `agents/prompts/` 配下

### その他
- **スライド作成ガイド**: `review_and_hypothesis/投資委員会資料作成/スライドスケルトン.md`
- **ヒアリングリスト**: `review_and_hypothesis/dd question/ヒアリングリスト.md`

## 🔄 更新履歴

- **2025年11月**: 初版作成
- **2026年1月**: 更新版作成

---

**作成者**: ojoknek
**用途**: スタートアップ企業への投資判断・デューデリジェンス  
**ライセンス**: 本ドキュメントの著作権はKen Kojoに帰属し、無断転載・配布を禁じます。

