import time
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os
import logging

class JobScraper:
    def __init__(self, base_url, output_dir="job_posts"):
        """Initialize the job scraper with configuration."""
        self.base_url = base_url
        self.output_dir = output_dir
        self.setup_logging()
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def setup_logging(self):
        """Set up logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('job_scraper.log'),
                logging.StreamHandler()
            ]
        )

    def get_jobs(self):
        """Fetch and parse the job listings page."""
        try:
            response = requests.get(self.base_url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, "lxml")
        except requests.RequestException as e:
            logging.error(f"Error fetching jobs: {e}")
            return None

    def parse_job(self, job):
        """Parse individual job listing and extract relevant information."""
        try:
            return {
                'company_name': job.find("h3", class_="joblist-comp-name").text.strip(),
                'skills': job.find("span", class_="srp-skills").text.strip(),
                'more_info': job.header.h2.a["href"],
                'published_date': job.find("span", class_="sim-posted").span.text.strip()
            }
        except AttributeError as e:
            logging.error(f"Error parsing job listing: {e}")
            return None

    def save_job(self, job_info, index):
        """Save job information to a file."""
        try:
            filepath = os.path.join(self.output_dir, f"job_{index}_{datetime.now().strftime('%Y%m%d')}.txt")
            with open(filepath, "w", encoding='utf-8') as file:
                for key, value in job_info.items():
                    file.write(f"{key.replace('_', ' ').title()}: {value}\n")
            logging.info(f"Saved job listing to {filepath}")
            return True
        except IOError as e:
            logging.error(f"Error saving job listing: {e}")
            return False

    def find_jobs(self, unfamiliar_skill):
        """Main method to find and filter jobs."""
        soup = self.get_jobs()
        if not soup:
            return

        jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
        logging.info(f"Found {len(jobs)} total job listings")

        filtered_count = 0
        for index, job in enumerate(jobs):
            job_info = self.parse_job(job)
            if not job_info:
                continue

            if "few" in job_info['published_date'] and unfamiliar_skill.lower() not in job_info['skills'].lower():
                if self.save_job(job_info, index):
                    filtered_count += 1

        logging.info(f"Filtered and saved {filtered_count} job listings")

def main():
    scraper = JobScraper(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    )
    
    print("Enter skills you want to filter out (comma-separated):")
    unfamiliar_skills = input("> ").strip()
    
    while True:
        try:
            scraper.find_jobs(unfamiliar_skills)
            wait_time = 600  # 10 minutes
            logging.info(f"Waiting {wait_time} seconds before next scan...")
            time.sleep(wait_time)
        except KeyboardInterrupt:
            logging.info("Scraper stopped by user")
            break
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            time.sleep(60)  # Wait a minute before retrying

if __name__ == "__main__":
    main()