# Gate.io_add_wl

Написал софт, который добавляет ваши адреса в белый список на Gate.io
софт на писан на запросах, но используется selenium, чтобы взять куки и отправлять запросы с куками

Функции бот:
- Посылает запросы на добавление ваших кошельков в вл🐬  + генерировать рандомные фразы для  "Описание адреса" (без этого нельзя)
- За один раз можно добавить 10 кошельков, не больше, но в address.txt можете записывать хоть сколько кошельков, бот автоматически добавит все, как только пройдёт пауза между первой/второй... десяткой кошельков

Как записывать в файл?
address.txt - кошельки в каждой новое строчке.

Чтобы установить все дополнительные библиотеки пропишите pip install -r requirements.txt в консоль

github - 
По вопросам - @Irorssss
Python 3.9 - 3.10 (мб, и другие версии подойдут)
