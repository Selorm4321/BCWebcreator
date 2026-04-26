---
name: local-seo-web-audit
description: End-to-end SEO audit and improvement workflow for local service business websites. Use for diagnosing indexing issues (like Search Console sitemap errors), fixing canonical tags, adding LocalBusiness schema, and creating location-specific landing pages to improve local search rankings.
license: Complete terms in LICENSE.txt
---

# Local SEO Web Audit

This skill provides a complete workflow for auditing and fixing technical SEO and local search signals for static HTML websites or simple web projects.

## Workflow Overview

A complete local SEO audit involves these steps:

1. **Run automated audit** (run `audit_site.py`)
2. **Fix technical fundamentals** (canonical tags, sitemap, robots.txt)
3. **Enhance structured data** (add LocalBusiness schema)
4. **Expand local footprint** (create location landing pages)
5. **Set up Google tools** (Search Console, Business Profile)

## Step 1: Run Automated Audit

Run the bundled Python script to quickly identify missing or misconfigured SEO signals on the live website:

```bash
python /home/ubuntu/skills/local-seo-web-audit/scripts/audit_site.py <domain.com>
```

The script checks:
- `www` vs `non-www` redirect consistency
- `robots.txt` and `sitemap.xml` validity
- Homepage title length, meta description, and canonical tags
- Presence of Open Graph tags and Schema markup

## Step 2: Fix Technical Fundamentals

Based on the audit results, fix the technical foundation of the site.

### The Canonical Domain Rule
Pick ONE canonical domain (usually non-www, e.g., `https://domain.com/`) and enforce it everywhere.
- If the sitemap uses `www` but the canonical tags use `non-www`, Google Search Console will show a "Couldn't fetch" error.
- Use `sed` or Python to find and replace incorrect domains across all HTML files.

### Update Sitemap and Robots.txt
If a new sitemap is needed, use the template:
`cat /home/ubuntu/skills/local-seo-web-audit/templates/sitemap_template.xml`

Ensure `robots.txt` points to the correct sitemap URL:
```text
User-agent: *
Allow: /
Sitemap: https://domain.com/sitemap.xml
```

## Step 3: Enhance Structured Data

Local service businesses need `LocalBusiness` schema to rank in local searches.

1. Read the schema template:
   `cat /home/ubuntu/skills/local-seo-web-audit/templates/local_business_schema.json`
2. Replace the placeholders (`DOMAIN`, `BUSINESS_NAME`, `PRIMARY_CITY`, etc.) with the client's actual data.
3. Inject the resulting JSON-LD script block into the `<head>` of the homepage.
4. Optional: Add `FAQPage` schema to trigger rich results. See `templates/faq_schema.json`.

## Step 4: Expand Local Footprint

To rank in surrounding cities, the business needs dedicated location landing pages.

1. Read the keyword strategy guide to understand what keywords to target:
   `cat /home/ubuntu/skills/local-seo-web-audit/references/keyword_strategy.md`
2. Create a new directory for the location (e.g., `locations/city-name/`)
3. Use the location page template as a starting point:
   `cat /home/ubuntu/skills/local-seo-web-audit/templates/location_page_template.html`
4. Write unique, high-quality content for the page targeting the specific city.
5. Add the new page to the `sitemap.xml`.

## Step 5: Google Tools Setup

Technical fixes alone aren't enough. Guide the user through setting up their Google properties.

Read the setup guide for instructions to provide to the user:
`cat /home/ubuntu/skills/local-seo-web-audit/references/google_tools_setup.md`

Key actions to advise the user on:
- Deleting the broken sitemap and submitting the new one in Search Console.
- Claiming and fully optimizing their Google Business Profile.
- Gathering their first 5 Google reviews.
