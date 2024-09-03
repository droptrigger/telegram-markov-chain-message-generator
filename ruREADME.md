[English](README.md)

<div align="center">

# Генерация текста на основе отправленных сообщений
#### ! __БЕЗ ПОСТОРОННИХ БИБЛИОТЕК__ !
Бот, который использует цепи Маркова для генерации сообщений на основе тех, что были отправлены в ходе беседы.  
Мой телеграм канал - [Клик](https://t.me/CreateTrigger)

<img src='https://github.com/user-attachments/assets/2da0ccce-3d7e-4591-8d62-fdf76a382a84' width=60%/>
</div>

## 📖 Описание

После добавления в беседу, бот создает текстовый документ со всеми словами, которые вы пишете в беседу.

Далее, с помощью алгоритма из этих слов генерируется сообщение методом цепей Маркова. Можно генерировать сообщения самому, а можно настроить шанс ответа на сообщение в [config](bot/data/config.py).

* `citatgen` - Генерация рандомного сообщения.
<div align="center">
<img src='https://github.com/user-attachments/assets/d2086b44-78d9-4b4c-905b-22b7f4c0f95b' width=70%/>
</div>

* `citatgen <число>` - Генерация рандомного сообщения из определенного __числа__ слов.
<div align="center">
<img src='https://github.com/user-attachments/assets/0df66d22-b2a1-4a5b-900c-f1183cf0fc55' width=70%/>
</div>


## 🤖 Запуск бота

### 1. Для начала вам потребуeтcя клонировать репозиторий к себе на компьютер через Git Bash.

```git
git clone https://github.com/droptrigger/telegram-markov-chain-message-generator.git
```

### 2. Установим все необходимые библиотки:

```pip
pip install aiogram
pip install numpy
```

### 3. Переходим в https://t.me/BotFather и создаем бота. Разрешаем приглашать его в каналы (Должно быть `enabled`).
<div align="center">
<img src='https://github.com/user-attachments/assets/d82aff71-41dd-43c0-a41e-5344f8a6b404' width=50%/>
</div>

### 4. В том же BotFather копируем токен API.
<div align="center">
<img src="https://github.com/user-attachments/assets/16d2b471-2818-49c9-a248-4a8e77b37685" width=60% height=50%>
</div>

### 5. В [config](bot/data/config.py) вписываем этот токен вместо пропуска. Настраиваем переменные.

### 6. Добавляем бота в беседу.

## ! Обратите внимание !

Первые 3-10 сообщений бот не сможет генерировать цитаты, так ему недостаточно слов :)

<div align="center">
<img src="https://github.com/user-attachments/assets/1a44d4c6-af96-4892-84ce-a7874422b624" width=60% height=50%>
</div>

## ✅ Well done! Общайтесь! Теперь все должно работать.

Данный проект я сделал, вдохновившись сглыпой!
