
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


slide_elem.find("div", class_="content_title")


news_title = slide_elem.find("div", class_="content_title").get_text()
news_title


news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
news_p

url = 'https://spaceimages-mars.com'
browser.visit(url)


full_image_elem = browser.find_by_tag("button")[1]
full_image_elem.click()



# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


img_url_rel = img_soup.find("img", class_="fancybox-image").get("src")
img_url_rel


img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df



df.to_html()


# ## Deliverable 1


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

main_url = 'https://marshemispheres.com/'

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
title_soup = soup(html, 'html.parser')

items = title_soup.find_all("div", class_="item")

for i in items:
    
    title = i.find('h3').text
    
    url_to_pic = i.find("a", class_="itemLink product-item")["href"]

    browser.visit(main_url + url_to_pic)

    html_image = browser.html
    
    img_soup = soup(html_image, "html.parser")

    img_url = img_soup.find("img", class_="wide-image")["src"]

    full_img_url = (main_url + img_url)
    
    hemisphere_image_urls.append({"title": title, "Img URL": full_img_url})



# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# 5. Quit the browser
browser.quit()

