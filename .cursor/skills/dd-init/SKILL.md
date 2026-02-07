---
name: dd-init
description: DD初期セットアップの一括実行。ステップ2〜4（資料配置→サマリ→事業概要・投資条件→ヒアリングリスト）をまとめて進行。コマンド /dd:init または dd_init の実行時に適用する。
---

# DD 初期セットアップ一括（/dd:init）

DD作業の初期セットアップを一括で実行する。ステップ2〜4を**指定した案件ルート**に対してまとめて進行する。

## コマンド・プロンプト

- **コマンド**: `/dd:init 案件=deals/株式会社ABC 会社名="XXX" 対象期間="2024-2025"`
- **実行**: このスキルの手順に従う

## 入力パラメータ

- **案件**（案件ルート）: 例 `deals/株式会社ABC`
- **会社名**: 対象企業名
- **対象期間**: 例 2024-2025
- **資料の現状**: 当該案件の `業務整理用/` フォルダ内の資料状況

## 実行内容（順序）

1. **資料の配置** — dd-copy-classify に準拠。当該案件の `業務整理用/` → 同案件の `dd materials/` にコピー（元は残す）。`python program/run_copy.py <案件ルート>` を実行
2. **サマリ作成** — dd-summarize に準拠。当該案件の各フォルダの `{フォルダ名}サマリ.md` に非mdファイルのサマリを記載
3. **基本情報の更新** — dd-update-basics に準拠。当該案件の `dd materials/business/事業概要.md` と `dd materials/round table/投資条件概要.md` を更新
4. **ヒアリングリストの更新** — dd-hearing-list に準拠。当該案件の `review_and_hypothesis/dd question/ヒアリングリスト.md` を更新

## 成果物（いずれも案件ルート内）

- `dd materials/*` の各サマリファイルが更新されている
- `dd materials/business/事業概要.md` が更新されている
- `dd materials/round table/投資条件概要.md` が更新されている
- `review_and_hypothesis/dd question/ヒアリングリスト.md` が更新されている

## 参照スキル

- dd-copy-classify（ステップ2）
- dd-summarize（ステップ2.5）
- dd-update-basics（ステップ3）
- dd-hearing-list（ステップ4）

詳細手順は各参照スキル（dd-copy-classify, dd-summarize, dd-update-basics, dd-hearing-list）の SKILL.md を参照。
