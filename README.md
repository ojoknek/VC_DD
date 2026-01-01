# DD Template（デューデリジェンステンプレート）

投資判断に必要な情報を体系的に整理し、評価を行うための標準的なデューデリジェンス（DD）フレームワークです。

## 📋 概要

本テンプレートは、スタートアップ企業への投資判断を行う際に必要な情報収集・分析・評価のプロセスを標準化し、効率的かつ網羅的なデューデリジェンスを実施するためのものです。

## 🚀 クイックスタート

### 初めて使用する場合

1. **まず `DD方法.md` を読む**
   - DD作業の全体像と手順を把握してください
   - 各ステップの目的と作業内容を確認してください
   - Curosorで最初に依頼する内容を「`DD方法.md` を読んで」にしてください

2. **業務整理用資料の分類**
   - `業務整理用/` フォルダ内の資料を `dd materials/` の各セクションに適切に配置してください

3. **基本情報の更新**
   - `dd materials/business/事業概要.md` を更新
   - `dd materials/round table/投資条件概要.md` を更新

4. **ヒアリングリストの更新**
   - `review_and_hypothesis/dd question/ヒアリングリスト.md` を更新

詳細な手順は `DD方法.md` を参照してください。

## 📁 ディレクトリ構成

```
DD_template/
├── DD方法.md                    # DD作業の手順ガイド（必読）
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

### DD方法.mdのプロセス

`DD方法.md`に記載されている標準的なDD作業プロセスは以下の通りです：

1. **`業務整理用/` にあるファイルを `dd materials/` にコピー**
   - `業務整理用/` フォルダ内の各ファイルを、対応表に従って `dd materials/` の適切なディレクトリにコピー
   - 元のファイルは `業務整理用/` に残しておく（バックアップとして）

2. **`dd materials/` のそれぞれのディレクトリ内にあるファイル内容をそれぞれのmdファイルに分析を記録**
   - 各ディレクトリ内のMarkdownファイル以外のファイル（PDF、Excel、Word等）のサマリを、各フォルダ内のサマリファイル（`{フォルダ名}サマリ.md`）に記載
   - ファイルの内容を分析し、投資判断に必要な情報を整理

3. **`research/` を `dd materials/` から推察してざっくりテーマを決めてリサーチ結果を追加していく**
   - `dd materials/` の内容を基に、必要なリサーチテーマを特定
   - 市場・競合分析、M&A事例、IPO事例等の調査を実施
   - 調査結果を `research/` フォルダ内の適切なMarkdownファイルにまとめる

4. **`review_and_hypothesis/` の初期レビューを `dd materials/` と `research/` をもとに更新**
   - `dd materials/` と `research/` の情報を統合的に分析
   - 事業性評価、契約書レビュー、財務状況評価、投資条件評価等の評価結果を `review_and_hypothesis/review_results/` に記載
   - 投資仮説、競合優位性、リスク要因等を `review_and_hypothesis/` 内の各ファイルに記載

### その他のアクション

上記の標準プロセスに加えて、以下のアクションを必要に応じて実施します：

1. **自分で `review_and_hypothesis/` の文章mdを執筆する**
   - 投資テーゼ、成長シナリオ、競合優位性、リスク分析等を自分で執筆・更新
   - 評価結果を踏まえた投資判断の根拠を明確化

2. **`dd materials/web resource/` に参考資料を追加し、`review_and_hypothesis/` を若干更新する**
   - 参考になったWeb記事やNotion情報を `dd materials/web resource/` に保存
   - 参考資料の内容を踏まえて、`review_and_hypothesis/` 内の関連ファイルを更新

3. **`research/` の中でリサーチを行う**
   - 市場動向、競合企業、業界課題等の追加リサーチを実施
   - 調査結果を `research/` フォルダ内の適切なファイルに追加

4. **`research/` に参考資料を追加し、`review_and_hypothesis/` を若干更新する**
   - リサーチ中に得た参考資料を `research/` に保存
   - 参考資料の内容を踏まえて、`review_and_hypothesis/` 内の関連ファイルを更新

5. **`review_and_hypothesis/投資委員会資料作成/スライドスケルトン.md` を投資委員会用にそれ以外の資料から若干アップデートする**
   - スライドスケルトンを参照しながら、`dd materials/` と `review_and_hypothesis/` の情報を基に投資委員会資料を作成
   - 各スライドで参照すべきファイルを確認しながら、情報を統合してスライドを作成

## 📝 主要ファイル

### ガイドファイル
- **`DD方法.md`**: DD作業の全体手順と各ステップの詳細説明
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

- **DD方法ガイド**: `DD方法.md`
- **スライド作成ガイド**: `review_and_hypothesis/投資委員会資料作成/スライドスケルトン.md`
- **ヒアリングリスト**: `review_and_hypothesis/dd question/ヒアリングリスト.md`

## 🔄 更新履歴

- **2025年11月**: 初版作成

---

**作成者**: Ken Kojo
**用途**: スタートアップ企業への投資判断・デューデリジェンス  
**ライセンス**: 本ドキュメントの著作権はKen Kojoに帰属し、無断転載・配布を禁じます。

