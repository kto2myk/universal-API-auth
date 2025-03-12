
---

## ** 6️ `api_spec.md`（API仕様書）**
```markdown
# API 仕様書

##  freee API - OAuth 2.0 認証エンドポイント
### 認可URL
```plaintext
https://accounts.secure.freee.co.jp/public_api/authorize
?client_id=YOUR_CLIENT_ID
&redirect_uri=https://your-ngrok-url.ngrok.io/callback
&response_type=code
&scope=read
