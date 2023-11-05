
import scrapy

class LinkedJobsSpider(scrapy.Spider):
    name = "linkedin_jobs"
    api_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=python&location=India&geoId=&trk=public_jobs_jobs-search-bar_search-submit&start=25' 

    def start_requests(self):
        first_job_on_page = 0
        first_url = self.api_url + str(first_job_on_page)
        yield scrapy.Request(url=first_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})


    def parse_job(self, response):
        first_job_on_page = response.meta['first_job_on_page']

        job_item = {}
        jobs = response.css("li")


        num_jobs_returned = len(jobs)
        print("******* Num Jobs Returned *******")
        print(num_jobs_returned)
        print('*****')
        
        for job in jobs:
            job_location = job.css('.job-search-card__location::text').get(default='not-found').strip()

            # Check if the job location contains "United States" or "Canada" and exclude those listings
            if "United States" not in job_location and "Canada" not in job_location:
                job_item['job_title'] = job.css("h3::text").get(default='not-found').strip()
                job_item['job_detail_url'] = job.css(".base-card__full-link::attr(href)").get(default='not-found').strip()
                job_item['job_listed'] = job.css('time::text').get(default='not-found').strip()
                job_item['company_name'] = job.css('h4 a::text').get(default='not-found').strip()
                job_item['company_link'] = job.css('h4 a::attr(href)').get(default='not-found')
                job_item['company_location'] = job_location

                yield job_item


                            #### REQUEST NEXT PAGE OF JOBS HERE ######
        if num_jobs_returned > 0:
            first_job_on_page = int(first_job_on_page) + 25
            next_url = self.api_url + str(first_job_on_page)
            yield scrapy.Request(url=next_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})
    
