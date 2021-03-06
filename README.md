# Обрезка ссылок с помощью Битли

Проект предназначен для генерации короткой ссылки для введеного web адреса используя интерфейс 
сервиса https://bitly.com.  
Если ввести полный web адрес, возвращается короткая ссылка формата https://bit.ly/..  
Если ввести полученную короткую ссылку, возвращается статистика посещений исходного web адреса 
по данной короткой ссылке.

### Как установить

Для использования программы необходимо зарегистрироваться и получить персональный ключ - "токен" Bitly.  
[Сервис Bitly](https://app.bitly.com/),  
[Документация Bitly](https://dev.bitly.com/)  
Ключ должен быть указан в файле .env, расположенном в папке проекта в формате  
`TOKEN_BITLY = {ваш токен}`

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`

### Примеры использования

```cmd
\Bitly>python main.py http://google.com
Битлинк: bit.ly/3JGkNT2
\Bitly>python main.py https://bit.ly/3JGkNT2
Счетчик: 6
```

### Цели проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
