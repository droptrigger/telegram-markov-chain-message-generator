[Russian](ruREADME.md)

<div align="center">

# Text generation based on sent messages
#### ! __WITHOUT OUTSIDE LIBRARIES__ !
A bot that uses Markov chains to generate messages based on those sent during the conversation.  
My TG channel - [Click](https://t.me/CreateTrigger)

<img src='https://github.com/user-attachments/assets/2da0ccce-3d7e-4591-8d62-fdf76a382a84' width=60%/>
</div>

## 📖 Description

After adding to the conversation, the bot creates a text document with all the words that you write in the conversation.

Next, using an algorithm, a message is generated from these words using the Markov chain method. You can generate messages yourself, or you can configure the chance of a response to a message in [config](bot/data/config.py).

* `citatgen` - Random message generation.
<div align="center">
<img src='https://github.com/user-attachments/assets/d2086b44-78d9-4b4c-905b-22b7f4c0f95b' width=70%/>
</div>

* `citatgen <number>` - Generating a random message from a certain __number__ of words.
<div align="center">
<img src='https://github.com/user-attachments/assets/0df66d22-b2a1-4a5b-900c-f1183cf0fc55' width=70%/>
</div>

## 🤖 Launching the bot

### 1. First, you will need to clone the repository to your computer via Git Bash.

```git
git clone https://github.com/droptrigger/telegram-markov-chain-message-generator.git
```

### 2. We will install all the necessary libraries:

```pip
pip install aiogram
pip install numpy
```

### 3. Go to https://t.me/BotFather and we create a bot. We allow you to invite him to the channels (It should be `enabled`).
<div align="center">
<img src='https://github.com/user-attachments/assets/d82aff71-41dd-43c0-a41e-5344f8a6b404' width=50%/>
</div>

### 4. In the same BotFather, we copy the API token.
<div align="center">
<img src="https://github.com/user-attachments/assets/16d2b471-2818-49c9-a248-4a8e77b37685" width=60% height=50%>
</div>

### 5. In [config](bot/data/config.py) enter this token instead of a pass. Setting up variables.

### 6. Adding a bot to the conversation.

## ! Please note!

The bot will not be able to generate quotes for the first 3-10 messages, as there are not enough words for it :)

<div align="center">
<img src="https://github.com/user-attachments/assets/1a44d4c6-af96-4892-84ce-a7874422b624" width=60% height=50%>
</div>

## ✅ Well done! Общайтесь! Теперь все должно работать.
