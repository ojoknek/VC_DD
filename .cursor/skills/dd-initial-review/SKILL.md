---
name: dd-initial-review
description: dd materials と research を読み、評価結果を review_and_hypothesis に整理。ステップ5。領域別に review_business / review_contracts / review_corporate / review_financial / review_roundtable / review_market_competitors / review_market_opportunity。コマンド /dd:review の実行時に適用する。
---

# DD 初期レビュー（ステップ5）

**案件ルート**内の `dd materials/` と `research/` を読み、評価結果を同案件の `review_and_hypothesis/` に整理する。

## コマンド・プロンプト

- **コマンド**: `/dd:review`（対象は指定した案件ルート）
- **実行**: このスキルの手順に従う。領域別の目的・対象・出力は下表のとおり。

## レビュー対象と出力先（いずれも案件ルート相対）

| レビュー対象 | 評価結果ファイル |
|-------------|------------------|
| dd materials/business/ | review_and_hypothesis/review_results/事業性評価.md |
| dd materials/contract/ | review_and_hypothesis/review_results/契約書レビュー.md |
| dd materials/corporate/ | review_and_hypothesis/review_results/組織評価.md |
| dd materials/financial/ | review_and_hypothesis/review_results/財務評価.md |
| dd materials/round table/ | review_and_hypothesis/review_results/投資条件評価.md |
| research/market and competitors/ | review_and_hypothesis/review_results/市場・競合評価.md |
| research/業界課題とソリューション/ | review_and_hypothesis/review_results/市場機会評価.md |

## 評価結果に含める内容

概要、主要な発見事項、ポジティブ要因、リスク要因、推奨事項、結論、根拠となる資料の参照先。

## 品質基準（dd-common 準拠）

レビューには「概要 / 主要発見 / ポジティブ要因 / リスク / 推奨 / 結論 / 参照先」が揃っていること。

## 注意事項

- 客観的な評価を心がける
- 根拠となる資料を明記する
- 不足情報は「未確認」「要ヒアリング」として明示する

## 次ステップ

- ステップ6: 投資仮説作成 → dd-investment-thesis スキル / `/dd:thesis`
