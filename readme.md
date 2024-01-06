# Create virtual environment for python
install virtual env

Open git bash terminal, activate the environment
```
source venv/Scripts/activate
```
Move into the rental scraper and run the mogi_spider and passing the PAGE_NUMBER
```
cd rental_scraper/
scrapy crawl mogi_spider -a crawling_pages=PAGE_NUMBER
```