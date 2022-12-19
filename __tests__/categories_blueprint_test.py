from ward import test
from flask import url_for

from __tests__.fixtures import browser
from __tests__.factories.post_factory import PostFactory
from app.models import Category


@test('User register category', tags=['categories'])
def _(browser=browser):
    browser.visit(url_for('home.index'))
    browser.find_by_text('Register category').click()
    browser.fill('name', 'Europe')
    browser.find_by_value('Save').click()


    assert browser.url == url_for('home.index')
    assert Category.query.first().name == 'Europe'
    assert Category.query.count() == 1

