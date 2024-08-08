import requests
import pandas as pd

# Define the URL of the API to get the data from.
authors_url = "http://localhost:8600/api/author/"
books_url = "http://localhost:8600/api/book/"

# [Optional] If your API endpoint requires authentication, include your token here.
#api_token = "your-api-token-here"
#headers = {
#    "Authorization":api_token,
#}

# Send GET request to the API endpoint
#response = requests.get(authors_url, headers=headers)
response = requests.get(authors_url)

# Return response code from succesfully request.
if response.status_code == 200:
    # Get the data as a json format.
    data = response.json()
    
    # Transform json to a Data Frame from pandas to show it as a table on terminal.
    data_frame = pd.DataFrame(data)
    
    print("Data: ", data_frame)
else:
    print("Request has failed:", response.status_code)