# Google Tools Setup Guide

## Table of Contents
1. Google Search Console — Sitemap Fix Workflow
2. Google Business Profile — Setup Checklist
3. Common Search Console Issues and Fixes

---

## 1. Google Search Console — Sitemap Fix Workflow

**When to use:** After fixing www/non-www domain issues or adding new pages.

### Steps
1. Go to [Search Console Sitemaps](https://search.google.com/search-console/sitemaps)
2. Select the correct property (use domain property, not URL prefix)
3. **Delete broken sitemaps:** Click the three-dot menu next to any sitemap showing "Couldn't fetch" → Remove
4. **Submit new sitemap:** Enter `https://yourdomain.com/sitemap.xml` → Submit
5. Wait 3–7 days for Google to crawl and index

### Canonical Domain Rule
Pick ONE canonical domain and enforce it everywhere:
- `https://bcwebcreator.com/` ← preferred (non-www)
- All canonical tags, sitemap URLs, robots.txt, og:url, twitter:url must use this exact form
- Set up a 301 redirect from the other form (www → non-www or vice versa) at the hosting level

### Checking Indexing Status
- **Coverage report:** Search Console → Indexing → Pages → check "Not indexed" tab
- **URL Inspection:** Paste any URL to see if Google has indexed it and when it was last crawled
- **Request indexing:** After fixing a page, use URL Inspection → Request Indexing

---

## 2. Google Business Profile — Setup Checklist

Google Business Profile (GBP) is the single highest-impact free SEO action for local businesses. It controls the Google Maps "Local Pack" results.

### Setup Steps
1. Go to [business.google.com](https://business.google.com)
2. Search for the business name — if it exists, claim it; if not, create it
3. Fill in every field:

| Field | What to Enter |
|---|---|
| Business name | Exact legal/brand name (no keyword stuffing) |
| Category | Most specific primary category (e.g., "Web Designer") |
| Service area | List all cities served (no physical storefront needed) |
| Website | https://yourdomain.com |
| Phone | Local phone number |
| Hours | Accurate business hours |
| Description | 750 chars max — include primary keyword and city naturally |
| Services | List each service with description |
| Photos | Minimum 5: logo, cover, work samples, team |

### Getting Reviews (Critical)
- Ask every satisfied client directly: "Would you mind leaving us a Google review?"
- Send them the direct review link: `https://g.page/r/YOUR_PLACE_ID/review`
- Aim for 5+ reviews in the first 60 days
- Respond to every review (positive and negative)

### Posts
- Publish a GBP Post at least once per month
- Types: What's New, Offer, Event
- Include a photo and a call-to-action link

---

## 3. Common Search Console Issues and Fixes

| Issue | Cause | Fix |
|---|---|---|
| "Couldn't fetch" sitemap | www/non-www mismatch, or file doesn't exist | Fix domain consistency; verify sitemap URL is accessible |
| "Discovered — currently not indexed" | Page exists but Google hasn't crawled it | Request indexing via URL Inspection; add internal links to the page |
| "Crawled — currently not indexed" | Google crawled but chose not to index | Improve content quality; ensure page has unique, substantial content |
| "Duplicate without canonical" | Two URLs serve same content | Add canonical tag pointing to preferred URL |
| "Page with redirect" | Old URL redirects to new | Update internal links and sitemap to point directly to final URL |
| Low click-through rate | Title/description not compelling | Rewrite title and meta description to be more specific and action-oriented |
