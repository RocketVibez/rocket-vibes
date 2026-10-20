# Rocket Vibez — Grok Build Launch Brief (Pre-Launch, No Payments)

**Site:** https://rocketvibez.grok.me
**Goal:** Make the storefront live and operational as a **pre-launch store**. Visitors can browse, build a cart, and join the launch list. **No payments are taken.**

---

## 1. Instructions for Grok Build (paste this block first)

> You are updating the existing Rocket Vibez storefront at https://rocketvibez.grok.me.
>
> **Keep:**
> - Every existing page, product, size option, color option (black/white), and the custom AI-print flow. Prices change per item 5 below.
> - The current design system: dark theme, orange accent, bold display font, loud playful tone.
> - The cart. It should keep working exactly as it does now.
> - The "under construction" status for Caps, Totes, Pins, Stickers, and Socks.
>
> **Do not:**
> - Add a payment processor, card fields, or any payment step. Checkout stays payment-free.
> - Mention or link to any other company or brand. Rocket Vibez stands alone.
> - Invent an email address, phone number, street address, or delivery times. Use the bracketed placeholders exactly as written (e.g. `[X–Y business days]`). Bentley will fill them in. The contact email is therocketvibez@gmail.com.
>
> **Add:**
> 1. Six new pages using the copy in Section 2: `/about`, `/contact`, `/shipping`, `/returns`, `/privacy`, `/terms`. All six currently return 404. Use the existing page layout, header, and footer.
> 2. An updated footer (Section 3).
> 3. A pre-launch "Join the launch list" flow that replaces "Place order" (Section 4).
> 4. A slim banner across the whole site: **"Launching soon — join the list for first dibs."** (Section 4).
> 5. New prices everywhere they appear (product cards, product pages, Kids/Teen/Grown toggles, set offers, custom builder, cart, homepage copy such as "from $18.00"):
>
> | Item | Old | New |
> |---|---|---|
> | Kids tee (4–14) | $18 | **$22** |
> | Teen tee (S–XL) | $22 | **$26** |
> | Grown tee (XS–3X) | $26 | **$30** |
> | Custom print fee | +$10 | **+$10** (kids custom $32, teen $36, grown $40) |
> | Kids hoodie | $36 | **$42** |
> | Teen and grown hoodie | — | **$48** |
> | Tee + hoodie set ($6 off) | $48 kids | **$58 kids / $68 teen / $72 grown** |
> | Free shipping minimum | over $60 | **over $55** ($8 flat below that) |
>
> Update homepage lines like "Kids sizes 4–14 from $18.00. Teen sizes S–XL from $22.00." to "from $22.00" and "from $26.00".
>
> Caps, totes, pins, stickers, and socks stay under construction. You may show their planned prices as "coming soon": cap $28, tote $22, enamel pin $10, sticker $4 (3 for $10), socks $14. They are not addable to cart yet.
>
> Keep the brand voice short, confident, loud, and kid-safe. Make sure everything works on mobile.

---

## 2. Page Copy (final, paste-ready)

Placeholders in `[BRACKETS]` must stay visible as written until Bentley replaces them. Show them as plain text, and don't style them as links.

---

### 2.1 `/about` — About

**Page title (SEO):** About Rocket Vibez — Clothes for the Loud Years

# Clothes for the loud years.

Rocket Vibez makes graphic tees and hoodies for kids who are too big for quiet. And for teens who never were quiet. And for grown-ups who still aren't.

**Big graphics. Bold colors. Zero beige.**

### What we make
- **Kids (sizes 4–14):** Tees, hoodies, and the tee + hoodie set. Made for climbing, spilling, and showing off.
- **Teen (S–XL):** Tees with attitude. Fewer cartoons, same volume.
- **Grown (XS–3X):** Because loud doesn't stop at 18.
- **Custom AI prints:** Dream it up, we print it. Any idea, your shirt.

Every piece comes in **black or white**. Your design does the talking.

### Made when you order it
We don't sit on piles of shirts. Every Rocket Vibez piece is printed **on demand**, so it's made just for you after you order. Less waste, more vibes.

### Coming soon
Caps, totes, pins, stickers, and socks are on the launch pad. 🚀 Stay tuned.

**[Button: Shop the drop →]** (links to the shop/home page)

---

### 2.2 `/contact` — Contact

**Page title (SEO):** Contact Rocket Vibez

# Say hey. Loudly.

Question about sizing? A custom print idea? Something not right with your order? Drop us a line and a real human will get back to you.

