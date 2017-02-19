Title: Decentralizing Website with ActivityPub - Notes
Date: 2014-12-18 20:30
Slug: ActivityPub
Status: Draft

# Decentralized websites

GNU Social, Diaspora, Media Goblin, qutter, [mastodon.social](https://github.com/Gargron/mastodon).

Whatever implements Atom feeds, ActivityStreams, Salmon, PubSubHubbub and Webfinger becomes a part of the network.

# Protocols
So there's a bunch of protocols making decentralized websites work.

Here's the ones used by GNU Social and mastodon.social:

- ActivityStreams - (XML), essentially Atom XML feeds of statuses.
- WebFinger - a way to query servers for users they host.
- PubSubHubbub - (PuSH), a way to register your server with a hub that will start pushing updates you want.
- Salmon -  a way to sign activities so they can be verified across servers. Makes federated commenting / liking possible.
