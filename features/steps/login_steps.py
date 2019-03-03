from behave import *

use_step_matcher("re")


@given("I am a registered user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I am a registered user')