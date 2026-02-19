# BUILD PLAN: "it's not"

## Overview
A Python CLI tool for an art installation featuring a receipt printer that endlessly generates negative responses to questions about America. Uses the Claude API to generate evocative, poetic one-liner responses in the format "it's not [x]".

## Core Behavior
- Each response is a single "it's not ___" statement
- Responses should be evocative, specific, politically charged, poetic — not generic
- Every press of Enter generates one new response
- No response should repeat within a session
- Tone: direct, visceral, honest — like protest art on a receipt

## Technical Stack
- Python 3.10+
- `anthropic` Python SDK for Claude API calls
- No other external dependencies (use only stdlib + anthropic)

## File Structure
```
its-not/
├── its_not.py          # Main script (single file, keep it simple)
├── requirements.txt    # Just: anthropic
└── README.md           # Setup instructions for non-technical users
```

## Build Steps

### Step 1: Create `requirements.txt`
```
anthropic
```

### Step 2: Create `its_not.py` with the following flow:

#### 2a: API Key Setup
- On launch, check for `ANTHROPIC_API_KEY` environment variable
- If not found, prompt the user: "Enter your Anthropic API key (paste it here):"
- Accept the key via input, use it for the session
- Print a brief confirmation that the key was accepted

#### 2b: Question Selection Menu
Display a simple numbered menu:
```
═══════════════════════════════════
        it's not
═══════════════════════════════════

Select a question:

  1. What is good for America?
  2. What is America?
  3. Enter your own question

Choice (1/2/3):
```

If option 3 is selected, prompt: "Enter your question:" and accept freeform input.

#### 2c: Generation Mode
After question is selected, display:
```
Question: "What is good for America?"

Press ENTER to generate. Type 'q' to quit, 'b' to go back.

───────────────────────────────────
```

Then enter a loop:
- Wait for user to press Enter
- Call Claude API to generate the next response
- Print the response on its own line, e.g.: `it's not mass deportations`
- Track all previous responses in the session to avoid repeats
- Loop continues until user types 'q' or 'b'

#### 2c-2: Auto Mode
Before entering the generation loop, offer a mode selection:
```
Mode:
  1. Manual (press Enter for each response)
  2. Auto (generate 25 responses automatically)

Choice (1/2):
```

In auto mode:
- After one press of Enter, generate 25 responses back-to-back
- Add a short delay between prints (~1-2 seconds) for a receipt-printer feel
- Each response still gets added to the previous responses list to avoid repeats
- After all 25 are printed, pause and say: "── 25 responses generated. Press ENTER for 25 more, or 'q' to quit. ──"
- If they hit Enter again, generate another batch of 25
- All the same deduplication and error handling applies

#### 2d: Claude API Prompt Design
Use the following system prompt (refine as needed):

```
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
```

The user message should be structured as:
```
Question: "{selected_question}"

Previous responses (do not repeat any of these):
{list of all previous responses in session}

Generate the next response.
```

API call parameters:
- Model: `claude-sonnet-4-20250514`
- Max tokens: 100 (these should be short)
- Temperature: 1.0 (maximize variety and creativity)

#### 2e: Output Formatting
Each generated line should print as:
```
it's not {response}
```
Lowercase, no period, matching receipt/installation aesthetic.

### Step 3: Create `README.md`
Include:
- What this project is (1-2 sentences)
- Setup instructions:
  1. Install Python 3.10+
  2. `pip install -r requirements.txt`
  3. Run: `python its_not.py`
  4. Paste your API key when prompted (or set `ANTHROPIC_API_KEY` env var)
- How to use: select a question, press Enter to generate responses, 'q' to quit

## Notes for Implementation
- Keep it to a single Python file — simplicity is the point
- Use `input()` for Enter detection — no fancy curses/terminal libraries
- Handle API errors gracefully (print a message, let the user try again with Enter)
- The "it's not" prefix is added by the script, not by the API — this keeps formatting consistent
- Strip any leading/trailing whitespace, quotes, or "it's not" prefix from API responses (in case the model includes it despite instructions)
