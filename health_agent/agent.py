import requests

# Configuration 
api_key = '08TaIp1S3RY1FAz4wgQdfbZ4UOZ0Spa0'
external_user_id ='677a6bf91103754dbe658b09'
base_url = 'https://api.on-demand.io/chat/v1/sessions'

# Step 1: Create Chat Session
headers = {
    'apikey': api_key
}

session_data = {
    "pluginIds": [],
    "externalUserId": external_user_id
}

response = requests.post(base_url, headers=headers, json=session_data)

if response.status_code == 201:
    # Extract session ID from response
    session_id = response.json().get('data', {}).get('id')
    if session_id:
        # Step 2: Submit Query
        query_url = f'{base_url}/{session_id}/query'
        query_data = {
            "endpointId": 'predefined-openai-gpt4o',
            "query": "Put your query here",
            "pluginIds": ["plugin-1712327325", "plugin-1713962163", "plugin-1717416016"],
            "responseMode": "sync"
        }

        query_response = requests.post(query_url, headers=headers, json=query_data)

        if query_response.status_code == 200:
            result = query_response.json()
            print(result)
        else:
            print('Error:', query_response.status_code, query_response.text)
    else:
        print('Error: Session ID not found in response.')
else:
    print('Error:', response.status_code, response.text)