**Email:** therocketvibez@gmail.com
**We usually reply within:** [X] business days

### Contact form

| Field | Type | Required |
|---|---|---|
| Name | Text | Yes |
| Email | Email (validate format) | Yes |
| Order number | Text | No (helper text: "If it's about an order") |
| What's up? | Dropdown: Sizing · Custom print · My order · Returns & exchanges · Something else | Yes |
| Message | Textarea | Yes |

- **Above the submit button:** "Under 13? Ask a parent or guardian to reach out for you."
- **Submit button:** **Send it 🚀**
- **On success:** "Got it! We'll get back to you soon."
- **On error:** "Whoops, that didn't launch. Try again, or email us at therocketvibez@gmail.com."

**For Grok Build:** Store each form submission (name, email, order number, topic, message, timestamp) where Bentley can view it, and email it to therocketvibez@gmail.com once that address is set. Add basic spam protection, such as a honeypot field or rate limit. No street address, no phone number.

---

### 2.3 `/shipping` — Shipping

**Page title (SEO):** Shipping — Rocket Vibez

# Shipping: the short version.

- **$8 flat-rate shipping** on every order.
- **FREE shipping on orders over $55.**
- Ships to: [SHIPPING REGIONS — e.g., all 50 US states]

### Made to order (that's the point)
Every Rocket Vibez piece is printed **on demand**, so your shirt is made just for you after you order. Here's the timeline:

| Step | How long |
|---|---|
| Printing & packing | [X–Y business days] |
| Shipping to you | [X–Y business days] |
| **Total, door to door** | **About [X–Y business days]** |

Custom AI prints may need [X] extra business day(s) for us to check and prep your design.

### Tracking
When your order ships, we'll email you a tracking link at the address you used to order.

