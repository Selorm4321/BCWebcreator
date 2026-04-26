#!/usr/bin/env python3
"""
audit_site.py — Quick SEO audit for a static HTML website.

Usage:
    python audit_site.py <domain>

Example:
    python audit_site.py bcwebcreator.com

Checks performed:
  - www vs non-www redirect consistency
  - robots.txt existence and sitemap pointer
  - sitemap.xml existence and URL consistency (www vs non-www)
  - Homepage: title length, meta description, canonical tag, schema type
  - Open Graph tags presence
  - Structured data (ld+json) presence
"""

import sys
import re
import urllib.request
import urllib.error

def fetch(url, timeout=8):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "SEO-Audit-Bot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="replace"), r.geturl(), r.status
    except Exception as e:
        return None, None, str(e)

def check(label, passed, detail=""):
    status = "PASS" if passed else "FAIL"
    line = f"  [{status}] {label}"
    if detail:
        line += f" — {detail}"
    print(line)
    return passed

def main():
    if len(sys.argv) < 2:
        print("Usage: python audit_site.py <domain>")
        sys.exit(1)

    domain = sys.argv[1].strip().rstrip("/")
    if domain.startswith("http"):
        domain = re.sub(r"https?://(www\.)?", "", domain).rstrip("/")

    base = f"https://{domain}"
    www_base = f"https://www.{domain}"
    issues = []

    print(f"\n{'='*55}")
    print(f"  SEO AUDIT: {domain}")
    print(f"{'='*55}\n")

    # ── 1. www redirect ──────────────────────────────────────
    print("[ www Redirect ]")
    _, final_url, _ = fetch(www_base)
    if final_url:
        redirects_to_nonwww = "www." not in final_url.replace("https://www.", "PLACEHOLDER")
        if not check("www redirects to non-www", redirects_to_nonwww, f"landed on {final_url}"):
            issues.append("Set up a 301 redirect from www to non-www (or vice versa) and pick one canonical domain.")
    print()

    # ── 2. robots.txt ────────────────────────────────────────
    print("[ robots.txt ]")
    robots_content, _, _ = fetch(f"{base}/robots.txt")
    has_robots = robots_content is not None and len(robots_content) > 10
    if not check("robots.txt exists", has_robots):
        issues.append("Create a robots.txt at the root. Minimum: 'User-agent: *\\nAllow: /\\nSitemap: https://yourdomain.com/sitemap.xml'")
    if has_robots:
        has_sitemap_ref = "sitemap" in robots_content.lower()
        if not check("robots.txt references sitemap", has_sitemap_ref):
            issues.append("Add 'Sitemap: https://yourdomain.com/sitemap.xml' to robots.txt")
        www_in_robots = f"www.{domain}" in robots_content
        if not check("robots.txt uses non-www URLs", not www_in_robots, "www found" if www_in_robots else ""):
            issues.append("Update robots.txt sitemap URL to use non-www domain.")
    print()

    # ── 3. sitemap.xml ───────────────────────────────────────
    print("[ sitemap.xml ]")
    sitemap_content, _, _ = fetch(f"{base}/sitemap.xml")
    has_sitemap = sitemap_content is not None and "<url>" in sitemap_content
    if not check("sitemap.xml exists and has URLs", has_sitemap):
        issues.append("Create a sitemap.xml listing all your pages and submit it in Google Search Console.")
    if has_sitemap:
        www_in_sitemap = f"www.{domain}" in sitemap_content
        if not check("sitemap.xml uses non-www URLs", not www_in_sitemap, "www URLs found" if www_in_sitemap else ""):
            issues.append("Replace all 'www.' URLs in sitemap.xml with non-www versions, then resubmit in Search Console.")
        url_count = sitemap_content.count("<loc>")
        check("sitemap has multiple pages", url_count > 1, f"{url_count} URL(s) found")
    print()

    # ── 4. Homepage ──────────────────────────────────────────
    print("[ Homepage ]")
    html, _, _ = fetch(base)
    if html is None:
        print("  [FAIL] Could not fetch homepage")
        issues.append("Homepage could not be fetched — check your hosting.")
    else:
        title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else ""
        has_title = bool(title)
        if not check("Has <title> tag", has_title):
            issues.append("Add a <title> tag to the homepage.")
        if has_title:
            good_len = 30 <= len(title) <= 65
            if not check("Title length 30–65 chars", good_len, f"{len(title)} chars: '{title}'"):
                issues.append(f"Adjust title length to 30–65 characters (currently {len(title)}).")

        desc_match = re.search(r'<meta\s+name=["\']description["\'][^>]+content=["\']([^"\']+)', html, re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta\s+content=["\']([^"\']+)["\'][^>]+name=["\']description["\']', html, re.IGNORECASE)
        desc = desc_match.group(1).strip() if desc_match else ""
        has_desc = bool(desc)
        if not check("Has meta description", has_desc):
            issues.append("Add a meta description tag (120–160 characters).")
        if has_desc:
            good_desc = 80 <= len(desc) <= 165
            if not check("Meta description 80–165 chars", good_desc, f"{len(desc)} chars"):
                issues.append(f"Adjust meta description to 80–165 characters (currently {len(desc)}).")

        canonical_match = re.search(r'<link\s+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', html, re.IGNORECASE)
        has_canonical = canonical_match is not None
        if not check("Has canonical tag", has_canonical):
            issues.append("Add <link rel='canonical' href='https://yourdomain.com/'> to the homepage <head>.")
        if has_canonical:
            canon_url = canonical_match.group(1)
            www_in_canon = "www." in canon_url
            if not check("Canonical uses non-www", not www_in_canon, canon_url):
                issues.append(f"Update canonical tag to use non-www URL: https://{domain}/")

        has_og = 'property="og:title"' in html or "property='og:title'" in html
        if not check("Has Open Graph tags", has_og):
            issues.append("Add Open Graph meta tags (og:title, og:description, og:image, og:url) for social sharing.")

        has_schema = '"@type"' in html or "@type" in html
        if not check("Has structured data (schema.org)", has_schema):
            issues.append("Add LocalBusiness schema markup in a <script type='application/ld+json'> block.")

        if has_schema:
            is_local_biz = '"LocalBusiness"' in html or '"ProfessionalService"' in html
            has_area_served = '"areaServed"' in html
            has_faq = '"FAQPage"' in html
            check("Schema uses LocalBusiness type", is_local_biz,
                  "upgrade from ProfessionalService if needed" if '"ProfessionalService"' in html else "")
            if not check("Schema includes areaServed", has_area_served):
                issues.append("Add 'areaServed' to your LocalBusiness schema listing the cities/regions you serve.")
            if not check("FAQPage schema present", has_faq):
                issues.append("Add a FAQPage schema block — it can trigger rich FAQ results in Google search.")

    print()

    # ── Summary ──────────────────────────────────────────────
    print(f"{'='*55}")
    if issues:
        print(f"  {len(issues)} issue(s) to fix:\n")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
    else:
        print("  All checks passed!")
    print(f"{'='*55}\n")

if __name__ == "__main__":
    main()
