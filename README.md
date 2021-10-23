# 起動方法

```bash

#事前にneolgd辞書の場所を.envファイルにて指定しておく(場所は環境ごとに異なる)
### 例: dockerイメージ「python:3.8.6」（Mac M1）チップの場合
MECAB_DIC_URL='-d /usr/lib/aarch64-linux-gnu/mecab/dic/mecab-ipadic-neologd'

$ docker-compose build

$ docker-compose up -d

# それぞれのコンテナに入り以下起動コマンドを実行

### front
$ yarn dev

##### ＊もしエラーが出た時はyarn.lockを削除して以下コマンドを実行
$ yarn install
$ yarn dev

### server
$ uwsgi --ini uwsgi.ini
```