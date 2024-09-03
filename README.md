[Russian](ruREADME.md)

<div align="center">

# Text generation based on sent messages
#### ! __WITHOUT OUTSIDE LIBRARIES__ !
A bot that uses Markov chains to generate messages based on those sent during the conversation.  
My TG channel - [Click](https://t.me/CreateTrigger)

<img src='https://github.com/user-attachments/assets/e286aa6e-dac9-4e6b-98a7-03142881295a' width=60%/>
</div>

## 📖 Description

After adding to the conversation, the bot creates a text document with all the words that you write in the conversation.

Next, using an algorithm, a message is generated from these words using the Markov chain method. You can generate messages yourself, or you can configure the chance of a response to a message in [config](bot/data/config.py).

* `citatgen` - Random message generation.
<div align="center">
<img src='https://github.com/user-attachments/assets/fbf3029d-f648-442f-9113-03ce9edcc893' width=70%/>
</div>

* `citatgen <number>` - Generating a random message from a certain __number__ of words.
<div align="center">
<img src='https://github.com/user-attachments/assets/da75fb86-92e4-4011-b1d5-e44eb0dac50b' width=70%/>
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
<img src="https://github.com/user-attachments/assets/4d721edc-7af1-4c71-bdcb-8ea05849cbf4" width=60% height=50%>
</div>

## ✅ Well done! Общайтесь! Теперь все должно работать.