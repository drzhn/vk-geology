vk-geology

требуется взять токен для работы с разделами "друзья", "стена" и "группы", его можно получить на странице
https://oauth.vk.com/authorize?client_id=6271151&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=270338&response_type=token&v=5.69

после подтверждения, токен окажется в строке браузера, его нужно вставить в файл settings, там же лежит и id пользователя
и id искомого поста, вставить нужные значения

затем запустить файл GetUserInfo.py. Он запишет в файл data.txt список всех друзей и групп пользователя и текст поста
потом файл Geology.py, он произведет поиск