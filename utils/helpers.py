import asyncio
import datetime

async def auto_delete_msg(bot, chat_id, message_id, delay=30):
    await asyncio.sleep(delay)
    try:
        await bot.delete_messages(chat_id, message_id)
    except:
        pass

def parse_time(time_str):
    unit = time_str[-1].lower()
    if unit not in ['m', 'h', 'd']:
        return None
    try:
        value = int(time_str[:-1])
        if unit == 'm':
            return datetime.timedelta(minutes=value)
        elif unit == 'h':
            return datetime.timedelta(hours=value)
        elif unit == 'd':
            return datetime.timedelta(days=value)
    except ValueError:
        return None
