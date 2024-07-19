from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import CommandStart, Command
from handlers.muha import wiki_bot
translate_router: Router = Router()
@translate_router.message()
async def trans_handler(msg:Message):
    await msg.answer(googletran(msg.text))