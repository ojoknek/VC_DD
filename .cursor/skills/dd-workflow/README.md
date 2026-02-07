# dd-workflow スキル（入口・インデックス）

VC DD 用の**入口スキル**です。全体フローとコマンド一覧を提供し、各ステップの詳細は**分解スキル**に委譲しています。

## このスキル内

- **SKILL.md** — いつ使うか、分解スキル一覧、標準DDフロー、DD手順への参照
- **DD手順.md** — DD作業の全ステップの詳細ガイド（目的・コマンド・対応表・注意事項）

## 分解スキル（.cursor/skills/ 配下）

| スキル | 役割 |
|--------|------|
| dd-common | 共通ルール・品質基準・コマンド一覧 |
| dd-init | 初期セットアップ一括（2〜4） |
| dd-copy-classify | ステップ2: 資料分類・配置 |
| dd-summarize | ステップ2.5: サマリ作成 |
| dd-update-basics | ステップ3: 事業概要・投資条件 |
| dd-hearing-list | ステップ4: ヒアリングリスト |
| dd-initial-review | ステップ5: 初期レビュー |
| dd-investment-thesis | ステップ6: 投資仮説 |
| dd-research | ステップ7: リサーチ |
| dd-resources | ステップ8: 参考資料 |
| dd-completion | ステップ9: 完了報告 |
| dd-ic-slides | 投資委員会資料の骨格更新 |

## リポジトリ参照

- 擬似コマンド・品質基準: `.cursor/skills/dd-common/SKILL.md`
- チェックリスト: `.cursor/skills/dd-completion/SKILL.md`
- 各ステップの実行内容: 上記スキル一覧の各 SKILL.md
