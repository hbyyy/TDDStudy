import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep
"""


class NewVisitorTest(unittest.TestCase):
    # TODO: clean up database after Functional Testing
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user access the index page
        self.browser.get('http://localhost:8000')
        self.assertIn(
            'To-Do lists',
            self.browser.title
        )

        # page title and header text is To-Do lists
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(
            'To-Do lists',
            header_text
        )

        # User can make to-do item on home page
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # types 'Buy peacock feathers' into a text box
        input_box.send_keys('Buy peacock feathers')

        # when user hits enter, add to-do item, and page immediately update, and input_box text erase
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 2nd to-do item input
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # check the table has 1st and 2nd items
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # '1: Buy peacock feathers' must be in the to-do list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
