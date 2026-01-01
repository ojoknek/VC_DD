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

### 1. 初期セットアップ
- 業務整理用資料の分類・配置
- 基本情報（企業概要、投資条件）の更新

### 2. 資料レビューと評価
- 事業性評価
- 契約書レビュー
- 財務状況評価
- 投資条件評価

### 3. 投資仮説の作成
- 投資テーゼの構築
- 成長シナリオの検討
- 競合優位性の分析
- リスク要因の特定

### 4. リサーチの実施
- 市場・競合分析
- M&A事例・ROI事例の調査
- 現場調査

### 5. 投資委員会資料の作成
- `review_and_hypothesis/投資委員会資料作成/スライドスケルトン.md` を参照
- 各セクションで参照すべきファイルを確認しながら作成

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

