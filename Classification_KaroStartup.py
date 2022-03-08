#!/usr/bin/env python
# coding: utf-8

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

data = pd.read_excel("skill_data.xlsx")

web_developer_skills = ['django','html','css','nodejs','reactjs','nodejs','flask','laravel']

machine_learning_skills = ['nosql','pandas','numpy','matpotlib','seabron','scipy']

data["Total Skills"]=np.nan
data["Designation"]=np.nan

data['Skills'] = [x.strip("[]").replace("'", "").strip().split(",") for x in data['Skills']]

for i in range(50):
    skill_list=[]
    wds=0
    mlskill=0
    total_skill=0
    [skill_list.append(x.replace("'", "").strip()) for x in data.loc[i,"Skills"] if x.replace("'", "").strip() not in skill_list]
    for j in skill_list:
        total_skill+=1
        if j in web_developer_skills:
            wds+=1
        elif j in machine_learning_skills:
            mlskill+=1
    
    data.loc[i,"Total Skills"]=total_skill
    if total_skill<3:
        data.loc[i,"Designation"]="Not Eligible"
    elif wds>=3:
        data.loc[i,"Designation"]="Web developer"
    elif mlskill>=3:
        data.loc[i,"Designation"]="ML Engineer"
    else:
        data.loc[i,"Designation"]="Not Eligible"

data.to_excel('Output.xlsx')