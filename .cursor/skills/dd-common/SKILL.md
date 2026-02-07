---
name: dd-common
description: DD_template における共通ルール・案件ルート・リポジトリ役割・擬似コマンドの呼び方・成果物の品質基準。他の dd-* スキルと併用する。DD作業の基本ルール、システム指示、品質基準を参照するときに適用する。
---

# DD Common（共通ルール・品質基準）

DD_template リポジトリでDD作業を行う際の共通ルールと品質基準です。各ステップスキル（dd-copy-classify, dd-summarize 等）と併用してください。

## 案件ルート

- **案件ルート**とは、1件のDD案件を扱うフォルダのルートです。例: `deals/株式会社ABC`
- 新規案件は `deals/{会社名}/` に `dd_logic/template` をコピーして作成する
- 依頼時は **「案件は deals/株式会社ABC」** のように案件ルートを指定する
- 本スキルおよび各ステップスキル内のパス（`dd materials/`、`review_and_hypothesis/`、`業務整理用/` 等）は、**案件ルート相対**で解釈する

## リポジトリの役割分担（案件ルート内）

- **インプット（素材）**: 案件ルート内の `dd materials/` と `research/`
- **アウトプット（評価・仮説）**: 案件ルート内の `review_and_hypothesis/`
- **共通思考法**: リポジトリ共通の `dd_logic/investment_methodology/`（全案件で参照、人間が記述）
- **ガイド・運用**: `.cursor/skills/`（入口は dd-workflow、DD手順全文は dd-workflow/DD手順.md）

## 基本ルール（システム指示）

- **言語**: 出力は日本語を基本とする
- **改変**: 既存のファイル構造・命名を尊重し、必要最小限の差分で更新する
- **根拠**: 断定せず、根拠となる資料（案件ルート内の `dd materials/` や `research/` の参照先）を必ず併記する
- **不足情報**: 推測で埋めず、「未確認」「要ヒアリング」として明示する
- **粒度**: 大量更新は避け、アクションごとに分割して進める（擬似コマンド単位で実行）

## 擬似コマンドの呼び方

1. **コマンド形式**: `/dd:init 案件=deals/株式会社ABC 会社名="XXX" 対象期間="2024-2025"` を実行して
2. **スキル参照**: 対応するスキル（例: dd-init）の `.cursor/skills/dd-init/SKILL.md` を**この案件（案件ルート）**に合わせて実行して

各コマンドの実行内容は、下表の「参照先（スキル）」の SKILL.md に記載されている。

## コマンドと対応スキル（参照先）

| コマンド | 目的 | 参照先（スキル） |
|----------|------|------------------|
| `/dd:init` | 初期セットアップ一括 | dd-init |
| `/dd:copy` | 資料分類・配置（案件内 業務整理用→dd materials） | dd-copy-classify |
| `/dd:summarize` | サマリ追記 | dd-summarize |
| `/dd:update_basics` | 事業概要・投資条件 | dd-update-basics |
| `/dd:questions` | ヒアリングリスト | dd-hearing-list |
| `/dd:review` | 初期レビュー | dd-initial-review |
| `/dd:thesis` | 投資仮説（共通思考法は dd_logic/investment_methodology 参照） | dd-investment-thesis |
| `/dd:research` | リサーチ追加 | dd-research |
| `/dd:resource` | 参考資料（Web/Notion） | dd-resources |
| `/dd:ic_slide` | 投資委資料骨格 | dd-ic-slides |
| `/dd:wrap` | 完了報告 | dd-completion |

## 成果物の品質基準

- **サマリ**: 基本情報 / 内容サマリ / 主要ポイント / 投資判断への影響 が揃っている
- **レビュー**: 概要 / 主要発見 / ポジティブ要因 / リスク / 推奨 / 結論 / 参照先 が揃っている
- **仮説**: 投資テーゼ / 成長シナリオ / MOAT / 出口 / リスクと対策 が揃っている。共通の「どう考えるか」は `dd_logic/investment_methodology/` を参照する

## 作業の進め方のコツ

- 段階的に進める
- 各ステップ完了時に前ステップとの整合性を確認する
- 判断の根拠や仮説は必ず文書化する
