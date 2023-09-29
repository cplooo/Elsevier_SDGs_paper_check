# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 09:07:52 2023

@author: user
"""

import re
import streamlit as st


# def search_strings(article, exact_strings, substring_prefixes):
#    found_exact_strings = []
#    found_substring_prefixes = []
#     # Search for exact strings
#    for string in exact_strings:
#        matches = re.findall(r"\b" + re.escape(string) + r"\b", article, flags=re.IGNORECASE)
#        found_exact_strings.extend(matches)
#     # Search for strings starting with specific substrings
#    for prefix in substring_prefixes:
#        matches = re.findall(r"\b" + re.escape(prefix) + r"\w*", article, flags=re.IGNORECASE)
#        found_substring_prefixes.extend(matches)
#    return found_exact_strings, found_substring_prefixes
#
# ## Test the code
# article = "This is a sample article used for testing the search functionality. This article contains some specific strings, such as Python, search, and substring."
# exact_strings_to_search = ["search", "substring","used f", "article u"]
# substring_prefixes_to_search = ["Python", "s", "th","used f", "article u"]
# found_exact_strings, found_substring_prefixes = search_strings(article, exact_strings_to_search, substring_prefixes_to_search)
# print("Exact strings found in the article:")
# for string in found_exact_strings:
#     print(string)

# print("\n")

# print("Strings starting with specific substrings found in the article:")
# for word in found_substring_prefixes:
#     print(word)
 

def find_quoted_content(string):
   pattern = r'"([^"]*)"'
   matches = re.findall(pattern, string)
   return matches

# # Test the code
# string = 'This is a "sample" string with "quoted" substrings.'
# quoted_substrings = find_quoted_content(string)
# print(quoted_substrings)

# ## "" 後面添加 'in found_substring_prefixes':
# def add_suffix(string):
#     pattern = r'"([^"]*)"'
#     result = re.sub(pattern, r'"\1" in found_substring_prefixes', string)
#     return result

## for 引號 "" 中的內容沒有或只有一個 星號 *
def check_strings(article, substring):
   #for substring in substrings:
   pattern = r'\b' + re.escape(substring) + r'\w*'
   matches = re.findall(pattern, article, flags=re.IGNORECASE)
   #if matches:
       #print(f"The substring '{substring}' starting in '{matches[0]}' is present in the article.")
   #else:
       #print(f"The substring '{substring}' is not found in the article.")
   return matches

## for 引號 "" 中的內容有兩個 星號 *
def check_continuous_words(article, substrings):
   pattern = r'\b' + substrings[0] + r'\w*\b\s+' + substrings[1] + r'\w*\b'
   matches = re.search(pattern, article, flags=re.IGNORECASE)
   #if match:
       #print(f"The two continuous words '{match.group(0)}' are present in the article.")
   #else:
       #print("The two continuous words are not found in the article.")
   return matches
# # 測試程式碼
# article = "This is a sample article to check if it contains two continuous words starting with 'promoting regimeddd."
# substrings_to_check = ["promot", "regime"]
# check_continuous_words(article, substrings_to_check)





# def replace_quoted_content(string):
#     pattern = r'"([^"]*)"'
#     result = re.sub(pattern, r'check_strings(article, "\1")', string)
#     return result


# def replace_quoted_content(string):
#    quoted_content = find_quoted_content(string)
#    for content in quoted_content:
#        if "*" not in content:
#            replacement = f'check_strings(article, "{content}")'
#        elif content.count("*") == 1:
#            content_without_asterisk = content.replace("*", "")
#            replacement = f'check_strings(article, "{content_without_asterisk}")'
#        else:
#            substrings = [substring.replace("*", "") for substring in content.split() if "*" in substring]
#            replacement = f'check_continuous_words(article, {substrings})'
#        string = string.replace(f'"{content}"', replacement)
#    return string
# # # Test the code
# # string = '這是一個包含"tax transition", "tax transition*", "tax* transition*"的字串'
# # result = replace_quoted_content(string)
# # print(result)


def replace_quoted_content(string):
   quoted_content = find_quoted_content(string)
   for content in quoted_content:
       if "*" not in content:
           replacement = f'check_strings(article, "{content}")'
       elif content.count("*") == 1:
           content_without_asterisk = content.replace("*", "")
           replacement = f'check_strings(article, "{content_without_asterisk}")'
       else:
           substrings = [substring.replace("*", "") for substring in content.split() if "*" in substring]
           replacement = f'check_continuous_words(article, ["{substrings[0]}", "{substrings[1]}"])'
       string = string.replace(f'"{content}"', replacement)
   return string
# # 測試程式碼
# string = '這是一個包含"tax transition", "tax transition*", "tax* transition*"的字串'
# result = replace_quoted_content(string)
# print(result)





# SDGs_choice = input('輸入您要查詢的 SDGS 項目編號(整數): ')
# title       = input('輸入您的論文 title: ')
# abstract    = input('輸入您的論文 abstract: ')
# keywords    = input('輸入您的論文 keywords: ')

SDGs_choice = st.text_input('輸入您要查詢的 SDGS 項目編號(整數)', '17')
title       = st.text_input('輸入您的論文 title')
abstract    = st.text_input('輸入您的論文 abstract')
keywords    = st.text_input('輸入您的論文 keywords')
  
# title = "SDGs"
# abstract = "sustainable energy"
# keywords = "tax transition"
article = title+" "+abstract+" "+keywords
#article = "This is a sample article used for testing the search functionality. This article contains some specific strings, such as Python, search, and substring."
#article = 'a business taxations c'

if SDGs_choice == '17':
    
    ### 條件 1   
    cond1='''\
    (
    
    TITLE-ABS-KEY ( "tax transition" OR "tax system" )
    OR
    
    TITLE-ABS-KEY ( "tax policy" OR "tax policies" )
    OR
    
    TITLE-ABS-KEY ( "excise duty" OR "excise duties" OR "excise tax" OR "excise taxes" )
    OR
    TITLE-ABS-KEY
    (
    "revenue collection*"
    )
    OR
    TITLE-ABS-KEY
    (
    "cycle of money"
    )
    OR
    TITLE-ABS-KEY
    (
    "Slippery Slope Framework"
    )
    OR
    TITLE-ABS-KEY
    (
    "tax morale"
    )
    OR
    TITLE-ABS-KEY
    (
    "tax administration"
    )
    OR
    TITLE-ABS-KEY
    (
    "tax avoidance"
    )
    OR
    
    TITLE-ABS-KEY ( "business taxation*" OR "business tax*" OR "corporate taxation*" OR "corporate tax*" )
    OR
    
    TITLE-ABS-KEY ( "inheritance tax*" OR "international tax*" )
    OR
    TITLE-ABS-KEY
    (
    "shadow econom*"
    )
    OR
    
    TITLE-ABS-KEY ( "tax behaviour*" OR "tax behavior*" )
    OR
    TITLE-ABS-KEY
    (
    "tax law*"
    )
    OR
    TITLE-ABS-KEY
    (
    "tax efficiency*"
    )
    OR
    
    TITLE-ABS-KEY ( "value added tax*" OR "value-added tax*" )
    OR
    
    TITLE-ABS-KEY ( "fiscal polic*" OR "monetary polic*" )
    OR
    
    TITLE-ABS-KEY ( "informal economy*" OR "informal sector*" )
    OR
    TITLE-ABS-KEY
    (
    "envelope wage*"
    )
    OR
    
    TITLE-ABS-KEY ( "underground econom*" OR "underground sector*" )
    OR
    TITLE-ABS-KEY
    (
    "informal employment*"
    )
    OR
    
    TITLE-ABS-KEY ( "under declared employ*" OR "underdeclared employ*" OR "undeclared work*" OR "informal job*" )
    OR
    
    TITLE-ABS-KEY ( "hidden econom*" OR "black economy" OR "money laundering" OR "tax evasion*" OR "undeclared work*" )
    OR
    
    TITLE-ABS-KEY ( "VAT gap" OR "VAT fraud" )
    OR
    TITLE-ABS-KEY
    (
    "currency demand approach*"
    )
    OR
    TITLE-ABS-KEY
    (
    "Base Erosion And Profit Shifting"
    )
    OR
    
    ( TITLE-ABS-KEY ( {BEPS} ) AND ( TITLE-ABS-KEY ( "Tax*" ) OR TITLE-ABS-KEY ( "financ*" ) ) )
    OR
    TITLE-ABS-KEY
    (
    "transfer pricing"
    )
    OR
    
    TITLE-ABS-KEY ( "tax treaty" OR "tax treaties" )
    OR
    TITLE-ABS-KEY
    (
    "taxation of capital"
    )
    OR
    
    ( TITLE-ABS-KEY ( "endogenous growth" ) AND TITLE-ABS-KEY ( "public capital" ) )
    ) \
    '''  
    key_terms = []
    key_terms = key_terms+find_quoted_content(cond1)
    #len(key_terms)  ## 56
    #print(key_terms)
    
    cond1_1 = cond1.replace('TITLE-ABS-KEY', "")
    #print(cond1_1)
    # cond1_2 = cond1_1.replace('*"', '"')
    # print(cond1_2)
    #pattern = r'\*'
    #cond1_2 = re.sub(pattern, '', cond1_1)
    #print(cond1_2)
    
    cond1_2 = cond1_1.lower()
    #print(cond1_2)
    
    
    ## {}改成""
    pattern = r'[{}]'
    cond1_3 = re.sub(pattern, '"', cond1_2)
    #print(cond1_3)
    
    cond1_4 = replace_quoted_content(cond1_3)
    #print(cond1_4)
    cond1_final = eval(cond1_4)
    
    
    # ### 詢找條件中的terms:
    # substring_prefixes_to_search = []
    # exact_strings_to_search = []
    # substring_prefixes_to_search = find_quoted_content(cond1_3)
    # #print(substring_prefixes_to_search)
    
    # found_exact_strings, found_substring_prefixes = search_strings(article, exact_strings_to_search, substring_prefixes_to_search)
    # # for string in found_exact_strings:
    # #     print(string)
    # # print("\n")
    # #print("Strings starting with specific substrings found in the article:")
    # #for word in found_substring_prefixes:
    #     #print(word)
    
    # ## "" 後面添加 in found_substring_prefixes:
    # #cond1_5 = add_suffix(cond1_4)
    # #print(cond1_5)
    # #type(cond1_5)  ## str
    # #cond1_final = bool(cond1_5)
    # #cond1_final = eval(cond1_5)
    # #print(cond1_final)  ## True
    # #type(cond1_final)  ## bool
    

    ### 條件 2   
    cond2='''\
    (
    TITLE-ABS-KEY
    (
    "official development assistance*"
    )
    OR
    
    (
    TITLE-ABS-KEY
    (
    {ODA}
    )
    AND
    TITLE-ABS-KEY
    (
    "development assist*"
    )
    )
    OR
    TITLE-ABS-KEY
    (
    "foreign aid"
    )
    OR
    TITLE-ABS-KEY
    (
    "development aid"
    )
    OR
    TITLE-ABS-KEY
    (
    "developmental aid"
    )
    OR
    TITLE-ABS-KEY
    (
    "development assistance"
    )
    OR
    TITLE-ABS-KEY
    (
    "development cooperation"
    )
    OR
    TITLE-ABS-KEY
    (
    "international development cooperation"
    )
    OR
    TITLE-ABS-KEY
    (
    "global civil society"
    )
    OR
    TITLE-ABS-KEY
    (
    "international cooperation"
    )
    OR
    TITLE-ABS-KEY
    (
    "international public finance*"
    )
    OR
    TITLE-ABS-KEY
    (
    "shared prosperity*"
    )
    OR
    TITLE-ABS-KEY
    (
    "bilateral aid"
    )
    OR
    
    (
    
    (
    TITLE-ABS-KEY
    (
    "foreign direct investment*"
    )
    OR
    TITLE-ABS-KEY
    (
    "foreign investment*"
    )
    )
    AND
    TITLE-ABS-KEY
    (
    "developing*"
    )
    )
    OR
    TITLE-ABS-KEY
    (
    "belt and road initiative"
    )
    OR
    TITLE-ABS-KEY
    (
    "international development"
    )
    OR
    TITLE-ABS-KEY
    (
    "cross border cooperation*"
    )
    OR
    TITLE-ABS-KEY
    (
    "cross border collaboration*"
    )
    OR
    TITLE-ABS-KEY
    (
    "non government development organi*"
    )
    OR
    TITLE-ABS-KEY
    (
    {NGDO}
    )
    OR
    TITLE-ABS-KEY
    (
    "b&r initiative"
    )
    OR
    TITLE-ABS-KEY
    (
    "north-south cooperation"
    )
    OR
    TITLE-ABS-KEY
    (
    "north-south partnerships"
    )
    OR
    TITLE-ABS-KEY
    (
    "north-south collaboration"
    )
    OR
    TITLE-ABS-KEY
    (
    "north-south research partnerships"
    )
    )\
    '''  
    
    key_terms = key_terms+find_quoted_content(cond2)
    #len(key_terms)  # 82
    #print(key_terms)
    
    cond2_1 = cond2.replace('TITLE-ABS-KEY', "")
    #print(cond1_1)
    # cond1_2 = cond1_1.replace('*"', '"')
    # print(cond1_2)
    #pattern = r'\*'
    #cond2_2 = re.sub(pattern, '', cond2_1)
    #print(cond1_2)
    
    cond2_2 = cond2_1.lower()
    #print(cond1_3)
    
    
    ## {}改成""
    pattern = r'[{}]'
    cond2_3 = re.sub(pattern, '"', cond2_2)
    #print(cond1_4)
    
    cond2_4 = replace_quoted_content(cond2_3)
    #print(cond2_5)
    cond2_final = eval(cond2_4)
    
    
    # ### 詢找條件中的terms:
    # substring_prefixes_to_search = []
    # exact_strings_to_search = []
    # substring_prefixes_to_search = find_quoted_content(cond2_3)
    # #print(substring_prefixes_to_search)
    
    # found_exact_strings, found_substring_prefixes = search_strings(article, exact_strings_to_search, substring_prefixes_to_search)
    # # for string in found_exact_strings:
    # #     print(string)
    # # print("\n")
    # #print("Strings starting with specific substrings found in the article:")
    # #for word in found_substring_prefixes:
    #     #print(word)
    
    # ## "" 後面添加 in found_substring_prefixes:
    # #cond1_5 = add_suffix(cond1_4)
    # #print(cond1_5)
    # #type(cond1_5)  ## str
    # #cond1_final = bool(cond1_5)
    # #cond1_final = eval(cond1_5)
    # #print(cond1_final)  ## True
    # #type(cond1_final)  ## bool


    ### 條件 3   
    cond3='''\
    (
    
    (
    
    (
    
    TITLE-ABS-KEY
    (
    "developing countr*" OR
    "poor countr*" OR
    "poor countr*" OR
    "emerging countr*" OR
    "developing world*" OR
    "developing nation" OR
    "developing nations" OR
    "developing state" OR
    "developing states" OR
    "low income countr*" OR
    "middle income countr*" OR
    "low income nation*" OR
    "middle income nation*" OR
    "low income state*" OR
    "middle income state*" OR
    "least developed countr*" OR
    "least developed nation*" OR
    "least developed state*" OR
    "Afghanistan" OR
    "Albania" OR
    "Algeria" OR
    "American Samoa" OR
    "Angola" OR
    "Antigua and Barbuda" OR
    "Argentina" OR
    "Armenia" OR
    "Azerbaijan" OR
    "Bangladesh" OR
    "Belarus" OR
    "Belize" OR
    "Benin" OR
    "Bhutan" OR
    "Bolivia" OR
    "Bosnia" OR
    "Herzegovina" OR
    "Botswana" OR
    "Brazil" OR
    "Bulgaria" OR
    "Burkina Faso" OR
    "Burundi" OR
    "Cambodia" OR
    "Cameroon" OR
    "Cape Verde" OR
    "Central African Republic" OR
    "Chad" OR
    "Chile" OR
    "China" OR
    "Colombia" OR
    "Comoros" OR
    "Congo" OR
    "Costa Rica" OR
    "Côte d'Ivoire" OR
    "Cuba" OR
    "Djibouti" OR
    "Dominica" OR
    "Dominican Republic" OR
    "Ecuador" OR
    "Egypt" OR
    "El Salvador" OR
    "Eritrea" OR
    "Ethiopia" OR
    "Fiji" OR
    "Gabon" OR
    "Gambia" OR
    "Georgia" OR
    "Ghana" OR
    "Grenada" OR
    "Guatemala" OR
    "Guinea" OR
    "Guinea-Bisau" OR
    "Guyana" OR
    "Haiti" OR
    "Honduras" OR
    "India" OR
    "Indonesia" OR
    "Iran" OR
    "Iraq" OR
    "Jamaica" OR
    "Jordan" OR
    "Kazakhstan" OR
    "Kenya" OR
    "Kiribati" OR
    "North Korea" OR
    "Kosovo" OR
    "Kyrgyz Republic" OR
    "Lao" OR
    "Latvia" OR
    "Lebanon" OR
    "Lesotho" OR
    "Liberia" OR
    "Libya" OR
    "Lithuania" OR
    "Macedonia" OR
    "Madagascar" OR
    "Malawi" OR
    "Malaysia" OR
    "Maldives" OR
    "Mali" OR
    "Marshall Islands" OR
    "Mauritania" OR
    "Mauritius" OR
    "Mayotte" OR
    "Mexico" OR
    "Micronesia" OR
    "Moldova" OR
    "Mongolia" OR
    "Montenegro" OR
    "Morocco" OR
    "Mozambique" OR
    "Myanmar" OR
    "Namibia" OR
    "Nepal" OR
    "Nicaragua" OR
    "Niger" OR
    "Nigeria" OR
    "Pakistan" OR
    "Palau" OR
    "Panama" OR
    "Papua New Guinea" OR
    "Paraguay" OR
    "Peru" OR
    "Philippines" OR
    "Romania" OR
    "Russia" OR
    "Rwanda" OR
    "Samoa" OR
    "São Tomé and Principe" OR
    "Senegal" OR
    "Serbia" OR
    "Seychelles" OR
    "Sierra Leone" OR
    "Solomon Islands" OR
    "Somalia" OR
    "South Africa" OR
    "Sri Lanka" OR
    "Saint Kitts and Nevis" OR
    "Saint Lucia" OR
    "Saint Vincent and the Grenadines" OR
    "Sudan" OR
    "Suriname" OR
    "Swaziland" OR
    "Syrian Arab Republic" OR
    "Tajikistan" OR
    "Tanzania" OR
    "Thailand" OR
    "Timor-Leste" OR
    "Togo" OR
    "Tonga" OR
    "Tunisia" OR
    "Turkey" OR
    "Turkmenistan" OR
    "Tuvalu" OR
    "Uganda" OR
    "Ukraine" OR
    "Uruguay" OR
    "Uzbekistan" OR
    "Vanuatu" OR
    "Venezuela" OR
    "Vietnam" OR
    "West Bank" OR
    "Gaza" OR
    "Yemen" OR
    "Zambia" OR
    "Zimbabwe" OR
    "BRICS" OR
    "Africa" OR
    "South America" OR
    "latin America"
    )
    )
    AND
    
    ( TITLE-ABS-KEY ( "promotion regime*" ) OR TITLE-ABS-KEY ( "promot* regime*" ) OR TITLE-ABS-KEY ( "investment* regime*" ) OR TITLE-ABS-KEY ( "foreign investment*" ) OR TITLE-ABS-KEY ( "foreign direct investment*" ) OR TITLE-ABS-KEY ( "foreign trade*" ) OR TITLE-ABS-KEY ( "trade relation*" ) OR TITLE-ABS-KEY ( "trade regime*" ) OR TITLE-ABS-KEY ( "trade promotion*" ) OR TITLE-ABS-KEY ( "international investment*" ) OR TITLE-ABS-KEY ( "international investment agreement*" ) OR TITLE-ABS-KEY ( "trade* and investment*" ) OR TITLE-ABS-KEY ( "trade* & investment*" ) OR TITLE-ABS-KEY ( "trade*" AND "investment*" ) OR TITLE-ABS-KEY ( "capital flight" ) OR TITLE-ABS-KEY ( "FDI" ) OR TITLE-ABS-KEY ( "WTO" ) OR TITLE-ABS-KEY ( "WTO accession" ) OR TITLE-ABS-KEY ( "fdi inflow*" ) OR TITLE-ABS-KEY ( "trade rule*" ) OR TITLE-ABS-KEY ( "internat* trad*" ) OR TITLE-ABS-KEY ( "international trade law*" ) OR TITLE-ABS-KEY ( "trade openness" ) OR TITLE-ABS-KEY ( "trade shock*" ) OR TITLE-ABS-KEY ( "belt and road initiative" ) OR TITLE-ABS-KEY ( "belt & road initiative" ) OR TITLE-ABS-KEY ( "ISDS" ) OR TITLE-ABS-KEY ( "RCEP" ) OR TITLE-ABS-KEY ( "bilateral investment treat*" ) OR TITLE-ABS-KEY ( "investment treat*" ) OR TITLE-ABS-KEY ( "economic statecraft*" ) OR TITLE-ABS-KEY ( "world trade organisation" ) OR TITLE-ABS-KEY ( "world trade organization" ) OR TITLE-ABS-KEY ( "economic integration" ) OR TITLE-ABS-KEY ( "economic development board" ) OR TITLE-ABS-KEY ( "economic cooperation" ) OR TITLE-ABS-KEY ( "EDB" ) OR TITLE-ABS-KEY ( "trade liberal*" ) OR TITLE-ABS-KEY ( "import competition" ) OR TITLE-ABS-KEY ( "cross-border e-commerce" ) OR TITLE-ABS-KEY ( "free trade agreement*" ) OR TITLE-ABS-KEY ( "regional integration" ) OR TITLE-ABS-KEY ( "nafta" ) OR TITLE-ABS-KEY ( "north american free trade agreement" ) )
    )
    )\
    '''  

    key_terms = key_terms+find_quoted_content(cond3)
    #len(key_terms)  # 295
    #print(key_terms)


         
    cond3_1 = cond3.replace('TITLE-ABS-KEY', "")
    #print(cond3_1)
    # cond1_2 = cond1_1.replace('*"', '"')
    # print(cond1_2)
    #pattern = r'\*'
    #cond3_2 = re.sub(pattern, '', cond3_1)
    #print(cond1_2)
    
    cond3_2 = cond3_1.lower()
    #print(cond3_2)
    
    
    ## {}改成""
    pattern = r'[{}]'
    cond3_3 = re.sub(pattern, '"', cond3_2)
    #print(cond3_3)
    
    cond3_4 = replace_quoted_content(cond3_3)
    #print(cond3_4)
    cond3_final = eval(cond3_4)
    
    
    # ### 詢找條件中的terms:
    # substring_prefixes_to_search = []
    # exact_strings_to_search = []
    # substring_prefixes_to_search = find_quoted_content(cond3_3)
    # #print(substring_prefixes_to_search)
    
    # found_exact_strings, found_substring_prefixes = search_strings(article, exact_strings_to_search, substring_prefixes_to_search)


    # ### 條件 4   
    # cond4='''\
    # (
    # TITLE-ABS-KEY
    # (
    # "debt sustain*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "debt relief*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "debt restruct*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "debt struct*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "sovereign default*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "sovereign debt restruct*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "sovereign debt struct*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "Paris Club"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "Highly Indebted Poor Countries Initiative"
    # )
    # OR
    
    # (
    # TITLE-ABS-KEY
    # (
    # "Highly Indebted Poor Countries"
    # )
    # and TITLE-ABS-KEY
    # (
    # "Initiative"
    # )
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "HIPC Initiative"
    # )
    # OR
    
    # (
    # TITLE-ABS-KEY
    # (
    # "HIPC"
    # )
    # and TITLE-ABS-KEY
    # (
    # "debt*"
    # )
    # )
    # OR
    
    # (
    
    # (
    
    # TITLE-ABS-KEY
    # (
    # "developing countr*" OR
    # "poor countr*" OR
    # "poor countr*" OR
    # "emerging countr*" OR
    # "developing world*" OR
    # "developing nation" OR
    # "developing nations" OR
    # "developing state" OR
    # "developing states" OR
    # "low income countr*" OR
    # "middle income countr*" OR
    # "low income nation*" OR
    # "middle income nation*" OR
    # "low income state*" OR
    # "middle income state*" OR
    # "least developed countr*" OR
    # "least developed nation*" OR
    # "least developed state*" OR
    # "Afghanistan" OR
    # "Albania" OR
    # "Algeria" OR
    # "American Samoa" OR
    # "Angola" OR
    # "Antigua and Barbuda" OR
    # "Argentina" OR
    # "Armenia" OR
    # "Azerbaijan" OR
    # "Bangladesh" OR
    # "Belarus" OR
    # "Belize" OR
    # "Benin" OR
    # "Bhutan" OR
    # "Bolivia" OR
    # "Bosnia" OR
    # "Herzegovina" OR
    # "Botswana" OR
    # "Brazil" OR
    # "Bulgaria" OR
    # "Burkina Faso" OR
    # "Burundi" OR
    # "Cambodia" OR
    # "Cameroon" OR
    # "Cape Verde" OR
    # "Central African Republic" OR
    # "Chad" OR
    # "Chile" OR
    # "China" OR
    # "Colombia" OR
    # "Comoros" OR
    # "Congo" OR
    # "Costa Rica" OR
    # "Côte d'Ivoire" OR
    # "Cuba" OR
    # "Djibouti" OR
    # "Dominica" OR
    # "Dominican Republic" OR
    # "Ecuador" OR
    # "Egypt" OR
    # "El Salvador" OR
    # "Eritrea" OR
    # "Ethiopia" OR
    # "Fiji" OR
    # "Gabon" OR
    # "Gambia" OR
    # "Georgia" OR
    # "Ghana" OR
    # "Grenada" OR
    # "Guatemala" OR
    # "Guinea" OR
    # "Guinea-Bisau" OR
    # "Guyana" OR
    # "Haiti" OR
    # "Honduras" OR
    # "India" OR
    # "Indonesia" OR
    # "Iran" OR
    # "Iraq" OR
    # "Jamaica" OR
    # "Jordan" OR
    # "Kazakhstan" OR
    # "Kenya" OR
    # "Kiribati" OR
    # "North Korea" OR
    # "Kosovo" OR
    # "Kyrgyz Republic" OR
    # "Lao" OR
    # "Latvia" OR
    # "Lebanon" OR
    # "Lesotho" OR
    # "Liberia" OR
    # "Libya" OR
    # "Lithuania" OR
    # "Macedonia" OR
    # "Madagascar" OR
    # "Malawi" OR
    # "Malaysia" OR
    # "Maldives" OR
    # "Mali" OR
    # "Marshall Islands" OR
    # "Mauritania" OR
    # "Mauritius" OR
    # "Mayotte" OR
    # "Mexico" OR
    # "Micronesia" OR
    # "Moldova" OR
    # "Mongolia" OR
    # "Montenegro" OR
    # "Morocco" OR
    # "Mozambique" OR
    # "Myanmar" OR
    # "Namibia" OR
    # "Nepal" OR
    # "Nicaragua" OR
    # "Niger" OR
    # "Nigeria" OR
    # "Pakistan" OR
    # "Palau" OR
    # "Panama" OR
    # "Papua New Guinea" OR
    # "Paraguay" OR
    # "Peru" OR
    # "Philippines" OR
    # "Romania" OR
    # "Russia" OR
    # "Rwanda" OR
    # "Samoa" OR
    # "São Tomé and Principe" OR
    # "Senegal" OR
    # "Serbia" OR
    # "Seychelles" OR
    # "Sierra Leone" OR
    # "Solomon Islands" OR
    # "Somalia" OR
    # "South Africa" OR
    # "Sri Lanka" OR
    # "Saint Kitts and Nevis" OR
    # "Saint Lucia" OR
    # "Saint Vincent and the Grenadines" OR
    # "Sudan" OR
    # "Suriname" OR
    # "Swaziland" OR
    # "Syrian Arab Republic" OR
    # "Tajikistan" OR
    # "Tanzania" OR
    # "Thailand" OR
    # "Timor-Leste" OR
    # "Togo" OR
    # "Tonga" OR
    # "Tunisia" OR
    # "Turkey" OR
    # "Turkmenistan" OR
    # "Tuvalu" OR
    # "Uganda" OR
    # "Ukraine" OR
    # "Uruguay" OR
    # "Uzbekistan" OR
    # "Vanuatu" OR
    # "Venezuela" OR
    # "Vietnam" OR
    # "West Bank" OR
    # "Gaza" OR
    # "Yemen" OR
    # "Zambia" OR
    # "Zimbabwe" OR
    # "BRICS" OR
    # "Africa" OR
    # "South America" OR
    # "latin America"
    # )
    # )
    # AND
    
    # (
    # TITLE-ABS-KEY
    # (
    # "public debt"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "external debt"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "foreign debt"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "vulture fund*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "Collective Action Clause*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "Debt Collection*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "Relief Provision"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "fiscal* sustain*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "insolvency"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "creditor*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "financ* distress*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "debt maturity"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "fiscal rule*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "debt crisis*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "fiscal space*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "fiscal recover*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "sovereign bond*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "government debt*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "debt overhang*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "Fiscal Reaction Function*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "Sovereign credit risk*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "primary balance*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "debt manag*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "domestic debt*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "debt dynamic*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "international debt*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "scheme* of arrangement*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "exit consent*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "borrower*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "sovereign risk*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "pari passu"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "debt service*"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "debt reduction*"
    # )
    # OR
    # (
    # TITLE-ABS-KEY("public finance") AND TITLE-ABS-KEY("debt management" OR "debt crisis" OR "indebtness" OR "debt relief")
    # )
    # OR
    # (
    # TITLE-ABS-KEY("*negotiate*") and TITLE-ABS-KEY("debt*")
    # )
    # )
    # )
    # )
    # '''  
    # #### 1110th and 737th Lines: W/4 -> and
    
    # key_terms = key_terms+find_quoted_content(cond4)
    # #len(key_terms)  # 
    # #print(key_terms)

    
    # cond4_1 = cond4.replace('TITLE-ABS-KEY', "")
    # #print(cond1_1)
    # # cond1_2 = cond1_1.replace('*"', '"')
    # # print(cond1_2)
    # #pattern = r'\*'
    # #cond4_2 = re.sub(pattern, '', cond4_1)
    # #print(cond1_2)
    
    # cond4_2 = cond4_1.lower()
    # #print(cond1_3)
    
    
    # ## {}改成""
    # pattern = r'[{}]'
    # cond4_3 = re.sub(pattern, '"', cond4_2)
    # #print(cond1_4)
    
    # cond4_4 = replace_quoted_content(cond4_3)
    # #print(cond2_5)
    # cond4_final = eval(cond4_4)
    
    
    # #### 詢找條件中的terms:
    # #substring_prefixes_to_search = []
    # #exact_strings_to_search = []
    # #substring_prefixes_to_search = find_quoted_content(cond4_3)
    # ##print(substring_prefixes_to_search)
    
    # #found_exact_strings, found_substring_prefixes = search_strings(article, exact_strings_to_search, substring_prefixes_to_search)


    # ### 條件 5   
    # cond5='''\
    # (
    # TITLE-ABS-KEY
    # (
    # "developing countr*" OR
    # "poor countr*" OR
    # "poor countr*" OR
    # "emerging countr*" OR
    # "developing world*" OR
    # "developing nation" OR
    # "developing nations" OR
    # "developing state" OR
    # "developing states" OR
    # "low income countr*" OR
    # "middle income countr*" OR
    # "low income nation*" OR
    # "middle income nation*" OR
    # "low income state*" OR
    # "middle income state*" OR
    # "least developed countr*" OR
    # "least developed nation*" OR
    # "least developed state*" OR
    # "Afghanistan" OR
    # "Albania" OR
    # "Algeria" OR
    # "American Samoa" OR
    # "Angola" OR
    # "Antigua and Barbuda" OR
    # "Argentina" OR
    # "Armenia" OR
    # "Azerbaijan" OR
    # "Bangladesh" OR
    # "Belarus" OR
    # "Belize" OR
    # "Benin" OR
    # "Bhutan" OR
    # "Bolivia" OR
    # "Bosnia" OR
    # "Herzegovina" OR
    # "Botswana" OR
    # "Brazil" OR
    # "Bulgaria" OR
    # "Burkina Faso" OR
    # "Burundi" OR
    # "Cambodia" OR
    # "Cameroon" OR
    # "Cape Verde" OR
    # "Central African Republic" OR
    # "Chad" OR
    # "Chile" OR
    # "China" OR
    # "Colombia" OR
    # "Comoros" OR
    # "Congo" OR
    # "Costa Rica" OR
    # "Côte d'Ivoire" OR
    # "Cuba" OR
    # "Djibouti" OR
    # "Dominica" OR
    # "Dominican Republic" OR
    # "Ecuador" OR
    # "Egypt" OR
    # "El Salvador" OR
    # "Eritrea" OR
    # "Ethiopia" OR
    # "Fiji" OR
    # "Gabon" OR
    # "Gambia" OR
    # "Georgia" OR
    # "Ghana" OR
    # "Grenada" OR
    # "Guatemala" OR
    # "Guinea" OR
    # "Guinea-Bisau" OR
    # "Guyana" OR
    # "Haiti" OR
    # "Honduras" OR
    # "India" OR
    # "Indonesia" OR
    # "Iran" OR
    # "Iraq" OR
    # "Jamaica" OR
    # "Jordan" OR
    # "Kazakhstan" OR
    # "Kenya" OR
    # "Kiribati" OR
    # "North Korea" OR
    # "Kosovo" OR
    # "Kyrgyz Republic" OR
    # "Lao" OR
    # "Latvia" OR
    # "Lebanon" OR
    # "Lesotho" OR
    # "Liberia" OR
    # "Libya" OR
    # "Lithuania" OR
    # "Macedonia" OR
    # "Madagascar" OR
    # "Malawi" OR
    # "Malaysia" OR
    # "Maldives" OR
    # "Mali" OR
    # "Marshall Islands" OR
    # "Mauritania" OR
    # "Mauritius" OR
    # "Mayotte" OR
    # "Mexico" OR
    # "Micronesia" OR
    # "Moldova" OR
    # "Mongolia" OR
    # "Montenegro" OR
    # "Morocco" OR
    # "Mozambique" OR
    # "Myanmar" OR
    # "Namibia" OR
    # "Nepal" OR
    # "Nicaragua" OR
    # "Niger" OR
    # "Nigeria" OR
    # "Pakistan" OR
    # "Palau" OR
    # "Panama" OR
    # "Papua New Guinea" OR
    # "Paraguay" OR
    # "Peru" OR
    # "Philippines" OR
    # "Romania" OR
    # "Russia" OR
    # "Rwanda" OR
    # "Samoa" OR
    # "São Tomé and Principe" OR
    # "Senegal" OR
    # "Serbia" OR
    # "Seychelles" OR
    # "Sierra Leone" OR
    # "Solomon Islands" OR
    # "Somalia" OR
    # "South Africa" OR
    # "Sri Lanka" OR
    # "Saint Kitts and Nevis" OR
    # "Saint Lucia" OR
    # "Saint Vincent and the Grenadines" OR
    # "Sudan" OR
    # "Suriname" OR
    # "Swaziland" OR
    # "Syrian Arab Republic" OR
    # "Tajikistan" OR
    # "Tanzania" OR
    # "Thailand" OR
    # "Timor-Leste" OR
    # "Togo" OR
    # "Tonga" OR
    # "Tunisia" OR
    # "Turkey" OR
    # "Turkmenistan" OR
    # "Tuvalu" OR
    # "Uganda" OR
    # "Ukraine" OR
    # "Uruguay" OR
    # "Uzbekistan" OR
    # "Vanuatu" OR
    # "Venezuela" OR
    # "Vietnam" OR
    # "West Bank" OR
    # "Gaza" OR
    # "Yemen" OR
    # "Zambia" OR
    # "Zimbabwe" OR
    # "BRICS" OR
    # "Africa" OR
    # "South America" OR
    # "latin America"
    # )
    # AND
    
    # (
    
    # ( TITLE-ABS-KEY ( "regime" OR "agreement" OR "policies" OR "policy" OR "rules" OR "law" OR "laws" OR "legislat*" OR "rule*" OR "treaty" OR "treaties" OR "strateg*" ) AND TITLE-ABS-KEY ( ("foreign" OR "international" OR "abroad" OR "cross-border" OR "bilateral") and ("capital" OR "fund" OR "investment" OR "promotion" OR "investor*") ) )
    # OR
    # TITLE-ABS-KEY
    # (
    # "capital flight"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "belt and road initiative"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "belt & road initiative"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "china comprehensive agreement on investment"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "b&r initiative"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "ISDS"
    # )
    # OR
    # TITLE-ABS-KEY
    # (
    # "investor-state dispute settlement"
    # )
    # )
    # )
    # '''  
    # ## 1407th line: W/4 -> and 
    # key_terms = key_terms+find_quoted_content(cond5)
    # #len(key_terms)  # 
    # #print(key_terms)


        
    # cond5_1 = cond5.replace('TITLE-ABS-KEY', "")
    # #print(cond5_1)
    # # cond1_2 = cond1_1.replace('*"', '"')
    # # print(cond1_2)
    # #pattern = r'\*'
    # #cond5_2 = re.sub(pattern, '', cond5_1)
    # #print(cond1_2)
    
    # cond5_2 = cond5_1.lower()
    # #print(cond5_2)
    
    
    # ## {}改成""
    # pattern = r'[{}]'
    # cond5_3 = re.sub(pattern, '"', cond5_2)
    # #print(cond5_3)
    
    # cond5_4 = replace_quoted_content(cond5_3)
    # #print(cond5_4)
    
    # #article = "developing country"
    # cond5_final = eval(cond5_4)
    # #cond3_final = eval(cond3_4)
    
    ### 條件 6   
    cond6='''\
    (
    
    (
    
    TITLE-ABS-KEY
    (
    "developing countr*" OR
    "poor countr*" OR
    "poor countr*" OR
    "emerging countr*" OR
    "developing world*" OR
    "developing nation" OR
    "developing nations" OR
    "developing state" OR
    "developing states" OR
    "low income countr*" OR
    "middle income countr*" OR
    "low income nation*" OR
    "middle income nation*" OR
    "low income state*" OR
    "middle income state*" OR
    "least developed countr*" OR
    "least developed nation*" OR
    "least developed state*" OR
    "Afghanistan" OR
    "Albania" OR
    "Algeria" OR
    "American Samoa" OR
    "Angola" OR
    "Antigua and Barbuda" OR
    "Argentina" OR
    "Armenia" OR
    "Azerbaijan" OR
    "Bangladesh" OR
    "Belarus" OR
    "Belize" OR
    "Benin" OR
    "Bhutan" OR
    "Bolivia" OR
    "Bosnia" OR
    "Herzegovina" OR
    "Botswana" OR
    "Brazil" OR
    "Bulgaria" OR
    "Burkina Faso" OR
    "Burundi" OR
    "Cambodia" OR
    "Cameroon" OR
    "Cape Verde" OR
    "Central African Republic" OR
    "Chad" OR
    "Chile" OR
    "China" OR
    "Colombia" OR
    "Comoros" OR
    "Congo" OR
    "Costa Rica" OR
    "Côte d'Ivoire" OR
    "Cuba" OR
    "Djibouti" OR
    "Dominica" OR
    "Dominican Republic" OR
    "Ecuador" OR
    "Egypt" OR
    "El Salvador" OR
    "Eritrea" OR
    "Ethiopia" OR
    "Fiji" OR
    "Gabon" OR
    "Gambia" OR
    "Georgia" OR
    "Ghana" OR
    "Grenada" OR
    "Guatemala" OR
    "Guinea" OR
    "Guinea-Bisau" OR
    "Guyana" OR
    "Haiti" OR
    "Honduras" OR
    "India" OR
    "Indonesia" OR
    "Iran" OR
    "Iraq" OR
    "Jamaica" OR
    "Jordan" OR
    "Kazakhstan" OR
    "Kenya" OR
    "Kiribati" OR
    "North Korea" OR
    "Kosovo" OR
    "Kyrgyz Republic" OR
    "Lao" OR
    "Latvia" OR
    "Lebanon" OR
    "Lesotho" OR
    "Liberia" OR
    "Libya" OR
    "Lithuania" OR
    "Macedonia" OR
    "Madagascar" OR
    "Malawi" OR
    "Malaysia" OR
    "Maldives" OR
    "Mali" OR
    "Marshall Islands" OR
    "Mauritania" OR
    "Mauritius" OR
    "Mayotte" OR
    "Mexico" OR
    "Micronesia" OR
    "Moldova" OR
    "Mongolia" OR
    "Montenegro" OR
    "Morocco" OR
    "Mozambique" OR
    "Myanmar" OR
    "Namibia" OR
    "Nepal" OR
    "Nicaragua" OR
    "Niger" OR
    "Nigeria" OR
    "Pakistan" OR
    "Palau" OR
    "Panama" OR
    "Papua New Guinea" OR
    "Paraguay" OR
    "Peru" OR
    "Philippines" OR
    "Romania" OR
    "Russia" OR
    "Rwanda" OR
    "Samoa" OR
    "São Tomé and Principe" OR
    "Senegal" OR
    "Serbia" OR
    "Seychelles" OR
    "Sierra Leone" OR
    "Solomon Islands" OR
    "Somalia" OR
    "South Africa" OR
    "Sri Lanka" OR
    "Saint Kitts and Nevis" OR
    "Saint Lucia" OR
    "Saint Vincent and the Grenadines" OR
    "Sudan" OR
    "Suriname" OR
    "Swaziland" OR
    "Syrian Arab Republic" OR
    "Tajikistan" OR
    "Tanzania" OR
    "Thailand" OR
    "Timor-Leste" OR
    "Togo" OR
    "Tonga" OR
    "Tunisia" OR
    "Turkey" OR
    "Turkmenistan" OR
    "Tuvalu" OR
    "Uganda" OR
    "Ukraine" OR
    "Uruguay" OR
    "Uzbekistan" OR
    "Vanuatu" OR
    "Venezuela" OR
    "Vietnam" OR
    "West Bank" OR
    "Gaza" OR
    "Yemen" OR
    "Zambia" OR
    "Zimbabwe" OR
    "BRICS" OR
    "Africa" OR
    "South America" OR
    "latin America" OR
    "south-south" OR
    "north-south" OR
    "south-north" OR
    "triangular coop*" OR
    "triangular coll*"
    )
    )
    AND
    
    (
    
    TITLE-ABS-KEY
    (
    "science" OR
    "scientific" OR
    "technolog*" OR
    "innovat*" OR
    "knowledge" OR
    "global health"
    )
    OR
    
    (
    TITLE-ABS-KEY
    (
    "research*"
    )
    AND NOT
    TITLE-ABS-KEY
    (
    "research output*"
    )
    )
    )
    AND
    
    (
    
    TITLE-ABS-KEY
    (
    "international cooperat*" OR
    "international collab*" OR
    "international partnership*" OR
    "regional cooperat*" OR
    "regional collab*" OR
    "regional partnership*"
    )
    )
    )\
    '''  
    #print(cond6)
    key_terms = key_terms+find_quoted_content(cond6)
    #len(key_terms)  # 295
    #print(key_terms)


         
    cond6_1 = cond6.replace('TITLE-ABS-KEY', "")
    #print(cond6_1)
    # cond1_2 = cond1_1.replace('*"', '"')
    # print(cond1_2)
    #pattern = r'\*'
    #cond3_2 = re.sub(pattern, '', cond3_1)
    #print(cond1_2)
    
    cond6_2 = cond6_1.lower()
    #print(cond6_2)
    
    
    ## {}改成""
    pattern = r'[{}]'
    cond6_3 = re.sub(pattern, '"', cond6_2)
    #print(cond6_3)
    
    cond6_4 = replace_quoted_content(cond6_3)
    #print(cond6_4)
    cond6_final = eval(cond6_4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    st.title("Elsevier SDGs 論文 收錄查詢系統")
    
    if cond1_final or cond2_final or cond3_final or cond6_final:
        st.write(f'查核結果: 恭喜您 ! 你的論文被收錄在 Elsevier SDGs {SDGs_choice}: Partnerships for the Goals')
    else:
        st.write(f'查核結果: 很遺憾 ! 你的論文沒有被收錄在 Elsevier SDGs {SDGs_choice}: Partnerships for the Goals')

    with st.expander(f"SDGs {SDGs_choice} 重要關鍵字, 添加這些關鍵字於 title, abstract, keywords 將有助於論文被收錄於 SDGs 17"):
        #st.title("SDGs 17 關鍵字")
        st.write(key_terms)