### Heads up
- Business days are Monday–Friday and don't include holidays.
- Big sales and holidays can slow things down. We'll post any delays here.
- Double-check your address at checkout. If a package comes back to us because the address was wrong, [ADDRESS-ERROR POLICY — e.g., we'll reship once you cover the new shipping cost].
- Package lost or stuck? Email therocketvibez@gmail.com and we'll sort it out.

---

### 2.4 `/returns` — Returns & Exchanges

**Page title (SEO):** Returns & Exchanges — Rocket Vibez

# Returns & exchanges.

Every piece is made just for you after you order, so our policy works a little differently from a regular store. Here's the deal.

### Wrong size? We'll swap it.
Kids grow. It happens. If your size is off, we'll exchange it for a different size of the same design.
- Ask within **[X] days** of delivery.
- The item has to be unworn, unwashed, and in its original condition.
- **[EXCHANGE SHIPPING DECISION — e.g., "You cover return shipping; we ship the new size free." OR "Exchanges ship free, both ways."]**
- One size exchange per item.
- Custom AI prints: **[CUSTOM EXCHANGE DECISION — e.g., "eligible for one size exchange" OR "final sale"]**

Not sure about sizing? Check the size chart on each product page before you order.

### Misprint or damaged? That's on us.
If your order shows up misprinted, damaged, defective, or just plain wrong, we'll send a replacement **free**.
- Email therocketvibez@gmail.com within **[X] days** of delivery.
- Include your order number and a photo of the problem.
- No need to send it back unless we ask.

### What we can't take back
Because everything is made to order, we **don't accept returns for refunds** for changed minds, wrong color picks, or "I just didn't love it." **[REFUND POLICY DECISION — confirm, or replace with your chosen policy, e.g. store credit.]**

### How to start
Email therocketvibez@gmail.com with:
1. Your order number
2. What's wrong (size, misprint, damage)
3. A photo (for misprints or damage)

We'll reply within [X] business days with next steps.

---

### 2.5 `/privacy` — Privacy Policy

> ⚠️ **DRAFT — NEEDS LEGAL REVIEW BEFORE LAUNCH.** This is a plain-English starter template, not legal advice. Have a qualified attorney review it for COPPA, state privacy laws (e.g., California), and your actual vendors before you take payments or run ads. **For Grok Build:** do not show this warning box on the live site. Show the policy text only.

**Page title (SEO):** Privacy Policy — Rocket Vibez

# Privacy Policy

**Last updated:** [DATE]

Rocket Vibez ("we," "us," "our") runs the website at [DOMAIN] (the "Site"). This policy explains what information we collect, how we use it, and the choices you have. We wrote it in plain English on purpose.

#### 1. Who this Site is for
We sell clothes for kids, but **this Site is for parents, guardians, and teens 13 and older.** We do not knowingly collect personal information from children under 13. If you're under 13, please ask a parent or guardian to shop or contact us for you.

If you believe a child under 13 has given us personal information, email therocketvibez@gmail.com and we'll delete it promptly. This is how we follow the Children's Online Privacy Protection Act (COPPA).

#### 2. What we collect
- **Info you give us:** your name and email when you join the launch list, use the contact form, or place an order. When we start shipping orders, this will also include your shipping address and order details.
- **Custom print ideas:** the text prompts and designs you submit for custom AI prints.
- **Cart contents:** items you add to your cart. Right now, these are saved on your own device.
- **Automatic info:** basic technical data such as browser type, device, pages viewed, and approximate location, collected through cookies or similar tools. [LIST ANALYTICS TOOLS, IF ANY]
- **Payment info:** we don't take payments yet. When we do, payments will be handled by a third-party payment processor, and we won't store full card numbers.

#### 3. How we use it
- To run the launch list and email you when the drop goes live
- To answer your messages
- To make, ship, and support your orders (once orders open)
- To make and check your custom prints
- To keep the Site working, safe, and improving
- To send updates or promos, but only if you signed up for them. You can unsubscribe anytime.

#### 4. Who we share it with
**We don't sell your personal information.** We share it only with service providers who help us run the shop, such as our print-on-demand fulfillment partner, website host, email provider, shipping carriers, and (later) payment processor. They may use it only to provide services to us. We may also share information if the law requires it, or to protect our rights and safety.

[LIST KEY SERVICE PROVIDERS — TO BE CONFIRMED]

#### 5. Cookies
We use cookies and similar tools to keep your cart working and to understand how the Site is used. You can block cookies in your browser, but parts of the Site may not work.

#### 6. Your choices and rights
- **Unsubscribe** from emails using the link in any email.
- **Ask us** to see, correct, or delete your personal information by emailing therocketvibez@gmail.com.
- Depending on where you live (for example, California), you may have extra rights under state law. Contact us and we'll help.

#### 7. How long we keep it
We keep personal information only as long as we need it for the purposes above, or as long as the law requires. [RETENTION PERIOD — TO BE CONFIRMED]

#### 8. Security
We take reasonable steps to protect your information. No website is 100% secure, but we take this seriously.

#### 9. Changes
If we update this policy, we'll change the "Last updated" date above. Big changes will get a clear notice on the Site.

#### 10. Contact
Questions? Email therocketvibez@gmail.com.
[BUSINESS LEGAL NAME AND MAILING ADDRESS — TO BE ADDED IF REQUIRED]

---

### 2.6 `/terms` — Terms of Service

> ⚠️ **DRAFT — NEEDS LEGAL REVIEW BEFORE LAUNCH.** This is a plain-English starter template, not legal advice. Have a qualified attorney review it, especially the sections on custom content, liability, and governing law. **For Grok Build:** do not show this warning box on the live site. Show the terms text only.

**Page title (SEO):** Terms of Service — Rocket Vibez

# Terms of Service

**Last updated:** [DATE]

Welcome to Rocket Vibez. These Terms of Service ("Terms") apply when you use [DOMAIN] (the "Site") and when you buy from us. By using the Site, you agree to these Terms.

#### 1. Who can use the Site
You must be **at least 13** to use the Site. You must be **18 or older, or have a parent or guardian's permission and involvement**, to place an order. Kids under 13 should have a parent or guardian shop for them.

#### 2. Pre-launch
Right now the Site is in **pre-launch**. Joining the launch list or "reserving" a cart **is not a purchase.** No payment is taken, and nothing is guaranteed to be held for you. We'll email you when orders open.

#### 3. Products and pricing
- Prices are in US dollars and are listed on the Site. We may change prices, products, or availability at any time before you place an order.
- Colors on screen can look a little different from the real thing.
- Every item is printed on demand, so it's made after you order.
- We do our best to keep the Site accurate. If we make a pricing or listing mistake, we may cancel affected orders and tell you why.

#### 4. Orders, shipping, and returns
When ordering opens, our [Shipping](/shipping) and [Returns & Exchanges](/returns) policies apply and are part of these Terms.

#### 5. Custom AI prints
When you submit a prompt, text, or image for a custom print:
- You're responsible for what you submit. You confirm you have the right to use it.
- **Don't submit** anything hateful, violent, sexual, harassing, illegal, or not kid-friendly, or anything that uses someone else's trademark, copyrighted character, logo, or a real person's likeness without permission.
- We may review, edit, or refuse any custom design for any reason. If we refuse a design after you've paid, we'll refund that item.
- AI-generated designs can be unpredictable. We'll do our best to match your idea, but results can vary.
- You give us permission to use your submission to make your product. [DECISION: whether Rocket Vibez may show custom designs in marketing. If yes, add "and, with your permission, to show it off."]

#### 6. Our stuff
The Site, the Rocket Vibez name and logo, and our original designs belong to Rocket Vibez. Please don't copy, resell, or reuse them without our written permission.

#### 7. Be cool
Don't misuse the Site. That means no hacking, scraping, spamming, fake orders, or anything illegal.

#### 8. Disclaimers
The Site is provided "as is." We work hard to keep it running smoothly, but we can't promise it will always be available or error-free.

#### 9. Limits on liability
To the fullest extent the law allows, Rocket Vibez isn't liable for indirect or consequential damages. Our total liability for any claim related to a product won't be more than what you paid for that product. Some places don't allow these limits, so they may not apply to you.

#### 10. Governing law
These Terms are governed by the laws of [STATE], USA. [DISPUTE RESOLUTION — TO BE CONFIRMED BY LEGAL COUNSEL]

#### 11. Changes
We may update these Terms. If we do, we'll change the "Last updated" date. Continuing to use the Site after an update means you accept the new Terms.

#### 12. Contact
Questions? Email therocketvibez@gmail.com.

---

## 3. Footer Spec

Apply this footer site-wide and replace the current one. Keep it dark with orange hover/active states, and match the existing fonts.

**Layout:** three link columns on desktop with a Follow row below them. On mobile, stack in this order: Shop, Help, Rocket Vibez, Follow.

| Column | Links |
|---|---|
| **Shop** | Kids · Teen · Grown · Custom · Coming Soon (point these at the existing category pages/anchors) |
| **Help** | Shipping (`/shipping`) · Returns & Exchanges (`/returns`) · Contact (`/contact`) |
| **Rocket Vibez** | About (`/about`) · Privacy Policy (`/privacy`) · Terms of Service (`/terms`) |

**Follow row:**
- **Heading:** "Follow the noise"
- Instagram icon linking to https://www.instagram.com/therocketvibez/
- Facebook icon linking to https://www.facebook.com/share/1E1MuxqBcC/
- TikTok icon linking to https://www.tiktok.com/@therocketvibez
- Until real URLs are added, render each icon with `href="#"` and the bracketed placeholder in a `data-` attribute or code comment, so it's easy to find and swap. Open the real links in a new tab.

**Optional footer email capture** (reuses the launch list): "Get first dibs on the drop." Field: email. Button: **I'm in**

**Bottom line:**
`© 2026 Rocket Vibez. Clothes for the loud years.`

**Do not** add a street address, a phone number, or links to any other company.

---

## 4. Pre-Launch Checkout Change

### 4.1 Site-wide banner
- A slim bar fixed at the very top of every page, above the header.
- Background: orange accent. Text: dark, bold, centered.
- Text: **"Launching soon — join the list for first dibs."**
- Clicking anywhere on the banner opens the launch-list form, or scrolls/links to it.
- Should collapse to one line on mobile. Not dismissible, or dismissible for that session only.

### 4.2 Cart (keep as-is)
- The cart, quantities, sizes, colors, custom options, the subtotal, and the shipping math ($8, or FREE over $55) all stay exactly as they work now.
- Keep a free-shipping nudge if one exists, e.g. "You're $X away from free shipping."

### 4.3 Replace "Place order" with the reserve flow
- On the checkout/preview page, **remove** the "Place order" button and any wording about orders being "saved on your device."
- **Add the heading:** "The drop isn't live yet. Get first dibs."
- **Add the subtext:** "No payment, no commitment. Drop your name and email and we'll ping you the second orders open. Want us to remember your picks? We'll save your cart too."

**Form fields:**

| Field | Type | Required |
|---|---|---|
| First name | Text | Yes |
| Email | Email (validate format) | Yes |
| Save my cart with my spot | Checkbox, checked by default when the cart has items | No |
| Send me Rocket Vibez news and drops | Checkbox, **unchecked** by default | No |

- Small print under the fields: "You must be 13 or older to join. Under 13? Ask a parent or guardian. See our [Privacy Policy](/privacy)."
- **Button:** **Join the launch list**

**On submit:**
- Save the entry with: first name, email, timestamp, marketing opt-in (true/false), and, if the box is checked, the cart contents (product, audience, size, color, custom prompt if any, quantity, line price, and subtotal). Store it where Bentley can view or export it as a CSV.
- Don't create a paid order, and don't collect any payment or address info.
- If the same email signs up twice, update the existing entry instead of duplicating it.
- Keep the cart in the browser after submitting.

**Confirmation (on-page or modal):**
> **You're on the list. 🚀**
> We'll email you when the drop goes live.
> [Button: Keep browsing]

**Error state:** "Hmm, that didn't launch. Check your email and try again."

### 4.4 Other launch-list entry points
- The banner, the optional footer field, and (optionally) the "under construction" items, labeled "Notify me," all use the same list. The banner and footer only collect first name and email, or just email.

---

## 5. Launch-Readiness Checklist (for Bentley)

### ✅ Done in Grok Build (with this brief)
- [ ] `/about`, `/contact`, `/shipping`, `/returns`, `/privacy`, `/terms` pages are live (no more 404s)
- [ ] The footer has all six page links plus Instagram, Facebook, and TikTok links
- [ ] The site-wide "Launching soon" banner is live
- [ ] "Place order" is replaced with "Join the launch list". No payment is taken anywhere.
- [ ] Launch-list entries (with optional cart) are stored and exportable
- [ ] Contact form submissions are stored and viewable
- [ ] Mobile check: banner, cart, form, and footer all work on a phone
- [ ] Test it yourself: join the list, send a contact message, and confirm both show up
- [ ] Search the whole site for leftover `[BRACKETS]` before announcing

### 🟠 Decisions still needed from Bentley
| # | Decision | Where it goes |
|---|---|---|
| 1 | **Contact email**: done, therocketvibez@gmail.com (can move to your own domain later) | Contact, Shipping, Returns, Privacy, Terms, form routing |
| 2 | **Domain**: keep `rocketvibez.grok.me` or connect a custom domain | Privacy & Terms `[DOMAIN]`, email setup |
| 3 | **Socials**: Instagram, Facebook, TikTok live: @therocketvibez + Facebook share link | Footer socials filled |
| 4 | **Print-on-demand partner**: choose one and confirm its production and shipping times | Shipping `[X–Y business days]`, Privacy provider list |
| 5 | **Shipping regions** (US only? International?) | Shipping page |
| 6 | **Return/exchange window** (e.g., 14 or 30 days), who pays exchange shipping, and whether custom prints can be exchanged | Returns page |
| 7 | **Refund stance** (no refunds vs. store credit) | Returns page |
| 8 | **Wrong-address policy** | Shipping page |
| 9 | **Payment provider (later)**: pick one before turning on real checkout, then update Privacy and Terms | Checkout, Privacy §2 |
| 10 | **Legal review** of the Privacy Policy and Terms (COPPA, state privacy law, governing state, dispute terms) | Privacy, Terms |
| 11 | **Business legal name / mailing address** (may be needed for policies and commercial email under CAN-SPAM) | Privacy §10, marketing emails |
| 12 | **Analytics/cookies**: what's actually running on the site | Privacy §2, §5 |
| 13 | **Custom AI print moderation**: who reviews prompts, and what's blocked, especially on kids' items | Terms §5, operations |

### 🔴 Kids' product safety (sizes 12 and under) — required before selling
- [ ] **CPSIA tracking labels**: permanent labels on the garment and packaging (manufacturer/brand, production date and location, batch/run info). Confirm your POD partner can print them, or add them as a neck print or label.
- [ ] **Children's Product Certificate (CPC)**, based on third-party testing at a CPSC-accepted lab (e.g., lead in surface coatings/substrates, and flammability for apparel). Ask your POD partner which garments and inks already have testing and certificates.
- [ ] **Kids' hoodies: no drawstrings in the hood or neck** for kids' sizes (federal rule for children's upper outerwear). Confirm the hoodie blank.
- [ ] **Care and fiber-content labels** (FTC Care Labeling and Textile rules) and country-of-origin labeling.
- [ ] Confirm whether size 14 falls under your children's-product compliance (depends on how it's marketed and who it's for). Ask your POD partner or legal counsel.

### 📦 Before opening real orders
- [ ] **Sample orders**: order at least one of each type (kids tee, kids hoodie, set, teen tee, grown tee, custom print) in both black and white. Check print quality, sizing, labels, and packaging.
- [ ] Use the samples for your own product photos and a real size chart.
- [ ] Time a sample order from order to doorstep, then put real numbers on the Shipping page.
- [ ] Hook up the payment provider, swap "Join the launch list" back to a real checkout, and remove the banner.
- [ ] Email the launch list: "The drop is live." 🚀
