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


print(json.dumps(language_translator.get_models(), indent=2))

print(json.dumps(
  language_translator.translate('기계학습의 한 분야인 딥러닝은 최근 다양한 분야에서 비약적인 성능 향상에 기여하였다.', source='ko', target='en'),
      indent=2,
      ensure_ascii=False))

