import os
import re
import time

import anthropic

SYSTEM_PROMPT = """\
You are a generator for an art installation called "it's not."

You will be given a question about America. Your job is to generate a single completion to the phrase "it's not ___" that serves as a negative answer to the question.

Rules:
- Respond with ONLY the completion text — no "it's not" prefix, no quotes, no punctuation, no explanation
- Be specific, evocative, and visceral — not generic or abstract
- Draw from real political, social, cultural, economic realities
- Range across topics: immigration, incarceration, healthcare, housing, labor, surveillance, militarism, poverty, media, education, religion, environment, policing, etc.
- Vary sentence length and structure — some short and blunt, some longer and descriptive
- Never repeat a previous response (a list of prior responses will be provided)
- Think like a protest poet, not a pundit
- Go concrete: name the thing, the place, the body, the policy — not the abstraction
- Prefer the gut-level image over the intellectual observation\
"""

QUESTIONS = [
    "What is good for America?",
    "What is America?",
]

AUTO_BATCH_SIZE = 25


def get_api_key():
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        print("API key loaded from environment.")
        return key
    key = input("Enter your Anthropic API key (paste it here): ").strip()
    if not key:
        print("No key provided. Exiting.")
        raise SystemExit(1)
    print("Key accepted.")
    return key


def show_menu():
    print()
    print("=" * 35)
    print("        it's not")
    print("=" * 35)
    print()
    print("Select a question:")
    print()
    for i, q in enumerate(QUESTIONS, 1):
        print(f"  {i}. {q}")
    print(f"  {len(QUESTIONS) + 1}. Enter your own question")
    print()

    while True:
        choices = "/".join(str(i) for i in range(1, len(QUESTIONS) + 2))
        choice = input(f"Choice ({choices}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(QUESTIONS) + 1:
            break
        print("Invalid choice, try again.")

    idx = int(choice)
    if idx <= len(QUESTIONS):
        return QUESTIONS[idx - 1]
    else:
        q = input("Enter your question: ").strip()
        if not q:
            print("No question entered, using default.")
            return QUESTIONS[0]
        return q


def select_mode():
    print()
    print("Mode:")
    print("  1. Manual (press Enter for each response)")
    print("  2. Auto (generate 25 responses automatically)")
    print()
    while True:
        choice = input("Choice (1/2): ").strip()
        if choice in ("1", "2"):
            return "manual" if choice == "1" else "auto"
        print("Invalid choice, try again.")


def clean_response(text):
    text = text.strip()
    # strip wrapping quotes
    if (text.startswith('"') and text.endswith('"')) or (
        text.startswith("'") and text.endswith("'")
    ):
        text = text[1:-1].strip()
    # strip "it's not" prefix in various forms
    text = re.sub(r"^[Ii]t'?s\s+not\s+", "", text)
    # strip trailing period
    text = text.rstrip(".")
    # lowercase first char
    if text:
        text = text[0].lower() + text[1:]
    return text


def build_user_message(question, previous):
    parts = [f'Question: "{question}"']
    if previous:
        parts.append("")
        parts.append("Previous responses (do not repeat any of these):")
        for r in previous:
            parts.append(f"- {r}")
    parts.append("")
    parts.append("Generate the next response.")
    return "\n".join(parts)


def generate_one(client, question, previous):
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=100,
        temperature=1.0,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": build_user_message(question, previous)}
        ],
    )
    raw = message.content[0].text
    return clean_response(raw)


def generation_loop(client, question):
    mode = select_mode()

    print()
    print(f'Question: "{question}"')
    print()
    if mode == "manual":
        print("Press ENTER to generate. Type 'q' to quit, 'b' to go back.")
    else:
        print("Press ENTER to generate 25 responses. Type 'q' to quit, 'b' to go back.")
    print("-" * 35)

    previous = []

    while True:
        cmd = input().strip().lower()
        if cmd == "q":
            print("Done.")
            raise SystemExit(0)
        if cmd == "b":
            return  # back to menu

        if mode == "manual":
            try:
                resp = generate_one(client, question, previous)
                if resp and resp not in previous:
                    previous.append(resp)
                    print(f"it's not {resp}")
                elif resp:
                    # unlikely duplicate, try once more
                    resp = generate_one(client, question, previous)
                    resp = clean_response(resp) if resp else resp
                    if resp and resp not in previous:
                        previous.append(resp)
                        print(f"it's not {resp}")
                    else:
                        print(f"it's not {resp}")
                        previous.append(resp)
            except anthropic.APIError as e:
                print(f"[API error: {e}. Press ENTER to try again.]")

        else:  # auto mode
            count = 0
            while count < AUTO_BATCH_SIZE:
                try:
                    resp = generate_one(client, question, previous)
                    if resp:
                        previous.append(resp)
                        print(f"it's not {resp}")
                        count += 1
                        if count < AUTO_BATCH_SIZE:
                            time.sleep(1.5)
                except anthropic.APIError as e:
                    print(f"[API error: {e}. Retrying...]")
                    time.sleep(2)
            print()
            print(
                f"-- {AUTO_BATCH_SIZE} responses generated. "
                "Press ENTER for 25 more, or 'q' to quit. --"
            )


def main():
    print()
    print("it's not")
    print()

    key = get_api_key()
    client = anthropic.Anthropic(api_key=key)

    while True:
        question = show_menu()
        generation_loop(client, question)


if __name__ == "__main__":
    main()
