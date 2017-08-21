# coding=utf-8
import json
from watson_developer_cloud import LanguageTranslatorV2
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

# create new custom model
# with open('../resources/language_translator_model.tmx', 'rb') as \
#         custom_model:
#     print(json.dumps(language_translator.create_model(
#         base_model_id='en-fr', name='test_glossary',
#         forced_glossary=custom_model), indent=2))

print(json.dumps(language_translator.get_models(), indent=2))

# print(
#     json.dumps(language_translator.get_model('en-es-conversational'),
#                indent=2))

# delete custom model
# print(json.dumps(language_translator.delete_model(
# '13860c86-ec3f-4e60-8cbe-3ef0048f92af'), indent=2))

print(json.dumps(
  language_translator.translate('this is my name. what is your name?', source='en', target='ko'), 
      indent=2,
      ensure_ascii=False))

# print(json.dumps(
#     language_translator.translate('Messi is the best ever',
#                                   model_id='en-es-conversational'),
#     indent=2))

# print(json.dumps(language_translator.identify('你好'), indent=2))

# print(json.dumps(language_translator.get_identifiable_languages(), indent=2))
