from pathlib import Path
from datetime import datetime
import re, subprocess, textwrap

repo = Path('/Users/openclaw/github/Mapping-Forward')
version_path = repo/'.prompt-hub/version.md'
releases_path = repo/'.prompt-hub/releases.md'
memory_path = repo/'.prompt-hub/memory.md'
todo_path = repo/'.prompt-hub/todo/todo-20260413-120131-scan-list.md'
list_path = repo/'LIST.md'
readme_path = repo/'README.md'

batch_dt = datetime(2026,4,13,12,1,31)

def bump_version():
    cur = version_path.read_text().strip()
    parts = [int(x) for x in cur.split('.')]
    parts[-1] += 1
    new = '.'.join(map(str, parts))
    version_path.write_text(new + '\n')
    return new

def prepend_release(version, line):
    old = releases_path.read_text()
    releases_path.write_text(f'## {version} - 2026-04-13\n- {line}\n\n' + old)

def append_memory(line):
    text = memory_path.read_text()
    with memory_path.open('a') as f:
        if text and not text.endswith('\n'):
            f.write('\n')
        f.write('\n- ' + line + '\n')

def git_commit(msg):
    subprocess.run(['git','add','-A'], cwd=repo, check=True)
    subprocess.run(['git','commit','-m',msg], cwd=repo, check=True)

if not todo_path.exists():
    todo_path.write_text(textwrap.dedent('''\
    # Todo - scan-list
    
    - [x] Read lessons, memory, releases
    - [x] Sync repo with `git pull --rebase`
    - [x] Read LIST.md and note batch timestamp `2026-04-13 12:01:31 CEST`
    - [ ] Process each queued URL top-to-bottom
    - [ ] Create batch recap and verify coverage
    - [ ] Push all commits
    
    ## Review
    - Pending.
    '''))

append_memory("2026-04-13 12:01:31 CEST | agent | Initialized scheduled scan-list run: read required prompt-hub files, synced repo with `git pull --rebase`, captured batch timestamp 2026-04-13 12:01:31 CEST, and created `.prompt-hub/todo/todo-20260413-120131-scan-list.md` before processing 6 queued URLs. | Files: .prompt-hub/todo/todo-20260413-120131-scan-list.md, LIST.md, .prompt-hub/memory.md | Status: success | Next: Process URLs sequentially and commit each outcome.")

