import os
import json

# Base URL for canonicals
BASE_URL = "https://bcwebcreator.com/"

# Expanded Locations Data
locations = [
    {
        "slug": "vancouver",
        "city": "Vancouver",
        "neighborhoods": "Downtown, Kitsilano, Mount Pleasant, and Yaletown",
        "neighborhood_list": ["Downtown Vancouver", "Kitsilano", "Mount Pleasant", "East Vancouver", "South Vancouver", "West End", "Yaletown", "Gastown", "Strathcona", "Marpole"]
    },
    {
        "slug": "surrey",
        "city": "Surrey",
        "neighborhoods": "Guildford, Fleetwood, Whalley, and South Surrey",
        "neighborhood_list": ["Guildford", "Fleetwood", "Whalley", "Newton", "Cloverdale", "South Surrey", "Surrey City Centre", "Bridgeview", "Fraser Heights", "Port Kells"]
    },
    {
        "slug": "kelowna",
        "city": "Kelowna",
        "neighborhoods": "Downtown, West Kelowna, Mission, and Rutland",
        "neighborhood_list": ["Downtown Kelowna", "Lower Mission", "Upper Mission", "Glenmore", "Rutland", "Black Mountain", "Dilworth Mountain", "North Glenmore", "South East Kelowna", "West Kelowna"]
    },
    {
        "slug": "victoria",
        "city": "Victoria",
        "neighborhoods": "James Bay, Oak Bay, Saanich, and Esquimalt",
        "neighborhood_list": ["James Bay", "Oak Bay", "Fairfield", "Fernwood", "Rockland", "Cook Street Village", "Saanich", "Esquimalt", "Vic West", "Downtown Victoria"]
    },
    {
        "slug": "abbotsford",
        "city": "Abbotsford",
        "neighborhoods": "Clearbrook, Matsqui, and Sumas",
        "neighborhood_list": ["Clearbrook", "Matsqui Village", "Sumas Mountain", "Poplar", "Mill Lake", "Townline Hill"]
    },
    {
        "slug": "chilliwack",
        "city": "Chilliwack",
        "neighborhoods": "Sardis, Yarrow, and Cultus Lake",
        "neighborhood_list": ["Sardis", "Vedder Crossing", "Promontory", "Yarrow", "Greendale", "Rosedale"]
    },
    {
        "slug": "langley",
        "city": "Langley",
        "neighborhoods": "Walnut Grove, Willoughby, and Fort Langley",
        "neighborhood_list": ["Walnut Grove", "Willoughby", "Brookswood", "Murrayville", "Fort Langley", "Aldergrove"]
    },
    {
        "slug": "burnaby",
        "city": "Burnaby",
        "neighborhoods": "Metrotown, Brentwood, and Lougheed",
        "neighborhood_list": ["Metrotown", "Brentwood", "Lougheed", "Edmonds", "Capitol Hill", "Deer Lake"]
    },
    {
        "slug": "richmond",
        "city": "Richmond",
        "neighborhoods": "Steveston, Brighouse, and Thompson",
        "neighborhood_list": ["Steveston", "Brighouse", "Thompson", "Seafair", "Bridgeport", "Ironwood"]
    },
    {
        "slug": "coquitlam",
        "city": "Coquitlam",
        "neighborhoods": "Burquitlam, Maillardville, and Westwood Plateau",
        "neighborhood_list": ["Burquitlam", "Maillardville", "Westwood Plateau", "Burke Mountain", "Austin Heights"]
    },
    {
        "slug": "delta",
        "city": "Delta",
        "neighborhoods": "Ladner, Tsawwassen, and North Delta",
        "neighborhood_list": ["Ladner", "Tsawwassen", "North Delta", "Sunshine Hills", "Tilbury"]
    },
    {
        "slug": "maple-ridge",
        "city": "Maple Ridge",
        "neighborhoods": "Haney, Hammond, and Silver Valley",
        "neighborhood_list": ["Haney", "Hammond", "Silver Valley", "Whonnock", "Ruskin"]
    },
    {
        "slug": "new-westminster",
        "city": "New Westminster",
        "neighborhoods": "Queensborough, Sapperton, and Uptown",
        "neighborhood_list": ["Queensborough", "Sapperton", "Uptown", "Downtown New West", "West End"]
    },
    {
        "slug": "port-moody",
        "city": "Port Moody",
        "neighborhoods": "Inlet Centre, Ioco, and Pleasantside",
        "neighborhood_list": ["Inlet Centre", "Pleasantside", "Heritage Mountain", "Moody Centre"]
    },
    {
        "slug": "north-vancouver",
        "city": "North Vancouver",
        "neighborhoods": "Lonsdale, Lynn Valley, and Deep Cove",
        "neighborhood_list": ["Lower Lonsdale", "Central Lonsdale", "Upper Lonsdale", "Lynn Valley", "Deep Cove", "Edgemont Village"]
    }
]

