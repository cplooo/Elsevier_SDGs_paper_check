# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 09:07:52 2023

@author: user
"""

import re
import streamlit as st


def search_strings(article, exact_strings, substring_prefixes):
    found_exact_strings = []
    found_substring_prefixes = []
    # Search for exact strings
    for string in exact_strings:
        matches = re.findall(r"\b" + re.escape(string) + r"\b", article, flags=re.IGNORECASE)
        found_exact_strings.extend(matches)
    # Search for strings starting with specific substrings
    for prefix in substring_prefixes:
        matches = re.findall(r"\b" + re.escape(prefix) + r"\w*", article, flags=re.IGNORECASE)
        found_substring_prefixes.extend(matches)
    return found_exact_strings, found_substring_prefixes

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
   #matches = re.search(pattern, article, flags=re.IGNORECASE)
   matches = re.findall(pattern, article, flags=re.IGNORECASE)
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


def find_key_terms_cited(key_terms):
   key_terms_cited = [] 
   #key_terms = ["promot* regime*"]
   #key_terms = ["promot*"]
   #content = "promot* regime*"
   for content in key_terms:
       if "*" not in content:
           #matches = check_strings(article, content)
           key_terms_cited  = key_terms_cited + check_strings(article, content)
           #key_terms_cited.append(matches.group(0))
       elif content.count("*") == 1:
           content_without_asterisk = content.replace("*", "")
           #matches = check_strings(article, content_without_asterisk)
           key_terms_cited  = key_terms_cited + check_strings(article, content_without_asterisk)
           #key_terms_cited.append(matches.group(0))
       else:
           substrings = [substring.replace("*", "") for substring in content.split() if "*" in substring]
           key_terms_cited  = key_terms_cited + check_continuous_words(article, [substrings[0], substrings[1]])
           #matches = check_continuous_words(article, [substrings[0], substrings[1]])
           #key_terms_cited.append(matches.group(0))
   key_terms_cited = list(set(key_terms_cited))        
   return key_terms_cited




def fix_parentheses(expression):
    open_count = expression.count("(")
    close_count = expression.count(")")
    diff = open_count - close_count
    if diff > 0:
        expression += ")" * diff
    elif diff < 0:
        expression = "(" * abs(diff) + expression
    return expression

# def remove_star_from_list(lst):
#     # 將列表中的元素中的星號符號去除
#     return [word.replace('*', '') for word in lst]

# def find_words_with_prefix(string, lst):
#     # 去除星號符號後的列表
#     cleaned_list = remove_star_from_list(lst)

#     # 尋找以列表中元素開頭的所有單詞
#     words = string.split()
#     result = [word for word in words if any(word.startswith(prefix) for prefix in cleaned_list)]

#     return result

# # # 測試程式
# # input_string = "apple banana cat dog elephant"
# # input_list = ['"ap*', '"ca*', '"ele*']
# # result = find_words_with_prefix(input_string, input_list)
# # print(result)


def remove_star_from_list(lst):
    # 將列表中的元素中的星號符號去除
    return [re.sub(r'\*', '', word) for word in lst]

# def find_words_with_prefix(string, lst):
#     # 去除星號符號後的列表
#     cleaned_list = remove_star_from_list(lst)

#     # 尋找以列表中元素開頭的所有單詞
#     pattern = r'\b(?:' + '|'.join(cleaned_list) + r')\w+\b'
#     result = re.findall(pattern, string)

#     return result


# SDGs_choice = input('輸入您要查詢的 SDGS 項目編號(整數): ')
# title       = input('輸入您的論文 title: ')
# abstract    = input('輸入您的論文 abstract: ')
# keywords    = input('輸入您的論文 keywords: ')

st.title("Elsevier SDGs 論文 收錄查詢系統")

SDGs_choice = st.text_input('輸入您要查詢的 SDGS 項目編號(整數 1-17)', '17')
title       = st.text_input('輸入您的論文 title')
abstract    = st.text_input('輸入您的論文 abstract')
keywords    = st.text_input('輸入您的論文 keywords')
  
# title = "promoted regime"  #"SDGs"
# abstract = "" #"sustainable energy"
# keywords = "" #"tax transition"
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
    # #### 1110th and 737th Lines: and -> and
    
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
    
    
    ### 條件 7   
    cond7='''\
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
    AND
    
    TITLE-ABS-KEY ( "technolog*" OR "innovat*" OR "new knowledge" OR "ICT" )
    AND
    
    ( ( TITLE-ABS-KEY("sustainable" OR "sustainability" OR "sound" ) AND TITLE-ABS-KEY("environment*" OR "climate change" OR "global warming" OR "ecolog*") ) OR TITLE-ABS-KEY ( "green development*" ) )
    AND
    
    TITLE-ABS-KEY ( "collaborat*" OR "cooperat*" OR "work together" OR "disseminat*" OR "transfer" OR "transferred" OR "diffusion" OR "develop*" OR "creat*" )
    AND
    
    TITLE-ABS-KEY ( "promot*" OR "encourag*" OR "motivat*" OR "inspir*" OR "incentive" OR "foster" OR "agreement*" OR "stimulate" OR "partnership" OR "preferential term" OR "favourable term" OR "concessional term*" OR "favorable term" OR "agreeable term" OR "support*" OR "pathway to" OR "pathway towards" )
    )
    )\
    '''  

    key_terms = key_terms+find_quoted_content(cond7)
    #len(key_terms)  # 295
    #print(key_terms)


         
    cond7_1 = cond7.replace('TITLE-ABS-KEY', "")
    #print(cond3_1)
    # cond1_2 = cond1_1.replace('*"', '"')
    # print(cond1_2)
    #pattern = r'\*'
    #cond3_2 = re.sub(pattern, '', cond3_1)
    #print(cond1_2)
    
    cond7_2 = cond7_1.lower()
    #print(cond3_2)
    
    
    ## {}改成""
    pattern = r'[{}]'
    cond7_3 = re.sub(pattern, '"', cond7_2)
    #print(cond3_3)
    
    cond7_4 = replace_quoted_content(cond7_3)
    #print(cond7_4)
    cond7_final = eval(cond7_4)
    

    # ### 條件 8   
    # cond8='''\
    # (
    
    # TITLE-ABS-KEY ( "developing countr*" OR "poor countr*" OR "poor countr*" OR "emerging countr*" OR "developing world*" OR "developing nation" OR "developing nations" OR "developing state" OR "developing states" OR "low income countr*" OR "middle income countr*" OR "low income nation*" OR "middle income nation*" OR "low income state*" OR "middle income state*" OR "least developed countr*" OR "least developed nation*" OR "least developed state*" OR "Afghanistan" OR "Albania" OR "Algeria" OR "American Samoa" OR "Angola" OR "Antigua and Barbuda" OR "Argentina" OR "Armenia" OR "Azerbaijan" OR "Bangladesh" OR "Belarus" OR "Belize" OR "Benin" OR "Bhutan" OR "Bolivia" OR "Bosnia" OR "Herzegovina" OR "Botswana" OR "Brazil" OR "Bulgaria" OR "Burkina Faso" OR "Burundi" OR "Cambodia" OR "Cameroon" OR "Cape Verde" OR "Central African Republic" OR "Chad" OR "Chile" OR "China" OR "Colombia" OR "Comoros" OR "Congo" OR "Costa Rica" OR "Côte d'Ivoire" OR "Cuba" OR "Djibouti" OR "Dominica" OR "Dominican Republic" OR "Ecuador" OR "Egypt" OR "El Salvador" OR "Eritrea" OR "Ethiopia" OR "Fiji" OR "Gabon" OR "Gambia" OR "Georgia" OR "Ghana" OR "Grenada" OR "Guatemala" OR "Guinea" OR "Guinea-Bisau" OR "Guyana" OR "Haiti" OR "Honduras" OR "India" OR "Indonesia" OR "Iran" OR "Iraq" OR "Jamaica" OR "Jordan" OR "Kazakhstan" OR "Kenya" OR "Kiribati" OR "North Korea" OR "Kosovo" OR "Kyrgyz Republic" OR "Lao" OR "Latvia" OR "Lebanon" OR "Lesotho" OR "Liberia" OR "Libya" OR "Lithuania" OR "Macedonia" OR "Madagascar" OR "Malawi" OR "Malaysia" OR "Maldives" OR "Mali" OR "Marshall Islands" OR "Mauritania" OR "Mauritius" OR "Mayotte" OR "Mexico" OR "Micronesia" OR "Moldova" OR "Mongolia" OR "Montenegro" OR "Morocco" OR "Mozambique" OR "Myanmar" OR "Namibia" OR "Nepal" OR "Nicaragua" OR "Niger" OR "Nigeria" OR "Pakistan" OR "Palau" OR "Panama" OR "Papua New Guinea" OR "Paraguay" OR "Peru" OR "Philippines" OR "Romania" OR "Russia" OR "Rwanda" OR "Samoa" OR "São Tomé and Principe" OR "Senegal" OR "Serbia" OR "Seychelles" OR "Sierra Leone" OR "Solomon Islands" OR "Somalia" OR "South Africa" OR "Sri Lanka" OR "Saint Kitts and Nevis" OR "Saint Lucia" OR "Saint Vincent and the Grenadines" OR "Sudan" OR "Suriname" OR "Swaziland" OR "Syrian Arab Republic" OR "Tajikistan" OR "Tanzania" OR "Thailand" OR "Timor-Leste" OR "Togo" OR "Tonga" OR "Tunisia" OR "Turkey" OR "Turkmenistan" OR "Tuvalu" OR "Uganda" OR "Ukraine" OR "Uruguay" OR "Uzbekistan" OR "Vanuatu" OR "Venezuela" OR "Vietnam" OR "West Bank" OR "Gaza" OR "Yemen" OR "Zambia" OR "Zimbabwe" OR "BRICS" OR "Africa" OR "South America" OR "latin America" )
    # AND
    
    # ( ( TITLE ( "science" OR "scientific" OR "research" OR "technolog*" OR "innov*" and "capacity" OR "capabilit*" OR "access to" OR "capacity-building" OR "implement*" ) OR AUTHKEY ( "science" OR "scientific" OR "research" OR "technolog*" OR "innov*" and "capacity" OR "capabilit*" OR "access to" OR "capacity-building" OR "implement*" ) ) OR TITLE-ABS-KEY ( "enabling techn*" OR "ICT" OR "ICTs" OR "information and communications techn*" and "access" OR "adoption" OR "enhancing use" OR "enhanced use" OR "enhance use" OR "increase use" OR "increasing use" OR "increased use" ) OR TITLE-ABS-KEY ( "technolog*" OR "innovation" and "capacity utilization" OR "enhanced implementation capacity" OR "enhanced implementation capabilit*" OR "enhancing implementation capacity" OR "enhancing implementation capabilit*" OR "increased implementation capacity" OR "increased implementation capabilit*" OR "increasing implementation capacity" OR "increasing implementation capabilit*" ) OR TITLE-ABS-KEY ( "technolog*" OR "innovation" and "implementation system*" OR "implementation strateg*" OR "access*" ) OR TITLE-ABS-KEY ( "enabling research capa*" OR "enabling innovation capa*" ) )
    # AND NOT
    
    # TITLE-ABS-KEY ( "sexual*" OR "tourism" OR "cyberbullying" OR "cardiovascular risk*" OR "cyberqueer*" OR "career develop*" OR "intraveanous" OR "midwife" OR "food polic*" OR "tobacco" )
    # )\
    # '''  

    # key_terms = key_terms+find_quoted_content(cond8)
    # #len(key_terms)  # 295
    # #print(key_terms)


         
    # cond8_1 = cond8.replace('TITLE-ABS-KEY', "")
    # #print(cond3_1)
    # # cond1_2 = cond1_1.replace('*"', '"')
    # # print(cond1_2)
    # #pattern = r'\*'
    # #cond3_2 = re.sub(pattern, '', cond3_1)
    # #print(cond1_2)
    
    # cond8_2 = cond8_1.lower()
    # #print(cond3_2)
    
    
    # ## {}改成""
    # pattern = r'[{}]'
    # cond8_3 = re.sub(pattern, '"', cond8_2)
    # #print(cond3_3)
    
    # cond8_4 = replace_quoted_content(cond8_3)
    # #print(cond8_4)
    
    # cond8_4_r='''(

    #  ( check_strings(article, "developing countr") or check_strings(article, "poor countr") or check_strings(article, "poor countr") or check_strings(article, "emerging countr") or check_strings(article, "developing world") or check_strings(article, "developing nation") or check_strings(article, "developing nations") or check_strings(article, "developing state") or check_strings(article, "developing states") or check_strings(article, "low income countr") or check_strings(article, "middle income countr") or check_strings(article, "low income nation") or check_strings(article, "middle income nation") or check_strings(article, "low income state") or check_strings(article, "middle income state") or check_strings(article, "least developed countr") or check_strings(article, "least developed nation") or check_strings(article, "least developed state") or check_strings(article, "afghanistan") or check_strings(article, "albania") or check_strings(article, "algeria") or check_strings(article, "american samoa") or check_strings(article, "angola") or check_strings(article, "antigua and barbuda") or check_strings(article, "argentina") or check_strings(article, "armenia") or check_strings(article, "azerbaijan") or check_strings(article, "bangladesh") or check_strings(article, "belarus") or check_strings(article, "belize") or check_strings(article, "benin") or check_strings(article, "bhutan") or check_strings(article, "bolivia") or check_strings(article, "bosnia") or check_strings(article, "herzegovina") or check_strings(article, "botswana") or check_strings(article, "brazil") or check_strings(article, "bulgaria") or check_strings(article, "burkina faso") or check_strings(article, "burundi") or check_strings(article, "cambodia") or check_strings(article, "cameroon") or check_strings(article, "cape verde") or check_strings(article, "central african republic") or check_strings(article, "chad") or check_strings(article, "chile") or check_strings(article, "china") or check_strings(article, "colombia") or check_strings(article, "comoros") or check_strings(article, "congo") or check_strings(article, "costa rica") or check_strings(article, "côte d'ivoire") or check_strings(article, "cuba") or check_strings(article, "djibouti") or check_strings(article, "dominica") or check_strings(article, "dominican republic") or check_strings(article, "ecuador") or check_strings(article, "egypt") or check_strings(article, "el salvador") or check_strings(article, "eritrea") or check_strings(article, "ethiopia") or check_strings(article, "fiji") or check_strings(article, "gabon") or check_strings(article, "gambia") or check_strings(article, "georgia") or check_strings(article, "ghana") or check_strings(article, "grenada") or check_strings(article, "guatemala") or check_strings(article, "guinea") or check_strings(article, "guinea-bisau") or check_strings(article, "guyana") or check_strings(article, "haiti") or check_strings(article, "honduras") or check_strings(article, "india") or check_strings(article, "indonesia") or check_strings(article, "iran") or check_strings(article, "iraq") or check_strings(article, "jamaica") or check_strings(article, "jordan") or check_strings(article, "kazakhstan") or check_strings(article, "kenya") or check_strings(article, "kiribati") or check_strings(article, "north korea") or check_strings(article, "kosovo") or check_strings(article, "kyrgyz republic") or check_strings(article, "lao") or check_strings(article, "latvia") or check_strings(article, "lebanon") or check_strings(article, "lesotho") or check_strings(article, "liberia") or check_strings(article, "libya") or check_strings(article, "lithuania") or check_strings(article, "macedonia") or check_strings(article, "madagascar") or check_strings(article, "malawi") or check_strings(article, "malaysia") or check_strings(article, "maldives") or check_strings(article, "mali") or check_strings(article, "marshall islands") or check_strings(article, "mauritania") or check_strings(article, "mauritius") or check_strings(article, "mayotte") or check_strings(article, "mexico") or check_strings(article, "micronesia") or check_strings(article, "moldova") or check_strings(article, "mongolia") or check_strings(article, "montenegro") or check_strings(article, "morocco") or check_strings(article, "mozambique") or check_strings(article, "myanmar") or check_strings(article, "namibia") or check_strings(article, "nepal") or check_strings(article, "nicaragua") or check_strings(article, "niger") or check_strings(article, "nigeria") or check_strings(article, "pakistan") or check_strings(article, "palau") or check_strings(article, "panama") or check_strings(article, "papua new guinea") or check_strings(article, "paraguay") or check_strings(article, "peru") or check_strings(article, "philippines") or check_strings(article, "romania") or check_strings(article, "russia") or check_strings(article, "rwanda") or check_strings(article, "samoa") or check_strings(article, "são tomé and principe") or check_strings(article, "senegal") or check_strings(article, "serbia") or check_strings(article, "seychelles") or check_strings(article, "sierra leone") or check_strings(article, "solomon islands") or check_strings(article, "somalia") or check_strings(article, "south africa") or check_strings(article, "sri lanka") or check_strings(article, "saint kitts and nevis") or check_strings(article, "saint lucia") or check_strings(article, "saint vincent and the grenadines") or check_strings(article, "sudan") or check_strings(article, "suriname") or check_strings(article, "swaziland") or check_strings(article, "syrian arab republic") or check_strings(article, "tajikistan") or check_strings(article, "tanzania") or check_strings(article, "thailand") or check_strings(article, "timor-leste") or check_strings(article, "togo") or check_strings(article, "tonga") or check_strings(article, "tunisia") or check_strings(article, "turkey") or check_strings(article, "turkmenistan") or check_strings(article, "tuvalu") or check_strings(article, "uganda") or check_strings(article, "ukraine") or check_strings(article, "uruguay") or check_strings(article, "uzbekistan") or check_strings(article, "vanuatu") or check_strings(article, "venezuela") or check_strings(article, "vietnam") or check_strings(article, "west bank") or check_strings(article, "gaza") or check_strings(article, "yemen") or check_strings(article, "zambia") or check_strings(article, "zimbabwe") or check_strings(article, "brics") or check_strings(article, "africa") or check_strings(article, "south america") or check_strings(article, "latin america") )
    # and

    # ( (  ( check_strings(article, check_strings(article, "science")) or check_strings(article, check_strings(article, "scientific")) or check_strings(article, check_strings(article, "research")) or check_strings(article, "technolog") or check_strings(article, "innov") and check_strings(article, check_strings(article, "capacity")) or check_strings(article, "capabilit") or check_strings(article, check_strings(article, "access to")) or check_strings(article, check_strings(article, "capacity-building")) or check_strings(article, "implement") ) or authkey ( check_strings(article, check_strings(article, "science")) or check_strings(article, check_strings(article, "scientific")) or check_strings(article, check_strings(article, "research")) or check_strings(article, "technolog") or check_strings(article, "innov") and check_strings(article, check_strings(article, "capacity")) or check_strings(article, "capabilit") or check_strings(article, check_strings(article, "access to")) or check_strings(article, check_strings(article, "capacity-building")) or check_strings(article, "implement") ) ) or  ( check_strings(article, "enabling techn") or check_strings(article, "ict") or check_strings(article, "icts") or check_strings(article, "information and communications techn") and check_strings(article, "access") or check_strings(article, "adoption") or check_strings(article, "enhancing use") or check_strings(article, "enhanced use") or check_strings(article, "enhance use") or check_strings(article, "increase use") or check_strings(article, "increasing use") or check_strings(article, "increased use") ) or  ( check_strings(article, "technolog") or check_strings(article, check_strings(article, "innovation")) and check_strings(article, "capacity utilization") or check_strings(article, "enhanced implementation capacity") or check_strings(article, "enhanced implementation capabilit") or check_strings(article, "enhancing implementation capacity") or check_strings(article, "enhancing implementation capabilit") or check_strings(article, "increased implementation capacity") or check_strings(article, "increased implementation capabilit") or check_strings(article, "increasing implementation capacity") or check_strings(article, "increasing implementation capabilit") ) or  ( check_strings(article, "technolog") or check_strings(article, check_strings(article, "innovation")) and check_strings(article, "implementation system") or check_strings(article, "implementation strateg") or check_strings(article, "access") ) or  ( check_strings(article, "enabling research capa") or check_strings(article, "enabling innovation capa") ) )
    # and not

    #  ( check_strings(article, "sexual") or check_strings(article, "tourism") or check_strings(article, "cyberbullying") or check_strings(article, "cardiovascular risk") or check_strings(article, "cyberqueer") or check_strings(article, "career develop") or check_strings(article, "intraveanous") or check_strings(article, "midwife") or check_strings(article, "food polic") or check_strings(article, "tobacco") )
    # )'''
    # print(cond8_4_r)
    # #fixed_expression = fix_parentheses(cond8_4_r)
    # #type(fixed_expression)
    # #print(fixed_expression)
    # #cond8_final = eval(fixed_expression)
    # cond8_final = eval(cond8_4_r)
    
    ### 條件 9: 有原來是 OR 改成 OR 
    cond9='''\
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
    AND
    
    (
    
    ( TITLE-ABS-KEY ( "international" OR "south-south" OR "north-south" OR "triangular" OR "partner countr*" OR "industrialized countr*" OR "europe*" OR "north america*" OR "united states" OR "canada" OR "australia" OR "united kingdom" OR "france" OR "japan" OR "usa" OR "new zealand" OR "austria" OR "belgium" OR "denmark" OR "finland" OR "Germany" OR "Greece" OR "Iceland" OR "Ireland" OR "Italy" OR "Luxembourg" OR "Netherlands" OR "Norway" OR "Portugal" OR "Spain" OR "Sweden" OR "Switzerland" ) AND TITLE-ABS-KEY ( "commit*" OR "achiev*" OR "positive impact*" OR "impactful" OR "alleviat*" OR "acknowledg*" OR "participa*" OR "contribut*" OR "work together" OR "working together" OR "worked together" OR "response*" OR "respond*" OR "engag*" OR "support*" OR "address*" OR "help*" OR "aid" OR "assist*" OR "partner*" OR "collabora*" OR "cooperat*" OR "joint work" OR "effort*" OR "transfer" OR "sharing" OR "shared" OR "share" OR "alliance*" OR "progress" OR "synerg*" OR "implement*" OR "adopt*" OR "gap" OR "barrier" OR "barriers" OR "opportunit*" OR "initiativ*" OR "challenge*" OR "invest*" OR "fund" OR "funds" OR "funded" OR "financed" OR "financial" OR "financing" OR "technical" OR "knowledge" OR "technolog*" OR "equit*" OR "inequalit*" OR "inequit*" OR "innovat*" OR "scientific" OR "capacit*" OR "capabilit*" OR "know-how" OR "competenc*" OR "global dev*" OR "global health" OR "skill*" ) )
    AND
    
    ( TITLE-ABS-KEY ( "SDG" OR "SDGs" OR "Sustainable development goal*" ) OR TITLE-ABS-KEY ( "Agenda 2030" OR "Agenda2030" OR "2030 Agenda" ) )
    )
    )\
    '''  

    key_terms = key_terms+find_quoted_content(cond9)
    #len(key_terms)  # 295
    #print(key_terms)


         
    cond9_1 = cond9.replace('TITLE-ABS-KEY', "")
    #print(cond3_1)
    # cond1_2 = cond1_1.replace('*"', '"')
    # print(cond1_2)
    #pattern = r'\*'
    #cond3_2 = re.sub(pattern, '', cond3_1)
    #print(cond1_2)
    
    cond9_2 = cond9_1.lower()
    #print(cond3_2)
    
    
    ## {}改成""
    pattern = r'[{}]'
    cond9_3 = re.sub(pattern, '"', cond9_2)
    #print(cond3_3)
    
    cond9_4 = replace_quoted_content(cond9_3)
    #print(cond3_4)
    cond9_final = eval(cond9_4)


    ### 條件 10: 
    cond10='''\
    (
    
    TITLE-ABS-KEY
    (
    "fair trade" OR
    "global trade" OR
    "trading system" or "trading treat*" OR
    "world trade org*" OR
    "WTO" OR
    "doha development agenda" OR
    "trading rule*" OR
    "trading law*" OR
    "worldwide weighted tariff-average" OR
    "wwta" OR
    "import-export" OR
    "anti-dumpint" OR
    "protectionist tariff*" OR
    "foreign import*" OR
    "fair market value" OR
    "bound tariff*" OR
    "market distortion*" OR
    "competition polic*" OR
    "anti-competitiv*" OR
    "global-supply chain*" OR
    "economic partnership agreement*" OR
    "collusion"
    )
    AND
    
    TITLE-ABS-KEY
    (
    "peer-to-peer" OR
    "universal" OR
    "inclusive" OR
    "equit*" OR
    "inequit*" OR
    "equitab*" OR
    "inequitab*" OR
    "non-discriminat*" OR
    "discriminator*" OR
    "multilateral*" OR
    "worldwide" OR
    "nctad" OR
    "united nations conference on trade and develop*" OR
    "sustainab*"
    )
    )\
    '''  

    key_terms = key_terms+find_quoted_content(cond10)
    #len(key_terms)  # 295
    #print(key_terms)


         
    cond10_1 = cond10.replace('TITLE-ABS-KEY', "")
    #print(cond3_1)
    # cond1_2 = cond1_1.replace('*"', '"')
    # print(cond1_2)
    #pattern = r'\*'
    #cond3_2 = re.sub(pattern, '', cond3_1)
    #print(cond1_2)
    
    cond10_2 = cond10_1.lower()
    #print(cond3_2)
    
    
    ## {}改成""
    pattern = r'[{}]'
    cond10_3 = re.sub(pattern, '"', cond10_2)
    #print(cond3_3)
    
    cond10_4 = replace_quoted_content(cond10_3)
    #print(cond3_4)
    cond10_final = eval(cond10_4)


    # ### 條件 11: 有 w/3 改成 OR
    # cond11='''\
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
    
    # TITLE-ABS-KEY
    # (
    # "potential" OR
    # "expansion" OR
    # "expand*" OR
    # "performance" OR
    # "growth" OR
    # "grow" OR
    # "competitiveness" OR
    # "enhanced" OR
    # "increas*" OR
    # "intensity" OR
    # "intensification" OR
    # "improved strateg*" OR
    # "better strateg*" OR
    # "promotion" OR
    # "diversification" OR
    # "assistance" OR
    # "higher commitment*" OR
    # "higher demand" OR
    # "increased demand" OR
    # "create demand" OR
    # "creating demand" OR
    # "spillover*" OR
    # "success*" OR
    # "potential" OR
    # "share" OR
    # "channel*" OR
    # "barrier*" OR
    # "credit*" OR
    # "activit*" OR
    # "amplification" OR
    # "developing" OR
    # "market economy development" OR
    # "economic development" OR
    # "accelerat*" OR
    # "marketing" OR "export" OR
    # "exporter*" OR
    # "trade market" OR
    # "trading volume"
    # )
    # AND NOT
    
    # TITLE-ABS-KEY
    # (
    # "media regulation" OR
    # "meteorological export" OR
    # "eutrophication" OR
    # "malaria" OR
    # "cell membrane" OR
    # "saccharomyces" OR
    # "aspergillus" OR
    # "bacteria*"
    # )
    # )\
    # '''  

    # key_terms = key_terms+find_quoted_content(cond11)
    # #len(key_terms)  # 295
    # #print(key_terms)


         
    # cond11_1 = cond11.replace('TITLE-ABS-KEY', "")
    # #print(cond3_1)
    # # cond1_2 = cond1_1.replace('*"', '"')
    # # print(cond1_2)
    # #pattern = r'\*'
    # #cond3_2 = re.sub(pattern, '', cond3_1)
    # #print(cond1_2)
    
    # cond11_2 = cond11_1.lower()
    # #print(cond3_2)
    
    
    # ## {}改成""
    # pattern = r'[{}]'
    # cond11_3 = re.sub(pattern, '"', cond11_2)
    # #print(cond3_3)
    
    # cond11_4 = replace_quoted_content(cond11_3)
    # #print(cond11_4)
    # cond11_4_r = '''\
    # (


    # (
    # check_strings(article, "developing countr") or
    # check_strings(article, "poor countr") or
    # check_strings(article, "poor countr") or
    # check_strings(article, "emerging countr") or
    # check_strings(article, "developing world") or
    # check_strings(article, "developing nation") or
    # check_strings(article, "developing nations") or
    # check_strings(article, "developing state") or
    # check_strings(article, "developing states") or
    # check_strings(article, "low income countr") or
    # check_strings(article, "middle income countr") or
    # check_strings(article, "low income nation") or
    # check_strings(article, "middle income nation") or
    # check_strings(article, "low income state") or
    # check_strings(article, "middle income state") or
    # check_strings(article, "least developed countr") or
    # check_strings(article, "least developed nation") or
    # check_strings(article, "least developed state") or
    # check_strings(article, "afghanistan") or
    # check_strings(article, "albania") or
    # check_strings(article, "algeria") or
    # check_strings(article, "american samoa") or
    # check_strings(article, "angola") or
    # check_strings(article, "antigua and barbuda") or
    # check_strings(article, "argentina") or
    # check_strings(article, "armenia") or
    # check_strings(article, "azerbaijan") or
    # check_strings(article, "bangladesh") or
    # check_strings(article, "belarus") or
    # check_strings(article, "belize") or
    # check_strings(article, "benin") or
    # check_strings(article, "bhutan") or
    # check_strings(article, "bolivia") or
    # check_strings(article, "bosnia") or
    # check_strings(article, "herzegovina") or
    # check_strings(article, "botswana") or
    # check_strings(article, "brazil") or
    # check_strings(article, "bulgaria") or
    # check_strings(article, "burkina faso") or
    # check_strings(article, "burundi") or
    # check_strings(article, "cambodia") or
    # check_strings(article, "cameroon") or
    # check_strings(article, "cape verde") or
    # check_strings(article, "central african republic") or
    # check_strings(article, "chad") or
    # check_strings(article, "chile") or
    # check_strings(article, "china") or
    # check_strings(article, "colombia") or
    # check_strings(article, "comoros") or
    # check_strings(article, "congo") or
    # check_strings(article, "costa rica") or
    # check_strings(article, r"côte d'ivoire") or
    # check_strings(article, "cuba") or
    # check_strings(article, "djibouti") or
    # check_strings(article, "dominica") or
    # check_strings(article, "dominican republic") or
    # check_strings(article, "ecuador") or
    # check_strings(article, "egypt") or
    # check_strings(article, "el salvador") or
    # check_strings(article, "eritrea") or
    # check_strings(article, "ethiopia") or
    # check_strings(article, "fiji") or
    # check_strings(article, "gabon") or
    # check_strings(article, "gambia") or
    # check_strings(article, "georgia") or
    # check_strings(article, "ghana") or
    # check_strings(article, "grenada") or
    # check_strings(article, "guatemala") or
    # check_strings(article, "guinea") or
    # check_strings(article, "guinea-bisau") or
    # check_strings(article, "guyana") or
    # check_strings(article, "haiti") or
    # check_strings(article, "honduras") or
    # check_strings(article, "india") or
    # check_strings(article, "indonesia") or
    # check_strings(article, "iran") or
    # check_strings(article, "iraq") or
    # check_strings(article, "jamaica") or
    # check_strings(article, "jordan") or
    # check_strings(article, "kazakhstan") or
    # check_strings(article, "kenya") or
    # check_strings(article, "kiribati") or
    # check_strings(article, "north korea") or
    # check_strings(article, "kosovo") or
    # check_strings(article, "kyrgyz republic") or
    # check_strings(article, "lao") or
    # check_strings(article, "latvia") or
    # check_strings(article, "lebanon") or
    # check_strings(article, "lesotho") or
    # check_strings(article, "liberia") or
    # check_strings(article, "libya") or
    # check_strings(article, "lithuania") or
    # check_strings(article, "macedonia") or
    # check_strings(article, "madagascar") or
    # check_strings(article, "malawi") or
    # check_strings(article, "malaysia") or
    # check_strings(article, "maldives") or
    # check_strings(article, "mali") or
    # check_strings(article, "marshall islands") or
    # check_strings(article, "mauritania") or
    # check_strings(article, "mauritius") or
    # check_strings(article, "mayotte") or
    # check_strings(article, "mexico") or
    # check_strings(article, "micronesia") or
    # check_strings(article, "moldova") or
    # check_strings(article, "mongolia") or
    # check_strings(article, "montenegro") or
    # check_strings(article, "morocco") or
    # check_strings(article, "mozambique") or
    # check_strings(article, "myanmar") or
    # check_strings(article, "namibia") or
    # check_strings(article, "nepal") or
    # check_strings(article, "nicaragua") or
    # check_strings(article, "niger") or
    # check_strings(article, "nigeria") or
    # check_strings(article, "pakistan") or
    # check_strings(article, "palau") or
    # check_strings(article, "panama") or
    # check_strings(article, "papua new guinea") or
    # check_strings(article, "paraguay") or
    # check_strings(article, "peru") or
    # check_strings(article, "philippines") or
    # check_strings(article, "romania") or
    # check_strings(article, "russia") or
    # check_strings(article, "rwanda") or
    # check_strings(article, "samoa") or
    # check_strings(article, r"são tomé and principe") or
    # check_strings(article, "senegal") or
    # check_strings(article, "serbia") or
    # check_strings(article, "seychelles") or
    # check_strings(article, "sierra leone") or
    # check_strings(article, "solomon islands") or
    # check_strings(article, "somalia") or
    # check_strings(article, "south africa") or
    # check_strings(article, "sri lanka") or
    # check_strings(article, "saint kitts and nevis") or
    # check_strings(article, "saint lucia") or
    # check_strings(article, "saint vincent and the grenadines") or
    # check_strings(article, "sudan") or
    # check_strings(article, "suriname") or
    # check_strings(article, "swaziland") or
    # check_strings(article, "syrian arab republic") or
    # check_strings(article, "tajikistan") or
    # check_strings(article, "tanzania") or
    # check_strings(article, "thailand") or
    # check_strings(article, "timor-leste") or
    # check_strings(article, "togo") or
    # check_strings(article, "tonga") or
    # check_strings(article, "tunisia") or
    # check_strings(article, "turkey") or
    # check_strings(article, "turkmenistan") or
    # check_strings(article, "tuvalu") or
    # check_strings(article, "uganda") or
    # check_strings(article, "ukraine") or
    # check_strings(article, "uruguay") or
    # check_strings(article, "uzbekistan") or
    # check_strings(article, "vanuatu") or
    # check_strings(article, "venezuela") or
    # check_strings(article, "vietnam") or
    # check_strings(article, "west bank") or
    # check_strings(article, "gaza") or
    # check_strings(article, "yemen") or
    # check_strings(article, "zambia") or
    # check_strings(article, "zimbabwe") or
    # check_strings(article, "brics") or
    # check_strings(article, "africa") or
    # check_strings(article, "south america") or
    # check_strings(article, "latin america")
    # )
    # and


    # (
    # check_strings(article, check_strings(article, "potential")) or
    # check_strings(article, "expansion") or
    # check_strings(article, "expand") or
    # check_strings(article, "performance") or
    # check_strings(article, "growth") or
    # check_strings(article, "grow") or
    # check_strings(article, "competitiveness") or
    # check_strings(article, "enhanced") or
    # check_strings(article, "increas") or
    # check_strings(article, "intensity") or
    # check_strings(article, "intensification") or
    # check_strings(article, "improved strateg") or
    # check_strings(article, "better strateg") or
    # check_strings(article, "promotion") or
    # check_strings(article, "diversification") or
    # check_strings(article, "assistance") or
    # check_strings(article, "higher commitment") or
    # check_strings(article, "higher demand") or
    # check_strings(article, "increased demand") or
    # check_strings(article, "create demand") or
    # check_strings(article, "creating demand") or
    # check_strings(article, "spillover") or
    # check_strings(article, "success") or
    # check_strings(article, check_strings(article, "potential")) or
    # check_strings(article, "share") or
    # check_strings(article, "channel") or
    # check_strings(article, "barrier") or
    # check_strings(article, "credit") or
    # check_strings(article, "activit") or
    # check_strings(article, "amplification") or
    # check_strings(article, "developing") or
    # check_strings(article, "market economy development") or
    # check_strings(article, "economic development") or
    # check_strings(article, "accelerat") or
    # check_strings(article, "marketing") or check_strings(article, "export") or
    # check_strings(article, "exporter") or
    # check_strings(article, "trade market") or
    # check_strings(article, "trading volume")
    # )
    # and not


    # (
    # check_strings(article, "media regulation") or
    # check_strings(article, "meteorological export") or
    # check_strings(article, "eutrophication") or
    # check_strings(article, "malaria") or
    # check_strings(article, "cell membrane") or
    # check_strings(article, "saccharomyces") or
    # check_strings(article, "aspergillus") or
    # check_strings(article, "bacteria")
    # )
    # )\
    # '''
    # cond11_final = eval(cond11_4_r)
    # #cond11_final = eval(cond11_4)
    

    ### 條件 12: 
    cond12='''\
    (
    
    TITLE-ABS-KEY
    (
    "trade barrier*" OR
    "trading barrier*" OR
    "trade restriction*" OR
    "trading restriction*" OR
    "export ban*" OR
    "trade embargo*" OR
    "trading embargo*" OR
    "trade injunction*" OR
    "trading injunction*" OR
    "trade sanction*" OR
    "trading sanction*" OR
    "duty free" or "quota free" OR
    "market access" OR
    "access to market" OR
    "access to markets" OR
    "trade liberali*" OR
    "global value chain*" OR
    "free trade" OR
    "free trading" OR
    "protectionism" OR
    "protectionist*" OR
    "trade facilitation" OR
    "trade facilit*" OR
    "trading facilitation" OR
    "trading facilit*" OR
    "antidumping" OR
    "anti-dumping" OR
    "comparative advantage" OR
    "preferential trade agreement*" OR
    "preferential trading agreement*" OR
    "non-tariff measure*" OR
    "trade preference*" OR
    "general* system of preference*" OR
    "market participation*" OR
    "foreign entry mode*" OR
    "NAFTA" OR
    "AFCFTA" OR
    "USMCA" OR
    "RCEP" OR
    "regional comprehensive economic partnership" OR
    "north american free trade agreement" OR
    "united states-mexico-canada agreement" OR
    "CPTPP" OR
    "comprehensive and progressive agreement for trans-pacific partnership" OR
    "trans-pacific partnership"
    )
    AND
    
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
    AND NOT
    
    TITLE-ABS-KEY
    (
    "television" OR
    "tropical cyclone*"
    )
    )\
    '''  

    key_terms = key_terms+find_quoted_content(cond12)
    #len(key_terms)  # 295
    #print(key_terms)
    


         
    cond12_1 = cond12.replace('TITLE-ABS-KEY', "")
    #print(cond3_1)
    # cond1_2 = cond1_1.replace('*"', '"')
    # print(cond1_2)
    #pattern = r'\*'
    #cond3_2 = re.sub(pattern, '', cond3_1)
    #print(cond1_2)
    
    cond12_2 = cond12_1.lower()
    #print(cond3_2)
    
    
    ## {}改成""
    pattern = r'[{}]'
    cond12_3 = re.sub(pattern, '"', cond12_2)
    #print(cond3_3)
    
    cond12_4 = replace_quoted_content(cond12_3)
    #print(cond3_4)
    cond12_final = eval(cond12_4)
    
    
    ### 條件 13: 
    cond13='''\
    (
    
    TITLE-ABS-KEY
    (
    "trade barrier*" OR
    "trading barrier*" OR
    "trade restriction*" OR
    "trading restriction*" OR
    "export ban*" OR
    "trade embargo*" OR
    "trading embargo*" OR
    "trade injunction*" OR
    "trading injunction*" OR
    "trade sanction*" OR
    "trading sanction*" OR
    "duty free" or "quota free" OR
    "market access" OR
    "access to market" OR
    "access to markets" OR
    "trade liberali*" OR
    "global value chain*" OR
    "free trade" OR
    "free trading" OR
    "protectionism" OR
    "protectionist*" OR
    "trade facilitation" OR
    "trade facilit*" OR
    "trading facilitation" OR
    "trading facilit*" OR
    "antidumping" OR
    "anti-dumping" OR
    "comparative advantage" OR
    "preferential trade agreement*" OR
    "preferential trading agreement*" OR
    "non-tariff measure*" OR
    "trade preference*" OR
    "general* system of preference*" OR
    "market participation*" OR
    "foreign entry mode*" OR
    "NAFTA" OR
    "AFCFTA" OR
    "USMCA" OR
    "RCEP" OR
    "regional comprehensive economic partnership" OR
    "north american free trade agreement" OR
    "united states-mexico-canada agreement" OR
    "CPTPP" OR
    "comprehensive and progressive agreement for trans-pacific partnership" OR
    "trans-pacific partnership"
    )
    AND
    
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
    AND NOT
    
    TITLE-ABS-KEY
    (
    "television" OR
    "tropical cyclone*"
    )
    )\
    '''  

    key_terms = key_terms+find_quoted_content(cond13)
    #len(key_terms)  # 295
    #print(key_terms)
    


         
    cond13_1 = cond13.replace('TITLE-ABS-KEY', "")
    #print(cond3_1)
    # cond1_2 = cond1_1.replace('*"', '"')
    # print(cond1_2)
    #pattern = r'\*'
    #cond3_2 = re.sub(pattern, '', cond3_1)
    #print(cond1_2)
    
    cond13_2 = cond13_1.lower()
    #print(cond3_2)
    
    
    ## {}改成""
    pattern = r'[{}]'
    cond13_3 = re.sub(pattern, '"', cond13_2)
    #print(cond3_3)
    
    cond13_4 = replace_quoted_content(cond13_3)
    #print(cond3_4)
    cond13_final = eval(cond13_4)
    
    
    ### 條件 14: 
    cond14='''\
    (
    
    (
    
    TITLE-ABS-KEY
    (
    "policy" OR
    "policies" OR
    "policymak*" OR
    "policy mak*" OR
    "decisionmak*" OR
    "decision mak*" OR
    "regulation" OR
    "regulations" OR
    "accountability" OR
    "action plan*"
    )
    OR
    
    (
    TITLE-ABS-KEY
    (
    "framework*"
    )
    AND
    TITLE-ABS-KEY
    (
    "countr*" OR "government*" OR "federal" OR "state" OR "legal" OR "public" OR "nation*" OR "international"
    )
    )
    )
    AND
    
    (
    
    TITLE-ABS-KEY
    (
    "sustainable development" OR
    "SDG" OR
    "SDGS" OR
    "millenium development goal*" OR
    "Agenda2030" OR
    "Agenda 2030" OR
    "sustainable forestry" OR
    "sustainable transport*" OR
    "sustainable engineering" OR
    "sustainable solution*" OR
    "UNFCCC"
    )
    OR
    
    (
    TITLE-ABS-KEY
    (
    "sustainability" OR "sustainable"
    )
    AND
    TITLE-ABS-KEY
    (
    "forest management" OR "clean development mechanism*" OR "green development mechanism*" OR "bioenergy" OR "bioenergies" OR "green energ*" OR "bio-energy" OR "bio-energies" OR "bioenergetics" OR "bio-energetics" OR "continous cover forest*" OR "renewable energy" OR "renewable energies" OR "land use" OR "land consumption" OR "land management" OR "environment*" OR "green technolog*" OR "green engineering" OR "green building*" OR "desalination" OR "renewable resource*" OR "natural resource*" OR "energy performance" OR "green cities" OR "green city" OR "transportation" OR "ethical consumption" OR "food system*" OR "innovation*" OR "waste management" OR "agriculture" OR "agricultural" OR "deforestation" OR "reducing emission*" OR "reduced emission*" OR "forest land" OR "forestry" OR "carbon emission*" OR "CO2 emission*" OR "CO-2 emission*" OR "carbon dioxide emission*" OR "GHG" OR "greenhouse gas" OR "resilient" OR "resilience" OR "governance" OR "pollution" OR "pollutant*" OR "ecosystem*" OR "urbanization" OR "urbanisation" OR "urban planning"
    )
    )
    AND NOT
    
    TITLE-ABS-KEY
    (
    "auto-bidding" OR
    "intellectual capital" OR
    "cheat" OR
    "cheating" OR
    "artificial regulation"
    )
    )
    )\
    '''  

    key_terms = key_terms+find_quoted_content(cond14)
    #len(key_terms)  # 295
    #print(key_terms)
    


         
    cond14_1 = cond14.replace('TITLE-ABS-KEY', "")
    #print(cond3_1)
    # cond1_2 = cond1_1.replace('*"', '"')
    # print(cond1_2)
    #pattern = r'\*'
    #cond3_2 = re.sub(pattern, '', cond3_1)
    #print(cond1_2)
    
    cond14_2 = cond14_1.lower()
    #print(cond3_2)
    
    
    ## {}改成""
    pattern = r'[{}]'
    cond14_3 = re.sub(pattern, '"', cond14_2)
    #print(cond3_3)
    
    cond14_4 = replace_quoted_content(cond14_3)
    #print(cond3_4)
    cond14_final = eval(cond14_4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if cond1_final or cond2_final or cond3_final or cond6_final or cond7_final or cond9_final or cond10_final or cond12_final or cond13_final or cond14_final:
        st.write(f'查核結果: 恭喜您 ! 你的論文可以被收錄在 Elsevier SDGs {SDGs_choice}.')
    else:
        st.write(f'查核結果: 很遺憾 ! 你的論文無法被收錄在 Elsevier SDGs {SDGs_choice}.')

    with st.expander(f"你的論文中屬於 SDGs {SDGs_choice} 的關鍵字如下:"):
        # key_terms_noAsterisk = remove_star_from_list(key_terms)
        # exact_strings_to_search = []
        # substring_prefixes_to_search = key_terms_noAsterisk 
        # found_exact_strings, found_substring_prefixes = search_strings(article, exact_strings_to_search, substring_prefixes_to_search)
        # key_terms_cited = found_substring_prefixes
        # #result = find_words_with_prefix(input_string, input_list)
        key_terms_cited = find_key_terms_cited(key_terms)
        for string in key_terms_cited:
            st.write(string)
        


    with st.expander(f"SDGs {SDGs_choice} 重要關鍵字列表, 添加這些關鍵字於 title, abstract, keywords 將有助於論文被收錄於 SDGs {SDGs_choice}. 完整收錄條件如下連結 https://tinyurl.com/26xxakca."):
        #st.title("SDGs 17 關鍵字")
        st.write(key_terms)
