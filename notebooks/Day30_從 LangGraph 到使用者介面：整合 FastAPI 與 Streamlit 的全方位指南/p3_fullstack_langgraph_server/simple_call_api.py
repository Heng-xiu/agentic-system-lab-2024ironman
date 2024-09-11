import requests
import json

API_URL = "http://localhost:8000/websearch/invoke"
inputs = {"input": "2024 鐵人賽關於 LangGraph 文章？"}
response = requests.post(API_URL, json=inputs)
result = response.json()
print(result['output'])
