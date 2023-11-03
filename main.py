# 2018 code i used before tiktok got strong!!
# Patched will not work but gives you a basic understanding how easy it is
# 2024 version is based on 10 more method put together
# You will not find a woring one on gihub or another place as Developers keep it private

import os, threading, random, time, requests

class Sharebot():
    def __init__(self, video_id, threads, mode):
        self.video_id = video_id
        self.threads  = threads
        self.start    = time.time()
        self.mode     = mode
        
        self.sess     = requests.Session()
        self.shares   = 0
        
    def starter(self):
        while True:
            if threading.active_count() < self.threads:
                threading.Thread(target=self.send_request).start()
    # credts @ultve
    def send_request(self):
        try:
            req = self.sess.post(
                    url     = "https://api19-core-useast5.us.tiktokv.com/aweme/v1/aweme/stats/?", # url backend
                    headers = {
                        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "user-agent": "com.zhiliaoapp.musically/2022501030 (Linux; U; Android 7.1.2; fr; SM-N976N; Build/QP1A.190711.020;tt-ok/3.12.13.1)"
                    }, 
                    params = { # Fake Gen to confuse the server
                        "aid": 1988,
                        "channel": "googleplay",
                        "device_type": "SM-N976N",
                        "device_id": random.randint(1000000000000000000, 9999999999999999999),
                        "os_version": "7.1.2",
                        "version_code": 250103,
                        "app_name": "musical_ly",
                        "device_platform": "android",
                        "item_id": self.video_id,
                        self.mode: 1
                    },
                    stream = True
            )
            
            if req.json()["status_code"] == 0:
                self.shares += 1
                os.system(f"title Sent :{self.shares} ^| Speed :{round((int(self.shares) / (time.time() - self.start)), 2)}/s ^| Credits: @ultve") # output
                pass
        except:
            pass

if __name__ == "__main__":

    bot = Sharebot(
        video_id = input("[?] id > "), # look for tiktok web its a long number like 792837252425273
        threads = 50,
        mode = "share_delta" #play_delta
    )
    
    bot.starter()
