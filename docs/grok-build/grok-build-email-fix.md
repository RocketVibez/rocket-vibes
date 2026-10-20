# Rocket Vibez — Grok Build paste: fix broken emails on live policy pages

Paste into Grok Build for https://rocketvibez.grok.me

> On every page of the Rocket Vibez site, find every instance of the placeholder email `[email.com]` (including in shipping, returns, privacy, and terms) and replace it with `therocketvibez@gmail.com`.
>
> Also on `/contact`, replace `We usually reply within: [X] business days` with `We usually reply within: 2 business days` (unless a different number is already set correctly).
>
> Do not invent shipping times, regions, refund rules, legal names, analytics tools, or other bracketed decisions. Leave those brackets as they are for now.
>
> Keep design, products, prices, and the pre-launch / no-payment behavior unchanged.
>
> After the edit, confirm there is no remaining `[email.com]` string anywhere on the site.

## Why
Live check on Oct 15, 2026 (ET): `/shipping`, `/returns`, `/privacy`, and `/terms` still showed `[email.com]` after the Oct 14 LIVE post on X. Contact already correctly lists therocketvibez@gmail.com.
