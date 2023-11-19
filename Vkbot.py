import vk_api
import logging
import sys
from vk_api.longpoll import VkLongPoll, VkEventType

vk = vk_api.VkApi(token='vk1.a.F9zyUvx2pmMypVlBBlHk6wD4UGkHnA03Emu3lkrPmf0JiTTqtBzvHbn0Ouh-Y-qek7PuAERfpDT-4dYjRhfO97aV4iiwLz8fTxa9bYbw0SsOOSBzZ8K3T4yxODIhGBYiUuuVyJBH3dRy5tvZPy0b5FbHdw9S2FEdV2WrH_B6cQCTShi9pHQoyOsadn7aHQW3kO1tuWxh7tynWii4aBM0MA')
vk.get_api()
longpoll = VkLongPoll(vk)

def send_message(id, message):
    vk.method("messages.send", {'chat_id': id, 'message': message, 'random_id': 0})

def user_info(id):
    return vk.method("users.get", {'user_ids': id})

# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_chat:
            if event.to_me:
                if str(event.message).lower() == '/getid':
                    send_message(event.chat_id, message=f'Ваш личный ID: {event.user_id}')

                if str(event.message).lower() == '/stats':
                    user = user_info(id=event.user_id)
                    send_message(id=event.chat_id, message=f'''Имя: {user[0]['first_name']}
                    Фамилия: {user[0]['last_name']}
                    Никнейм: {user[0]['nickname']}
                    ''')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)