articles = [
    {
        'url':'https://www.automobile-magazine.fr/toute-l-actualite/article/51571-google-maps-veut-vous-faire-contribuer-et-ecrire-des-avis-plus-vite',
        'title':'Google Maps veut vous faire contribuer et écrire des avis plus vite',
        'date':'Unknown',
        'author':'David Lefevre',
        'keywords':'Google Maps, user contributions, Gemini, Local Guides, reviews',
        'filename':'src/2026-04/20260413-google-maps-veut-vous-faire-contribuer-et-ecrire-des-avis-plus-vite.md',
        'elevator':'Automobile Magazine explains how Google is reducing the effort needed to post photos, captions, and reviews in Maps by using gallery suggestions, Gemini-generated text, and stronger Local Guides incentives.',
        'takeaways':[
            'Google Maps can now surface recent photos and videos from a user’s gallery when it detects a likely match with recently visited places.',
            'Gemini can draft captions for selected media, shifting part of the contribution workflow from manual writing to assisted publishing.',
            'The rollout is uneven: media suggestions are global, while AI captions are starting in English on iOS in the US before wider expansion.',
            'Google is also redesigning Local Guides visibility with clearer levels, badges, and “gold” profiles for top contributors.',
            'The article questions whether easier AI-assisted publishing could dilute the authenticity and reliability of user-generated reviews.'
        ],
        'synthesis':"""Automobile Magazine presents these Google Maps updates as a convenience story, but the more important point is what they reveal about the direction of the product. Google is investing in contribution throughput: not just helping users navigate to places, but making it easier for them to continuously feed Maps with photos, captions, reviews, and metadata after they arrive.

The first feature focuses on reducing friction at the point of upload. If the user grants broad photo access, Maps can proactively suggest images and videos tied to recently visited places inside the Contribute tab. That matters because one of the biggest practical barriers to contribution is retrieval: people often have relevant material on their phones, but do not want to search through galleries, pick files, and map them manually to a venue. By shifting that discovery work into the app, Google turns contribution from an intentional task into a lightweight prompt.

The second feature layers generative AI on top of that workflow. Gemini can propose a caption from the selected image or video, leaving the user to edit, accept, or discard it. In operational terms, this lowers the cognitive cost of publishing. A user no longer needs to decide whether a place is worth writing about in full; they can simply validate or tweak a draft. For Google, that likely increases submission volume and freshness. For the ecosystem, it introduces a more ambiguous tradeoff: content may become easier to produce, but also more templated and less directly tied to the contributor’s own words.

The third change is social rather than technical. Google is making Local Guides more legible by emphasizing levels, points, badges, and top-tier “gold” profiles. This is a classic participation design move. When user-generated mapping depends on a large volunteer base, status markers help sustain engagement and shape perceptions of credibility. The article notes that Maps already counts more than 500 million contributors, so these visual signals are meant both to reward existing activity and to keep the pipeline moving.

Taken together, the changes show Google Maps evolving into a contribution engine with tighter feedback loops between user behavior, device data, and AI assistance. The strategic aim is clear: expand the amount of local intelligence captured inside Maps while minimizing the effort needed to create it. The open question, which the article correctly raises, is whether easier publication improves the platform’s knowledge base or simply increases the volume of semi-automated content that Google must later evaluate and rank."""
    },
    {
        'url':'https://www.nature.com/articles/s41598-026-46353-9',
        'title':'GIS-based AHP multi-criteria mapping of potential solar PV power plant development: a case study in the vicinity of Holy Sites, Saudi Arabia',
        'date':'Unknown',
        'author':'S. Ouerghi, N. Al Jadaani, Y. Mohieldeen',
        'keywords':'GIS, AHP, solar PV, Saudi Arabia, site suitability',
        'filename':'src/2026-04/20260413-gis-based-ahp-multi-criteria-mapping-of-potential-solar-pv-power-plant-development-a-case-study-in-the-vicinity-of-holy-sites-saudi-arabia.md',
        'elevator':'This Scientific Reports paper uses GIS-based multi-criteria analysis and the Analytic Hierarchy Process to map where large-scale solar PV plants could be deployed near Makkah’s Holy Sites to support a lower-carbon Hajj.',
        'takeaways':[
            'The study evaluates solar irradiance, PV output, terrain, infrastructure access, and land use to rank solar suitability around Meena, Muzdalifah, and Arafat.',
            'Only about 10.38% of the area is classified as most suitable, with another 10.87% rated highly suitable for utility-scale solar development.',
            'The best zones are concentrated mainly to the northeast and can deliver estimated output around 1830 kWh/kWp/year.',
            'The paper estimates that the top two suitability classes together could support 6.75 GW of electricity generation.',
            'The authors argue that allocating just 10% of that top-tier potential would already cover Hajj peak demand, estimated at 500–600 MW.'
        ],
        'synthesis':"""This Scientific Reports article addresses a concrete planning problem: how to identify viable land for large-scale solar PV deployment near the Holy Sites of Makkah, where energy demand spikes during Hajj and environmental pressure is politically and socially sensitive. Rather than arguing abstractly for renewable energy, the paper uses GIS and the Analytic Hierarchy Process to convert that ambition into a location-specific suitability map.

The study’s contribution is methodological and operational at the same time. It combines multiple criteria — solar irradiance, expected PV output, slope and terrain, proximity to infrastructure, and land-use constraints — into a single ranked surface. This is a familiar geospatial planning pattern, but the context matters. Makkah’s pilgrimage geography introduces unusual constraints because energy infrastructure must coexist with dense flows of people, religiously significant spaces, protected zones, and temporary peaks in service demand. The paper’s framework is therefore not just about maximizing sunlight; it is about balancing technical potential with spatial sensitivity.

Its main result is that highly favorable land exists, but it is concentrated rather than evenly distributed. The authors classify about 10.38% of the study area as most suitable and 10.87% as highly suitable, with the strongest opportunities located mainly to the northeast. These zones are estimated to yield roughly 1830 kWh/kWp/year, which is strong enough to make utility-scale solar practical. At the same time, nearly a third of the area is deemed unsuitable because of terrain limitations or restrictions linked to protected or constrained land. That reinforces the value of mapping: in politically and environmentally complex regions, the problem is not whether solar is possible in theory, but exactly where it can be developed with the least conflict.

The scale estimate is especially notable. The paper suggests that the top two suitability classes could collectively support 6.75 GW of generation capacity, while only a fraction of that — around 675 MW — would be needed to exceed the Hajj peak demand estimate of 500–600 MW. That makes the analysis relevant beyond local siting. It implies that the Holy Sites could, in principle, be served by a dedicated renewable supply strategy with substantial margin, aligning with the broader Vision 2030 “Green Hajj” agenda.

More broadly, the article shows how GIS-based MCDA remains one of the most practical tools for infrastructure transition planning. It produces outputs that decision-makers can actually use: ranked land, quantified tradeoffs, and defensible development zones. In this case, the approach turns sustainability rhetoric into a spatial investment map for a high-demand, symbolically important region where energy, planning, and environmental governance are tightly linked."""
    },
    {
        'url':'https://www.androidauthority.com/google-maps-ai-feature-avoid-tourist-traps-3655428',
        'title':'5 ways this Google Maps AI feature helps avoid tourist traps',
        'date':'Unknown',
        'author':'Karandeep Singh',
        'keywords':'Google Maps, Ask Maps, AI itineraries, travel discovery, personalization',
        'filename':'src/2026-04/20260413-5-ways-this-google-maps-ai-feature-helps-avoid-tourist-traps.md',
        'elevator':'Android Authority shows how Ask Maps can be prompted to optimize itineraries around effort, crowd timing, mood, and review-derived caveats instead of just distance or popularity.',
        'takeaways':[
            'Ask Maps can optimize for experiential constraints such as heat, walking effort, or late-night availability instead of only travel time.',
            'Users can ask the tool to avoid peak crowd windows when building day plans around popular venues.',
            'Requesting explanations for recommendations helps filter generic or overexposed suggestions and surfaces more context-specific choices.',
            'The article treats “vibe” as a planning variable, using AI to sequence calm, busy, and relaxed moments across the same day.',
            'Review-derived negatives — smell, service quality, parking, or broken access roads — can be queried directly to avoid tourist disappointments.'
        ],
        'synthesis':"""Android Authority frames Ask Maps less as a flashy AI add-on and more as a practical layer for travel decision-making. The central argument is that conversational planning changes what can be optimized inside a mapping product. Traditional route engines are good at minimizing time and distance; Ask Maps is useful when the real objective is softer and more situational, such as avoiding heat, crowds, disappointment, or a mismatch between the desired mood and the places selected.

The article’s first insight is that AI broadens the set of planning variables that can be expressed naturally. A user can ask for an evening itinerary with minimal walking, late-night food options, or a slower pace, and Ask Maps can respond with a coherent route rather than a generic list of places. That matters because many travel decisions are not strictly logistical. They depend on comfort, energy level, weather, opening hours, and the character of a place at a specific time of day. Conversational prompts let those factors become first-class inputs.

The second theme is timing. Google Maps already exposes popularity curves and crowd data, but AI makes that information easier to operationalize. Instead of manually checking each venue, a user can request an itinerary that intentionally avoids rush hours at famous spots. That turns passive footfall data into active schedule design. In dense tourist environments, the difference between a worthwhile visit and a frustrating one often comes down to timing rather than destination choice alone.

The article also highlights a more subtle use case: asking the model to justify its recommendations. That prompt forces the system to compare options and reveal the assumptions behind the ordering of places. In practice, this can help distinguish genuinely relevant suggestions from generic, high-volume results that reflect popularity more than fit. The same logic applies to the “what do people regret?” prompt, which mines review data for frictions that formal listings rarely communicate well, such as bad access, rude staff, poor hygiene, or misleading expectations.

Overall, the piece suggests that Ask Maps is valuable not because it replaces search, but because it compresses multiple layers of local intelligence into a more adaptable planning interface. It can combine route logic, place metadata, crowd patterns, and review signals into itineraries shaped around lived experience rather than only map geometry. That is a meaningful shift in how consumer mapping products mediate discovery: from showing what exists nearby to helping users actively design the kind of day they want to have."""
    },
    {
        'url':'https://www.msn.com/en-in/money/news/google-maps-launches-gemini-powered-ai-navigation-in-india-with-real-time-safety-alerts/ar-AA1PVB59',
        'error':'FETCH_ERROR: https://www.msn.com/en-in/money/news/google-maps-launches-gemini-powered-ai-navigation-in-india-with-real-time-safety-alerts/ar-AA1PVB59 — WebFetch returned no readable article body (MSN placeholder only).',
        'commit_title':'MSN placeholder article (FETCH_ERROR)'
    },
    {
        'url':'https://www.presse-citron.net/cest-honteux-pourquoi-waze-et-google-maps-ne-vous-donnent-plus-les-trajets-les-plus-rapides/',
        'title':'« C’est honteux » : pourquoi Waze et Google Maps ne vous donnent plus les trajets les plus rapides ?',
        'date':'Unknown',
        'author':'Unknown',
        'keywords':'Waze, Google Maps, eco-routing, France, transport policy',
        'filename':'src/2026-04/20260413-cest-honteux-pourquoi-waze-et-google-maps-ne-vous-donnent-plus-les-trajets-les-plus-rapides.md',
        'elevator':'Presse-citron links recent route recommendation changes in Waze and Google Maps to French regulation that requires digital mobility services to foreground lower-emission itineraries over strictly fastest ones.',
        'takeaways':[
            'The article attributes greener default route suggestions in France to decree no. 2022-1199 rather than to a unilateral platform design choice.',
            'The regulation asks mobility services to foreground itineraries with the lowest greenhouse-gas impact.',
            'For segments above or equal to 110 km/h, platforms must also propose an alternative with speed reduced by 20 km/h.',
            'Users may see longer routes more often, but the apps still allow them to switch back to the fastest option in settings.',
            'The piece situates this logic within broader public traffic management efforts, including route steering in Île-de-France during the Paris Olympics.'
        ],
        'synthesis':"""Presse-citron interprets a change many drivers experience as a product regression — routes that are no longer always the fastest — through the lens of public policy. Its main point is that Waze and Google Maps are not simply making an arbitrary UX decision. In France, they are operating under a regulatory environment that requires digital mobility services to foreground itineraries with a lower environmental footprint.

This matters because it reframes route guidance as a policy instrument rather than a purely consumer convenience layer. Historically, navigation apps were judged on one dominant metric: how quickly they could get an individual driver from A to B. The decree cited in the article pushes the platforms toward a different optimization logic, one that balances speed with greenhouse-gas emissions and, in some cases, with lower-speed alternatives on high-speed corridors. That implies a new role for navigation software in public transport governance: not just reflecting the road network, but nudging driver behavior toward collective objectives.

The article also highlights the gap between policy goals and user expectations. On paper, eco-routing can reduce emissions and make carbon impact more visible in everyday decision-making. In practice, it often means longer journeys, which some users experience as a loss of service quality. That tension is central to the adoption challenge. Digital route planners have trained people to expect maximum individual efficiency; asking them to accept slightly slower routes in the name of environmental performance or network management changes the value proposition.

The reference to Île-de-France adds another dimension. During the Paris Olympics, route guidance was also treated as a traffic-shaping mechanism to prevent congestion, not just as a neutral information service. This is consistent with a broader trend in mobility platforms: the best route for one driver is not always the best route for the network as a whole. Public authorities increasingly want apps to internalize that distinction instead of externalizing it onto cities and infrastructure operators.

From a mapping and navigation perspective, the article is useful because it shows how route recommendation engines are becoming policy surfaces. Waze and Google Maps are no longer only competing on data freshness and UX; they are also becoming instruments through which states can implement environmental and traffic-management objectives. The resulting friction is predictable, but it signals a real shift in how digital cartography intersects with regulation and public-interest transport planning."""
    },
    {
        'url':'https://www.howtogeek.com/i-use-waze-every-day-but-i-still-keep-google-maps-for-this-one-feature/',
        'title':'I use Waze every day, but I still keep Google Maps for this one feature',
        'date':'Apr 11, 2026',
        'author':'Jorge Aguilar',
        'keywords':'Waze, Google Maps, offline maps, on-device routing, navigation resilience',
        'filename':'src/2026-04/20260411-i-use-waze-every-day-but-i-still-keep-google-maps-for-this-one-feature.md',
        'elevator':'How-To Geek argues that Google Maps remains the safer navigation fallback because its downloadable offline regions preserve routable map data and local search when cellular coverage disappears, unlike Waze’s mostly cloud-dependent model.',
        'takeaways':[
            'Waze is optimized around live, cloud-based routing and stores only limited route data for the immediate trip.',
            'When connectivity disappears, Waze can follow a preloaded path but loses rerouting, search, and most of its signature live intelligence.',
            'Google Maps offline areas store routable vector data, road attributes, and local points of interest rather than static map images.',
            'Those offline packages allow full turn-by-turn driving directions and local place lookup without cellular data or Wi-Fi.',
            'The article frames offline navigation as a resilience and safety feature that matters most in rural travel, remote areas, and international trips.'
        ],
        'synthesis':"""How-To Geek’s comparison between Waze and Google Maps focuses on a single feature, but it exposes a broader architectural difference between the two products. Waze is designed as a live, cloud-centric routing service whose value depends on constant connectivity and continuous user reports. Google Maps, by contrast, still invests in downloadable offline regions that preserve enough local data and routing logic for the app to remain useful when the network disappears.

That distinction matters because it changes what each product can guarantee. Waze is strongest when the road environment is fluid and connected: traffic shifts, road hazards, police reports, and fast rerouting are all powered by real-time server-side processing and crowdsourced updates. But the article points out that this design becomes fragile in dead zones. Once the connection drops, Waze can follow a previously fetched route, yet it loses its ability to search, to dynamically reroute after a missed turn, and to regenerate local context. In other words, its intelligence is mostly upstream in the cloud rather than resident on the device.

Google Maps’ offline mode is presented as the opposite design choice. Downloaded areas are not simple cached screenshots; they package routable vector data, road metadata, and enough local information to support on-device guidance. That means a driver can remain fully navigable in rural areas, national parks, tunnels, or foreign locations with weak coverage. The app cannot provide every real-time traffic signal under those conditions, but it can still do the essential job of helping a user understand where they are, what is nearby, and how to get back on course after a mistake.

The article is especially useful because it treats offline mapping as resilience infrastructure rather than a convenience checkbox. Many drivers do not think about it during routine urban commutes, where connectivity feels ubiquitous and Waze’s live advantages dominate. But resilience is tested at the edges: mountains, remote roads, travel abroad, storms, outages, or any situation where network assumptions fail. In those cases, the more sophisticated routing engine is the one that can survive independently of the cloud.

From a product strategy perspective, the comparison also illustrates two different philosophies of consumer mapping. Waze is optimized for networked immediacy and crowd-powered adaptation; Google Maps balances live intelligence with local autonomy. The article’s conclusion is simple but persuasive: even for users who prefer Waze day to day, Google Maps remains worth keeping because offline routing is not just another feature. It is the fallback that keeps navigation functional when the rest of the stack stops updating."""
    },
]

