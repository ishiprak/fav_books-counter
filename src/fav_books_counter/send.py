import requests

# body={}
headers={}
headers["Authorization"] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg2OTE2MDgwLCJqdGkiOiI2YTFjZmMzMjQyZDc0OTUxOGJmNDAyNjZjOTM1OWYyOCIsInVzZXJfaWQiOjEyfQ.iC25FvdFaM2xXlXqPNCCVdudwlFYlvPMbJI5P3Q1Mx8'

r=requests.get('http://127.0.0.1:8000/books/books/refresh', headers=headers)

# r=requests.post('http://127.0.0.1:8000/books/api/token/', data=body)

print(r.text)
