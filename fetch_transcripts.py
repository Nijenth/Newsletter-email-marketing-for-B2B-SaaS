"""
Fetch YouTube transcripts for the 10 newsletter/email marketing experts (B2B SaaS).
Uses the free youtube-transcript-api library (no cost).
Saves each transcript as a clean markdown file in research/youtube-transcripts/
"""

from youtube_transcript_api import YouTubeTranscriptApi
import os

# Each entry: (filename-safe-slug, expert name, video title, video ID, source URL)
VIDEOS = [
    ("emily-kramer-dear-marketers-mailbag", "Emily Kramer",
     "Dear Marketers, We have more Questions! | Mailbag Ep",
     "Eg8KjnXlr_A", "https://www.youtube.com/watch?v=Eg8KjnXlr_A"),

    ("jay-schwedelson-email-marketing-converts", "Jay Schwedelson",
     "117: Email Marketing that Converts with Jay Schwedelson",
     "9m85a4sGScw", "https://www.youtube.com/watch?v=9m85a4sGScw"),

    ("matt-mcgarry-newsletter-growth-tactics", "Matt McGarry",
     "Newsletter Growth Tactics with Matt McGarry",
     "DxP5I15yESI", "https://www.youtube.com/watch?v=DxP5I15yESI"),

    ("kyle-poyar-software-pricing-ai-era", "Kyle Poyar",
     "Episode 16 | Kyle Poyar: Software Pricing in the AI Era",
     "lNEZVo5Ci8Y", "https://www.youtube.com/watch?v=lNEZVo5Ci8Y"),

    ("sujan-patel-gaining-first-customers", "Sujan Patel",
     "Gaining Your First Customers w/ Sujan Patel",
     "MhAwRqjO24o", "https://www.youtube.com/watch?v=MhAwRqjO24o"),

    ("harry-dry-learn-copywriting-76-minutes", "Harry Dry",
     "Learn Copywriting in 76 Minutes",
     "TUMjnmfsPeM", "https://www.youtube.com/watch?v=TUMjnmfsPeM"),

    ("will-allred-cold-email-breakdowns", "Will Allred",
     "Episode 197: Cold email breakdowns with Will Allred",
     "eGibkMf0mes", "https://www.youtube.com/watch?v=eGibkMf0mes"),

    ("florin-tatulea-cold-email-secrets", "Florin Tatulea",
     "Cold Email Secrets from Outbound Expert Florin Tatulea",
     "aaFjjDBBEzk", "https://www.youtube.com/watch?v=aaFjjDBBEzk"),
]


def fetch_and_save(slug, expert, title, video_id, url, out_dir):
    print(f"Fetching: {expert} — {title}")
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched = ytt_api.fetch(video_id)
        full_text = " ".join(snippet.text for snippet in fetched)

        filename = os.path.join(out_dir, f"{slug}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Expert:** {expert}\n\n")
            f.write(f"**Source:** {url}\n\n")
            f.write("---\n\n")
            f.write(full_text)

        print(f"  Saved -> {filename}\n")
        return True
    except Exception as e:
        print(f"  FAILED: {e}\n")
        return False


def main():
    out_dir = os.path.join("research", "youtube-transcripts")
    os.makedirs(out_dir, exist_ok=True)

    succeeded = 0
    failed = []

    for slug, expert, title, video_id, url in VIDEOS:
        ok = fetch_and_save(slug, expert, title, video_id, url, out_dir)
        if ok:
            succeeded += 1
        else:
            failed.append((expert, title, url))

    print("=" * 50)
    print(f"Done: {succeeded}/{len(VIDEOS)} transcripts saved successfully.")
    if failed:
        print("\nFailed (likely no captions available, or video is region/age-restricted):")
        for expert, title, url in failed:
            print(f"  - {expert}: {title}\n    {url}")


if __name__ == "__main__":
    main()