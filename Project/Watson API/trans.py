# -*- coding: utf-8 -*-
import json
from watson_developer_cloud import LanguageTranslatorV2
import io, sys
import nltk
'''
{
"url" : "https://gateway.aibril-watson.kr/language-translator/api",
"username" : "1e32bd76-f647-4467-bbf8-06523e9fb06b",
"password" : "KKXchvFPAOaJ" 
}
'''
language_translator = LanguageTranslatorV2(
    username="1e32bd76-f647-4467-bbf8-06523e9fb06b",
    password="KKXchvFPAOaJ")


# model=''
# with open('glossary.tmx', 'rb') as training_data:
#     custom_model = language_translator.create_model(
#         base_model_id = 'ko-en',
#         name = 'custom-korean-to-english',
#         forced_glossary = training_data)
#     print(json.dumps(custom_model, indent=2))
#     model=json.dumps(custom_model, indent=2).split("\"")[3]


#print(json.dumps(language_translator.get_models(), indent=2))

file= 'test-ko.txt'
test = open(file).readline().decode('utf-8')
print test

# print(json.dumps(
#   language_translator.translate(
#           '밤',
#           source='ko',
#           target='en',
#           ), 
#       indent=2,
#       ensure_ascii=False))



# delete
# language_translator.delete_model(model)
