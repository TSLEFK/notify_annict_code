
# 実装時メモ

https://github.com/kk6/python-annict

ユニットテスト実行コマンド

> pipenv run pytest

## 実装機能

- Eventから日付取得

Key:s_date(%Y-%m-%d) で日付の指定を可能に

- graphqlでquery実行
    pythonでのclient実装ライブラリの選択。
    最多のStarになっていた、gqlを選択。
    https://graphql.org/code/#python-1
- graphqlの結果加工
- SNSにpush

## graphqlのqueryスキーマ

```schema
# Write your query or mutation here
query {
  viewer {
    programs {
      nodes {
        work {
          seasonName
          seasonYear
          title
          viewerStatusState
        }
        channel {
          name
        }
        episode {
          number
          title
        }
        startedAt
        rebroadcast
      }
    }
  }
}
```

結果一部

```schema
{
  "data": {
    "viewer": {
      "programs": {
        "nodes": [
          {
            "work": {
              "seasonName": "WINTER",
              "seasonYear": 2018,
              "title": "衛宮さんちの今日のごはん",
              "viewerStatusState": "WATCHING"
            },
            "channel": {
              "name": "ABEMA アニメ"
            },
            "episode": {
              "number": 4,
              "title": "春野菜とベーコンのサンドイッチ"
            },
            "startedAt": "2018-04-01T12:00:00Z",
            "rebroadcast": false
          },
```
