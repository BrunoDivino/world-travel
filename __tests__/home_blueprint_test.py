from ward import test
from faker import Faker
from flask import url_for

from app import db
from app.models import Post
from __tests__.fixtures import browser

@test('main page must be online')
def _(browser=browser):
    browser.visit(url_for('home.index'))
    
    assert browser.is_text_present('Hello Flask')

@test('Visitor accesses main page and sees posts')
def _(browser=browser):
    faker = Faker()
    post = Post(title=faker.paragraph(), 
                published=True, 
                text='text...')
    db.session.add(post)
    db.session.commit()
    browser.visit(url_for('home.index'))
    
    assert browser.is_text_present(post.title)
    
@test("Visitor can't see any posts")
def _(browser=browser):
    browser.visit(url_for('home.index'))
    
    assert browser.is_text_present('No post has been found')