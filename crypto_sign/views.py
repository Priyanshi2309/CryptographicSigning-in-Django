
from django.http import HttpResponse
from django.core import signing

def sign_data(request):
    # Data to be signed
    data = {'user_id': 1, 'username': 'Alice_Charlie'}

    # Secret key for signing
    secret_key = 'Geeks_for_Geeks'

    # Sign the data
    signed_data = signing.dumps(data, key=secret_key)
    
    return HttpResponse(f"Success!Your data has been signed successfully. Here's your signed token: {signed_data}")
