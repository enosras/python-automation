import emoji

# emojiTools = emoji.emojize.__doc__
# print(emojiTools)
import pyemoji

print(emoji.emojize("Python is fun :thumbsup:", language="alias"))
print("-------------------------------------------")
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# help(emoji)
print(emoji.emojize("Python is fun :black_man:", variant="text_type"))
print(emoji.demojize("Python is fun 👍"))
print(emoji.demojize("I 🥹 Python"))
print("-------------------------------------------")
print(emoji.emojize("I love :pizza:", language="alias"))
print(emoji.emojize("I love :pizza:", variant="emoji_type"))
print(emoji.emojize("I love :pizza:", variant="text_type"))
