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
        
        
import json
from collections import Counter

with open("./test.json") as file:
    regions = json.load(file)

for item in regions.items():
    region_name = item[0]
    street_weights = item[1]
    sample_list = []
    for it in street_weights.items():
        sample_list.extend([it[0] for _ in range(int(it[1]/1000))])
    sample = random.sample(sample_list, 100)
    counter = Counter(sample)
    most5 = counter.most_common(5)
    choice = random.choice(most5)[0]
    print(choice)
