# rtt_checker

SSH のポートフォワードの RTT を計測するやつ

## サーバーの起動

```sh
ssh $host_name -L 8080:localhost:8080 python3 < server.py
```

## クライアントの起動

```sh
python3 client.py
```

## 実行結果の例

```sh
$ python3 client.py
合計時間: 1447 ms
平均時間: 14.47 ms
```
