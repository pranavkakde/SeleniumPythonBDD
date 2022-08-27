from page_objects import PageElement, PageObject
from allure_commons.types import AttachmentType
import allure

class searchPage(PageObject):
    searchtextbox = PageElement(id_='search_query_top')
    submitsearch = PageElement(name = 'submit_search')
    searchresult = PageElement(xpath ="//*[@id='center_column']/div[1]/div[2]/div[2]")
    searchresult_dress = PageElement(xpath = "//*[@id='center_column']/div[3]/div[2]/div[2]")
    dressesmenu = PageElement(link_text = 'DRESSES')
    cottonoption = PageElement(id_="layered_id_feature_5")
    cottonoptionlink= PageElement(xpath='//*[@id="ul_layered_id_feature_5"]/li[1]/label/a')
    def is_search_text_box_visible(self):
        allure.attach(self.w.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        if self.searchtextbox.is_displayed():
            return True
        else:
            return False
    def is_dressesmenu_visible(self):
        allure.attach(self.w.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        if self.dressesmenu.is_displayed():
            return True
        else:
            return False
    def dressmenu_click(self):
        allure.attach(self.w.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        self.dressesmenu.click()
    def cotton_option_click(self):
        allure.attach(self.w.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        self.cottonoption.click()
    def is_cotton_option_link_visible(self):
        allure.attach(self.w.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        if self.cottonoptionlink.is_displayed():
            return True
        else:
            return False
    def searchresults_dress_text(self):
        allure.attach(self.w.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        return self.searchresult_dress.text
