# notify_annict_code

[Annict](https://annict.jp/)の[放送予定](https://annict.jp/programs)から、当日のものを取得し、AWS SNSにmessageとして渡すLambda。  
EventBridgeでcronを使って日次で実行、AWS Chatbotを使って、Slackへ通知する。

srcディレクトリをSAMのcode_uriに設定して、SAM deployできれば、結構楽になりそう・・・

## 実装時メモ

- 環境変数
  - ANNICT_ENDPOINT
    - default: https://api.annict.com/graphql
  - ANNICT_TOKEN
    - [個人用アクセストークン](https://annict.jp/settings/apps)の作成
  - SNS_TOPIC_ARN

- [AnnictのGraphQLドキュメント](https://developers.annict.jp/graphql-api/)
- [AnnictのgraphQLリファレンス](https://developers.annict.jp/graphql-api/reference/)
- ユニットテスト実行コマンド

> pipenv run pytest

## 実装機能

- Eventから日付取得  
  Key:s_date(%Y-%m-%d) で日付の指定を可能に
  デフォルトは当日
- graphqlでquery実行  
  pythonでのclient実装ライブラリは、最多のStar数になっていた、gqlを選択。
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
