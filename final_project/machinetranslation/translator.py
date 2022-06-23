import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

# Create a new instance of Watson translator service
translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)

translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translate English to French
    """
    if len(english_text.strip())==0:
        raise ValueError("Text must not be empty!")
    result = translator.translate(
        text=english_text,
        model_id="en-fr"
    ).get_result()

    return result.get("translations")[0]["translation"]

def french_to_english(french_text):
    """
    Translate French to English
    """
    if len(french_text.strip())==0:
        raise ValueError("Text must not be empty!")
    result = translator.translate(
        text=french_text,
        model_id="fr-en"
    ).get_result()

    return result.get("translations")[0]["translation"]
