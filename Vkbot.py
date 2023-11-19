import vk_api
import logging
import sys
from vk_api.longpoll import VkLongPoll, VkEventType

vk = vk_api.VkApi(token='vk1.a.F9zyUvx2pmMypVlBBlHk6wD4UGkHnA03Emu3lkrPmf0JiTTqtBzvHbn0Ouh-Y-qek7PuAERfpDT-4dYjRhfO97aV4iiwLz8fTxa9bYbw0SsOOSBzZ8K3T4yxODIhGBYiUuuVyJBH3dRy5tvZPy0b5FbHdw9S2FEdV2WrH_B6cQCTShi9pHQoyOsadn7aHQW3kO1tuWxh7tynWii4aBM0MA')
vk.get_api()
longpoll = VkLongPoll(vk)

def send_message(message, chat_id = None, user_id = None):
    #Функция для отправки сообщений
    if chat_id:
        vk.method("messages.send", {'chat_id': chat_id, 'message': message, 'random_id': 0})
    if user_id:
        vk.method("messages.send", {'user_id': user_id, 'message': message, 'random_id': 0})

def user_info(user_id):
    return vk.method("users.get", {'user_ids': user_id, 'fields': ['nickname', 'followers_count']})


for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_chat:
            if event.to_me:
                if str(event.message).lower() == '/getid':
                    send_message(chat_id=event.chat_id, message=f'Ваш личный ID: {event.user_id}')

                if str(event.message).lower() == '/stats':
                    user = user_info(user_id=event.user_id)
                    print(user)
                    send_message(chat_id=event.chat_id, message=f'''@id{event.user_id} ({user[0]['first_name']})
                    Имя: {user[0]['first_name']}
                    Фамилия: {user[0]['last_name']}
                    У вас: {user[0]['followers_count']} подписчиков 
                    ''')

    if event.type == VkEventType.CHAT_UPDATE:
        if event.from_chat:
            if event.update_type == 6:
                send_message(chat_id=event.chat_id, message=f'Приветствуем тебя, {event.}')
            if event.update_type == 7:
                send_message(chat_id=event.chat_id, message=f'Прощай, {event}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)