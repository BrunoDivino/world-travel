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

@test('Visitor sees posts')
def _(browser=browser):
    post = PostFactory.create()

    browser.visit(url_for('home.index'))
    browser.links.find_by_text(post.title).click()
    
    assert browser.is_text_present(post.title)
    assert browser.is_text_present(post.text)

@test("Visitor accesses main page and doesn't see posts that aren't published")
def _(browser=browser):
    published_post = PostFactory.create(title='Enjoying a vacation at Salvador')
    not_published_drafts = PostFactory.create_batch(2, published=False)

    browser.visit(url_for('home.index'))
    
    assert browser.is_text_present(published_post.title)
    assert browser.is_text_not_present(not_published_drafts[0].title)
    assert browser.is_text_not_present(not_published_drafts[1].title)
    
@test("Visitor can't see any posts")
def _(browser=browser):
    browser.visit(url_for('home.index'))
    
    assert browser.is_text_present('No post has been found')