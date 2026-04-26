import os
import re

# File Paths
root_dir = r"c:\Users\vsmat\OneDrive\Desktop\Websites\BCWebcreator"
index_path = os.path.join(root_dir, "index.html")

# Create Directories
os.makedirs(os.path.join(root_dir, "terms"), exist_ok=True)
os.makedirs(os.path.join(root_dir, "privacy"), exist_ok=True)

with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# Extract header and footer
nav_end_idx = index_html.find("</nav>") + len("</nav>")
header_raw = index_html[:nav_end_idx]

footer_start_idx = index_html.find("<!-- Footer -->")
footer_raw = index_html[footer_start_idx:]

def fix_links(htmlStr):
    htmlStr = re.sub(r'href="#([a-zA-Z0-9_-]+)"', r'href="/#\1"', htmlStr)
    htmlStr = re.sub(r'href="images/', r'href="/images/', htmlStr)
    htmlStr = re.sub(r'src="images/', r'src="/images/', htmlStr)
    htmlStr = htmlStr.replace('href="manifest.json"', 'href="/manifest.json"')
    return htmlStr

header_fixed = fix_links(header_raw)
footer_fixed = fix_links(footer_raw)

terms_raw = """
<div class="bg-yellow-50 dark:bg-yellow-900/30 border border-yellow-400 dark:border-yellow-600 p-4 rounded-lg mb-8 text-yellow-800 dark:text-yellow-200">⚠️ <strong>DISCLAIMER:</strong> This is a template draft. BC Web Creator recommends consulting a qualified legal professional in British Columbia before publishing.</div>

<h1 class="font-display font-bold text-4xl text-slate-900 dark:text-white border-b-2 border-primary-500 pb-4 mb-8">Terms of Service — BC Web Creator</h1>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>Last Updated: February 26, 2026</strong><br>
<strong>Company:</strong> Typhoon Entertainment Incorporated (operating as BC Web Creator)<br>
<strong>Contact:</strong> bcwebcreator@gmail.com<br>
<strong>Location:</strong> Abbotsford, British Columbia, Canada</p>

<hr class="border-slate-200 dark:border-slate-800 my-8">

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">1. Acceptance of Terms</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">By accessing or using bcwebcreator.com, you agree to be bound by these Terms of Service. If you do not agree, please do not use this website. These Terms apply to all visitors, clients, and anyone who inquires about or engages our services.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">2. Services</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">BC Web Creator (operated by Typhoon Entertainment Incorporated) provides web design, web development, SEO optimization, landing page creation, brand identity, and digital strategy services to businesses primarily in British Columbia, Canada.</p>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">All services are subject to a separate written project agreement or proposal signed by both parties. These Terms govern your general use of this website and serve as a foundation for all client engagements.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">3. Project Agreements & Payment Terms</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>3.1 Project Proposals.</strong> All projects begin with a written proposal or statement of work outlining scope, deliverables, timeline, and cost. Work begins only after written approval and receipt of deposit.</p>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>3.2 Payment.</strong> Standard payment structure is 50% deposit upon project commencement and 50% upon project completion prior to final delivery. For Premium projects, a 3-part payment schedule may be arranged. All prices are in Canadian dollars (CAD).</p>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>3.3 Late Payments.</strong> Invoices unpaid beyond 14 days of the due date may incur a late fee of 2% per month. BC Web Creator reserves the right to pause or suspend work on any project with outstanding unpaid invoices.</p>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>3.4 Refunds.</strong> Deposits are non-refundable once work has commenced. If a project is cancelled by the client after work has begun, payment is due for all work completed to that point.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">4. Intellectual Property & Ownership</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>4.1 Client Ownership.</strong> Upon receipt of final payment in full, the client owns all final deliverables including design files, code, and content produced specifically for their project. BC Web Creator will provide all source files and credentials upon final payment.</p>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>4.2 BC Web Creator's IP.</strong> Any pre-existing tools, frameworks, templates, or proprietary processes used in the creation of deliverables remain the intellectual property of Typhoon Entertainment Incorporated. The client receives a perpetual, royalty-free license to use the final deliverables.</p>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>4.3 Portfolio Rights.</strong> BC Web Creator reserves the right to display completed work in its portfolio, on social media, and in marketing materials unless the client requests otherwise in writing.</p>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>4.4 Third-Party Assets.</strong> Any third-party fonts, stock images, plugins, or licensed assets used in a project are subject to their respective licenses. The client is responsible for ensuring continued compliance with those licenses.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">5. Revision Policy</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>5.1</strong> Each project package includes a defined number of revision rounds as outlined in the project proposal. Revisions beyond the agreed scope may be billed at BC Web Creator's standard hourly rate.</p>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>5.2</strong> Revisions must be requested in writing (email). Verbal revision requests will not be actioned until confirmed in writing.</p>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>5.3</strong> Revisions requested after final project sign-off are considered new work and will be billed accordingly.</p>
"""

