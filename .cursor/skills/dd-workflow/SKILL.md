---
name: dd-workflow
description: VC DD におけるデューデリジェンス作業の入口。擬似コマンド一覧とステップ概要を提供し、各ステップは分解スキル（dd-common, dd-copy-classify, dd-summarize 等）を参照する。DD作業、デューデリジェンス、投資判断の依頼時に適用する。
---

# DD Workflow（入口・インデックス）

VC DD リポジトリでDD作業を行う際の**入口スキル**です。全体フローとコマンド一覧を示し、各ステップの詳細は**分解スキル**を参照してください。

## いつ使うか

- ユーザーが `/dd:init` や `/dd:copy` などの擬似コマンドを指定したとき
- 「DD作業を進めて」「デューデリジェンスの手順で」「投資判断のための資料整理を」などと依頼されたとき
- コマンド一覧や手順を参照してほしいと言われたとき（dd-common および各ステップスキルを参照）

**重要**: 作業対象は **案件ルート**（例: `deals/株式会社ABC`）です。依頼時に案件ルートを指定し、すべてのパスは案件ルート相対で解釈します。

## 分解スキル一覧（DD手順に沿った要素）

| スキル | 内容 | コマンド |
|--------|------|----------|
| **dd-common** | 共通ルール・**案件ルート**・擬似コマンドの呼び方・品質基準 | — |
| **dd-init** | 初期セットアップ一括（ステップ2〜4） | `/dd:init` |
| **dd-copy-classify** | 資料分類・配置（ステップ2）案件内 業務整理用→dd materials | `/dd:copy` |
| **dd-summarize** | サマリ作成（ステップ2.5） | `/dd:summarize` |
| **dd-update-basics** | 事業概要・投資条件の更新（ステップ3） | `/dd:update_basics` |
| **dd-hearing-list** | ヒアリングリストの更新（ステップ4） | `/dd:questions` |
| **dd-initial-review** | 初期レビュー（ステップ5） | `/dd:review` |
| **dd-investment-thesis** | 投資仮説の作成（ステップ6）共通思考法は dd_logic/investment_methodology 参照 | `/dd:thesis` |
| **dd-research** | リサーチ（ステップ7） | `/dd:research` |
| **dd-resources** | 参考資料の整理（ステップ8） | `/dd:resource` |
| **dd-completion** | 完了報告（ステップ9） | `/dd:wrap` |
| **dd-ic-slides** | 投資委員会資料の骨格更新 | `/dd:ic_slide` |

共通ルール・品質基準・案件ルートは **dd-common** を参照。各ステップの手順・対応表・対象ファイルは上記スキルの SKILL.md を参照。

## 標準DDフロー（ステップ概要）

1. **ガイドライン確認** — `.cursor/skills/dd-common/SKILL.md`
2. **資料分類・配置** — dd-copy-classify / `/dd:copy`（案件ルート内 業務整理用→dd materials）
3. **サマリ作成** — dd-summarize / `/dd:summarize`
4. **基本情報更新** — dd-update-basics / `/dd:update_basics`
5. **ヒアリングリスト更新** — dd-hearing-list / `/dd:questions`
6. **初期レビュー** — dd-initial-review / `/dd:review`
7. **投資仮説作成** — dd-investment-thesis / `/dd:thesis`（共通思考法は dd_logic/investment_methodology 参照）
8. **リサーチ** — dd-research / `/dd:research`
9. **参考資料整理** — dd-resources / `/dd:resource`
10. **完了報告** — dd-completion / `/dd:wrap`

一括実行: **dd-init** / `/dd:init` でステップ2〜4までまとめて進行可能。

## DD手順（全文）

ステップごとの目的・コマンド・対応表・注意事項の詳細は、このスキル内の **[DD手順.md](DD手順.md)** を参照してください。

## 参照先（リポジトリ内）

- **擬似コマンド一覧・案件ルート・システム指示・品質基準**: `.cursor/skills/dd-common/SKILL.md`
- **チェックリスト（DD完了・週次・月次）**: `.cursor/skills/dd-completion/SKILL.md`
- **共通投資思考法（人間が記述）**: `dd_logic/investment_methodology/`
- **各ステップの実行内容**: 上記「分解スキル一覧」の各スキルの SKILL.md