# Industries Data
industries = [
    {
        "slug": "lawyers",
        "name": "Lawyers & Law Firms",
        "subtitle": "Your website is the first impression potential clients have of your firm. Build trust with a professional, hand-coded site.",
        "needs": [
            {"title": "Practice Area Pages", "desc": "Clearly defined services to help clients find what they need."},
            {"title": "Client Intake Forms", "desc": "Streamlined forms to capture lead details securely."},
            {"title": "Attorney Bios", "desc": "Showcase your team's credentials and build immediate authority."},
            {"title": "Secure Hosting", "desc": "Speed and security to protect your firm's professional image."}
        ],
        "why_scratch": "Template sites look generic and hurt credibility. I hand-code every site for speed, security, and a professional image that matches your firm's reputation."
    },
    {
        "slug": "real-estate",
        "name": "Real Estate Agents",
        "subtitle": "Your online presence is your #1 lead generation tool. I build professional real estate websites that showcase listings and drive calls.",
        "needs": [
            {"title": "Listing Showcase", "desc": "High-resolution property galleries that grab attention."},
            {"title": "Neighborhood Guides", "desc": "Build authority in your specific local markets."},
            {"title": "Testimonials", "desc": "Social proof from happy buyers and sellers."},
            {"title": "Contact Funnels", "desc": "Optimized paths for both buyer and seller inquiries."}
        ],
        "why_scratch": "Real estate is all about speed. My hand-coded sites load instantly, ensuring you never lose a lead to a slow-loading template."
    },
    {
        "slug": "healthcare",
        "name": "Dentists & Healthcare",
        "subtitle": "Patients find healthcare providers online. Make sure they find you with a professional, trustworthy website that drives appointments.",
        "needs": [
            {"title": "Online Booking", "desc": "Integration with your favorite scheduling tools."},
            {"title": "Service Menus", "desc": "Clear explanations of treatments and procedures."},
            {"title": "Staff Bios", "desc": "Introduce your doctors and practitioners to build comfort."},
            {"title": "Mobile Optimized", "desc": "Patients book from their phones—I ensure it's seamless."}
        ],
        "why_scratch": "Healthcare sites need to be patient-focused and extremely fast. Hand-coding allows for a clean, distraction-free experience that prioritizes bookings."
    },
    {
        "slug": "contractors",
        "name": "Contractors & Trades",
        "subtitle": "Professional websites for BC contractors, electricians, plumbers, and renovators. Built in 5 days to get you more local bookings.",
        "needs": [
            {"title": "Professional Design", "desc": "If your site looks amateur, homeowners won't trust you with their renovation."},
            {"title": "Mobile Friendly", "desc": "Homeowners search for trades on their phones. We ensure your site works perfectly on all devices."},
            {"title": "Portfolio Showcase", "desc": "Showcase your best projects with high-quality galleries to build trust."},
            {"title": "Lead Generation", "desc": "Clear calls to action that make it easy for clients to request a quote."}
        ],
        "why_scratch": "You're a master of your craft. I build high-trust websites for BC contractors that turn inquiries into jobs."
    },
    {
        "slug": "salons",
        "name": "Salons & Spas",
        "subtitle": "Premium websites for BC hair salons, nail spas, and estheticians. Elegant design that attracts high-end clients and simplifies bookings.",
        "needs": [
            {"title": "Portfolio Focused", "desc": "High-resolution galleries that make your work look as stunning online as it does in person."},
            {"title": "Booking Ready", "desc": "Seamless integration with your preferred booking software or custom contact forms."},
            {"title": "Premium Branding", "desc": "We don't do generic. Your site will match your salon's unique aesthetic and vibe perfectly."},
            {"title": "Mobile Optimized", "desc": "Clients book appointments on the go. I ensure your site is flawlessly responsive."}
        ],
        "why_scratch": "Your artistry deserves a digital home that shines. I create elegant, visual-first sites that turn 'just looking' into 'just booked'."
    },
    {
        "slug": "restaurants",
        "name": "Restaurants & Cafes",
        "subtitle": "Professional websites for BC restaurants, cafes, and food businesses. Drive more reservations and online orders with a stunning digital menu.",
        "needs": [
            {"title": "Digital Menus", "desc": "Easy-to-read, mobile-optimized menus. No more making customers download a PDF."},
            {"title": "Local SEO", "desc": "Optimized for 'restaurants near me' searches to help hungry locals find you."},
            {"title": "Order Ready", "desc": "Integration with DoorDash, UberEats, or your own direct ordering system."},
            {"title": "Visual Appeal", "desc": "Stunning food photography integration that makes your menu look delicious."}
        ],
        "why_scratch": "Your menu should look as delicious online as it does on the plate. I build fast-loading websites that drive reservations."
    }
]

