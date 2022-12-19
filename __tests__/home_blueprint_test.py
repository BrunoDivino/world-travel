from ward import test
from flask import url_for

from __tests__.fixtures import browser
from __tests__.factories.post_factory import PostFactory

@test('main page must be online')
def _(browser=browser):
    browser.visit(url_for('home.index'))
    
    assert browser.is_text_present('Hello Flask')

@test('Visitor accesses main page and sees posts')
def _(browser=browser):
    post = PostFactory.create()

    browser.visit(url_for('home.index'))
    
    assert browser.is_text_present(post.title)
    
@test("Visitor can't see any posts")
def _(browser=browser):
    browser.visit(url_for('home.index'))
    
    assert browser.is_text_present('No post has been found')