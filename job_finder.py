from bs4 import BeautifulSoup
from python_functions import common_data
import requests
import time

unfamiliar_skills_list = []
print('Put some skills that you are not familiar with: ')

while True:
    unfamiliar_skill = input('>')
    if unfamiliar_skill != 'end' :
        unfamiliar_skills_list.append(unfamiliar_skill)
        continue
    else:
        break


unfamiliar_skills_list = [x.lower() for x in unfamiliar_skills_list]
print(f'Filtering out {str(unfamiliar_skills_list)}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '').replace('\r', '').replace('\n', '').replace('"', '')
            more_info = job.header.h2.a['href']
            skills_list = skills.split(',')
            skills_list = [x.lower() for x in skills_list]

            if common_data(unfamiliar_skills_list, skills_list):
                continue
            else:
                with open(f'posts/{index}.text', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info.strip()}\n")
                print(f'File Saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

