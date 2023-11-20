import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardButton, VkKeyboardColor

#[Основные имена] =================================================================
vk = vk_api.VkApi(token='vk1.a.F9zyUvx2pmMypVlBBlHk6wD4UGkHnA03Emu3lkrPmf0JiTTqtBzvHbn0Ouh-Y-qek7PuAERfpDT-4dYjRhfO97aV4iiwLz8fTxa9bYbw0SsOOSBzZ8K3T4yxODIhGBYiUuuVyJBH3dRy5tvZPy0b5FbHdw9S2FEdV2WrH_B6cQCTShi9pHQoyOsadn7aHQW3kO1tuWxh7tynWii4aBM0MA')
vk.get_api()
longpoll = VkLongPoll(vk)
admin_id=397675048

#[/kick] =================================================================
def kick(chat_id, member_id):
    #Функция кик участника из беседы
    vk.method("messages.send", {'chat_id': chat_id, 'message': f'Участник @id{member_id} был кикнут', 'random_id': 0})
    vk.method("messages.removeChatUser", {'chat_id': chat_id, 'user_id': member_id})

#[Отправка сообщений в чат] =================================================================
def send_message(message, chat_id = None, user_id = None):
    #Функция для отправки сообщений
    if chat_id:
        vk.method("messages.send", {'chat_id': chat_id, 'message': message, 'random_id': 0})
    else:
        vk.method("messages.send", {'user_id': user_id, 'message': message, 'random_id': 0})

#[Информация о пользователе /getid] =========================================================
def user_info(user_id):
    return vk.method("users.get", {'user_ids': user_id, 'fields': ['nickname', 'followers_count']})

#[Обработчик событий] =================================================================
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_chat:
            if event.to_me:
                if str(event.message).lower() == '/getid':
                    send_message(chat_id=event.chat_id, message=f'Ваш личный ID: {event.user_id}')

                if str(event.message).lower() == '/stats':
                    user = user_info(user_id=event.user_id)
                    send_message(chat_id=event.chat_id, message=f'''@id{event.user_id} ({user[0]['first_name']})
                                    Имя: {user[0]['first_name']}
                                    Фамилия: {user[0]['last_name']}
                                    У вас: {user[0]['followers_count']} подписчиков 
                                    ''')
                    
                if str(event.message).lower() == '/kick':
                    kick(chat_id=event.chat_id, member_id=event.from_user)

    if event.type == VkEventType.CHAT_UPDATE:
        if event.from_chat:
            if event.update_type == 6:
                send_message(chat_id=event.chat_id, message=f'Приветствуем нового участника')
            if event.update_type == 7:
                send_message(chat_id=event.chat_id, message=f'Прощай дружище')


