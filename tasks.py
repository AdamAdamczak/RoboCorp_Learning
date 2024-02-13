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

    

