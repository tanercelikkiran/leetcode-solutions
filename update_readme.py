import requests
import json

url = 'https://leetcode.com/api/problems/all/'
response = requests.get(url)
num_solved = json.loads(response.content.decode('utf-8'))['num_solved']
num_total = json.loads(response.content.decode('utf-8'))['num_total']

# Find the line that contains the number of solved problems and replace it

with open('README.md', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'solved' in line:
            lines[i] = 'I solved {} problem out of {} so far.'.format(num_solved, num_total)