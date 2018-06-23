# -*- coding: utf-8 -*-


class Config:

    # The title of the feed
    FEED_TITLE = 'Some Group Name Here - Hypothes.is Feed'

    # The author of the feed
    FEED_AUTHOR = 'Various'

    # Your hypothes.is API token.
    # Visit https://hypothes.is/account/developer when signed in to generate
    # one
    HYPOTHESIS_API_TOKEN = ''

    # The ID of the group to generate the feed from.
    # You can grab this from various places, e.g. the URL for the group stream.
    HYPOTHESIS_GROUP_ID = ''

    # The type of cache to use in flask-caching
    # I suggest to start with 'simple', which saves to local disk and should
    # work in most cases.  If you have trouble with that, you can turn of the
    # cache by setting this to 'null'.  See the flask-caching docs for more
    # advanced usage
    CACHE_TYPE = 'simple'

    # How long (in seconds) to serve up a cached API response before flushing
    CACHE_TIMEOUT = 600
