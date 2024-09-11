import json
def pand(itm):
    if itm['title'].startswith('APT攻击') or itm['title'].startswith('恶意软件') or itm['title'].startswith('勒索软件') or itm['title'].startswith('数据泄露'):
        return False
    else:
        return True
links = []

# for i in range(0,87):
#     try:
#         with open(f"../reports/{i}.json",'r',encoding="utf-8") as f:
#             reports = json.load(f)
#     except:
#         reports = []
#     finally:
        
#         links.extend(filter(pand,reports))
with open(f'reports.json','r',encoding='utf-8')as f:
    reports=json.load(f)
answer=[]
for i in reports:
    if pand(i):
        
        answer.append(i)
with open(f'reports_.json','w',encoding='utf-8')as f:
    json.dump(answer,f,indent=2,ensure_ascii=False)
print(len(answer))