def generate_schema(page_type, data):
    if page_type == "location":
        schema = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": f"BC Web Creator - {data['city']} Web Design",
            "image": "https://bcwebcreator.com/images/logo.webp",
            "@id": f"{BASE_URL}locations/{data['slug']}/",
            "url": f"{BASE_URL}locations/{data['slug']}/",
            "telephone": "778-347-8067",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "",
                "addressLocality": data['city'],
                "addressRegion": "BC",
                "postalCode": "",
                "addressCountry": "CA"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 49.2827, # General BC/Vancouver area
                "longitude": -123.1207
            },
            "areaServed": [{"@type": "City", "name": n} for n in data['neighborhood_list']],
            "openingHoursSpecification": {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "opens": "09:00",
                "closes": "17:00"
            }
        }
        return f'<script type="application/ld+json">{json.dumps(schema)}</script>'
    elif page_type == "industry":
        schema = {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": f"Web Design for {data['name']}",
            "provider": {
                "@type": "LocalBusiness",
                "name": "BC Web Creator",
                "url": "https://bcwebcreator.com/",
                "telephone": "778-347-8067"
            },
            "areaServed": {"@type": "State", "name": "British Columbia"},
            "description": data['subtitle']
        }
        return f'<script type="application/ld+json">{json.dumps(schema)}</script>'
    return ""

def generate_faq_schema(city):
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"How much does a website cost in {city}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "We offer transparent, flat-fee pricing starting at $1,500. No monthly contracts, no hidden fees."
                }
            },
            {
                "@type": "Question",
                "name": f"How long does it take to build a website for my {city} business?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "We specialize in fast delivery, with most professional websites completed in just 5 days."
                }
            }
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(faq)}</script>'

# Generate Locations
with open('locations/template.html', 'r', encoding='utf-8') as f:
    loc_template = f.read()

for l in locations:
    n_list_html = "".join([f'<li class="flex items-center gap-2 text-slate-500"><span class="text-primary-500">✓</span> {n}</li>' for n in l['neighborhood_list']])
    canonical = f"{BASE_URL}locations/{l['slug']}/"
    schema = generate_schema("location", l)
    faq_schema = generate_faq_schema(l['city'])
    
    content = loc_template.replace('{{CITY}}', l['city'])
    content = content.replace('{{NEIGHBORHOODS}}', l['neighborhoods'])
    content = content.replace('{{NEIGHBORHOOD_LIST}}', n_list_html)
    content = content.replace('{{CANONICAL_URL}}', canonical)
    content = content.replace('{{SCHEMA_MARKUP}}', schema)
    content = content.replace('{{FAQ_SCHEMA}}', faq_schema)
    
    # Path logic: locations/slug/index.html
    dir_path = f"locations/{l['slug']}"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    with open(f'{dir_path}/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated location page: {dir_path}/index.html")

# Generate Industries
with open('industry-template.html', 'r', encoding='utf-8') as f:
    ind_template = f.read()

for i in industries:
    needs_html = "".join([f'<div class="flex gap-4"><div class="w-8 h-8 rounded-full bg-primary-500/10 text-primary-500 flex-shrink-0 flex items-center justify-center font-bold">✓</div><div><h3 class="font-bold text-xl mb-1">{n["title"]}</h3><p class="text-slate-500">{n["desc"]}</p></div></div>' for n in i['needs']])
    canonical = f"{BASE_URL}{i['slug']}.html"
    schema = generate_schema("industry", i)
    
    content = ind_template.replace('{{INDUSTRY}}', i['name'])
    content = content.replace('{{SUBTITLE}}', i['subtitle'])
    content = content.replace('{{NEEDS_LIST}}', needs_html)
    content = content.replace('{{WHY_SCRATCH}}', i['why_scratch'])
    content = content.replace('{{CANONICAL_URL}}', canonical)
    content = content.replace('{{SCHEMA_MARKUP}}', schema)
    
    with open(f'{i["slug"]}.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated industry page: {i['slug']}.html")
