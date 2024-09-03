import random

from aiofile import AIOFile
from aiogram import Router, Bot
from aiogram.types import Message

from bot.data.config import TOKEN_TG, CHANCE, SAVE_LINKS, SAVE_PINGS, MAX_WORDS
from bot.functions.words import write_words, send_and_gen_sentence

router = Router()
bot = Bot(TOKEN_TG)


@router.message()
async def general(message: Message):
    """Eating all messages"""

    if message.chat.type in ["supergroup", "group", "private"]:

        if message.new_chat_members is not None:
            new_members = message.new_chat_members
            for member in new_members:
                user_id = member.id
                if user_id == 7062857043:
                    await message.answer("Hello!")
                    async with AIOFile(f"../dialogs/dialogs{message.chat.id}.txt", "a", encoding="utf-8") as f:
                        await f.write("")

        if message.new_chat_members is None:
            if message.text is not None:
                if (
                        "citatgen" not in message.text.lower()
                        and
                        ((".com" not in message.text.lower() and "https://" not in message.text.lower()) if not SAVE_LINKS else True)
                        # To avoid saving links - https://example.com
                        and
                        ("@" not in message.text.lower() if not SAVE_PINGS else True)
                        # To avoid saving pings - @DropTrigger
                ):
                    await write_words(message.text, f"../dialogs/dialogs{message.chat.id}.txt")

                if random.randint(0, 100) <= CHANCE and "citatgen" not in message.text.lower():
                    result = await send_and_gen_sentence(f"../dialogs/dialogs{message.chat.id}.txt")
                    if message.chat.type == "supergroup":
                        await message.answer(result, reply_to_message_id=message.reply_to_message.message_id)
                    elif message.chat.type in ["group", "private"]:
                        await message.answer(result)

                if message.text.lower() == "citatgen":
                    result = await send_and_gen_sentence(f"../dialogs/dialogs{message.chat.id}.txt")
                    if message.chat.type == "supergroup":
                        await message.answer(result, reply_to_message_id=message.reply_to_message.message_id)
                    elif message.chat.type in ["group", "private"]:
                        await message.answer(result)

                if message.text.lower().startswith("citatgen "):
                    count = message.text.split(" ")[1]

                    try:
                        count = int(count)
                        if count <= MAX_WORDS:
                            result = await send_and_gen_sentence(f"../dialogs/dialogs{message.chat.id}.txt", count, count)
                            if message.chat.type == "supergroup":
                                await message.answer(result, reply_to_message_id=message.reply_to_message.message_id)
                            elif message.chat.type in ["group", "private"]:
                                await message.answer(result)
                        else:
                            if message.chat.type == "supergroup":
                                await message.answer("Too many characters", reply_to_message_id=message.reply_to_message.message_id)
                            elif message.chat.type in ["group", "private"]:
                                await message.answer("Too many characters")
                    except:
                        if message.chat.type == "supergroup":
                            await message.answer("Use: citatgen <number>\n"
                                             "Example: citatgen 10", reply_to_message_id=message.reply_to_message.message_id)
                        elif message.chat.type in ["group", "private"]:
                            await message.answer("Use: citatgen <number>\n"
                                                 "Example: citatgen 10")
