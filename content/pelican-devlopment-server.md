Title: How to have a devlopment server locally for Pelican
Date: 2022-10-11
Category: Pelican
Tags: pelican, python, it problems encountered, development
Slug: pelican-devlopment-server
Author: Daniel Muyshond
Summary: How to have a devlopment server running locally with Pelican

# The method using make devserver mentionned on the older Pelican documentation

Simply run the following command at the root of your Pelican project, where the `Makefile` file is located:

```
make devserver
```

This will start a development server on port 8000. You can access it by going to [http://localhost:8000](http://localhost:8000).

You can also specify a different port by running the following command:

```
make devserver PORT=8080
```

It can be useful if you already have a server running on port 8000.

# The method using pelican --listen --autoreload

This method seems more recent and is mentionned on the Pelican documention.

```
pelican --listen --autoreload --port 8181
```
Note : `--port` is optional, the default port is 8000.

## What if local server does not serve static files like CSS?

You might have a problem with the static files like CSS not being served by the local server. This is probably because the `pelicanconf.py` is configured with the same `SITEURL` as the production settings set in `publishconf.py`. You can fix this by changing the `SITEURL` in the `pelicanconf.py` file to `http://localhost:8000` or `http://localhost:8181` depending on the port you are using.

# Conclusion

Beginning with Pelican can be a bit tricky. I hope this article will help you to get started with Pelican.

## References

- [Pelican documentation](https://docs.getpelican.com/en/stable/)
- [Pelican documentation - Quickstart](https://docs.getpelican.com/en/stable/quickstart.html#developing-your-site)
- [Pelican documentation - Site generation](https://docs.getpelican.com/en/stable/publish.html#site-generation)