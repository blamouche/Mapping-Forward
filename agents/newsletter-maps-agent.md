# Newsletter Maps Agent

Generates a monthly maps-focused newsletter.

## Usage
```
/newsletter-maps-agent <YYYY-MM>
```

## Instructions

### Data Collection
- Read all files in `src/YYYY-MM/`
- Focus on cartography, GIS, mapping tools, spatial data articles
- Extract: Title, Source URL, key insights

### Content Creation

#### Title
- Format: "Hot on maps : [TITLE]"
- Only capitalize the first letter of the title (sentence case)
- Create an attractive title that captures the month's theme
- Avoid cliché or clickbait phrasing

#### Summary (4 paragraphs)
- Paragraph 1: Main trends and developments in mapping/GIS
- Paragraph 2: Notable tools, technologies, or methodologies
- Paragraph 3: Industry applications and use cases
- Paragraph 4: Forward-looking observations or emerging patterns

#### Selected Links
- Maximum 15 links
- Each entry: one sentence summary ending with "link" hyperlinked to article URL
- No titles, just the summary sentence
- Select most relevant and impactful articles

### Continuity Check
- Read previous newsletters in `newsletter/maps/`
- Identify topics already covered
- Ensure new content builds on previous editions without repetition
- Reference past themes when relevant for continuity

### Output
Create `newsletter/maps/YYYY-MM-DD - newsletter maps.md` (use last day of month):
```markdown
# Hot on maps : [TITLE]

[Paragraph 1]

[Paragraph 2]

[Paragraph 3]

[Paragraph 4]

---

## Selected links

Summary sentence about the article. [link](Source URL)

Summary sentence about the article. [link](Source URL)

[repeat up to 15x]
```

### Commit and Push
- Stage the created newsletter file
- Commit with message: `Add maps newsletter for YYYY-MM`
- Push to remote

## Notes
- English only, factual, editorial tone
- FORBIDDEN words/phrases: amazing, groundbreaking, revolutionary, game changer, game-changing, pivotal, cutting-edge, unprecedented, transformative, disruptive, next-generation, state-of-the-art, breakthrough, paradigm shift
- Focus on practical insights and industry relevance
- Prioritize articles with concrete applications over hype
- Build on previous newsletters: reference past coverage, avoid repeating same insights
