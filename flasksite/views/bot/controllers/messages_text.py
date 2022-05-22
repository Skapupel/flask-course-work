

start_without_username = '''Привіт я телеграм бот Flask Calendar📅!

Я призначений для перегляду вашого календаря та щоб отримувати сповіщення про події в календарі.

⚠️Для початку створіть логін для вашого календаря⚠️.
За допомогою команди /username ви можете встановити логін.
Використовуйте латинські літери, цифри та знаки пунктуації.
логін не може містити пробіли.

Коли ви створили логін, можете прописати команду /help.
Ця команда виведе всі доступні команди а також як відкрити ваш календар.'''


start_with_username = '''Привіт я телеграм бот Flask Calendar📅!

Я призначений для перегляду вашого календаря та щоб отримувати сповіщення про події в календарі.

Для того щоб переглянути всі доступні команди використовуйте команду /help.
Ця команда також покаже вам як відкрити ваш календар.'''


username_already_exists = '''Вибачте, але цей логін вже зайнятий.
Виберіть інший логін.

Використовуйте команду /username для встановлення логін.
Використовуйте латинські літери, цифри та знаки пунктуації.
логін не може містити пробіли.'''


TEXT = {
    'start_without_username': start_without_username,
    'start_with_username': start_with_username,
    'username_already_exists': username_already_exists,
}