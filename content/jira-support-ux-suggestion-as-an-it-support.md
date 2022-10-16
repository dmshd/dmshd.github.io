Title: How I improved my understanding time of a client's problems in Jira
Date: 2022-10-11
Category: UX/UI
Tags: UX, UI, Jira, support, IT, ticketing, ticket, problem, understanding, client, user, user experience, user interface
Author: Daniel Muyshond
Summary: I injected my own CSS code snippet in the Jira support page to improve my understanding time of a client's problems.
Lang: en
Translation: false


## The problem is it's sometimes hard to understand the problem in a support ticket

Clients are not always clear in their support tickets, and it is hard to understand what they are talking about.
Treating a lot of tickets and reading them with the attention they deserve can be a time and energy consuming task.

## The solution is to inject my own CSS code snippet in the Jira support page

I injected my own CSS code snippet in the Jira support page to improve my understanding time of a client's problems.

The effect I'm bringing here is a bit reminiscent of the native "reader" modes of browsers that allow you to get rid of all the visual superfluity to offer only the content to be read, presented in a more optimal way.

```css
.user-content-block {
    font-weight: bold;
    font-size: 19px;
    width: 50%;
    margin: auto;
}
```

### How to inject CSS on any page

You can inject CSS on any page using browsers extensions.
When I got this idea, I was using Firefox, so I used the [Stylus](https://addons.mozilla.org/en-US/firefox/addon/styl-us/) extension.

## Conclusion

Because when I'm reading a support ticket, I'm not interested in the visual superfluity of the page, I'm interested in the content of the ticket.
Improving the readability of the ticket is a way for me to consume less energy and time to understand the problem.
If it does that for me, it will probably do that for others too.

Applying this principle to a whole organisation can certainly have a positive impact on the productivity of the support team.