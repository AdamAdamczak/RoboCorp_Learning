from robocorp.tasks import task
from robocorp import browser
@task
def my_first_task():
    """My first task."""
    open_the_internet()
    
def open_the_internet():
    """Navigate to the internet."""
    browser.configure(
        slowmo=100,
    )
    browser.goto("https://robotsparebinindustries.com/")
    page = login()
    fill_form(page)

def login():
    """Login to the internet."""
    page = browser.page()
    page.fill('#username', 'maria')
    page.fill('#password', 'thoushallnotpass')
    page.click("button:text('Log in')")
    return page
def fill_form(page):
    """Fill out a form."""
    page.fill('#firstname', 'Maria')
    page.fill('#lastname', 'Smith')
    page.select_option('#salestarget','65000')
    page.fill('#salesresult', '123')
    
    page.click("button:text('Submit')")
    return page