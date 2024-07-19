from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import CommandStart, Command

wiki_router: Router = Router()

@wiki_router.message(CommandStart())
async def wiki_handler(msg: Message):
    await msg.answer("Salom xush kelibsiz!")