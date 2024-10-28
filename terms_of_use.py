from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from kb import read_terms_of_use_keyboard, \
    accept_keyboard, go_to_webapp_keyboard
from db import User

router = Router()

@router.message(Command('start'))
async def start_handler(message: Message):
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    if not User.exists(user_id):
        await message.answer(text=f"Hello, {full_name}",
                             reply_markup=read_terms_of_use_keyboard)
        User.add_new_user(user_id)
    else:
        user = User.find_user(user_id)
        if user.accepted == 1:
            await message.answer(text="Use webapp",
                                 reply_markup=go_to_webapp_keyboard)
        else:
            await message.answer(text=f"Hello, {full_name}",
                                 reply_markup=read_terms_of_use_keyboard)


@router.callback_query(F.data == "read_terms_of_use")
async def read_terms_of_use_handler(callback: CallbackQuery):
    try:
        await callback.message.edit_text(text="Terms of use",
                                         reply_markup=accept_keyboard)
    except Exception as e:
        print(e)
        await callback.message.answer(text="Terms of use",
                                      reply_markup=accept_keyboard)
    await callback.answer()

@router.callback_query(F.data == "accept_terms_of_use")
async def accept_terms_of_use_handler(callback: CallbackQuery):
    user = User.find_user(callback.from_user.id)
    if user is None:
        user = User.add_new_user(callback.from_user.id)
    user.update_terms_status(1)
    await callback.message.answer(text="You accepted terms of use")
    await callback.message.answer(text="Use webapp",
                                  reply_markup=go_to_webapp_keyboard)
    await callback.answer()

@router.callback_query(F.data == "decline_terms_of_use")
async def accept_terms_of_use_handler(callback: CallbackQuery):
    user = User.find_user(callback.from_user.id)
    if user is None:
        user = User.add_new_user(callback.from_user.id)
    user.update_terms_status(0)
    await callback.message.answer(text="You declined terms of use")
    await callback.answer()


