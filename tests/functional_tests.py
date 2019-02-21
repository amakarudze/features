""" Functional tests for our features app. """

from splinter import Browser

browser = Browser()
url = 'http://localhost:5000'

# IWS client base has grown rapidly over the past few years and this has made managing client feature requests a huge
# task for IWS. A new app has been developed to help track progress of these feature requests. Angela, a new engineer
# in the implementation division has decided to try it out by visiting its homepage.
browser.visit(url)

# She notices 'Feature Requests App' in the browser title.
assert 'Feature Requests App' in browser.title
header = browser.find_by_tag('h1').first
assert 'Feature Requests App' in header.text

# She is invited to log in.

# She is invited to enter a new feature request.

#
browser.quit()
