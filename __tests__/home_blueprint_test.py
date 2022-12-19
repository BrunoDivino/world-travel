from ward import test

from app import db
from app.models import Post
from __tests__.fixtures import browser

@test('main page must be online')
def _(browser=browser):
    browser.visit('/')
    
    assert browser.is_text_present('Hello Flask')

@test('Visitor accesses main page and sees posts')
def _(browser=browser):
    post = Post(title='Enjoying a vacation at Salvador', 
                published=True, 
                text='text...')
    db.session.add(post)
    db.session.commit()

    browser.visit('/')
    
    assert browser.is_text_present('Enjoying a vacation at Salvador')
    