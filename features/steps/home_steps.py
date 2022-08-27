from behave import given, when, then

@when('User visits "{browserpage}"')  
def step_impl(context,browserpage): 
   context.browser.get(browserpage)  

@then('it should have a title {browsertitle}')  
def step_impl(context,browsertitle):  
    assert context.browser.title == browsertitle
