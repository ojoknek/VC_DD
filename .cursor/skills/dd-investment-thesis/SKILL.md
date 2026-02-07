---
name: dd-investment-thesis
description: 初期レビューを踏まえた投資テーゼ・シナリオ・MOAT・出口・リスクの構築。ステップ6。共通思考法は dd_logic/investment_methodology を参照。コマンド /dd:thesis または dd_build_thesis の実行時に適用する。
---

# DD 投資仮説の作成（ステップ6）

初期レビューを踏まえ、投資テーゼと複数シナリオ（楽観的・現実的・悲観的）を構築する。**共通の「どう考えるか」**はリポジトリ共通の **`dd_logic/investment_methodology/`**（投資の考え方・評価の観点・リスクの見方・出口の考え方）を参照しつつ、**案件ごとの結論**を案件ルート内のファイルに記述する。

## コマンド・プロンプト

- **コマンド**: `/dd:thesis`（対象は指定した案件ルート）
- **実行**: このスキルの手順・更新対象ファイルに従う

## 投資仮説の構成要素

- **投資テーゼ**: なぜこの企業に投資するのか
- **成長シナリオ**: どのように成長するか
- **競合優位性（MOAT）**: 持続的な優位性は何か
- **出口戦略**: どのようにリターンを得るか
- **リスク要因**: 想定されるリスクと対策

## 更新対象ファイル（いずれも案件ルート相対）

| 内容 | ファイル |
|------|----------|
| 投資テーゼ・成長シナリオ（共通思考法は dd_logic/investment_methodology 参照） | review_and_hypothesis/senario/investment_theory.md |
| 競合優位性 | review_and_hypothesis/strength/MOAT.md, 競合優位性.md |
| 出口戦略・M&A候補 | review_and_hypothesis/senario/exit_plan.md, m_and_a_candidate.md |
| リスク要因 | review_and_hypothesis/risk/リスク項目.md |
| 事業シナジー | review_and_hypothesis/synergy/事業シナジー.md |
| DCF・EV/Sales | review_and_hypothesis/comps/DCF.md, EV_Sales.md |

## 作業内容

- ステップ5の評価結果を踏まえて投資仮説を構築する
- **dd_logic/investment_methodology/** の思考法を参照しつつ、本案件の結論を記述する
- 複数シナリオ（楽観的・現実的・悲観的）を検討する
- 各仮説の根拠を明確にする

## 品質基準（dd-common 準拠）

仮説には「投資テーゼ / 成長シナリオ / MOAT / 出口 / リスクと対策」が揃っていること。共通の評価観点は dd_logic/investment_methodology を参照する。

## 次ステップ

- ステップ7: リサーチ → dd-research スキル / `/dd:research`