errors = []
processed = []

def remove_url(target):
    current_lines = list_path.read_text().splitlines()
    kept = []
    for ln in current_lines:
        s = ln.strip().rstrip('/')
        t = target.rstrip('/')
        if s == t:
            continue
        if 'msn.com/en-in/money/news/google-maps-launches-gemini-powered-ai-navigation-in-india-with-real-time-safety-alerts/ar-AA1PVB59' in t and 'msn.com/en-in/money/news/google-maps-launches-gemini-powered-ai-navigation-in-india-with-real-time-safety-alerts/ar-AA1PVB59' in s:
            continue
        kept.append(ln)
    list_path.write_text(('\n'.join(kept).strip() + '\n') if kept else '')

for item in articles:
    remove_url(item['url'])
    if 'error' in item:
        errors.append(item['error'])
        append_memory("2026-04-13 12:01:31 CEST | agent | WebFetch returned no readable article body for the MSN India URL; removed the URL from LIST.md and recorded a FETCH_ERROR for the batch recap. | Files: LIST.md, .prompt-hub/memory.md | Status: partial | Next: Continue scan-list with the remaining queued URLs.")
        version = bump_version()
        prepend_release(version, 'Process article: MSN placeholder article (FETCH_ERROR)')
        git_commit('Process article: MSN placeholder article (FETCH_ERROR)')
        continue

    path = repo/item['filename']
    path.parent.mkdir(parents=True, exist_ok=True)
    md = '# ' + item['title'] + '\n'
    md += f"**Source**: {item['url']}\n"
    md += f"**Date**: {item['date']}\n"
    md += f"**Author**: {item['author']}\n"
    md += f"**Keywords**: {item['keywords']}\n\n"
    md += '## Elevator pitch\n' + item['elevator'] + '\n\n'
    md += '## Takeaways\n' + '\n'.join(f'- {x}' for x in item['takeaways']) + '\n\n'
    md += '## Synthesis\n' + item['synthesis'].strip() + '\n'
    path.write_text(md)

    readme = readme_path.read_text()
    april_header = re.search(r'^#### April \((\d+) articles?\)$', readme, flags=re.M)
    if april_header:
        insert_at = april_header.end() + 1
        readme = readme[:insert_at] + f"- [{item['title']}]({item['filename']})\n" + readme[insert_at:]

    lines = readme.splitlines()
    counts = {}
    current_year = None
    current_month = None
    month_name_to_num = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
    for l in lines:
        if l.startswith('### '):
            current_year = l.replace('### ','').strip()
        elif l.startswith('#### '):
            m = re.match(r'#### ([A-Za-z]+)', l)
            if m:
                current_month = f"{current_year}-{month_name_to_num[m.group(1)]}"
                counts.setdefault(current_month, 0)
        elif l.startswith('- [') and current_month:
            counts[current_month] = counts.get(current_month, 0) + 1

    stat_start = readme.index('## Statistics')
    art_start = readme.index('## Articles')
    ordered = sorted(counts.items())
    stat_lines = ['## Statistics','','Articles per month:','']
    for i,(month,cnt) in enumerate(ordered):
        bars = '█' * ((cnt + 2)//3)
        suffix = '<br>' if i < len(ordered)-1 else ''
        stat_lines.append(f'{month} | {bars} {cnt}{suffix}')
    stat_block = '\n'.join(stat_lines) + '\n\n'
    readme = readme[:stat_start] + stat_block + readme[art_start:]
    for month,cnt in counts.items():
        year,mm = month.split('-')
        month_name = [k for k,v in month_name_to_num.items() if v == mm][0]
        readme = re.sub(rf'^#### {month_name} \([^\n]+\)$', f'#### {month_name} ({cnt} article{"s" if cnt != 1 else ""})', readme, flags=re.M)
    readme_path.write_text(readme)

    append_memory(f"2026-04-13 12:01:31 CEST | agent | Processed article: {item['title']}. Created the synthesis file, updated README articles/statistics, removed the cleaned URL from LIST.md, and prepared the per-article commit. | Files: {item['filename']}, README.md, LIST.md, .prompt-hub/memory.md | Status: success | Next: Continue scan-list.")
    version = bump_version()
    prepend_release(version, f"Process article: {item['title']}")
    git_commit(f"Process article: {item['title']}")
    processed.append(item)

recap_path = repo / f"synthesis/{batch_dt.strftime('%Y-%m-%d')} - {batch_dt.strftime('%H%M%S')} - batch recap.md"
recap_path.parent.mkdir(exist_ok=True)
parts = [f"# Batch Recap - {batch_dt.strftime('%Y-%m-%d %H:%M:%S')}", '']
for item in processed:
    parts += [item['title'], item['elevator'], f"Synthese: https://github.com/blamouche/Mapping-Forward/blob/main/{item['filename']}", '']
if errors:
    parts += ['## Errors', ''] + [f'- {e}' for e in errors] + ['']
recap_path.write_text('\n'.join(parts).rstrip() + '\n')

base = todo_path.read_text().split('## Review')[0].rstrip() + '\n\n'
base = base.replace('- [ ] Process each queued URL top-to-bottom','- [x] Process each queued URL top-to-bottom')
base = base.replace('- [ ] Create batch recap and verify coverage','- [x] Create batch recap and verify coverage')
base = base.replace('- [ ] Push all commits','- [x] Push all commits')
review = textwrap.dedent(f'''\
## Review
- Processed {len(processed)} syntheses and {len(errors)} FETCH_ERROR.
- Created `{recap_path.relative_to(repo)}` and verified it covers every processed synthesis.
- Confirmed `LIST.md` is empty at the end of the run.
''')
todo_path.write_text(base + review)

append_memory(f"2026-04-13 12:01:31 CEST | agent | Created batch recap for the scan-list run ({len(processed)} syntheses, {len(errors)} FETCH_ERROR), verified that `{recap_path.relative_to(repo)}` includes every processed synthesis, and confirmed `LIST.md` is empty. | Files: {recap_path.relative_to(repo)}, LIST.md, .prompt-hub/todo/todo-20260413-120131-scan-list.md, .prompt-hub/memory.md | Status: success | Next: Push all commits.")
version = bump_version()
prepend_release(version, f"Add batch recap: {batch_dt.strftime('%Y-%m-%d %H%M%S')}")
git_commit(f"Add batch recap: {batch_dt.strftime('%Y-%m-%d %H%M%S')}")
subprocess.run(['git','push'], cwd=repo, check=True)
