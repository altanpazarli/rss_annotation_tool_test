from behave import *
from features.steps.account_creation_login_steps import *
import time


@given("the registered user logged in")
def user_logged_in(context):
    user_on_login_page(context)
    user_fills_valid_credentials(context)
    user_clicks_login_button(context)


@when("the user clicks new feed button")
def user_clicks_new_feed_button(context):
    context.web.open("http://localhost:8000/feeds/new/")
    new_feed_form = context.web.find_by_id("id_feed_url")
    new_feed_form.send_keys("http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    user_clicks_submit_button(context)


@then("the user should see added RSS")
def user_sees_rss_content(context):
    # TODO refactor below css selector of rss url
    feed_url = context.web.find_by_css(
        "body > div:nth-child(4) > div:nth-child(1) > div.col-md-8 > dl > dd:nth-child(4)").text
    assert feed_url == "http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"


@given("the user on feeds page")
def user_on_feeds_page(context):
    context.web.open("http://localhost:8000/feeds/")


@then("the user should be able to see feeds")
def user_sees_feeds(context):
    # TODO refactor below css selector of feeds
    feeds = context.web.find_list_by_css("body > div:nth-child(4) > div > table > tbody > tr")
    assert len(feeds) >= 2
