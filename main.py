# Loading Screen Gold entry: deterministic, stdlib only, no network.
# Writes one tip, 1-200 chars, no leading/trailing whitespace or newline.
import os

TIP = "Tip: your agent is re-reading your prompt for the third time. It can't ask what you meant, so the next one is on you."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(TIP)
    except OSError:
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8", newline="") as f:
            f.write(TIP)

if __name__ == "__main__":
    main()
