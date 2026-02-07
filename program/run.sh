#!/usr/bin/env bash
# リポジトリルートから実行: ./program/run.sh [案件ルート]
# 例: ./program/run.sh deals/株式会社ABC
# 案件ルートを省略した場合はリポジトリルートを案件ルートとして使用（後方互換）
# 初回は .venv 作成と pip install を行う
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV="$SCRIPT_DIR/.venv"

cd "$REPO_ROOT"
if [[ ! -d "$VENV" ]]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -r "$SCRIPT_DIR/requirements.txt"
fi
"$VENV/bin/python" "$SCRIPT_DIR/run_copy.py" "$@"
