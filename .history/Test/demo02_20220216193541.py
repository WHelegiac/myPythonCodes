'''
Author: WanHao
Date: 2022-02-16 19:35:20
LastEditors: Do not edit
LastEditTime: 2022-02-15 19:35:21
FilePath: \my_python_codes\Test\demo02.py
FileDescription: Lazy~~~
'''

import json
with open("./test.txt") as file:
    lines = file.readlines()
    regions = {}
    
    region = lines[0].split('\t')[0]
    for line in lines:
        name = line.split('\t')[0]
        population = int(line.split('\t')[1])
        if name.endswith('区'):
            region = name
            regions[region] = {}
        else:
            regions[region][name] = population

    with open("./test.json",'w') as newFile:
        json.dump(regions,newFile,ensure_ascii=False)