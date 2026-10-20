# Rocket Vibes: Apparel Sourcing & Pricing Research

**Prepared for:** Bentley, founder of Rocket Vibes (high-energy streetwear, US customers, store not live yet)
**First drop:** classic tee, oversized heavyweight hoodie, embroidered dad hat. 3–5 bold designs on dark bases (near-black, charcoal, navy) with neon accents (lime, magenta, orange).
**Research date:** Saturday, Oct 3, 2026. All prices were pulled that day from the cited pages. Prices change often, so re-check them before you buy.

> **How to read the numbers**
> - Every price links to its source. Where I estimated or assumed something, I say so.
> - POD base prices are for the **Free plan**, size **S–XL/M**, in a **dark color (Black)**, with **one front print** (for hats, one front embroidery). 2XL and up cost more (see notes).
> - **Gross margin (GM)** = (retail − product cost) ÷ retail.
> - **Contribution** = retail − product cost − shipping to the customer (assumes you offer free shipping) − card fee. This is the more honest number.
> - Card fee: Shopify Payments online rate of **2.9% + 30¢** on Basic ([shopify.com/pricing](https://www.shopify.com/pricing)).

---

## TL;DR

| | Tee | Oversized heavyweight hoodie | Embroidered dad hat |
|---|---|---|---|
| **Recommended retail** | **$38** | **$85** | **$34** |
| POD cost (Printful) | $15.60 (Comfort Colors 1717) | $37.23 (Bella+Canvas 4719) | $14.94 (Yupoong 6245CM) |
| POD gross margin | 58.9% | 56.2% | 56.1% |
| Bulk cost @ ~50 units | $12.84 (B+C 3001 + 3-color screen print) | $30.43 (IND4000 + 3-color screen print) | $8.13 (48-hat embroidered package) |
| Bulk gross margin | 66.2% | 64.2% | 76.1% |

**Recommendation:** launch on **print on demand (Printful as the main partner, Printify as a cheaper backup for tees)**, with **one exception: buy the dad hat in bulk from day one**. It's one size, so there's no size-curve risk, and it's the biggest per-unit win (about $4/hat more profit even after you pay to ship it yourself). Move a tee or hoodie design to bulk screen printing once it sells **about 50 units in 4–6 weeks** (or you can pre-sell that many). **Neon inks are the main quality reason to switch:** Printful says neon colors "simply won't print" with its DTG process ([Printful color guide](https://www.printful.com/blog/color-matching-guide-print-on-demand)).

---

## 1. Print-on-demand options

### 1a. Printful (in-house facilities, the most consistent quality)

Base prices come from Printful's public catalog API (`api.printful.com/products/{id}`), which feeds its product pages. The product price includes one print or embroidery placement ([Printful pricing](https://www.printful.com/pricing)).

| Item / blank | Base (Black, S–XL) | 2XL / 3XL | Source |
|---|---|---|---|
| **Tee – Bella+Canvas 3001** (4.2 oz, retail fit) | **$11.92** | $13.92 / $15.92 | [API #71](https://api.printful.com/products/71), [product page](https://www.printful.com/custom/t-shirts/71/bella-canvas-3001) (page shows $11.92) |
| **Tee – Comfort Colors 1717** (garment-dyed heavyweight) | **$15.60** (Black, Pepper, Graphite, Navy) | $17.60 / $19.60 | [API #586](https://api.printful.com/products/586) |
| Tee – Shaka Wear Max Heavyweight SHMHSS | $17.47 | $20.73 / $23.05 | [API #1636](https://api.printful.com/products/1636) |
| **Hoodie – Bella+Canvas 4719 Oversized Heavyweight** | **$37.23** (Black, Vintage Black, Navy) | $39.23 / $41.23 | [API #892](https://api.printful.com/products/892) |
| **Hoodie – Independent Trading IND4000 Heavyweight** | **$30.55** | $32.55 / $34.55 | [API #1543](https://api.printful.com/products/1543) |
| Hoodie – Champion S700 Powerblend | $35.70 | $37.70 / $39.70 | [API #842](https://api.printful.com/products/842) |
| Hoodie – Cotton Heritage M2580 (Black, Charcoal Heather) | $27.84 | $29.84 / $31.84 | [API #380](https://api.printful.com/products/380) |
| Hoodie – Gildan 18500 (budget; Black, Charcoal, Navy) | $22.63 | $24.63 / $26.63 | [API #146](https://api.printful.com/products/146) |
| **Dad hat – Yupoong 6245CM** (embroidered; Black, Navy, Dark Grey) | **$14.94** | one size | [API #206](https://api.printful.com/products/206), [product page](https://www.printful.com/custom/hats/206/yupoong-6245cm) (the page's headline price reads $14.02) |

**Add-ons** (same API records):
- Extra print placements: back print **+$5.95**; left-chest / center-chest / wrist **+$2.95**; tee sleeve **+$2.49**; hoodie sleeve **+$5.95**; inside label **+$0.99**; outside label **+$2.49**.
- Hat extra embroidery placements (back or sides): **+$2.95** each.
- Embroidery digitization: **$6.50 one-time per design** ($2.95 for back/side designs), waived on orders of 25+ items ([Printful Help](https://help.printful.com/hc/en-us/articles/50263327450257-What-are-digitization-and-adjustment-fees-for-embroidery)).
- Unlimited-color embroidery: **+$3.50 per item** ([Printful](https://www.printful.com/unlimited-color-embroidery)).
- 3D puff embroidery is available on hats only and costs more than flat embroidery ([Printful glossary](https://www.printful.com/glossary/3d-puff-embroidery)).

**US shipping** (flat rate, [printful.com/shipping](https://www.printful.com/shipping)):
- Tees: **$4.95** first item, +$2.20 each additional.
- Hoodies: **$8.79** first item, +$2.50 each additional.
- Hats: **$4.69** first item, +$2.00 each additional. Hats always ship as a separate package.

**Fulfillment time:** 2–5 business days to produce, then 3–4 business days for US standard shipping, or 1–3 for Express ([printful.com/shipping](https://www.printful.com/shipping)).

**Growth plan:** $24.99/mo with a 14-day free trial. It's free for a year once you pass $12K in annual sales. Discounts are up to 25% off DTG products, up to 9% off embroidery, and 9% off extra placements ([Printful Help](https://help.printful.com/hc/en-us/articles/10720462952988-What-should-I-know-about-the-Printful-Growth-plan), [growth perks](https://www.printful.com/growth-perks)). Exact per-item Growth prices only show inside a logged-in account, so they aren't used in the math below.

**Quality notes:**
- ⚠️ **Neons are the big problem for this brand.** Printful says its printers use the narrower "neon-less CMYK space" and tells sellers to "steer clear of neons and saturated shades as they simply won't print" ([Printful color guide](https://www.printful.com/blog/color-matching-guide-print-on-demand)). Lime, magenta and orange will print duller on DTG. Order color swatches or samples on the actual black/navy blank. Lean on embroidery, which uses real thread colors, for the brightest accents.
- Recent reviews on the B+C 3001 page are mixed. Some praise softness. Others mention a "dull" print, an off-center print, and a hole in one garment ([product page reviews](https://www.printful.com/custom/brands/bella-canvas/unisex-staple-t-shirt-bella-canvas-3001)). **Order samples before launch.** Samples are 20% off on the Free plan and 25% off on Growth ([Printful pricing](https://www.printful.com/pricing)).

### 1b. Printify (marketplace of third-party printers, usually cheaper, quality varies by provider)

Prices are the "Printify Choice" starting price (Printify picks the provider) on each US catalog page.

| Item / blank | Free plan "from" | Premium "from" | US shipping "from" | Avg. production | Source |
|---|---|---|---|---|---|
| **Tee – Bella+Canvas 3001** | **$11.29** | $9.04 | $3.99 | 1.3 days | [Printify #12](https://printify.com/app/products/12/bella-canvas/unisex-jersey-short-sleeve-tee) |
| **Tee – Comfort Colors 1717** | **$12.65** | $10.93 | $3.99 | 1.3 days | [Printify #706](https://printify.com/app/products/706/comfort-colors/unisex-garment-dyed-t-shirt) |
| **Hoodie – Independent Trading IND4000** | **$34.13** | $25.18 | $7.99 | 1.2 days (Monster Digital) | [Printify #2002](https://printify.com/app/products/2002/independent-trading-company/unisex-heavyweight-hooded-sweatshirt) |
| Hoodie – Lane Seven LS19001 Heavyweight | $31.87 | $23.42 | n/a | 2.2 days | [Printify #2001](https://printify.com/app/products/2001/lane-seven/unisex-heavyweight-pullover-hoodie) |
| Hoodie – Gildan 18500 (budget) | $21.58 | $15.89 | $7.39 | 1.7 days | [Printify #77](https://printify.com/app/products/77/gildan/unisex-heavy-blend-hooded-sweatshirt) |
| **Dad hat – Yupoong 6245CM** (embroidery) | **$16.12** | $11.92 | $4.69 | 1.1 days | [Printify #1447](https://printify.com/app/products/1447/yupoong/classic-dad-cap) |

- **Premium plan:** $39/mo billed monthly, or from $24.99/mo billed yearly ([printify.com/pricing](https://printify.com/pricing/)). On the IND4000 hoodie, Premium saves $8.95/unit ($34.13 → $25.18), so it pays for itself after about 3 hoodies a month.
- **Quality notes:** Printify routes orders to different print shops, so quality and turnaround depend on the provider. The B+C 3001 page notes that sleeve prints and neck labels from some providers are DTF, not DTG. Comfort Colors 1717 also lists other providers at higher prices: in Printify's own page data, Fulfill Engine is €15.56 and Shirt Monkey ships for €20.00 ([Printify #706](https://printify.com/app/products/706/comfort-colors/unisex-garment-dyed-t-shirt)). If you use Printify, **pin one provider per product after sampling** rather than letting Choice switch providers.

### 1c. Apliiq (streetwear-focused POD in LA and Philadelphia, with private-label options)

Apliiq's full seller pricing unlocks only after you connect a store, so these are the public figures.

| Item | Public price | Notes | Source |
|---|---|---|---|
| Tee – Bella+Canvas 3010 Heavyweight (6 oz) | "dropship this product **$9.50**" (garment); screen print **$16.99/item incl. 1-color imprint** ($13.59 VIP), 12-piece minimum per color | Decoration is priced in their designer | [Apliiq 3010](https://www.apliiq.com/customize/mens/tshirts/Heavyweight-Tee) |
| Hoodie – Independent IND4000 | "dropship this product **$29.45**"; screen print **$36.94/item incl. 1 color** ($29.55 VIP), 12-piece minimum | Decoration extra on dropship | [Apliiq IND4000](https://www.apliiq.com/customize/mens/hoodies/independent-heavyweight-pullover-hoodie) |
| Dad hat (BX001 soft cap), **embroidered** | **$15.90** dropship (up to 15,000 stitches, +$0.40 per extra 1,000); **$11 one-time digitization** | Bulk embroidered: 25 = $24.13, 50 = $22.22, 100 = $20.41 each | [Apliiq dad hats](https://www.apliiq.com/custom/hats/dad-hats) |
| Private label / woven labels | $0.75–$2.50 per product; woven label $0.60–$1.00 | Apliiq's main draw for a streetwear brand | [Apliiq dropship hoodies](https://www.apliiq.com/site/dropshipping/dropship-custom-hoodies) |

- **Fulfillment:** standard dropship orders take "about a week" to produce, and domestic shipping is 1–5 days ([Apliiq Help](https://help.apliiq.com/portal/en/kb/articles/how-long-does-it-take-to-get-my-order)).
- **Quality notes:** Apliiq is the only one of the three offering **screen printing with no long-run commitment (12-piece minimum per color)**, plus custom woven labels. That matters for neon inks and a "real brand" feel. It's slower and pricier than Printful or Printify for one-off dropshipping.

---

## 2. Bulk route: blanks + screen printing (and cut-and-sew)

### 2a. Wholesale blank prices (public prices, no account needed)

| Blank | Price | Tiers | Source |
|---|---|---|---|
| **Bella+Canvas 3001 – Black** | **$5.80** (XS–XL); 2XL $8.16; 3XL $9.85 | XS–XL $5.80 → $5.69 ($1K+ cart) → $5.53 ($2.5K+) → $5.03 ($5K+) | [ShirtSpace 3001C](https://www.shirtspace.com/bella-canvas/t-shirts/1998-bella-canvas-3001c-unisex-jersey-t-shirt) |
| Comfort Colors 1717 | **$7.38** (S–XL); 2XL $10.42; 3XL $12.76 (listed for the default Ivory color; check your exact dark color) | $7.09 at a $5K+ cart | [ShirtSpace C1717](https://www.shirtspace.com/comfort-colors/t-shirts/1012-comfort-colors-c1717-unisex-garment-dyed-heavyweight-t-shirt) |
| **Independent Trading IND4000 – Black** | **$23.39** (XS–XL); 2XL–3XL $28.89 | $23.34 ($2.5K+) → $21.22 ($5K+) | [ShirtSpace IND4000](https://www.shirtspace.com/independent-trading-co/sweatshirts/16116-independent-trading-co-ind4000-heavyweight-hooded-sweatshirt) |
| AS Colour Staple Tee 5001 (US) | $20.00 (1–9) / **$15.00 (10–49)** / **$13.00 (50+)** | | [AS Colour 5001](https://www.ascolour.com/staple-tee-5001) |
| AS Colour Heavy Hood 5146 (US, oversized heavyweight) | $54.00 (1–9) / **$40.50 (10–49)** / **$36.45 (50+)** | | [AS Colour 5146](https://ascolour.com/mens-heavy-hood-5146/) |
| Los Angeles Apparel 1801GD tee (6.5 oz, garment-dyed, made in USA) | **$16.26** (listed at 47% off $30.97) | | [BlankStyle 1801GD](https://www.blankstyle.com/los-angeles-apparel-1801gd-ss-grmnt-dye-crew-neck-65oz) |
| Los Angeles Apparel HF09 Heavy Fleece Hoodie (14 oz, garment dye) | $78.00 **retail** on LAA's own site. I couldn't find a public wholesale price; ask LAA wholesale. | | [LAA HF09](https://losangelesapparel.net/products/hf09-heavy-fleece-hoodie-garment-dye) |

*S&S Activewear blocked automated access (Cloudflare error page), and its pricing needs a login anyway. ShirtSpace is a public wholesale reseller of the same brands. French Press Custom (below) says it prices blanks "from the live S&S Activewear catalog."*

### 2b. Screen-print cost (decoration only, per piece, one location)

Planning assumption: a Rocket Vibes design with **2 neon spot colors on a dark shirt needs a white underbase, so price it as 3 colors.**

| Qty | Momentec Brands (published grid) | French Press Custom, Santa Fe Springs CA (live price engine, updated Oct 2, 2026) |
|---|---|---|
| **24** | 1c $8.90 · 2c $10.70 · **3c $12.30** (24–47 tier) | Won't screen print under 36 (uses DTG instead). 36–49: 1c $7.73 · 2c $8.87 · **3c $10.00** |
| **50** | 1c $6.90 · 2c $8.50 · **3c $9.90** (48–71 tier) | 1c $5.43 · 2c $6.24 · **3c $7.04** (50–99) |
| **100** | 1c $4.90 · 2c $6.30 · **3c $7.50** (72–143 tier) | 1c $3.77 · 2c $4.24 · **3c $4.71** (100–199) |
| Minimums / fees | 24-piece minimum run ("LTM $400"); 6-piece minimum per style/color; +$0.50 per extra color | 36-piece minimum; screens included in the per-piece price; the tier is set by **total pieces on the order**, so 2 designs × 50 price at the 100 tier; 2–3 week turnaround; blanks billed at **wholesale × 1.75** if they supply them |
| Source | [momentecbrands.com/screen-print](https://www.momentecbrands.com/screen-print) | [French Press 2026 guide](https://www.frenchpresscustom.com/blog/how-much-does-custom-screen-printing-cost-in-2026-pricing-guide) |

French Press reports real 100–249-piece orders at a median of **about $12/shirt all-in**, and 24–49-piece orders at **about $24** (same source). Specialty inks (puff, glow, etc.) cost extra. A local shop will usually stock neon plastisol, which DTG can't match. Momentec, for example, advertises neon pink, orange, yellow and green inks.

**Embroidered hats in bulk:** Bulk-Caps sells **24 embroidered dad caps for $220 ($9.17 each)** and **48 for $390 ($8.13 each)**. That includes one location, multi-color logos are fine, and turnaround is 2–3 weeks ([24-pack](https://bulk-caps.com/products/24-custom-embroidered-dad-caps), [48-pack](https://bulk-caps.com/products/48-custom-embroidered-dad-caps)).

**Shipping it yourself (bulk route):** USPS Ground Advantage commercial rates (effective July 12, 2026), Zone 4: **$7.46** for anything up to 15.999 oz (tee or hat) and **$8.51** at 2 lb (a heavyweight hoodie). Zone 1 is $6.93, Zone 8 is $8.40 ([USPS Notice 123](https://pe.usps.com/text/dmm300/Notice123.htm)). That's **more than Printful's flat $4.95 tee rate**, which eats much of the bulk savings unless you get discounted labels through Pirate Ship or ShipStation. Mailers and packaging aren't included.

### 2c. Cut-and-sew / private-label manufacturers (for later)

| Maker | Minimums | Price | Lead time | Source |
|---|---|---|---|---|
| **Plucky Reach** (Los Angeles), hoodies incl. 380–450 GSM oversized heavyweight | 50 per style per colorway; 100 for full private label | **$18–$45/unit**, depending on fabric, print and construction | 4–6 weeks from approved sample | [pluckyreach.com](https://pluckyreach.com/production/hoodie-manufacturing) |
| **Essentials Made** (Los Angeles), cut & sew | "Capsule Run" 72 pcs/style (styles must share fabric); "Growth Run" 150 pcs/style | ~$7,250/style for the capsule run (≈ $100.69/pc), ~$8,100/style for the growth run (≈ $54/pc); 50% deposit | n/a | [essentialsmade.com](https://essentialsmade.com/pages/cut-sew-manufacturing-in-los-angeles) |

Cut-and-sew only makes sense once a hoodie silhouette has proven demand. It isn't a launch option.

---

## 3. Competitor retail pricing

Prices are the listed prices on each brand's own store on Oct 3, 2026, read from the stores' public product feeds. "Typical" is the median across that store's tees, pullover hoodies and hats. Collabs and sale items can skew a range.

| Brand | Positioning | Tee (typical / example) | Hoodie (typical / example) | Hat (typical / example) |
|---|---|---|---|---|
| **Mad Poppy** | Rave / bass-music streetwear, closest "high-energy" match | $35. [ALLNIGHTER Drop Shoulder Tee $35](https://madpoppy.com/products/allnighter-drop-shoulder-t-shirt) | $60. [ALLNIGHTER Heavyweight Sunfade Oversized Hoodie $60](https://madpoppy.com/products/allnighter-heavyweight-sunfade-oversized-hoodie) | $33. [Bass Head Racing Dad Hat $33](https://madpoppy.com/products/bass-head-racing-distressed-dad-hat) |
| **No 925** | Indie graphic, oversized heavyweight | $32.99. [Always On tee](https://www.no925.co/products/always-on-unisex-t-shirt) | $69.99. [Deadweight Oversized Graphic Hoodie](https://www.no925.co/products/deadweight-oversized-graphic-hoodie) | $29.99. [Baseline Dad Hat](https://www.no925.co/products/baseline-dad-hat-black) |
| **Catori** | Indie anime/graphic | $35. [2Gunners T-Shirt](https://catoriclothing.com/products/2gunners-anime-t-shirt) | $69.99. [2Gunners Hoodie](https://catoriclothing.com/products/2gunners-anime-hoodie) (up to $90) | n/a |
| **Gods & Gold** | Indie heavyweight graphic | $40. [Acheron Heavyweight Tee](https://godsngold.com/products/acheron) | $85. [Crownbound Heavyweight Hoodie](https://godsngold.com/products/contrast-drawstring-hoodie) | $40. [Ampersand Snapback](https://godsngold.com/products/alpha-crown-flat-bill-snapback-luxury-streetwear-embroidered-cap) |
| **RIPNDIP** | Bright, playful, mid-tier | $36. [9 Lives Tee](https://ripndip.com/products/9-lives-tee-black) | $80. [420 MPH Hoodie](https://ripndip.com/products/420-mph-hoodie-black) | $36. [Castanza Dad Hat](https://ripndip.com/products/castanza-dad-hat-black-wash) |
| **Teddy Fresh** | Bold color, creator-led | $39–42. [Western Tie Dye Tee $42](https://teddyfresh.com/products/western-tie-dye-tee) | $80–88. [Come One Come All Hoodie $88](https://teddyfresh.com/products/come-one-come-all-hoodie) | $29. [Wide Wale Cord Hat](https://teddyfresh.com/products/wide-wale-cord-hat) |
| **HUF** | Established skate/street | $32. [Box Logo T-Shirt](https://hufworldwide.com/products/box-logo-t-shirt-ts02763) | $72. [Liberty Pullover Hoodie](https://hufworldwide.com/products/liberty-pullover-hoodie-pf00847) | $36. [89 Oval Snapback](https://hufworldwide.com/products/89-oval-5-panel-snapback-hat-ht00950) |
| **The Hundreds** | Established LA streetwear | $60 median (range $18–$200). [1980 T-Shirt](https://thehundreds.com/products/1980-t-shirt-gh-2025) | $80. [Natural Pullover Hoodie](https://thehundreds.com/products/natural-pullover-hoodie-gh2025) | $30. [Adam Dad Hat](https://thehundreds.com/products/adam-dad-hat-gh-2025) |
| **Pleasures** | Upper-mid anchor | $46. [Athor T-Shirt](https://pleasuresnow.com/products/pleasures-athor-t-shirt-black-fa26) | $130. [Dynamic Hoodie](https://pleasuresnow.com/products/pleasures-dynamic-hoodie-black-f26) | $46. [Film Snapback](https://pleasuresnow.com/products/pleasures-film-snapback-black-su26) |

**What this shows:** indie brands sell tees at **$33–42**, hoodies at **$60–88** and hats at **$29–40**. Established mid-tier labels go to $46/$130/$46. A new brand with no following should price at or just below the RIPNDIP / Teddy Fresh / Gods & Gold level, not at Pleasures.

---

## 4. Recommended pricing and margin math

**Retail:** Tee **$38** · Oversized heavyweight hoodie **$85** · Dad hat **$34**. Card fees at 2.9% + $0.30 come to $1.40 on the tee, $2.77 on the hoodie and $1.29 on the hat.

### 4a. POD route (Printful, Free plan, one front print or embroidery)

| Item | Retail | Unit cost | GM $ | **GM %** | + shipping absorbed | Contribution $ (%) |
|---|---|---|---|---|---|---|
| Tee, Comfort Colors 1717 | $38 | $15.60 | $22.40 | **58.9%** | $4.95 | 38 − 15.60 − 4.95 − 1.40 = **$16.05 (42.2%)** |
| Tee, B+C 3001 (cheaper option) | $38 | $11.92 | $26.08 | 68.6% | $4.95 | **$19.73 (51.9%)** |
| Tee, CC1717 **with a back print** (+$5.95) | $38 | $21.55 | $16.45 | 43.3% | $4.95 | $10.10 (26.6%) ⚠️ |
| Hoodie, B+C 4719 Oversized Heavyweight | $85 | $37.23 | $47.77 | **56.2%** | $8.79 | 85 − 37.23 − 8.79 − 2.77 = **$36.21 (42.6%)** |
| Hoodie, IND4000 (option) | $85 | $30.55 | $54.45 | 64.1% | $8.79 | $42.89 (50.5%) |
| Dad hat, Yupoong 6245CM | $34 | $14.94 | $19.06 | **56.1%** | $4.69 | 34 − 14.94 − 4.69 − 1.29 = **$13.08 (38.5%)** (+ $6.50 one-time digitization per design) |

Printify for comparison: CC1717 tee $12.65 → 66.7% GM, $19.96 contribution with $3.99 shipping. IND4000 hoodie $34.13 → 59.8% GM. Yupoong hat $16.12 → 52.6% GM.

If a design needs a back print, either price that tee at **$42–44** or use the cheaper B+C 3001.

### 4b. Bulk route (blank + screen print, you ship it)

Assumptions: 3-color screen print (2 neons + underbase); the blank price applies if the shop accepts your blanks; USPS Ground Advantage Zone 4 shipping. The low end uses French Press rates, the high end Momentec.

| Item @ qty | Unit cost (blank + print) | GM % | Shipping | Contribution $ (%) |
|---|---|---|---|---|
| Tee (3001 $5.80) @ **24** | 5.80 + 12.30 = **$18.10** | 52.4% | $7.46 | $11.04 (29.1%) |
| Tee @ **50** | 5.80 + 7.04 = **$12.84** (to $15.70) | **66.2%** (58.7%) | $7.46 | **$16.30 (42.9%)** |
| Tee @ **100** | 5.80 + 4.71 = **$10.51** (to $13.30) | **72.3%** (65.0%) | $7.46 | $18.63 (49.0%) |
| Hoodie (IND4000 $23.39) @ **50** | 23.39 + 7.04 = **$30.43** (to $33.29) | **64.2%** (60.8%) | $8.51 | **$43.29 (50.9%)** |
| Hoodie @ **100** | 23.39 + 4.71 = **$28.10** (to $30.89) | 66.9% (63.7%) | $8.51 | $45.62 (53.7%) |
| Hoodie (AS Colour 5146 oversized, $36.45) @ 50 | 36.45 + 7.04 = $43.49 | 48.8% | $8.51 | $30.23 (35.6%) |
| Dad hat @ **24** (Bulk-Caps) | $220 ÷ 24 = **$9.17** | 73.0% | $7.46 | $16.08 (47.3%) |
| Dad hat @ **48** (Bulk-Caps) | $390 ÷ 48 = **$8.13** | **76.1%** | $7.46 | **$17.12 (50.4%)** |

**What the math shows:**
- **Tees:** bulk at 50 units saves only $2.76/unit on product cost vs. Printful CC1717. Paying $7.46 to ship it yourself instead of $4.95 wipes almost all of that out (contribution $16.30 vs $16.05). Bulk only clearly pays at **100+ units per run** or with discounted shipping labels. The real reasons to switch are **neon plastisol inks, better hand-feel and brand control**.
- **Hoodies:** Printful's IND4000 ($30.55 *including* the print) costs about the same as bulk at 50 ($30.43). For the oversized fit, Printful's 4719 at $37.23 is actually **cheaper than AS Colour 5146 blank + print** ($43.49). POD is competitive for hoodies at launch volumes.
- **Hats:** bulk wins clearly. It's **+$4.04/hat** more contribution than Printful ($17.12 vs $13.08), there's no size curve to guess, and a 48-hat order is only $390 of cash.

### 4c. Launch / bundle ideas (math shown)

1. **"Liftoff Kit": tee + hoodie + hat for $135** (separately $157, so 14% off)
   - POD: cost 15.60 + 37.23 + 14.94 = $67.77. Printful shipping: 8.79 (hoodie) + 2.20 (tee as additional item) + 4.69 (hat ships separately) = $15.68. Fee $4.22. **Contribution = $47.34 (35.1%)**. GM = 49.8%.
   - Bulk (@50 / 48 hats): cost 12.84 + 30.43 + 8.13 = $51.40. One 3 lb USPS box (Zone 4) $9.67. Fee $4.22. **Contribution = $69.72 (51.6%)**.
2. **"Neon Duo": tee + hat for $64** (separately $72)
   - POD: 30.54 cost + 9.64 shipping + 2.16 fee → **$21.66 (33.8%)**.
   - Hybrid (POD tee + bulk hat) or bulk: up to **$33.41 (52.2%)** if you ship both in one package.
3. **Shipping policy:** charge shipping on single tees and hats, with **free US shipping over $75**. A hoodie or a bundle crosses the line, so the shipping cost you absorb lands where the margin is biggest.
4. **Pre-order drop window (7–10 days):** sell designs as pre-orders with a 2–3 week ship date, which matches screen-print turnaround. Any design with ≥ 36–50 pre-orders goes to a local screen printer for neon plastisol. The rest go to POD.

---

## 5. Recommendation: which route, and when to switch

**Launch with a hybrid that's mostly POD:**

1. **Tees and hoodies on Printful at launch**: Comfort Colors 1717 tee at $38 and Bella+Canvas 4719 oversized heavyweight hoodie at $85 (or IND4000 if samples show it looks better). Why:
   - No inventory risk across 3–5 designs × 3 colors × 6+ sizes.
   - Consistent in-house quality and fast fulfillment (2–5 business days to produce).
   - Hoodie POD cost is already about the same as bulk at 50 units.
   - Use **Printify (pinned to one sampled provider) for tees** if you want ~$3 more margin per tee.
2. **Hats in bulk from day one**: a 24- or 48-hat embroidered run ($220–$390) in neon thread on black/navy 6245-style caps, shipped by you (76% GM). If you don't want to handle shipping at all, put the hat on Printful at $34 (56% GM).
3. **Design for POD's limits:** avoid relying on true neon in DTG art, since Printful says neons "won't print". Use bright CMYK-safe lime, magenta and orange, put neon embroidery on chest hits and hats, and order samples on each dark base before going live.

**When to switch a SKU to bulk screen printing:**
- **Per design:** once it sells (or pre-sells) **about 50 units in 4–6 weeks**. At 100+ units per run, tee cost drops to about $10.51 (vs $15.60 on POD). Several designs on one order share the volume tier, so combine reorders.
- **Overall:** once you're steadily doing **about 100+ apparel orders a month**, set up discounted shipping labels (Pirate Ship / ShipStation) and either self-fulfill or use Apliiq's "print in bulk, ship on demand" warehousing.
- **Before switching tees, try Printful Growth** ($24.99/mo, up to 25% off DTG). It may close much of the gap without holding inventory.
- **Cut-and-sew** (Plucky Reach: 50-piece minimum, $18–45/unit) only once a hoodie fit is a proven bestseller and you want your own pattern and label.

---

### Caveats
- POD prices are Free-plan list prices for size M, Black. Exact checkout prices depend on plan, size, color and provider.
- ShirtSpace's Comfort Colors price is for the default color shown (Ivory). Check pricing for your exact dark color.
- Screen-print grids are from two specific decorators. Get 2–3 local quotes, and confirm whether the shop accepts customer-supplied blanks and charges for neon ink.
- USPS rates are retail commercial rates. Discounted label services can be lower.
- Margins exclude marketing, returns, packaging, Shopify subscription ($29/mo Basic, [shopify.com/pricing](https://www.shopify.com/pricing)) and sales tax.
