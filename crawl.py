import requests
from bs4 import BeautifulSoup
import json,time
from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED,FIRST_COMPLETED, as_completed
pool= ThreadPoolExecutor(max_workers=2)
pathlist = ['https://mp.weixin.qq.com/s/OU3ObJg4aea1yw6zWXq4KA',"https://mp.weixin.qq.com/s/-YDeI5dASfunjtv5bOLiLw",'https://mp.weixin.qq.com/s/poqwSVkmgl_WIBV5cVoM9A',
            "https://mp.weixin.qq.com/s/wMzsr9-FHSjY-4wJbbETiA",'https://mp.weixin.qq.com/s/yZxQLahnczG2z-cuplfy4w',"https://mp.weixin.qq.com/s/vsTQETpRAxKCHFjKtQLKFw",
            "https://mp.weixin.qq.com/s/DZZiYastA_D1u9z_d0Uu8A","https://mp.weixin.qq.com/s/WDpWnipoepw0_5BDKRnYAw","https://mp.weixin.qq.com/s/Q2zmwpVIJjm_0PoBhHUgxA",
            "https://mp.weixin.qq.com/s/rwa3DLJpie_hSQgeifKC0w","https://mp.weixin.qq.com/s/Ph2W2HHZXreTKJaKzwwPVQ","https://mp.weixin.qq.com/s/vWSATcrxEIXpgkzbAhs0uQ",
            "https://mp.weixin.qq.com/s/r5JrGVxe2yEjn5tAD5o12g","https://mp.weixin.qq.com/s/U-KPb-tWv5LuL4WUYtSLNw","https://mp.weixin.qq.com/s/8ubAxGyVUXSgkEepdQEueQ",
            "https://mp.weixin.qq.com/s/B7qdo4eN1Vzv2gwNJWWpGw","https://mp.weixin.qq.com/s/E9f0HCTjtuemxMXkOanowA","https://mp.weixin.qq.com/s/K2-lIhzIH22xF_NE12m01g",
"https://mp.weixin.qq.com/s/kJ9KAHF1bCy_z-XUz8jE1g",
"https://mp.weixin.qq.com/s/L0S5Gba9o-q0LiXQ_MBh_g",
"https://mp.weixin.qq.com/s/6mQDZz8msI-8FgwkvBBcXg",
"https://mp.weixin.qq.com/s/CcA5vL8GEOCV6xALmASvYA","https://mp.weixin.qq.com/s/6yPgSajVA7pRMYGzVMGGIA","https://mp.weixin.qq.com/s/4DcFiVaJ4GiWbSLS0jN43Q","https://mp.weixin.qq.com/s/T4DdVbp4FocGG2NC8JOSnw","https://mp.weixin.qq.com/s/6sXgw-grFWhCQpVeiaxr1g","https://mp.weixin.qq.com/s/xJM7gVwrKBOC9KqSAFMmWQ","https://mp.weixin.qq.com/s/U0xso5yTbAs7wUdpfvW32Q","https://mp.weixin.qq.com/s/pmqGd4IgQda0Ghnl_HQYBA","https://mp.weixin.qq.com/s/5XHEk18aTOIJxPp_8e27-w","https://mp.weixin.qq.com/s/wmcey1En7XyZbr1e1wNqsA","https://mp.weixin.qq.com/s/N6cgp-bjTfZ1D-sV8LW15Q","https://mp.weixin.qq.com/s/6DLBJAXEfkJJXhD1rpB0SQ","https://mp.weixin.qq.com/s/luJLyjIZ8-OI0A17DmqTTw","https://mp.weixin.qq.com/s/hvno-sUpcuFyhbuxJkJ7oA","https://mp.weixin.qq.com/s/22iwf7vhYcQPZa-WmlPuag","https://mp.weixin.qq.com/s/5ApKIw1ZdMK9t1WrhjgAsw","https://mp.weixin.qq.com/s/s2lkUjEil4pVCw0GUzDXDg","https://mp.weixin.qq.com/s/Y1FERHVAJBwpd4USMyEFRQ","https://mp.weixin.qq.com/s/_URUzQz3tXziu5mWA6BUYQ",
"https://mp.weixin.qq.com/s/UHRsH0YbjOAV_W5Sbgemmw","https://mp.weixin.qq.com/s/Xij--pK5JUrNFUFQVPzQVg",
"https://mp.weixin.qq.com/s/xfa3yx3frR-oL5zjzP4dTw","https://mp.weixin.qq.com/s/OjoWCBk58903keqVZ2Vkfg","https://mp.weixin.qq.com/s/Ih2UE0QXg6w1VAo5b2RHkQ","https://mp.weixin.qq.com/s/coP_QUvpOhTViLjlfhBKnQ","https://mp.weixin.qq.com/s/O-tJSlEOHlUHyR_P04cisw","https://mp.weixin.qq.com/s/ciE81Yx8ldcUcFqqo_-e0Q","https://mp.weixin.qq.com/s/Fw0XF_JwVNFvnSkBcgyuCQ","https://mp.weixin.qq.com/s/To7Nm3prnpWtThM8_khfvw","https://mp.weixin.qq.com/s/IwmT0M_KmXIVSWw68b6xDw","https://mp.weixin.qq.com/s/2o6cPzhN-v6dkVKcJhnn1Q","https://mp.weixin.qq.com/s/4Jl7m1B4_Rr62UNG-RLyvA","https://mp.weixin.qq.com/s/KyFo4csTr7TLf46caUSdQg","https://mp.weixin.qq.com/s/XudsEhjRGV3_UVfil36ZDQ","https://mp.weixin.qq.com/s/Ifk-kAEQ8HK1LifteTFe6w","https://mp.weixin.qq.com/s/84RFfekthxr6I-igHZBuwA","https://mp.weixin.qq.com/s/xr58wNmXejPUOiP0zre9TA","https://mp.weixin.qq.com/s/t5m8u6hWiRtR9H59YsAj8A","https://mp.weixin.qq.com/s/l8Ljl1x3nQhtQ1tYDr_5Ag","https://mp.weixin.qq.com/s/Ie1nqqIPXAfmpotctsWL-g","https://mp.weixin.qq.com/s/rz1qw44hgV5Tf1FbUZQSzA","https://mp.weixin.qq.com/s/mLUQ5A5WQvzIc8M8eCDzGQ","https://mp.weixin.qq.com/s/WoHAbP34IP0fFPCdlmKAsw","https://mp.weixin.qq.com/s/hD-LuhTRJYOqt05mWHbcFw",
"https://mp.weixin.qq.com/s/Ehbi_HcmWPBEjAEtuLeqCQ","https://mp.weixin.qq.com/s/TNZMNJVqsOyaEvA4dKLy5A","https://mp.weixin.qq.com/s/-k2BDT6zSeKwNf1niU5Whg","https://mp.weixin.qq.com/s/5DMScrIk-6PCWoa6bQd7yw",
"https://mp.weixin.qq.com/s/giD94RfRa2I3ZuUuBDjiDQ","https://mp.weixin.qq.com/s/aDG5OGHyr02xnd9HnONo4Q","https://mp.weixin.qq.com/s/8IU5rR7-f6C-0OIA6tzDfA","https://mp.weixin.qq.com/s/JpdWGpWM9i6ZsbB-SLG50w","https://mp.weixin.qq.com/s/lGSV5MDeJ6VAs1LimOhekg",
"https://mp.weixin.qq.com/s/fWQVjqDEydSjzbKkj8NGQw","https://mp.weixin.qq.com/s/RT1JAi-AJdO19CPlrf5NvA","https://mp.weixin.qq.com/s/QBIZHoWiI4Jjrh1o0FgExg","https://mp.weixin.qq.com/s/10fqSo5gCGocYPIq2yHHzw","https://mp.weixin.qq.com/s/4ggmWwRcsCGPWCwAWoWTqA",
"https://mp.weixin.qq.com/s/HQ8S7yPibfRc4nYqQzdSFw","https://mp.weixin.qq.com/s/pEHjitITmfOhd20I4smvTQ","https://mp.weixin.qq.com/s/6_tpFn5rR1KukdMG_G3IpA","https://mp.weixin.qq.com/s/Sb-zO4k-getOBVhf6roBXw",
"https://mp.weixin.qq.com/s/r2Fj9Le2dCwkJfxUznR8Jw","https://mp.weixin.qq.com/s/GPFLzhVZWOMUKYWYZQC4rA","https://mp.weixin.qq.com/s/aK0gxI3D_i43TFUUomjUaQ"
            ]

