from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)

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
    message_text = event.message.text
    if message_text == 'buttons':
        buttons_template = ButtonsTemplate(
            title='My buttons sample', text='Hello, my buttons', actions=[
                URIAction(label='Go to line.me', uri='https://line.me'),
                PostbackAction(label='ping', data='ping'),
                PostbackAction(label='ping with text', data='ping', text='ping'),
                MessageAction(label='Translate Rice', text='米')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif message_text == 'dome': 
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='ชล[th]'))
    elif message_text == 'tong': 
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='tongpond'))
    elif message_text == 'pond': 
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='pondtong'))
    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message_text+'ชลไข่'))

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    
    
 
        line_bot_api.reply_message(
            event.reply_token,
            LocationSendMessage(
                title='Location', address=event.message.address,
                latitude=event.message.latitude, longitude=event.message.longitude
            )
        )

if __name__ == "__main__":
    app.run()