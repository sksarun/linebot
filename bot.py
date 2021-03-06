from flask import Flask, request, abort
from Factory.PeriodsFactory import PeriodsFactory
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
from googletrans import Translator
import requests 
from simple_image_download import simple_image_download as simp

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
    message_text = event.message.text.lower()
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
    elif message_text == 'covid today':
        # heroku logs --app=lucyassistance
        r = requests.get("https://covid19.th-stat.com/api/open/today")
        enrichresult = r.json()
        finaltext = "วันที่:%s \n เพิ่มขึ้น:%d \n รวม:%d." % (enrichresult['UpdateDate'], enrichresult['NewConfirmed'],enrichresult['Confirmed'])
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=finaltext))
    elif message_text == 'pondperiod':
        period_fac = PeriodsFactory()
        description = period_fac.desc()
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=description))
    elif message_text == 'ovalimage':
        image_message = ImageSendMessage(
         original_content_url='https://i.ibb.co/h8j7dcP/S-88645640.jpg',
         preview_image_url='https://i.ibb.co/h8j7dcP/S-88645640.jpg'
        )
        line_bot_api.reply_message(
        event.reply_token,  
        image_message)
    elif message_text == 'itenary':
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='test'))
    elif message_text == 'readfile':

        f= open('guru99.txt','w+')
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='ola')
        )
    elif message_text == 'covid chart':
        image_message = ImageSendMessage(
         original_content_url='https://www.cs.umd.edu/~aporter/Tmp/bee.jpg',
         preview_image_url='https://www.cs.umd.edu/~aporter/Tmp/bee.jpg'
            )
        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif  "imagesearch"  in message_text: 
        l = message_text.split()
        response = simp.simple_image_download
        result = response().urls(l[1], 1)
        for i in result:
            image_message = ImageSendMessage(
            original_content_url=i,
            preview_image_url=i
            )
            line_bot_api.reply_message(
            event.reply_token,
            image_message)
    else:     
        translator = Translator()
        trans_text = translator.translate(message_text, dest='th')
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=trans_text.text))

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