import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    french_text = language_translator.translate(english_text,model_id='en-fr')
    return french_text
def french_to_english(french_text):
    english_text = language_translator.translate(french_text,model_id='fr-en')
    return english_text
