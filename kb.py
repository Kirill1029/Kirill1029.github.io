from aiogram.types import KeyboardButton, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


read_terms_of_use_builder = InlineKeyboardBuilder()
read_terms_of_use_builder.row(InlineKeyboardButton(text="Read",
                                                   callback_data="read_terms_of_use"))

read_terms_of_use_keyboard = read_terms_of_use_builder.as_markup()


accept_keyboard_builder = InlineKeyboardBuilder()
accept_keyboard_builder.add(InlineKeyboardButton(text="Accept",
                                                 callback_data="accept_terms_of_use"))
accept_keyboard_builder.add(InlineKeyboardButton(text="Decline",
                                                 callback_data="decline_terms_of_use"))

accept_keyboard = accept_keyboard_builder.as_markup()


go_to_webapp_builder = InlineKeyboardBuilder()
go_to_webapp_builder.add(InlineKeyboardButton(text="go to webapp",
                                              web_app=WebAppInfo(url='https://google.com')))

go_to_webapp_keyboard = go_to_webapp_builder.as_markup()
