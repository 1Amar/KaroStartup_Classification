# KaroStartup_Classification
Classification of applicants into Web Developer and ML engineer

Library used:

1. pandas 
2. To read excel file additional openpyexcel library is required. This can be installed using "!pip install openpyxl"

The additional column "Total Skills" added.

When machine learning skills are more than 3 or web development skills are more than 3 it is classified into ML engineer and
web developer respectively.
When total skills are not more than 3 or when the relevant skills are not more than 3 the applicant is classified as "Not 
eligible"

The output file is "Output.xlsx"
