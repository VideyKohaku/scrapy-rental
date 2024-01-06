# scrapy-rental
### Install Python
I assume that you had installed Python on your computer. For installation process, please checkout https://www.python.org/downloads/
### Install Dependencies
First, let's install virtualenv using pip
```
pip install virtualenv
```
Next, to create a virtual environment folder, you can replace venv by your custom folder name
```
virtualenv venv 
```
Then, we can activate the virtual environment.
if you can open gitbash, or you are using MacOS, Linux
```
source venv/bin/activate
```
if you are using Windows, you can open command prompt
```
venv\Scripts\activate.bat
```
Finally, you can install the dependencies for the project without installing them into your global PC
```
pip install -r requirements.txt
```
### How to use it
Right now, I had just modified the mogi_spider to crawl mogi.vn. You can run the spider with the followed commands
```shell
cd rental_scrapper
scrapy crawl mogi_spider -o mogi_rentals_data.csv -a crawling_page=NUMBER_PAGES
```
"-o mogi_rentals_data.csv": This is optional to export the result into csv file.

If you have any problem or you want to contribute anything. Feel free to let me know.
