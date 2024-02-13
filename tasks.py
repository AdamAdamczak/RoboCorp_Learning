from robocorp.tasks import task
from robocorp import browser
from RPA.HTTP import HTTP
from RPA.Excel.Files import Files

@task
def my_first_task():
    """My first task."""
    open_the_internet()
    
def open_the_internet():
    """Navigate to the internet."""
    # Configure browser settings
    browser.configure(
        slowmo=100,
    )
    # Navigate to the specified URL
    browser.goto("https://robotsparebinindustries.com/")
    # Login to the website
    page = login()
    # Fill the form on the page
    fill_form(page)
    # Download a file from the internet
    get_file('https://robotsparebinindustries.com/SalesData.xlsx')
    # Fill Excel data into the form
    fill_excel_data(page)

def login():
    """Login to the internet."""
    # Get the current page
    page = browser.page()
    # Fill in the username
    page.fill('#username', 'maria')
    # Fill in the password
    page.fill('#password', 'thoushallnotpass')
    # Click the login button
    page.click("button:text('Log in')")
    return page

def fill_form(page):
    """Fill out a form."""
    # Fill in the first name
    page.fill('#firstname', 'Maria')
    # Fill in the last name
    page.fill('#lastname', 'Smith')
    # Select the sales target
    page.select_option('#salestarget', '65000')
    # Fill in the sales result
    page.fill('#salesresult', '123')
    # Click the submit button
    page.click("button:text('Submit')")
    return page

def get_file(url):
    """Download a file from the internet."""
    http = HTTP()
    # Download the file
    http.download(url, overwrite=True)
    
def fill_excel_data(page):
    """Fill Excel data into the form."""
    excel = Files()
    # Open the workbook
    excel.open_workbook('SalesData.xlsx')
    # Read the worksheet as a table
    worksheet = excel.read_worksheet_as_table(header=True)
    # Close the workbook
    excel.close_workbook()
    # Iterate through the rows in the worksheet
    for row in worksheet:
        # Fill and submit the form for each row
        fill_and_submit_form(page, row)
    
def fill_and_submit_form(page, sales_rep):
    """Fill and submit the form with sales representative data."""
    # Fill in the first name
    page.fill("#firstname", sales_rep["First Name"])
    # Fill in the last name
    page.fill("#lastname", sales_rep["Last Name"])
    # Select the sales target
    page.select_option("#salestarget", str(sales_rep["Sales Target"]))
    # Fill in the sales result
    page.fill("#salesresult", str(sales_rep["Sales"]))
    # Click the submit button
    page.click("text=Submit")
