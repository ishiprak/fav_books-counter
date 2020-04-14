import requests

# body={}
# body['refresh'] = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4Njk5MTMxMywianRpIjoiMGQ4YzYxY2NlM2IxNDBiNmI0NzFlZDM3MTU5N2Y0MjkiLCJ1c2VyX2lkIjoxfQ.zZev08dReAEhwVsTiEGVAWmuMHupTorWutmBD9aCXi8'
# body['password'] = 'sp8434325522ps'

headers={}
headers["Authorization"]='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg2OTA1MjYyLCJqdGkiOiI4ZDU3OTEzNzlkYjY0OTY5ODdlMmMyYTE4ODEyMTY1MCIsInVzZXJfaWQiOjF9.gJKbfyN2O0R0DkXxTzxfH9KwPV4YiDn4g6WJd_lS7Uw'

r=requests.get('http://127.0.0.1:8000/books/books/', headers=headers)
print(r.text)
