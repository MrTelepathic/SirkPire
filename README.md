<h1>SirkPire 1.0<h1/>

> SirkPire is a powerful and easy library for building self bots in Rubika

<p align='center'>
    <img src='https://iili.io/HIjPRS9.jpg' alt='SirkPire Library 1.0' width='356'>
    <a href='https://github.com/MrTelepathic/SirkPire'>GitHub</a>
</p>

<hr>

**Example:**
``` python
from SirkPire import Bot, Message

bot = Bot('TOKEN')

for msg in bot.on_message():
    s = Message(msg)
    if s.text() == 'Hello':
        bot.send_text(s.chat_id(), 'Hello from SirkPire Library', s.message_id())
```

<hr>

### Features:
    
- *Fast* : **The minimum request time is 0.07 seconds and the maximum request time is 0.3 seconds**
- *Easy* : **All methods and features are designed as easy and optimal as possible**
- *Powerful* : **While the library is simple, it has high speed and features that make your work easier and faster**

<hr>

# Rubika : @SirkPire

### Install or Update:

``` bash
pip install -U SirkPire
```
