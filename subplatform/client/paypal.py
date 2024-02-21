import requests
import json

from .models import Subscription

def get_access_token():

    data = {'grant_type': 'client_credentials'}

    headers = {'Accept': 'application/json', 'Accept-Language': 'en_us'}

    client_id = 'AY9YOk6zLqvH6LaBHJnxxq5sBEV1lFEse80uJULCBBz2QIxeOkc56n_b436uKuNgdXtyCALK1Xu6D9Ga'

    secret_id = 'EFJxpWro9DlpDRNsmqG0BENNyYE-xirrZf5tygKyVZ4lebww2W_loVQC_Pe4pOcqTPje5QSeX30fyDXS'

    url = 'https://api.sandbox.paypal.com/v1/oauth2/token'

    r = requests.post(url, auth=(client_id, secret_id), headers = headers, data =data).json()

    access_token = r['access_token']

    return access_token


def cancel_subscription_paypal(access_token, subID):

    bearer_token = 'Bearer ' + access_token

    headers = {
        'Content-Type':'application/json',
        'Authorization':bearer_token,

    }

    url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions/' + subID +'/cancel'

    r = requests.post(url, headers=headers)

    print(r.status_code)

def update_subscription_paypal(access_token, subID):

    bearer_token = 'Bearer ' + access_token

    headers = {
        'Content-Type':'application/json',
        'Authorization':bearer_token,
        }
    subDetails = Subscription.objects.get(paypal_subscription_id=subID)
# current sub plan for user, standard or premium
    current_sub_plan = subDetails.subscription_plan
# to premium
    if current_sub_plan == "Standard":
        new_sub_plan = 'P-95V392642V8281434MXKHUMI' 
# to sandard
    elif current_sub_plan == "Premium":
        new_sub_plan_id  = 'P-1A292279BF333503WMXKHTGQ' 

    url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions/' + subID +'/revise'


    revision_data = {
        "plan_id": new_sub_plan_id
    }

    # make apost request to paypal api for updating subscription

    r = requests.post(url,headers = headers, data=json.dumps(revision_data))
# now we wanna output the response from paypal
    response_data = r.json()

    print(response_data)

    approve_link = None

    for link in response_data.get('links', []):

        if link.get('rel') == 'approve':

            approve_link = link['href']

    
    if r.status_code == 200:
        print("Request was a success")

        return approve_link

    else:
        print("Sorry error occured")


def get_current_subscription(access_token, subID):
    bearer_token = 'Bearer ' + access_token

    headers = {
        'Content-Type':'application/json',
        'Authorization':bearer_token,
        }

    url = f'https://api.sandbox.paypal.com/v1/billing/subscriptions/{subID}'

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        subscription_data = r.json()

        current_plan_id = subscription_data.get('plan_id')

        return current_plan_id

    else:
        print("Failed to retrieve subscription details")

        return None






















