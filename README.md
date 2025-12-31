# CSVデータ管理 & 履歴保存システム

## 概要
本ツールは、CSVファイルをアップロードし、その内容をブラウザで閲覧するだけでなく、**SQLiteデータベースへ自動保存・蓄積**できるWebアプリケーションです。

「単なる閲覧で終わらず、過去のデータをいつでも振り返り、管理できる」ことを目的として開発しました。
営業事務やキッティング現場での「データの散逸」という課題を解決するためのプロトタイプです。

## ディレクトリ構成
```text
csv-web-app/
├── instance/           # SQLiteデータベース保存用フォルダ（ローカル実行時に自動生成）
│   └── csv_history.db  # データベース本体（.gitignoreによりGit管理外）
├── templates/          # HTMLテンプレート
│   └── index.html      # メイン画面（アップロード・一覧表示）
├── .gitignore          # Git管理除外設定
├── app.py              # Flask/SQLAlchemyメインプログラム
├── requirements.txt    # 依存ライブラリ一覧
└── README.md           # 本ファイル
```

## 機能
- CSVアップロード & 解析: Pandasによる高速なデータ処理
- DB永続化: SQLAlchemyを採用し、アップロードデータをSQLiteへ保存
- 履歴閲覧機能: 過去にアップロードしたデータをDBから呼び出し表示
- セキュリティ配慮: `secure_filename` により、ファイル名のサニタイズ実装
- レスポンシブUI: HTML5/CSS3による、デバイスを問わないレイアウト最適化

## 動作内容
1. ブラウザでアプリ（localhost:5000）にアクセス
2. CSVファイルを選択し「アップロード」を実行
3. app.py がデータを受信し、Pandasで構造化
4. **同時にSQLAlchemyを介してSQLiteへデータを自動保存**
5. HTMLテンプレートを通じて、ブラウザ上に履歴と現在のデータを表示

## 実行方法

### 1. プロジェクトの準備
プロジェクトのフォルダに移動します。 
```bash
cd csv-web-app
```

### 2. 仮想環境の作成と起動 (推奨)
```bash
# Mac / Linux の場合
python -m venv venv
source venv/bin/activate

# Windows の場合
python -m venv venv
.\venv\Scripts\activate
```
### 3. 必要なライブラリの一括インストール
```bash
pip install -r requirements.txt
```
### 4. アプリケーションの起動
```bash
python app.py
```
### 5. ブラウザでアクセス
http://127.0.0.1:5000 にアクセスしてください

## 仕様詳細

### 1. Webサーバー仕様
| 項目 | 内容 |
| :--- | :--- |
| 言語 | Python 3.11 |
| フレームワーク | Flask 3.0.3 |
| データベース | SQLite (SQLAlchemy ORM)|
| データ解析| Pandas 2.0.3 |
| ポート番号| 5000|
| 対応ファイル | CSV(.csv)|

### 2. 画面構成
| 画面 | 内容 |
| :--- | :--- |
| アップロード画面 | ファイル選択および送信ボタン|
| 閲覧画面 | CSVの中身をテーブル形式で表示|
| 履歴一覧 | 過去のアップロード日時とファイル名の一覧表示 |

## 想定される利用シーン
- コマンドライン操作に慣れていないユーザーへのデータ提供
- CSVデータの中身を手軽にブラウザで確認
- 社内向け簡易データ管理ツールのプロトタイプ

## 今後の拡張予定
- データ分析: 保存された過去データからの傾向分析・グラフ化
- フィルタ機能: ブラウザ上での動的なデータの絞り込み・ソート
- ユーザー認証: 社内利用を想定したログイン・権限管理機能
- API連携: 蓄積データをJSON形式で外部システムへ提供

## 使用技術
- Language: Python 3.11
- Framework: Flask 3.0.3
- Database: SQLite / SQLAlchemy
- Library: Pandas 2.0.3
- Frontend: HTML5 / CSS3
- Environment: venv 
