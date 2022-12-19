from ward import test
from flask import url_for

from __tests__.fixtures import browser
from app.models import Post


@test('User register post', tags=['posts'])
def _(browser=browser):
    browser.visit(url_for('home.index'))
    browser.find_by_text('Register post').click()
    browser.fill('title', 'Taking a vacation at Salvador city')
    browser.fill('text', 'Just a generic text on a blog')
    browser.check('published')
    browser.find_by_value('Save').click()


    assert browser.url == url_for('home.index')
    assert browser.is_text_present('Post published successfully')
    assert Post.query.first().title == 'Taking a vacation at Salvador city'
    assert Post.query.first().text == 'Just a generic text on a blog'
    assert Post.query.first().published == True
    assert Post.query.count() == 1