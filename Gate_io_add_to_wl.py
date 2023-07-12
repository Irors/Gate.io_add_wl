import time
from random import choice
from tqdm import tqdm
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import loguru


def note(lenn):
    Note_10 = []
    for i in range(lenn):
        alf = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
        Note_10.append("".join([choice(alf) for i in range(8)]))
    return Note_10

def generate(mass):
        s = ''
        count = 1
        for i in range(len(mass)):
            s = s + "".join(f"{mass[i]}@")
        s = s[:-1]

        for ind, sumb in enumerate(s):
            if sumb == "@":

                if count % 10 == 0:
                    s = s[:ind] + " " + s[ind + 1:]
                    count += 1
                else:
                    count += 1

        massive = s.split()

        return massive


def generate_chain_curr_type(chain, len_addr):

    chain_ = (chain+"@")*len_addr

    s = ''
    count = 1
    s = chain_[:-1]

    for ind, sumb in enumerate(s):
        if sumb == "@":

            if count % 10 == 0:
                s = s[:ind] + " " + s[ind + 1:]
                count += 1
            else:
                count += 1

    massive = s.split()

    return massive

def add_wl():

    options = Options()
    options.add_argument("start-maximized") # запуск браузера в полный экран
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    s = driver.get("https://www.gate.io/login") #Переходим на сайт и логинимся
    WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topUicon"]')))  # Ожидаем логин

    cookies = driver.get_cookies()
    driver.quit()

    return cookies


def sess(cookies, coun, notes, chains, curr_type, repeat):

    with requests.Session() as session:

        # // Добавляем все куки \\

        cookie = {}
        for i in cookies:
            cookie.update({f"{i['name']}": f"{i['value']}"})


        # // Создаём headers для запроса \\

        headers = {
            'authority': 'www.gate.io',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'csrftoken': f'{cookie.get("csrftoken")}',
            'origin': 'https://www.gate.io',
            'referer': 'https://www.gate.io/ru/myaccount/add_withdraw_address_list',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data_mail = {
            'type': 'EMAIL_WITHDRAW',
        }

        data_sms = {
            'type': 'security',
        }

        # // Отправляем код на mail \\
        mail_code = session.post("https://www.gate.io/email", cookies=cookie, data=data_mail, headers=headers)

        if mail_code.status_code == 200:
            loguru.logger.info(mail_code.json()['msg'])
        else:
            loguru.logger.error("Ошибка")



        # // Отправляем код на телефон \\
        response_code = session.post('https://www.gate.io/sms/3', cookies=cookie, headers=headers, data=data_sms)

        if response_code.status_code == 200:
            loguru.logger.info(response_code.json()['msg'])
        else:
            loguru.logger.error("Ошибка")

        return request_all(cookie, headers, coun, notes, chains, curr_type, repeat)


def request_all(cookie, headers, address, notes, chains, curr_type, repeat):

        time.sleep(3)

        sms_code = str(input("\nВведите код из смс : "))
        email_code = str(input("Введите код c почты : "))
        fundpass = str(input("Введите свой торговый пароль : "))
        guard = str(input("Введите guard code : "))

        data = {
            'curr_type': f'{curr_type[repeat]}',
            'chain': f'{chains[repeat]}',
            'addr': f'{address[repeat]}',
            'receiver_name': f'{notes[repeat]}',
            'address_tag': f'{"@"*(chains[repeat].count("@"))}',
            'batch_sub': '1',
            'type': 'set_withdraw_address',
            'totp': f'{guard}',
            'smscode': f'{sms_code}',
            'emailcode': f'{email_code}',
            'fundpass': f'{fundpass}',
            'verified': '1',
            'is_universal': '0',
        }


        response = requests.post('https://www.gate.io/json_svr/query', cookies=cookie, headers=headers, data=data)
        loguru.logger.info(response.json())

        # progress bar
        mylist = [int(i) for i in range(20)]

        for i in tqdm(mylist, colour="green"):
            time.sleep(1)


