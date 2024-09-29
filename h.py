from pyrogram import Client

api_id = "22471979"
api_hash = "7bd48f479ef7421576f62c8d4b8a7832"
bot_token = "7686874073:AAEM8YFRDlaRzALHVqluXgSUeQLCDYP3G2Q"

app = Client(
    "ButmaloBot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
