#-*-coding:UTF_8-*-
import re
import json

sf= input('')
sf=sf[:-1]#删去末尾的'.'
pf={
    '姓名':'',
    '手机':'',
    '地址':[],
    }

#提取难度级别并删去
level=sf[0]
sf=sf.split(r'!')
sf=sf[1]

#提取号码并删去
telnum=re.findall("\d{11}",sf)
telnum=telnum[0]
sf=re.sub(r'\d{11}','',sf)

#提取人名并删去
name=re.sub(r',.*$',"",sf)
sf=re.sub(name,'',sf)
sf=re.sub(r',','',sf)#删去逗号

pf['姓名']=name
pf['手机']=telnum

#第一级地址
direct_cities=['北京','上海','重庆','天津']
if '省' in sf:
    first=re.sub(r'省.*$',"",sf)
    first+='省'
    sf=sf.replace(first,'',1)#删去第一级地址
elif '自治区' in sf:
    first = re.sub(r'自治区.*$',"",sf)
    first+='自治区'
    sf=sf.replace(first,'',1)
elif '北京市' in sf:
        first='北京市'
        sf=sf.replace(first,'',1)
        first='北京'
elif '上海市' in sf:
        first='上海市'
        sf=sf.replace(first,'',1)
        first='上海'
elif '重庆市' in sf:
        first='重庆市'
        sf=sf.replace(first,'',1)
        first='重庆'
elif '天津' in sf:
        first='天津市'
        sf=sf.replace(first,'',1)
        first='天津'
elif '北京' in sf:
        first='北京'
        sf=sf.replace(first,'',1)
elif '上海' in sf:
        first='上海'
        sf=sf.replace(first,'',1)
elif '重庆' in sf:
        first='重庆'
        sf=sf.replace(first,'',1)
elif '天津' in sf:
        first='天津'
        sf=sf.replace(first,'',1) 
elif '内蒙古' in sf:
        first='内蒙古自治区'
        one='内蒙古'
        sf=sf.replace(one,'',1)
elif '宁夏' in sf:
        first='宁夏回族自治区'
        one='宁夏'
        sf=sf.replace(one,'',1)
elif '广西' in sf:
        first='广西壮族自治区'
        one='广西'
        sf=sf.replace(one,'',1)
elif '新疆' in sf:
        first='新疆维吾尔族自治区'
        one='新疆'
        sf=sf.replace(one,'',1)
elif '西藏' in sf:
        first='西藏自治区'
        one='西藏'
        sf=sf.replace(one,'',1)
elif '黑龙江' in sf:
        first='黑龙江省'
        one='黑龙江'
        sf=sf.replace(one,'',1)
else:
    first=sf[:2]
    sf=sf.replace(first,'',1)
    first+='省'
pf['地址'].append(first)

#第二级地址
city={'市','地区','盟','自治州'}
for b in first:
    if b in direct_cities:
            second=b
            second+='市'
            break
for c in city:
    if c in sf:
            second=re.sub(c+'.*$',"",sf)
            second+=c
            sf=sf.replace(second,'',1)#删去第二级地址
            break
    else:
            second=''
pf['地址'].append(second)

#第三级地址
county=['区','市','县','旗','自治县','自治旗','林区','特区']
for d in county:
    if d in sf:
        third=re.sub(d+'.*$',"",sf)
        third+=d
        sf=sf.replace(third,'',1)
        break
    else:
        third=""
pf['地址'].append(third)

#第四级地址
town=['镇','乡','街道','民族乡','苏木','民族苏木']
for e in town:
    if e in sf:
        forth=re.sub(e+'.*$',"",sf)
        forth+=e
        sf=sf.replace(forth,'',1)
        break
    else:
        forth=""
pf['地址'].append(forth)

#第五级地址
street=['街','村','路']
if level=='1':
    fifth=sf
    pf['地址'].append(fifth)
elif level=='2' or '3': 
    for f in street:
        if f in sf:
            fifth=re.sub(f+'.*$',"",sf)
            fifth+=f
            pf['地址'].append(fifth)
            sf=sf.replace(fifth,'',1)
            break
        else:
            fifth=""

    #第六级地址
    if '号' not in sf :
        sixth=""
    else:
        sixth=re.sub(r'号.*$',"",sf)
        sixth+='号'
        sf=sf.replace(sixth,'',1)
    pf['地址'].append(sixth)

    #第七级地址
    seventh=sf
    pf['地址'].append(seventh)

json_str=json.dumps(pf,ensure_ascii=False)
print(json_str)
