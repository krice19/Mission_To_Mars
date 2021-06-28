
# Import dependencies
from bs4.builder import TreeBuilder
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    #initiate headless driver for deplyment     
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph  = mars_news(browser)

    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        hem_image_urls: {"title": title, "Img Url": full_img_url}

    }


    browser.quit()

    return data


def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)


    # convert brwoser html to a soup object 
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # use parent element to find the first tag and save as  news title
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # use parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None
    

    return news_title, news_p


## Find Space image
def featured_image(browser):
    
    #visit the url
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    #find and click the full image button
    full_image_elem = browser.find_by_tag("button")[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    #add try and except for errorr handling
    try:
        #find relative image url
        img_url_rel = img_soup.find("img", class_="fancybox-image").get("src")
    
    except AttributeError:
        return None
    
    #create absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    

    return img_url

## mars facts

def mars_facts():

    try: 
    # use read_html to scrape the facts table into a data frame       
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None
    
    # assign columns and index
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    
    
    return df.to_html()


def hem_images(browser):

    url = 'https://marshemispheres.com/'
    browser.visit(url)

    main_url = 'https://marshemispheres.com/'

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    html = browser.html
    title_soup = soup(html, 'html.parser')

    try: 
        items = title_soup.find_all("div", class_="item")

        for i in items:
            
            title = i.find('h3').text
            
            url_to_pic = i.find("a", class_="itemLink product-item")["href"]

            browser.visit(main_url + url_to_pic)

            html_image = browser.html
            
            img_soup = soup(html_image, "html.parser")

            img_url = img_soup.find("img", class_="wide-image")["src"]

            full_img_url = (main_url + img_url)
    
    except BaseException:
        return None
    
    hemisphere_image_urls.append({"title": title, "Img URL": full_img_url})

if __name__ == "__main__":
    print(scrape_all()
    
    )









