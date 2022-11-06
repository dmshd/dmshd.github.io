Title: How to verify domain to use Google Search Console
Date: 2022-11-06 16:55
Tags: seo, google search console, TXT record, domain verification, add website to google search console, article in english
Slug: how-to-verify-domain-to-use-google-search-console
Author: Daniel Muyshond
Summary: How to verify domain to use Google Search Console
Status: Published
Lang: en
Translation: false
Category: General Development Tricks

## Add website to Google Search Console

Once you're logged with your Google account, go to [Google Search Console](https://search.google.com/search-console/about) and click on "Add Property".

## Verify domain with TXT record

They will ask you to put a TXT record in your DNS zone file. You can do this in your hosting control panel. You can also do this in your domain registrar control panel. If you don't know how to do this, you can ask your hosting provider or domain registrar to do this for you.

The TXT record should look like this:
```
google-site-verification=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

I personnaly did this with OVHCloud. I had to go to the "DNS zone" section of my domain and add a new record. I had to choose "TXT" as type and put the value in the "Value" field.
Once I did this, they told that had to wait a few minutes for the DNS to be updated and that it can take 24h for DNS propagation.

I did not wait and checked just after a few seconds and it was already working. I had to go back to Google Search Console and click on "Verify".

## Conclusion

Verifying your domain with Google Search Console and OVHCloud is very easy. It took me less than 5 minutes to do this. I hope this article will help you to do this too.