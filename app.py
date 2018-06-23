# -*- coding: utf-8 -*-

import json
import requests
from datetime import datetime
from pyatom import AtomFeed
from flask import Flask, request, Response, redirect, url_for
from flask_caching import Cache
from config import Config as cfg


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': cfg.cache_type})


@app.route('/')
def index():
    return redirect(url_for('atom'))


@app.route('/feed.atom')
@cache.cached(timeout=cfg.cache_timeout)
def atom():
    feed = AtomFeed(title='Machine Learning and Pattern Recognition - Hypothes.is Feed',
                    feed_url=request.url,
                    url='https://hypothes.is/stream?q=group:%s' % cfg.group,
                    author='Iain Murray')
    r = requests.get('https://hypothes.is/api/search?group=%s' % cfg.group,
                     headers={'Authorization': 'Bearer %s' % cfg.token})
    for row in json.loads(r.text)['rows']:
        feed.add(title=row['document']['title'][0], content=row['text'],
                 content_type='text', author=row['user'], url=row['links']['html'],
                 updated=datetime.strptime(row['updated'][:-13], '%Y-%m-%dT%H:%M:%S'),
                 published=datetime.strptime(row['created'][:-13], '%Y-%m-%dT%H:%M:%S'))
    return Response(feed.to_string(), mimetype='application/atom+xml')


if __name__ == '__main__':
    app.run()
