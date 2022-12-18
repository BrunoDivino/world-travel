from ward import test
from splinter import Browser

from app import create_app

@test('main page must be online')
def _():
    app = create_app()
    browser = Browser('flask', app=app)

    browser.visit('/')
    assert browser.is_text_present('Hello Flask')
    