# ステップ5: 初期レビューの実践

## 目的
`dd materials/` と `research/` フォルダ内の資料を読み込み、評価結果を `review_and_hypothesis/` フォルダ内の各Markdownファイルに記載します。

## 対応コマンド
- `/dd:review` または領域別に：
  - `@agents/prompts/review_business.md`（事業性評価）
  - `@agents/prompts/review_contracts.md`（契約書レビュー）
  - `@agents/prompts/review_corporate.md`（組織評価）
  - `@agents/prompts/review_financial.md`（財務評価）
  - `@agents/prompts/review_roundtable.md`（投資条件評価）
  - `@agents/prompts/review_market_competitors.md`（市場・競合評価）
  - `@agents/prompts/review_market_opportunity.md`（市場機会評価）

## 初期レビューの目的

- 入手可能な資料を体系的にレビューし、投資判断に必要な情報を整理する
- 事業性、財務、契約、組織、市場・競合等の各観点から評価を行う
- 評価結果を`review_and_hypothesis/` フォルダ内に整理し、投資仮説構築の基礎とする

## レビュー対象と出力先

### dd materialsフォルダのレビュー

| レビュー対象フォルダ | 評価結果ファイル | 評価観点 |
|---------------------|-----------------|---------|
| `dd materials/business/` | `review_and_hypothesis/review_results/事業性評価.md` | 事業モデル、市場ポジション、成長性、競合優位性 |
| `dd materials/contract/` | `review_and_hypothesis/review_results/契約書レビュー.md` | 法的リスク、財務的影響、事業リスク、投資判断への影響 |
| `dd materials/corporate/` | `review_and_hypothesis/review_results/組織評価.md` | 経営陣の質、組織体制、人材、継続性 |
| `dd materials/financial/` | `review_and_hypothesis/review_results/財務評価.md` | 財務健全性、収益性、資金繰り、財務リスク |
| `dd materials/round table/` | `review_and_hypothesis/review_results/投資条件評価.md` | 評価額の妥当性、調達条件、資金使途、出口戦略 |

### researchフォルダのレビュー

| レビュー対象フォルダ | 評価結果ファイル | 評価観点 |
|---------------------|-----------------|---------|
| `research/market and competitors/` | `review_and_hypothesis/review_results/市場・競合評価.md` | 市場規模、成長性、競合ポジション、競争環境 |
| `research/業界課題とソリューション/` | `review_and_hypothesis/review_results/市場機会評価.md` | 業界課題、ソリューションの優位性、市場機会 |
| `research/deep research/MA事例/` | `review_and_hypothesis/senario/m_and_a_candidate.md` | M&A事例の分析、出口戦略への示唆 |
| `research/deep research/IPO事例/` | `review_and_hypothesis/senario/exit_plan.md` | IPO事例の分析、出口戦略への示唆 |

## 初期レビューの実施方法

1. **各フォルダ内の資料を体系的に読み込む**
   - `dd materials/` 配下の各フォルダ内のサマリファイルや資料を確認
   - `research/` 配下の各フォルダ内の調査結果を確認

2. **評価観点に基づいて分析を行う**
   - 各評価観点に沿って情報を整理
   - 数値データや具体的な事実を抽出
   - 関連する情報を横断的に分析

3. **評価結果を`review_and_hypothesis/` フォルダ内の各Markdownファイルに記載**
   - `review_and_hypothesis/review_results/` 配下に評価結果ファイルを作成・更新
   - `review_and_hypothesis/strength/` 配下に競合優位性を記載
   - `review_and_hypothesis/risk/` 配下にリスク要因を記載
   - `review_and_hypothesis/senario/` 配下に出口戦略やM&A候補を記載
   - `review_and_hypothesis/synergy/` 配下に事業シナジーを記載

4. **評価結果の記載内容**
   - 概要
   - 主要な発見事項
   - ポジティブ要因
   - リスク要因
   - 推奨事項
   - 結論
   - 根拠となる資料の参照先

## 初期レビューの実践例

**例: 事業性評価の初期レビュー**

1. **素材の確認**
   - `dd materials/business/事業概要.md`
   - `dd materials/business/今後の事業計画・予測表/今後の事業計画・予測表サマリ.md`
   - `dd materials/pitch slide/ピッチスライドサマリ.md`
   - `research/market and competitors/3C.md`
   - `research/market and competitors/競合企業.md`

2. **評価の実施**
   - 事業モデルの理解
   - 市場ポジションの分析
   - 成長性の評価
   - 競合優位性の抽出

3. **結果の記載**
   - `review_and_hypothesis/review_results/事業性評価.md` に評価結果を記載
   - `review_and_hypothesis/strength/競合優位性.md` に競合優位性を記載
   - `review_and_hypothesis/risk/リスク項目.md` に事業リスクを記載

## 注意事項

- 客観的な評価を心がける
- 根拠となる資料を明記する（`dd materials/` や `research/` の参照先を記載）
- 数値やデータを具体的に記載する
- リスクは過小評価・過大評価しない
- `dd materials/` と `research/` の情報を統合的に分析する
- 不足している情報は明確に記載し、次のステップ（ヒアリング等）で確認する

## 次のステップ

- ステップ6: 投資仮説の作成
- **コマンド**: `/dd:thesis` または `@agents/prompts/dd_build_thesis.md`
- **詳細**: `agents/cursor/dd_method/06_investment_hypotheses.md`