class pop:
    def __init__(self):
        self.x = []
        self.max_len = 0
    def add(self, txt):
        self.max_len = len(txt) if len(txt) > self.max_len else self.max_len
        self.x.append(txt)
    def pop(self):
        if len(self.x )==0:
            self.max_len = 0
            return None
        
        return self.x.pop(0)
    def clear(self):
        self.x = []
        print("clear")
    def ma(self):
        return self.max_len

def get(url,i):
    canel = pop()
    # for i,url in enumerate(pathlist[33:],start=34):
        # print(i)
    reports =[]
    # time.sleep(1)
    
    infos = requests.get(url)
    # print(infos)
    soup = BeautifulSoup(infos.content, 'html.parser')
    spans = soup.find_all("span")
    # print(spans)
    ref = False
    sum_strip =0
    for span in spans:
        
        x = span.get_text(strip=True)
        if x.strip() =="" or x =="":
            if ref:
                canel.clear()
            else:
                try:
                    space = canel.x[-1]
                    if space.strip() =="":
                        canel.clear()
                    else:
                        canel.add(x)
                except:
                    canel.add(x)
                
                
            
    
        else:
            # print(x)
            if ref:
                targetdict['reference']=x
                ref=False
                reports.append(targetdict.copy())
                targetdict={}
                canel.clear()
                continue
            
            # print("参考链接" in x or "来源" in x or "https://" in x)
            if "参考链接" in x or "来源" in x or "https://" in x:
                # print(canel.x)
                do = -1
                liststr  =[]
                while True:
                    do +=1
                    if do ==0:
                        
                        title = canel.pop()
                        if title is None:
                            break
                        while title.strip() =="":
                        
                            title = canel.pop()
                            if title is None:
                                break
                    if title is None:
                        break
                    
                    txt = canel.pop()
                    
                    if txt is None or "图" in txt and len(canel.x)==0:
                        break
                    
                    liststr.append(txt)
                    
                if title is not None:
                    # targetdict = {"title":title}
                    if len(liststr) ==0:
                        break
                    
                    info = "\n".join(liststr)
                    if info.strip() =="":
                        break
                    targetdict = {"title":title,
                                "txt": info ,
                                "reference":""}
                    ref = True
                    continue
            else:
                canel.add(x)
        print(canel.x)
            
        


    with open(f"reports/{i}.json",'w',encoding="utf-8") as f:
        json.dump(reports, f, indent=2, ensure_ascii=False)
if __name__ =="__main__":
    print(len(pathlist))
    all_task = []
    t=time.time()
    with ThreadPoolExecutor(max_workers=4) as pool:
        for i,url in enumerate(pathlist[33:],start=33):
            all_task.append(pool.submit(get, url,i))

        # 主线程等待所有子线程完成
        wait(all_task, return_when=ALL_COMPLETED)
        print("----complete-----",f"{time.time()-t}")