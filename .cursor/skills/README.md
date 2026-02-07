# DD Template 用 Cursor Skills

DD手順に沿って要素分解したスキル群です。入口は **dd-workflow**、共通ルールは **dd-common**、各ステップは対応するスキルを参照してください。

**重要**: 作業対象は **案件ルート**（例: `deals/株式会社ABC`）です。依頼時に「案件は deals/株式会社ABC」のように指定し、すべてのパスは案件ルート相対で解釈します。

## スキル一覧

| スキル | 役割 | 擬似コマンド |
|--------|------|--------------|
| **dd-workflow** | 入口・インデックス。全体フローとDD手順への参照 | — |
| **dd-common** | 共通ルール・**案件ルート**・リポジトリ役割・品質基準・コマンド一覧 | — |
| **dd-init** | 初期セットアップ一括（ステップ2〜4） | `/dd:init` |
| **dd-copy-classify** | ステップ2: 案件内 業務整理用→dd materials の分類・配置 | `/dd:copy` |
| **dd-summarize** | ステップ2.5: 案件内 各フォルダのサマリ作成 | `/dd:summarize` |
| **dd-update-basics** | ステップ3: 事業概要・投資条件の更新 | `/dd:update_basics` |
| **dd-hearing-list** | ステップ4: ヒアリングリストの更新 | `/dd:questions` |
| **dd-initial-review** | ステップ5: 初期レビュー（領域別） | `/dd:review` |
| **dd-investment-thesis** | ステップ6: 投資仮説の作成（共通思考法は dd_logic/investment_methodology 参照） | `/dd:thesis` |
| **dd-research** | ステップ7: リサーチテーマの設定と調査 | `/dd:research` |
| **dd-resources** | ステップ8: 参考資料の整理（Web/Notion） | `/dd:resource` |
| **dd-completion** | ステップ9: 完了報告 | `/dd:wrap` |
| **dd-ic-slides** | 投資委員会資料の骨格更新 | `/dd:ic_slide` |

## 使い方

- **DD作業を依頼されたとき**: dd-workflow が入口となり、**案件ルート**を指定したうえで dd-common と各ステップスキルが参照される
- **特定コマンドを指定されたとき**: 対応するスキルの指示に従い、**対象案件ルート**で実行する（例: 「案件は deals/株式会社ABC で /dd:copy を実行して」）
- **共通ルール・品質基準・案件ルート**: dd-common を参照
- **実際の使い方（新規案件作成〜コピー・レビュー・リサーチの流れ）**: リポジトリルートの [README.md](../../README.md) の「実際の使い方」「各コマンドの状況と参照関係」を参照

## DD手順（全文）

ステップごとの詳細（目的・対応表・注意事項）は **dd-workflow/DD手順.md** にあります。コマンド一覧・品質基準・案件ルートは **dd-common/SKILL.md**、チェックリストは **dd-completion/SKILL.md** を参照。
