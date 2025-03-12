# Universal OAuth 2.0 API Client

## 📌 概要
このリポジトリは、汎用的な **OAuth 2.0 認証 & API クライアント** の実装です。  
どんなAPIにも適用可能で、SlackやLINE Notifyに通知を送る機能も含まれています。

## 📌 機能
- OAuth 2.0 認証（アクセストークン & リフレッシュトークン管理）
- APIクライアント（GET / POST リクエストを簡単に送信）
- Slack / LINE 通知機能

## 📌 使い方
```python
from auth_manager import OAuthClient
from api_client import APIClient
from notifier import Notifier

auth_client = OAuthClient(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKEN_URL)
auth_client.get_access_token("AUTH_CODE")

api_client = APIClient("https://api.example.com", auth_client)
data = api_client.get("/endpoint")

notifier = Notifier(slack_webhook_url="https://slack.com/webhook")
notifier.send_slack_message("Hello, Slack!")
