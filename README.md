# Django を使ってWebサイトを作成する

リポジトリ作成

ローカルにクローン
```
% git clone リポジトリ名
```

仮想環境の作成
```
% pipenv shell
```

requirements.txt を作成し、開発に必要なパッケージを記載する

パッケージをインストール
```
% pip install -r requirements.txt
```

プロジェクトの作成
```
% django-admin startproject プロジェクト名 .
```

DBのセットアップ
```
% python manage.py migrate
```

ブラウザで確認
```
% python manage.py runserver
```

[こちら](http://127.0.0.1:8000/) にアクセス