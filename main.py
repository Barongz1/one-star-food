"""One Star, Five Stars for the Food — entry for make.fun.

Writes one sentence to /output/entry.txt.
"""
import os

# The review: an alien tourist gives Earth one star — broken gravity, endless queues — but the noodles almost make the abduction worth it.
TEXT = "One star. The gravity is broken, the locals queue for everything, but the noodles alone almost make the abduction worth it."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
