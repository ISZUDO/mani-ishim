from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import CommandStart, Command
from wiki import wiki_bot
kiril_lotin_router: Router = Router()
@kiril_lotin_router.message()
async def kiril_lotin_handler(msg:Message):
    await msg.answer(kiril_lotin_bot(msg.text))