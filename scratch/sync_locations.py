import os
import re

def update_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update navigation links (remove trailing slashes, add index.html)
    # Search for links like /locations/vancouver/ or /terms/
    # This regex looks for href="/something/" or href="/something/somethingelse/"
    def link_replacer(match):
        path = match.group(1)
        if path.endswith('/') and not path.startswith('http'):
            return f'href="{path}index.html"'
        return match.group(0)

    content = re.sub(r'href="(/[^"]*/)"', link_replacer, content)

    # 2. Update footer
    # Identify the footer block. The old footer is usually simple.
    footer_pattern = re.compile(r'<footer.*?</footer>', re.DOTALL)
    
    # New footer template
    # We need to customize the "Serving X" part based on the file path
    parent_dir = os.path.basename(os.path.dirname(filepath))
    if parent_dir == 'locations':
        city = os.path.basename(filepath.replace('/index.html', '')).capitalize()
    elif os.path.dirname(filepath).endswith('locations'):
        # For locations/city/index.html, dirname is locations/city
        city = os.path.basename(os.path.dirname(filepath)).capitalize()
    else:
        city = "all of BC"
    
    if city == 'Fraser-valley': city = 'Fraser Valley'
    if city == 'New-westminster': city = 'New Westminster'
    if city == 'North-vancouver': city = 'North Vancouver'
    if city == 'Port-moody': city = 'Port Moody'

    new_footer = f'''    <footer class="py-12 bg-slate-950 border-t border-white/5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row justify-between items-center gap-8">
                <div class="text-center md:text-left">
                    <div class="font-display font-bold text-2xl mb-2 text-white">BC<span class="text-primary-500">WebCreator</span></div>
                    <p class="text-slate-500">Helping new BC businesses get online. Fast. Professional. Affordable.</p>
                </div>
                <div class="flex gap-6 text-slate-400 text-sm">
                    <a href="/terms/index.html" class="hover:text-white transition-colors">Terms</a>
                    <a href="/privacy/index.html" class="hover:text-white transition-colors">Privacy</a>
                    <a href="/index.html#pricing" class="hover:text-white transition-colors">Pricing</a>
                </div>
            </div>
            <div class="mt-12 pt-8 border-t border-white/5 text-center text-slate-600 text-sm">
                <p>&copy; 2025 BC Web Creator. Serving {city} and all of BC.</p>
            </div>
        </div>
    </footer>'''

    content = footer_pattern.sub(new_footer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def main():
    # Update location pages
    root = 'locations'
    for subdir in os.listdir(root):
        dirpath = os.path.join(root, subdir)
        if os.path.isdir(dirpath):
            index_path = os.path.join(dirpath, 'index.html')
            if os.path.exists(index_path):
                update_html_file(index_path)
    
    # Update industry pages in root
    industries = [
        'contractors.html',
        'healthcare.html',
        'lawyers.html',
        'real-estate.html',
        'restaurants.html',
        'salons.html'
    ]
    for industry in industries:
        if os.path.exists(industry):
            update_html_file(industry)

if __name__ == '__main__':
    main()
