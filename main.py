"""Write the 3 AM commit message entry to /output/entry.txt."""
import os

MESSAGE = "fix: reverted prod at 3:04 AM \u2014 root cause was me, I approved my own PR, merged it, and confidently told you it was safe"

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE + "\n")

if __name__ == "__main__":
    main()
