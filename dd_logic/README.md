# dd_logic

DD作業の**ロジック・テンプレート**を格納するフォルダです。

## 構成

| パス | 役割 |
|------|------|
| **template/** | 新規案件のひな形。`deals/{会社名}/` を作るときにここをコピーして使う |
| **investment_methodology/** | 全案件に通底する「投資にかかる思考法」のテンプレート（人間が記述・編集） |

## 新規案件の作成

1. `dd_logic/template` を `deals/{会社名}/` にコピーする（例: `cp -r dd_logic/template deals/株式会社ABC`）
2. その案件の `業務整理用/` に、**対応表に従ったフォルダ名**でファイルを配置する（対応表は [.cursor/skills/dd-copy-classify/SKILL.md](../.cursor/skills/dd-copy-classify/SKILL.md) または [program/run_copy.py](../program/run_copy.py) の COPY_MAP）
3. Cursor で「案件は deals/株式会社ABC で /dd:copy を実行して」と依頼する（`run_copy.py` が案件ルートを指定して実行され、業務整理用→dd materials のコピー・PDF→PNG・XLSX→CSV が行われる）
4. 続けて `/dd:summarize`、`/dd:update_basics`、`/dd:questions` や `/dd:review`、`/dd:thesis` 等で作業を進める

**サンプルで試す場合**: `template/業務整理用` に対応表どおりのフォルダとサンプルファイルを用意しておけば、template を deals/会社名 にコピーした時点でそのまま `/dd:copy` の入力になる。

## 投資思考法（investment_methodology）

- **dd_logic/investment_methodology/** … 全案件共通の「どう考えるか」を人間が記述するテンプレート
- 各案件の **review_and_hypothesis/senario/investment_theory.md** … 当該案件の投資テーゼ・シナリオ（共通思考法を参照しつつ案件ごとに記述）

詳細は [investment_methodology/README.md](investment_methodology/README.md) を参照。
