"""Translates text from english to french and french to english"""

import os
import json

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import datetime_to_string

load_dotenv()

# Set some variables
apikey = os.environ.get("apikey")
url = os.environ.get("url")

print(apikey)
print(url)

authenticator = IAMAuthenticator(apikey)
print("The output:", authenticator)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    
)

print("The output:", language_translator)

language_translator.set_service_url(url)



# Translate from english to france

def english_to_french(request):
    """
    translate english to french
    """
    if request is None:
        return None
    response = language_translator.translate(text=request,model_id="en-fr").get_result()
    translation = response['translations'][0]['translation']
    return translation

# Translate from france to english
def french_to_english(request):
    """
    translate french to english
    """
    if request is None:
        return None
    response = language_translator.translate(text=request,model_id="fr-en").get_result()
    translation = response['translations'][0]['translation']
    return translation
