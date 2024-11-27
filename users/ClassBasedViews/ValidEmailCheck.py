import json
import requests
from django.conf import settings
from email_validator import validate_email, EmailNotValidError

# You may need to install Requests pip
# python -m pip install requests

class IPQS:
    key = settings.EMAIL_CHECK_VALID_API

    def email_validation_api(self, email: str, vars: dict={}) -> dict:
        url = "https://www.ipqualityscore.com/api/json/email/%s/%s" % (self.key, email)

        # timeout = 7
        # fast = 'false'
        # abuse_strictness = 0
        # additional_params = {
        #     'timeout' : timeout,
        #     'fast' : fast,
        #     'abuse_strictness' : abuse_strictness
        #     }
        # vars = additional_params
        x = requests.get(url, params = vars)

        result = json.loads(x.text)

        # Check to see if our query was successful.
        if 'success' in result and result['success']:

            #Example 1: Flag disposable and abusive emails
            if result['recent_abuse'] == True or result['disposable'] == True:
                return(False, 'Email is abusive or disposable, high chance of fraud.')
            else:
                return(True, 'Email is clean.')
        return json.loads(x.text)
    

    def emailvalidator_address(self, email):
        try:
            valid = validate_email(email)
            return(True, valid.normalized)
        except EmailNotValidError as e:
            return(False, str(e))
        

    

