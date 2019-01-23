from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = flask(__name__)

line_bot_api = LineBotApi('esy9NTcG4gXWdN77PEaX2QMKjtJA0kNd3GSMpa26H2XAX64+CSKHrHBRWhndS1FesEB2irM7o2lp8Tb61Spq3z85OqubPkuaPrdnPlsVBCp4Jde6DVn9+t67MAELbs1rv4j7hxubsab+ACxJG0ACLQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b653a289b8e5203b0e317d7ab077a7b3')


@app.route("/callback", methods=['POST'])
def callback():
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
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='hello'))


if __name__ == "__main__":
    app.run()