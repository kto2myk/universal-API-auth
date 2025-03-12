import os

# **フォルダを作成する場所を指定**
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# PROJECT_NAME = "izumo_insight"
# PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
PROJECT_PATH = BASE_DIR

# **作成するフォルダ**
dirs = [
    f"{PROJECT_PATH}/src",          # メインのPythonパッケージ
    f"{PROJECT_PATH}/src/logs",     # ログファイル
    f"{PROJECT_PATH}/src/tests",    # ユニットテスト
    f"{PROJECT_PATH}/scripts",      # 補助スクリプト
    f"{PROJECT_PATH}/docs",         # ドキュメント
]

# **作成するファイル**
files = [
    f"{PROJECT_PATH}/.env",                         # 環境変数（APIキーなど）
    f"{PROJECT_PATH}/.gitignore",                   # Git無視リスト
    f"{PROJECT_PATH}/requirements.txt",             # Pythonライブラリ管理
    f"{PROJECT_PATH}/config.py",                    # 設定ファイル
    f"{PROJECT_PATH}/main.py",                      # メインスクリプト
    f"{PROJECT_PATH}/src/__init__.py",              # Pythonパッケージ認識用
    f"{PROJECT_PATH}/src/settings.py",              # 設定管理
    f"{PROJECT_PATH}/src/auth_manager.py",          # OAuth認証 & トークン管理
    f"{PROJECT_PATH}/src/data_fetcher.py",          # APIデータ取得
    f"{PROJECT_PATH}/src/profit_calculator.py",     # 損益計算
    f"{PROJECT_PATH}/src/notifier.py",              # 通知処理
    f"{PROJECT_PATH}/src/utils.py",                 # ログ管理など
    f"{PROJECT_PATH}/src/logs/app.log",             # ログファイル
    f"{PROJECT_PATH}/scripts/start_ngrok.bat",      # ngrok起動スクリプト
    f"{PROJECT_PATH}/scripts/refresh_token.py",     # トークン更新スクリプト
    f"{PROJECT_PATH}/docs/README.md",               # プロジェクト概要
    f"{PROJECT_PATH}/docs/setup_guide.md",          # 開発環境セットアップ
    f"{PROJECT_PATH}/docs/api_spec.md",             # API仕様書
    f"{PROJECT_PATH}/src/tests/test_auth_manager.py",   # テスト（認証）
    f"{PROJECT_PATH}/src/tests/test_data_fetcher.py",   # テスト（データ取得）
    f"{PROJECT_PATH}/src/tests/test_profit_calculator.py",  # テスト（損益計算）
]

# **フォルダを作成**
for d in dirs:
    os.makedirs(d, exist_ok=True)

# **ファイルを作成**
for f in files:
    with open(f, "w") as file:
        pass  # 空ファイルを作成

print(f"✅ プロジェクトフォルダ & ファイルを {PROJECT_PATH} に作成しました！ 🚀")