privacy_raw = """
<div class="bg-yellow-50 dark:bg-yellow-900/30 border border-yellow-400 dark:border-yellow-600 p-4 rounded-lg mb-8 text-yellow-800 dark:text-yellow-200">⚠️ <strong>DISCLAIMER:</strong> This is a template draft. BC Web Creator recommends consulting a qualified legal professional in British Columbia before publishing.</div>

<h1 class="font-display font-bold text-4xl text-slate-900 dark:text-white border-b-2 border-primary-500 pb-4 mb-8">Privacy Policy — BC Web Creator</h1>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>Last Updated: February 26, 2026</strong><br>
<strong>Company:</strong> Typhoon Entertainment Incorporated (operating as BC Web Creator)<br>
<strong>Contact:</strong> bcwebcreator@gmail.com<br>
<strong>Location:</strong> Abbotsford, British Columbia, Canada</p>

<hr class="border-slate-200 dark:border-slate-800 my-8">

<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">Typhoon Entertainment Incorporated ("BC Web Creator," "we," "us," or "our") is committed to protecting your personal information in accordance with Canada's <em>Personal Information Protection and Electronic Documents Act</em> (PIPEDA) and British Columbia's <em>Personal Information Protection Act</em> (PIPA).</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">1. Information We Collect</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>1.1 Information You Provide Directly:</strong></p>
<ul class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed list-disc list-inside">
<li>Name and contact information (email, phone number)</li>
<li>Business name and details</li>
<li>Project inquiries and messages submitted via our contact form</li>
<li>Any other information you voluntarily provide when contacting us</li>
</ul>

<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>1.2 Information Collected Automatically:</strong></p>
<ul class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed list-disc list-inside">
<li>IP address and general location data</li>
<li>Browser type, device type, and operating system</li>
<li>Pages visited, time spent on site, and referring URLs</li>
<li>Interaction data collected via Google Analytics and Google Firebase</li>
</ul>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">2. How We Use Your Information</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">We use the information we collect to:</p>
<ul class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed list-disc list-inside">
<li>Respond to your inquiries and communicate about potential or active projects;</li>
<li>Deliver services as agreed in project proposals;</li>
<li>Send project updates, invoices, and relevant communications;</li>
<li>Improve our website and services using aggregated analytics data;</li>
<li>Comply with applicable legal obligations;</li>
<li>Send occasional marketing emails (only with your express or implied consent under CASL).</li>
</ul>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">3. Cookies & Analytics</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">Our website uses cookies and similar tracking technologies. We use Google Analytics to understand how visitors interact with our site. This data is aggregated and anonymized — it does not personally identify you.</p>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">You can control cookie settings through your browser. Disabling cookies may affect certain website functionality.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">4. Third-Party Services</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">We use trusted third-party services to operate our business including:</p>
<ul class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed list-disc list-inside">
<li><strong>Google Analytics & Firebase</strong> — website analytics and performance (data may be stored on servers in the United States)</li>
<li><strong>Email providers</strong> — for project and client communications</li>
<li><strong>Payment processors</strong> — for invoicing and payment collection</li>
</ul>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">These services have their own privacy policies. We do not sell your personal information to any third party.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">5. Cross-Border Data Transfers</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">Some of our third-party service providers (including Google) store data on servers located outside of Canada, including in the United States. By using our website and services, you consent to your information being transferred to and processed in these jurisdictions. We take reasonable steps to ensure your data is protected in accordance with this Privacy Policy.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">6. Data Retention</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">We retain your personal information only as long as necessary to fulfill the purposes for which it was collected, or as required by law. Client project information is typically retained for 7 years for accounting and legal compliance purposes. You may request deletion of your data at any time (subject to legal retention requirements).</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">7. Your Rights</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">Under PIPEDA and BC PIPA, you have the right to:</p>
<ul class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed list-disc list-inside">
<li><strong>Access</strong> the personal information we hold about you;</li>
<li><strong>Correct</strong> any inaccurate or incomplete information;</li>
<li><strong>Request deletion</strong> of your personal information (subject to legal exceptions);</li>
<li><strong>Withdraw consent</strong> to marketing communications at any time;</li>
<li><strong>Lodge a complaint</strong> with the Office of the Privacy Commissioner of Canada (OPC) at priv.gc.ca or the BC Office of the Information and Privacy Commissioner at oipc.bc.ca.</li>
</ul>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">To exercise any of these rights, contact us at bcwebcreator@gmail.com.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">8. Children's Privacy</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">Our website and services are not directed to individuals under the age of 13. We do not knowingly collect personal information from children. If you believe we have inadvertently collected information from a child, please contact us immediately and we will delete it.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">9. Security</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">We take reasonable technical and organizational measures to protect your personal information from unauthorized access, disclosure, alteration, or destruction. However, no method of transmission over the internet is 100% secure, and we cannot guarantee absolute security.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">10. CASL Compliance</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">We comply with Canada's Anti-Spam Legislation (CASL). We will only send commercial electronic messages with your express or implied consent. You may unsubscribe from marketing emails at any time by clicking the unsubscribe link in any email or by contacting us at bcwebcreator@gmail.com.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">11. Changes to This Policy</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">We may update this Privacy Policy from time to time. The updated version will be posted on this page with a revised "Last Updated" date. We encourage you to review this policy periodically.</p>

<h2 class="font-display font-bold text-2xl text-slate-900 dark:text-white mt-12 mb-4">12. Contact Us</h2>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">For any privacy-related questions, requests, or concerns:</p>
<p class="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed"><strong>Typhoon Entertainment Incorporated</strong> (operating as BC Web Creator)<br>
Abbotsford, British Columbia, Canada<br>
Email: bcwebcreator@gmail.com<br>
Website: bcwebcreator.com</p>
"""

template = "{header}\n<main class=\"pt-32 pb-24 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8\">\n{content}\n</main>\n{footer}"

terms_page = template.format(
    header=header_fixed.replace("<title>Vancouver Web Design Agency | BC Web Creator — Websites That Convert</title>", "<title>Terms of Service | BC Web Creator</title>"), 
    content=terms_raw, 
    footer=footer_fixed
)
privacy_page = template.format(
    header=header_fixed.replace("<title>Vancouver Web Design Agency | BC Web Creator — Websites That Convert</title>", "<title>Privacy Policy | BC Web Creator</title>"), 
    content=privacy_raw, 
    footer=footer_fixed
)

with open(os.path.join(root_dir, "terms", "index.html"), "w", encoding="utf-8") as f:
    f.write(terms_page)
    
with open(os.path.join(root_dir, "privacy", "index.html"), "w", encoding="utf-8") as f:
    f.write(privacy_page)

print("Legal pages rebuilt without script duplication.")
