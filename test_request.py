import requests

url = 'http://localhost:8000/send_email'  # Update the URL
payload = {
    'to': 'ruslan.00290@gmail.com',
    'subject': 'mf',
    'message': 'fu mf'
}
response = requests.post(url, json=payload)

print(response)
print(response.json())
