import requests
from bs4 import BeautifulSoup

from letter import write_letter

def get_url():
    # Get's the website URL
    link = input("Enter job listing URL: ")
    find_job_info(link)

def find_job_info(link):
    # Scrapes the page to get the company name and job title
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    job_title = soup.select(".jobsearch-JobInfoHeader-title")[0].get_text()
    company_name = soup.select(".jobsearch-InlineCompanyRating div")[0].get_text()

    write_letter(job_title, company_name)

def main():
    get_url()

main()