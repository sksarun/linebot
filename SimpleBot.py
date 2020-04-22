from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('KTT+7BjQjyahV6l1lBWBt+exfmZ40uihk3XDQur4Vt71qpUbE8LU6Zfo1XIomv4vIoiZxjKLR7yASC4kGtqnHOn2h3X0vBif4xEIGdOKAiGh1GTivAwPOPxH459cG+8ITo5Ff7qCweH2njy142s3FAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f12dee5ab00209df6404acd8cfa57435')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()