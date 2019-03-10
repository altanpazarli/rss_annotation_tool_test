from behave import *
import time

valid_username = "validusername04"
valid_password = "newuser04"


@given("the user is on the signup page")
def user_on_signup_page(context):
    context.web.open("http://localhost:8000/accounts/register/")


@when("the user fills related forms")
def user_fills_related_forms(context):
    context.web.find_by_id("id_username").send_keys(valid_username)
    context.web.find_by_id("id_password1").send_keys(valid_password)
    context.web.find_by_id("id_password2").send_keys(valid_password)


@step("the user clicks signup button")
def user_clicks_signup_button(context):
    context.web.find_by_id("submit-id-submit").click()


@then("the user should be redirected to feeds page")
def user_redirected_to_login(context):
    current_url: object = context.web.current_url()
    page_url: object = "http://localhost:8000/feeds/"
    time.sleep(5)
    assert current_url == page_url


@step("the user should see welcome message")
def user_sees_welcome_message(context):
    welcome_message_text = context.web.find_by_css(".alert.alert-success").text
    assert welcome_message_text == "Great success! Enjoy :)"


@given("the registered user on the login page")
def user_on_login_page(context):
    context.web.open("http://localhost:8000/accounts/login/")


@when("the user fills username and password")
def user_fills_username_password(context):
    context.web.find_by_id("id_username").send_keys(valid_username)
    context.web.find_by_id("id_password").send_keys(valid_password)


@then("the user should see my feeds button")
def user_sees_my_feeds(context):
    my_feed_button = context.web.find_by_css("a[href='/feeds/my/']")
    assert my_feed_button.is_displayed() == True