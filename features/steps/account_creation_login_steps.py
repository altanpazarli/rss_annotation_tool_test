from behave import *

valid_username = "validusername12"
valid_password = "newuser011"
invalid_username = "inval!dusername"
invalid_password = "p$W0rD"

signup_page = "http://localhost:8000/accounts/register/"
login_page = "http://localhost:8000/accounts/login/"
feeds_page = "http://localhost:8000/feeds/"


@given("the user is on the signup page")
def user_on_signup_page(context):
    context.web.open(signup_page)


@when("the user fills related forms")
def user_fills_related_forms(context):
    context.web.find_by_id("id_username").send_keys(valid_username)
    context.web.find_by_id("id_password1").send_keys(valid_password)
    context.web.find_by_id("id_password2").send_keys(valid_password)


@step("the user fills related forms with invalid data")
def user_fills_invalid_data(context):
    context.web.find_by_id("id_username").send_keys(invalid_username)
    context.web.find_by_id("id_password1").send_keys(invalid_password)
    context.web.find_by_id("id_password2").send_keys(invalid_password)


@step("the user clicks signup button")
def user_clicks_submit_button(context):
    context.web.find_by_id("submit-id-submit").click()


@step("the user clicks login button")
def user_clicks_login_button(context):
    context.web.find_by_css(".btn.btn-success.btn-sm").click()


@then("the user should be redirected to feeds page")
def user_redirected_to_feed(context):
    current_url = context.web.current_url()
    page_url: object = "http://localhost:8000/feeds/"
    assert current_url == page_url


@step("the user should see welcome message")
def user_sees_welcome_message(context):
    welcome_message_text = context.web.find_by_css(".alert.alert-success").text
    assert welcome_message_text == "Great success! Enjoy :)"


@given("the registered user on the login page")
def user_on_login_page(context):
    context.web.open(login_page)


@when("the user fills valid credentials")
def user_fills_valid_credentials(context):
    context.web.find_by_id("id_username").send_keys(valid_username)
    context.web.find_by_id("id_password").send_keys(valid_password)


@when("the user fills invalid credentials")
def user_fills_invalid_credentials(context):
    context.web.find_by_id("id_username").send_keys(valid_username)
    context.web.find_by_id("id_password").send_keys(invalid_password)


@then("the user should see my feeds button")
def user_sees_my_feeds(context):
    my_feed_button = context.web.find_by_css("a[href='/feeds/my/']")
    assert my_feed_button.is_displayed() == True


@then("the user should see wrong credentials warning")
def user_sees_wrong_credentials(context):
    wrong_credentials_warning = context.web.find_by_css(".alert.alert-block.alert-danger")
    assert wrong_credentials_warning.is_displayed() == True


@then("the user should see enter valid username warning")
def user_sees_enter_valid_username_warning(context):
    valid_username_warning = context.web.find_by_id("error_1_id_username")
    assert valid_username_warning.is_displayed() == True


@step("the user should see password is too short warning")
def user_sees_enter_valid_password_warning(context):
    password_is_too_short_warning = context.web.find_by_id("error_1_id_password2")
    assert password_is_too_short_warning.is_displayed() == True
