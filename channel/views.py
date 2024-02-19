import json
import requests
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from channel.services import create_user_session, get_default_menu, get_menu, get_menu_options, get_session

URL = f'{settings.APP_URL}/getpost/'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/'

@csrf_exempt
def telegram_bot(request):
    if request.method == 'POST':
        message = json.loads(request.body.decode('utf-8'))
        print(message)
        if 'callback_query' in message:
            handle_update(message)
        else:
            handle_update(message)
        
        return HttpResponse('ok')
    return HttpResponseBadRequest('Bad Request')

def handle_callback(update):
    chat_id = update['callback_query']['message']['chat']['id']
    response = update['callback_query']['data']
    f_msg = {
            'chat_id': chat_id,
            'text': f'You selected {response},\nPlease enter your MTN Mobile phone Number',
            'reply_markup':json.dumps({'remove_keyboard':True})
        }
    send_message('sendMessage', f_msg)

def handle_update(update):
    chat_id = update['callback_query']['message']['chat']['id'] if 'callback_query' in update else update['message']['chat']['id']
    text = update['callback_query']['data'] if 'callback_query' in update else update['message']['text']
    msg_id = update['callback_query']['message'] if 'callback_query' in update else update['message']['message_id']
    user_session = get_session(chat_id=chat_id)
    menu=None
    menu_options = []
    if not user_session:
        menu = get_default_menu()
        user_session = create_user_session(
            chat_id=chat_id,
            msg_id=msg_id, 
            message=text, 
            menu_id=menu.id
        )
        if menu.has_options:
            option_items = get_menu_options(menu_id=menu.id)
            for item in option_items:
                menu_options.append([{"text": item.label, "callback_data": item.data}])

    else:
        menu = get_menu(user_session.menu_id)
        user_session.menu_id = menu.id
        user_session.last_text = user_session.last_text + '|' + text
        user_session.is_closed = menu.close_session
        user_session.save()
        if menu.has_options:
            option_items = get_menu_options(menu_id=menu.id)
            for item in option_items:
                menu_options.append([{"text": item.label, "callback_data": item.data}])


    # keyboard = {
    #         "inline_keyboard": [
    #             [
    #                 {"text": "Normal", "callback_data": "Normal"},
                    
    #             ],
    #             [{"text": "VVIP", "callback_data": "VVIP"}]
    #         ],
    #         "resize_keyboard":'false'
    #     }
    f_msg = {
            'chat_id': chat_id,
            'text': menu.label,
            #'reply_markup': json.dumps(keyboard) ,
        }
    if len(menu_options):
        keyboard = {"inline_keyboard":menu_options}
        f_msg['reply_markup'] = json.dumps(keyboard)
    
    send_message("sendMessage", f_msg)
 

def send_message(method, data):
   print(data)
   return requests.post(TELEGRAM_API_URL + method, data)


def setwebhook(request):
    response = requests.post(TELEGRAM_API_URL+ "setWebhook?url=" + URL).json()
    print(TELEGRAM_API_URL)
    return HttpResponse(f"{response}")