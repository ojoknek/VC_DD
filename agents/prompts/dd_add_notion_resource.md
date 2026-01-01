# /dd:resource - Notion参考資料の追加

## 目的
Notionから取得した情報を `dd materials/web resource/Notion/` に保存し、必要に応じて `review_and_hypothesis/` を更新します。

## 入力パラメータ
- **NotionページのURL**: 参考になったNotionページのURL
- **要点**: 情報の主要な内容
- **投資判断との関連**: この情報が投資判断にどのように関連するか

## 実行手順

1. **情報の確認**
   - NotionページのURL、情報の種類、主要な内容を確認
   - 投資判断への関連性を明確化

2. **Markdownファイルの作成**
   - `dd materials/web resource/Notion/` フォルダにMarkdownファイルとして保存
   - 情報の種類ごとにサブフォルダを作成して分類
   - 以下を記載：
     - 情報の出典（NotionページのURL等）
     - 情報の種類
     - 主要な内容
     - 投資判断への関連性

3. **レビューの更新**
   - 参考資料の内容を踏まえて、`review_and_hypothesis/` 内の関連ファイルを更新
   - 必要に応じて評価結果を更新

## 成果物
- `dd materials/web resource/Notion/` に参考資料が保存されている
- `review_and_hypothesis/` 内の関連ファイルが更新されている（必要に応じて）

## 注意事項
- 著作権に注意し、必要に応じて引用元を明記
- 情報の信頼性を確認
- 日付を記載して情報の鮮度を管理

## 参照ファイル
- `agents/cursor/dd_method/08_resources.md`

