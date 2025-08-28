from pathlib import Path
import sys
import re

def parse_test_log(log_content: str) -> str:
    """
    Parses a pytest log and extracts the short test summary info.
    """
    summary_pattern = r"={10,} short test summary info ={10,}"
    match = re.search(summary_pattern, log_content)

    if not match:
        return ""

    # Extract the summary content, which is everything after the header
    summary_content = log_content[match.end():]
    
    return summary_content.strip()

def main():
    """
    Main function to read log from file and print markdown summary.
    """
    # Read input from file or stdin
    if len(sys.argv) > 1:
        content = Path(sys.argv[1]).read_text()
    else:
        content = sys.stdin.read()

    try:
        summary = parse_test_log(content)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if summary:
        print(summary)

if __name__ == "__main__":
    main()
