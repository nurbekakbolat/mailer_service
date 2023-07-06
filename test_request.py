import requests

url = 'http://localhost:8000/send_email'  # Update the URL
payload = {
    'to': '',
    'subject': 'zxc',
    'message': 'zxc'
}
response = requests.post(url, json=payload)

print(response)
print(response.json())
