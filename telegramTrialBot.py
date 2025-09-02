from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import Application, CommandHandler, CallbackQueryHandler


import os
from dotenv import load_dotenv
load_dotenv()
# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token below
Token = "YOUR_TELEGRAM_BOT_TOKEN"  # <-- Insert your Telegram bot token here
if not Token or Token == "YOUR_TELEGRAM_BOT_TOKEN":
    raise ValueError(
        "Please set your Telegram bot token in the Token variable.")
application = Application.builder().token(Token).build()


async def start(update, context):
    await update.message.reply_text("Hello! Welcome to Trial \n/help to know more")


async def help(update, context):
    await update.message.reply_text(
        """
        /start -> Welcome to the channel
/help -> This particular message
/content -> About various Animations
        """
    )

# async def content(update, context):
    await update.message.reply_text(" We have various Anime with their episodes available")

# Adding inline buttons to the content handler


async def content(update, context):
    keyboard = [
        [InlineKeyboardButton("Boruto", callback_data='Boruto')],
        [InlineKeyboardButton("Contact", callback_data='Contact')],
        [InlineKeyboardButton("More", callback_data='anime3')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose an Anime:", reply_markup=reply_markup)


async def button(update: Update, context):
    query = update.callback_query
    await query.answer()

    # Handle different callback data (button presses)
    if query.data == 'Boruto':
        await query.edit_message_text("Episode link : https://hianime.to/watch/boruto-naruto-next-generations-8143?ep=90259")
    elif query.data == 'Contact':
        await query.edit_message_text("You can contact on the registered mail I'd provided on the website")
    elif query.data == 'anime3':
        await query.edit_message_text(text="More Anime will be uploaded soon")


# async def Boruto(update, context):
    await update.message.reply_text("Episode link : https://hianime.to/watch/boruto-naruto-next-generations-8143?ep=90259")

# async def contact(update, context):
    await update.message.reply_text("You can contact on the registered mail I'd provided on the website")

application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('content', content))

application.add_handler(CallbackQueryHandler(
    button))  # Handles inline button clicks

application.add_handler(CommandHandler('help', help))

if __name__ == '__main__':
    application.run_polling()
