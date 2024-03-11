# ベースイメージの指定
FROM python:3.8-slim

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係ファイルのコピー
COPY requirements.txt ./

# 依存関係のインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードのコピー
COPY . .

# アプリケーションの実行
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]