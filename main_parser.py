from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException

from config import USER_AGENT
from helper import Helper


class MainParser(Helper):
    def __init__(self, url_playlist=''):
        # Initialize Firefox options
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference("general.useragent.override",
                                    USER_AGENT)  # Set custom user agent to avoid detection as a bot
        self.options.set_preference("dom.webdriver.enabled", False)  # Disable WebDriver detection
        self.options.set_preference("intl.accept_languages", 'en-us')  # Set language WebDriver
        self.options.set_preference("dom.webnotifications.enabled", False)  # Disable WebDriver notifications

        self.service = Service(executable_path='GeckoDriver/geckodriver.exe')  # Path to WebDriver

        self.driver = webdriver.Firefox(service=self.service,
                                        options=self.options)  # Create a new instance of the Firefox WebDriver with the

        self.url_playlist = url_playlist
        self.get_video_link()

    def xpath_exists(self, xpath):
        """Checks if an element with the given XPath exists on the page.

        Args:
            xpath (str): The XPath of the element to check.

        Returns:
            bool: True if the element exists, False otherwise.
        """
        try:
            # Attempt to find the element by XPath
            self.driver.find_element(By.XPATH, xpath)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def id_exists(self, element_id):
        """Checks if an element with the given ID exists on the page.

        Args:
            element_id (str): The ID of the element to check.

        Returns:
            bool: True if the element exists, False otherwise.
        """
        try:
            # Attempt to find the element by XPath
            self.driver.find_element(By.ID, element_id)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def class_exists(self, class_name):
        """Checks if an element with the given class name exists on the page.

        Args:
            class_name (str): The class name of the element to check.

        Returns:
            bool: True if the element exists, False otherwise.
        """
        try:
            # Attempt to find the element by class name
            self.driver.find_element(By.CLASS_NAME, class_name)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def send_by_url(self, url):
        """
        Navigates to the specified URL using the web driver.

        Args:
            url (str): The URL to navigate to.

        Raises:
            WebDriverException: If there is an issue with navigating to the URL.
        """
        # Use the web driver to open the specified URL
        self.driver.get(url=url)

    def get_title_playlist(self):
        # Find the outer element by class name
        outer_element = self.driver.find_element(By.CLASS_NAME, 'dynamic-text-view-model-wiz__h1')

        # Find the nested 'span' element and get the text
        author = self.driver.find_element(By.CLASS_NAME, 'yt-avatar-stack-view-model-wiz').get_attribute('aria-label')
        author = author.split('by')[1].strip()

        title_playlist = outer_element.find_element(By.TAG_NAME, 'span').get_property('innerHTML')
        title_playlist = title_playlist.replace(' ', '_')
        # return folder name
        return f'{author}_{title_playlist}'

    def get_video_link(self):
        self.send_by_url(url=self.url_playlist)
        self.driver.implicitly_wait(5)

        self.create_directory(name_directory=self.get_title_playlist())

        try:
            for i in range(1, 4):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            video_list = [video.get_attribute('href') for video in self.driver.find_element(By.ID, 'contents').find_elements(By.TAG_NAME, 'a') if 'iAQB' in video.get_attribute('href')]

            self.create_file_from_list(
                filename=f'{self.get_title_playlist()}/link_video.txt',
                data_list=video_list
            )
            self.remove_duplicate(
                default=f'{self.get_title_playlist()}/link_video.txt',
                sorted_filename=f'{self.get_title_playlist()}/sorted_link_video.txt',
            )

        except NoSuchElementException as ex:
            print(ex)

        self.close_driver()


    def close_driver(self):
        self.driver.close()
        self.driver.quit()


def main():
    return MainParser(url_playlist='https://www.youtube.com/playlist?list=PLPFzKsPt50V8azAzY0Sg2go23AL9nuAAF')


if __name__ == '__main__':
    main()