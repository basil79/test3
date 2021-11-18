import time

login = input("Введите логин:")  # НЕДО ТАЙМЕР
password = input("Введите пароль:")

if login == "bot":
    if password == "bulka228":
        print("Вы авторизованны")

        hours = int(input("введите часы"))
        seconds = int(input("введите секунды"))
        minutes = int(input("введите минуты"))
        day = int(input("введите дни"))

        while 1:
            seconds = seconds + 1
            if seconds == 60:
                minutes = minutes + 1
                seconds = 0

            if minutes == 60:
                hours = hours + 1
                minutes = 0

            if hours == 24:
                day = day + 1
                hours = 0

            print(day, ":", hours, ":", minutes, ":", seconds)
            time.sleep(1)

    else:
        print("логин или пароль не правильный")
else:
    print("логин или пароль не правильный")



