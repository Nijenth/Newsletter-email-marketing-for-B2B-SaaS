# Newsletter / Email Marketing for B2B SaaS — Research

This is my research project for the 100Hires growth/marketing assignment. I picked **newsletter and email marketing for B2B SaaS** as my topic.

## What this is

I found 10 people who actually practice newsletter and email marketing for B2B SaaS, not just write generic tips about it, and collected their content (YouTube/podcast transcripts plus one key written framework) so it's organized and annotated in one place. This is raw research, not a finished playbook.

## Why I picked these 10

My bar was simple: has this person actually built or run a real newsletter, email program, or email-focused company? I cared more about verifiable track records than follower counts, and I deliberately spread the list across different angles, newsletter economics, SaaS lifecycle email, cold outreach, onboarding sequences, and copywriting craft, instead of picking 10 people who'd all teach the same newsletter-growth tactics.

| Expert | Distinct angle |
|---|---|
| **Emily Kramer** | MKT1; built marketing at Asana/Carta/Astro from scratch, uses Claude Code in her own newsletter production |
| **Val Geisler** | SaaS lifecycle/onboarding email specialist; ex-ConvertKit, clients include Stripe and Trello |
| **Jay Schwedelson** | Subjectline.com; B2B email optimization research, testable over opinion-based |
| **Matt McGarry** | GrowLetter; newsletter business mechanics and monetization |
| **Kyle Poyar** | Ex-OpenView; the data/benchmarks behind why a lifecycle strategy matters |
| **Sujan Patel** | Built Mailshake; runs multiple B2B SaaS companies himself |
| **Ramli John** | Product-Led Onboarding author; the EUREKA onboarding email framework |
| **Harry Dry** | Marketing Examples; the copywriting craft underneath every email on this list |
| **Will Allred** | Lavender cofounder; billions of sales emails analyzed for what actually works |
| **Florin Tatulea** | 65x'd Loopio revenue, 20x'd Common Room outbound pipeline through cold email |

Full notes, links, and why I picked each one: [`research/sources.md`](research/sources.md)

## What changed how I think about this topic

Going in, I assumed newsletters were mostly about writing well and growing a list. What actually shifted my thinking was Matt McGarry's data on newsletter economics, he points out B2B newsletter sponsorships run $100-500 CPM versus $25-40 for typical consumer newsletters. That's not a small gap. It reframed why B2B newsletters specifically are worth building as a real channel, not just as "thought leadership" on the side.

The hardest judgment call wasn't finding 10 names, it was deciding how many people to include from each angle. It would've been easy to grab 10 newsletter-growth people since that's the easiest category to find strong names in. I made myself spread across newsletter economics, SaaS lifecycle email, cold outreach, onboarding, and copywriting craft instead, because I think a useful future playbook needs all of those, not just "how to grow a newsletter."

## What I collected

### `research/youtube-transcripts/` — 9 transcripts

Real video/podcast content for 9 of the 10 experts, using the free, open-source `youtube-transcript-api` Python library. No API key, no cost. Script included: [`fetch_transcripts.py`](fetch_transcripts.py).

### `research/other/` — 1 deep-dive

Val Geisler is the one expert without a clean YouTube match, so I went straight to her original MicroConf talk instead, where she lays out her Dinner Party Strategy framework for SaaS onboarding emails. I didn't pad this folder with weak material for every expert, I only added something here when it genuinely added value the transcripts couldn't.

### A note on LinkedIn

I didn't scrape LinkedIn for this research, LinkedIn's Terms of Service prohibit it. Anywhere I reference someone's LinkedIn content, it's manually read and summarized in my own words, with a link back to the original.

### A note I want to be upfront about

I initially considered Chase Dimond for this list, he's driven over $200M in email-attributable revenue. I cut him after realizing his practice is almost entirely ecommerce/DTC, not B2B SaaS. Including him would've been picking an impressive name over a genuinely fitting one, which is exactly what this assignment said not to do. Florin Tatulea replaced him, fully B2B SaaS-native.

## A few notes on how I did this

* I verified every name myself through web search rather than trusting existing "top X" lists at face value.
* For copyrighted material I summarized and annotated things in my own words, with links back to originals, instead of copying anything verbatim.
* YouTube transcripts are saved as-fetched (the actual captions), not paraphrased, that's just how transcripts work.

## Repo structure
research/

├── sources.md                  # All 10 experts: links, dates, why I picked them

├── youtube-transcripts/        # 9 real transcripts, one file per video

└── other/                      # Val Geisler's Dinner Party Strategy framework

fetch_transcripts.py             # Script I used to pull YouTube transcripts


## Tools I used

* **Claude** (claude.ai) — research, vetting, summarizing, repo structure
* **`youtube-transcript-api`** (Python, free/open-source) — transcript collection
* **Git/GitHub** — committed regularly as I went