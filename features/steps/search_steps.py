from behave import given, when, then
import time

@given('Search Text Box is visible')
def step_impl(context):
    assert context.SearchPage.is_search_text_box_visible()

@when('User enter {searchtext}')
def step_2_2(context,searchtext):
    context.SearchPage.searchtextbox.send_keys(searchtext)
    
    context.SearchPage.submitsearch.click()

@then('show {results} on search page')
def step_2_3(context,results):
    elemtext = context.SearchPage.searchresult.text
    assert elemtext.strip() == results.strip()

@given('Dresses menu option is visible')
def step_3_1(context):
    return context.SearchPage.is_dressesmenu_visible()

@given('User clicks on Dresses menu')
def step_3_2(context):
    context.SearchPage.dressmenu_click()
    time.sleep(2)

@given('Cotton option is visible')
def step_3_3(context):
    assert context.SearchPage.is_cotton_option_link_visible()
    
@when('User selects Cotton option')
def step_3_4(context):
    context.SearchPage.cotton_option_click()
    time.sleep(3)

@then('show filtered {results} on Dresses page')
def step_3_5(context,results):
    context.browser.implicitly_wait(5)
    assert results == context.SearchPage.searchresults_dress_text()