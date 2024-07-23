import requests
from bs4 import BeautifulSoup
import json,time
pathlist = ['https://mp.weixin.qq.com/s/OU3ObJg4aea1yw6zWXq4KA',"https://mp.weixin.qq.com/s/-YDeI5dASfunjtv5bOLiLw",'https://mp.weixin.qq.com/s/poqwSVkmgl_WIBV5cVoM9A',
            "https://mp.weixin.qq.com/s/wMzsr9-FHSjY-4wJbbETiA",'https://mp.weixin.qq.com/s/yZxQLahnczG2z-cuplfy4w',"https://mp.weixin.qq.com/s/vsTQETpRAxKCHFjKtQLKFw",
            "https://mp.weixin.qq.com/s/DZZiYastA_D1u9z_d0Uu8A","https://mp.weixin.qq.com/s/WDpWnipoepw0_5BDKRnYAw","https://mp.weixin.qq.com/s/Q2zmwpVIJjm_0PoBhHUgxA",
            "https://mp.weixin.qq.com/s/rwa3DLJpie_hSQgeifKC0w","https://mp.weixin.qq.com/s/Ph2W2HHZXreTKJaKzwwPVQ","https://mp.weixin.qq.com/s/vWSATcrxEIXpgkzbAhs0uQ",
            "https://mp.weixin.qq.com/s/r5JrGVxe2yEjn5tAD5o12g","https://mp.weixin.qq.com/s/U-KPb-tWv5LuL4WUYtSLNw","https://mp.weixin.qq.com/s/8ubAxGyVUXSgkEepdQEueQ",
            "https://mp.weixin.qq.com/s/B7qdo4eN1Vzv2gwNJWWpGw","https://mp.weixin.qq.com/s/E9f0HCTjtuemxMXkOanowA","https://mp.weixin.qq.com/s/K2-lIhzIH22xF_NE12m01g"]

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
canel = pop()
for i,url in enumerate(pathlist[16:],start=16):
    # print(i)
    reports =[]
    time.sleep(1)
    infos = requests.get(url)
    # print(infos)
    soup = BeautifulSoup(infos.content, 'html.parser')
    spans = soup.find_all("span")
    # print(spans)
    ref = False
    sum_strip =0
    for span in spans:
        
        x = span.get_text(strip=True)
        # print(x,"\n",span)
        if (x == "" or x.strip() =="") and not ref:
            sum_strip +=1
            if canel.ma() <10 and sum_strip>1:
                canel.clear()
                
            # print(f'空内容，{x}')
        else:
            # print(x)
            if ref:
                targetdict['reference']=x
                ref=False
                reports.append(targetdict.copy())
                targetdict={}
                canel.clear()
                continue
            
            # print("参考链接" in x or "来源" in x)
            if "参考链接" in x or "来源" in x:
                # print(canel.x)
                do = -1
                liststr  =[]
                while True:
                    do +=1
                    if do ==0:
                        
                        title = canel.pop()
                        if title is None:
                            break
                        continue
                    
                    txt = canel.pop()
                    
                    if txt is None or "图" in txt and len(canel.x)==0:
                        break
                    
                    liststr.append(txt)
                    
                if title is not None:
                    # targetdict = {"title":title}
                    if len(liststr) ==0:
                        break
                    info = "\n".join(liststr)
                    targetdict = {"title":title,
                                "txt": info ,
                                "reference":""}
                    ref = True
                    continue
            else:
                canel.add(x)
        print(canel.x)
            
        

    if len(reports)<2:
        continue
    with open(f"D:\\workstation\\RE\\REModel\\reports\\{i}.json",'w',encoding="utf-8") as f:
        json.dump(reports, f, indent=2, ensure_ascii=False)
