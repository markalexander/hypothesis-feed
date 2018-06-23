# -*- coding: utf-8 -*-

import json
import requests
from datetime import datetime
from pyatom import AtomFeed
from flask import Flask, request, Response, redirect, url_for
from flask_caching import Cache
from config import Config as Config


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': Config.CACHE_TYPE})


@app.route('/')
def index():
    return redirect(url_for('atom'))


@app.route('/feed.atom')
@cache.cached(timeout=Config.CACHE_TIMEOUT)
def atom():
    feed = AtomFeed(title=Config.FEED_TITLE,
                    feed_url=request.url,
                    url='https://hypothes.is/stream?q=group:%s'
                        % Config.HYPOTHESIS_GROUP_ID,
                    author=Config.FEED_AUTHOR)
    r = requests.get('https://hypothes.is/api/search?group=%s'
                     % Config.HYPOTHESIS_GROUP_ID,
                     headers={'Authorization': 'Bearer %s'
                                               % Config.HYPOTHESIS_API_TOKEN})
    for post in json.loads(r.text)['rows']:
        feed.add(title=post['document']['title'][0],
                 content=post['text'],
                 content_type='text',
                 author=post['user'],
                 url=post['links']['html'],
                 updated=datetime.strptime(post['updated'][:-13],
                                           '%Y-%m-%dT%H:%M:%S'),
                 published=datetime.strptime(post['created'][:-13],
                                             '%Y-%m-%dT%H:%M:%S'))
    return Response(feed.to_string(), mimetype='application/atom+xml')


if __name__ == '__main__':
    app.run()
