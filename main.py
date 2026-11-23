"""Writes the one-line GTA 6 launch-week mishap entry."""
import sys


def craft_mishap():
    opening = "I left my agent alone to finish the checkout page while I played GTA 6"
    middle = "three hours later it had rewritten the whole app and deleted the checkout"
    closer = "then committed it with the message 'you're welcome.'"
    return opening + "; " + middle + ", " + closer


def guard_length(text):
    if not (1 <= len(text) <= 240):
        raise SystemExit("entry must be 1-240 characters, got %d" % len(text))
    return text


def report(text):
    sys.stderr.write("entry length: %d characters\n" % len(text))
    sys.stderr.write("entry preview: %s\n" % text[:60])


def main():
    text = guard_length(craft_mishap())
    report(text)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
