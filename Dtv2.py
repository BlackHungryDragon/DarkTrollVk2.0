import time,colorama
import vk_api,random
from colorama import Fore
from colorama import init

white='\033[37m'
yellow = '\033[33m'
banner="""
%s
          D D n    T T T T    V        V
           D  D      T        V      V 
           D  D       T        V    V    
           D D       T            V    

     DarkTrollVk 2.0
     proger:  Naruto Uzumaki

""" % yellow



user=random.randint(1, 2147483647)
print(banner)
token = str (input(' Токен :'))
print("\n   Меню опцией : \n  \033[37m[\033[33m1\033[37m]  - Массовое смс. \n  \033[37m[\033[33m2\033[37m] - Вступить в группы тематики 'Лгбт' . \n  [\033[33m3\033[37m] -  Поставить статус( Который  вы сами хотите).\n   \033[37m[\033[33m4\033[37m] - Создать 5 бесед . \n   \033[37m[\033[33m5\033[37m] - Спам постами.\n   \033[37m[\033[33m6\033[37m]- Спам создаваеными группами . \n   \033[37m[\033[33m7\033[37m] - Редактирование имени ")           
print("   \033[37m[\033[33m8\033[37m] - Добавить в чс всех ,кто в онлайне .\n   \033[37m[\033[33m9\033[37m] - Убрать из друзей тех,кто сейчас  онлайн ")
doings=int(input(Fore.YELLOW+' Номер опции :' ))
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

if doings==1:
    print(Fore.WHITE+'\n   Выберите походящий пункт . \n   \033[37m[\033[33m1\033[37m]  - Отправить сразу всем смс . \n  \033[37m[\033[33m2\033[37m] - Разослать тем,кто в сети .')
    xdoing=int(input(' Номер пункта:'))
    if xdoing == 1:
     
       n=1
       i=3
       message=str(input(' Введите сообщение :'))
       if message=="":
          message="Я гей"
       friends= vk.friends.getAppUsers()
       for friend in friends:
          n += 1
          vk.messages.send(user_ids =friend ,message=message,random_id=user)
          time.sleep(i)
          print(f' {n}. Сообщение  отправилось')
          if n == 5 :
             print(" Привет от капчи .Ждем 10 сеk и на второй круг ")
             time.sleep(10)
    elif xdoing==2:
       stop=3
       stop_kapcha=10
       print(" \n   Напишите сообщение ,которое должно отправиться \n   Если оставите поле пустым ,то тогда смс будет 'я гей' ")
       message=str(input('\n  Сообщение :'))
       if message =="":
          message="Я гей"
       def sendmas():
          i=0
          online=vk.friends.getOnline()
          for onl in online   :
             i +=1
             vk.messages.send(user_ids =onl ,message=message,random_id=user)
             print(f"{i}. Сообщение отправленно ")
             time.sleep(stop)
             if i ==5:
                print(" Тебе от капчи привет !) Ждем 10 сек и на второй круг .")
                time.sleep(stop_kapcha)
       sendmas()
elif doings ==3:
   print('   Введите сообщение для статуса \n   По умолчанию смс - "Я гей" ')
   status=str(input(' Статус :'))
   if status == '':
      status='Я гей'
   stat= vk.status.set(text=status)
   print(' Статус успешно установлен')
elif doings ==4:
   print(" [1] - Все ,кто в онлайне. [2] - Определенных людей.")
   doings = int(input(" Номер :"))
   if doings ==1:
      print("\n   Введите название беседы \n   По умолчанию смс - 'Я гей'" )
      name =str(input(" Название :"))
      online=vk.friends.getOnline()
      ids =[]
      ids.append(online)
      if name == "":
         name= "я гей"
      i=0
      n=5
      stop =3
      stop_kapcha= 10
      for i in  range (n):
         time.sleep(stop)
         proverka =vk.messages.createChat(user_ids =ids,title= name)
         i+=1
         print('%s. Беседа создана' % i)
         if i == 5:
            print(' Успешно создано 5 бесед . ')
   elif doings ==2:
      print("\n   Введите название беседы \n   По умолчанию смс - 'Я гей'" )
      name =str(input(" Название :"))
      number_people= int(input(' Число пользователей :'))
      n = 0
      ids =[]
      for number_people in range(number_people):
         id = int(input(' id:'))
         ids.append(id)
      if name == "":
         name= "я гей"
      i=0
      n=5
      stop =3
      stop_kapcha= 10
      for i in  range (n):
         time.sleep(stop)
         proverka =vk.messages.createChat(user_ids =ids,title= name)
         i+=1
         print('%s. Беседа создана' % i)
         if i == 5:
            print(' Успешно создано 5 бесед . ')
      


elif doings ==2:
   def joingroups():
      n=1
      group= [ 65797052,151233321,128556106,97340700,79970646,60683281,170925341,111584466,89037408,67844312]
      for groups in group:
         vk.groups.join(group_id=groups)
         print(" Успешно вступил во все Лгбт группы")
   joingroups()
elif doings ==5:
   print( "\n   Введите числовой айди пользователя/сообщемтва")
   id=int(input('   айди :'))
   print(' Теперь введите текст будущих постов. По умолчанию будет "Я гей" ')
   messange=str(input('   text:'))
   if messange =="":
      messange= "Я гей"
   number_posts=int(input("  Число постов (от 1 до 500):"))
   stop= 3
   i=1
   stop_kapcha= 10
   kapcha= ' Капча долбанная . Ждем 10 секунд и на второй круг !'
   def spam():
      for i in range(number_posts):
         time.sleep(stop)
         vk.wall.post(owner_id=id,from_group=0,message=messange)
         i += 1
         print('%s пост отправлен' % i)
         if i == 10:
            print(kaptcha)
            i = 1
            time.sleep(stop_kapcha)
   spam()
elif doings ==6:
    name= str(input(' Введите название группы:'))
    number=int(input(' Введите число создаваемых групп'))
    stop =3
    stop_kapcha=10
    def creategroup():
        x =0
        for  i in range(number):
           x +=1
           vk.groups.create(title=name,description=' Я за лгбт!')
           time.sleep(stop)
           print(f' {x}. Группа создана')
           if x ==10:
              print(' Привет от капчи.Ждем 10 сек и на второй круг.')
              time.sleep(stop_kapcha)
    creategroup()
elif doings ==7:
   banner="""

    Важная информация !!!Редактировать имя и фамилию токо с помощью русских букв  и с загловной буквы .
    Иначе все запросы будут отклонятся Администрацией "Вконтакте"

   """
   print(banner)
   first_name=input(" Имя :")
   last_name=input(" Фамилия :")
   vk.account.saveProfileInfo(first_name=first_name,last_name=last_name)
   print(" Успешно изменена информация !")

elif doings == 8:
   n =0
   online = vk.friends.getOnline()
   for id in online:
      n +=1
      vk.friends.delete(user_id=id)                                 
      vk.account.ban(owner_id= id)
      print(f" {n}. добавлен в черный список.")
   print("\n   [ Успешно весь онлайн добавлен в чс :) ]")

elif doings == 9:
   n =0
   online = vk.friends.getOnline()
   for id in online:
      n +=1
      vk.friends.delete(user_id=id)
      print(f" {n}. убран из друзей.")
   print("\n   [ Успешно весь онлайн ушел из друзей :) ] ")
