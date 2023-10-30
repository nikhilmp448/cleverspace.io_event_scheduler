import requests

def parse_token(url,token = None):

    # Create a dictionary containing the Authorization header with the Bearer token
    headers = {
        'Authorization': f'Bearer {token}'
    }

    # Make the API request with the access token in the headers
    response = requests.get(url, headers=headers)
    return response

    # Check the response and handle it accordingly
    # if response.status_code == 200:
    #     # Successful request, do something with the response
    #     data = response.json()
    #     print(data)
    # else:
    #     # Request failed, handle errors here
    #     print(f'Request failed with status code: {response.status_code}')
    #     print(response.text)
