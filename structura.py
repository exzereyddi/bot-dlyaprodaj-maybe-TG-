# structura.py
import telebot
from telebot import types
from config import WEBSITE_URLS, FUNPAY_URL  # , record_user_messages
from storage import record_user_messages


def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_command(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        item_shop = types.KeyboardButton("/shop")
        item_clients = types.KeyboardButton("/clients")
        item_promo = types.KeyboardButton("/promo")
        item_contact = types.KeyboardButton("/contact")
        markup.add(item_shop, item_clients, item_promo, item_contact)

        help_text = """Навигация:
        /shop - Ссылка на FunPay.
        /clients - Сайты читов.
        /promo - Промокоды.
        /contact - Контакты."""
        bot.send_message(message.chat.id, help_text, reply_markup=markup, disable_web_page_preview=True) # disable_web_page_preview=True

    @bot.message_handler(commands=['shop'])
    def shop_command(message):
        markup = types.InlineKeyboardMarkup()
        button_funpay = types.InlineKeyboardButton("FunPay", url=FUNPAY_URL)
        markup.add(button_funpay)
        bot.send_message(message.chat.id, "Перейти в магазин:", reply_markup=markup, disable_web_page_preview=True) # disable_web_page_preview=True

    @bot.message_handler(commands=['clients'])
    def clients_command(message):
        markup = types.InlineKeyboardMarkup()
        for name, url in WEBSITE_URLS.items():
            button = types.InlineKeyboardButton(name, url=url)
            markup.add(button)

        bot.send_message(message.chat.id, "Нажми на кнопку ниже, чтобы перейти на сайты:", reply_markup=markup, disable_web_page_preview=True) # disable_web_page_preview=True

    @bot.message_handler(commands=['promo'])
    def promo_command(message):
        promo_text = """Промокоды:
        Stormhvh: Fluger
        Wexside: Fluger
        Delta: FLUGERNEW"""
        bot.send_message(message.chat.id, promo_text, disable_web_page_preview=True) # disable_web_page_preview=True

    @bot.message_handler(commands=['contact'])
    def contact_command(message):
        contact_text = """Контакты:
        ТГ Канал: t.me/Flugerovs
        Сотрудничество Флюги: t.me/FlugerOld
        Ютуб Флюги: youtube.com/@FlugerNew
        Fluger Client ВК: vk.com/fluger_client
        Fluger Client ТГ Канал: t.me/FlugerClientDLC"""
        bot.send_message(message.chat.id, contact_text, disable_web_page_preview=True) # disable_web_page_preview=True