# it's not

A CLI tool for an art installation featuring a receipt printer that endlessly generates negative responses to questions about America. Each response completes the phrase "it's not ___" — specific, visceral, like protest poetry on a receipt.

---

## Complete Setup Guide (No Experience Needed)

This guide assumes you've never used Python or a command line before. We'll walk through every step together.

---

### Step 1: Install Python

Python is the programming language this project is written in. You need to install it before anything else.

1. Open your web browser and go to [python.org](https://www.python.org/)
2. Click the big yellow **"Download Python"** button
3. Open the downloaded file to start the installer
4. **IMPORTANT:** On the very first screen of the installer, check the box that says **"Add Python to PATH"** at the bottom. This is the most common thing people miss, and the tool won't work without it.
5. Click **"Install Now"** and wait for it to finish
6. Click **"Close"** when it's done

### Step 2: Open a Terminal

A "terminal" is the text-based window where you'll type commands. On Windows, it's called **Command Prompt** or **PowerShell**.

1. Click the **Start menu** (the Windows icon in the bottom-left corner of your screen, or press the Windows key on your keyboard)
2. Type **Command Prompt** or **PowerShell**
3. Click on it to open it

You'll see a black (or blue) window with some text and a blinking cursor. This is where you'll type commands.

### Step 3: Navigate to the Project Folder

Right now, your terminal is pointed at some default location on your computer (usually your user folder). You need to tell it to look at the folder where this project lives.

The command `cd` stands for **"change directory"** — it's how you move between folders in the terminal.

Type this and press **Enter**:

```
cd Desktop\its-not
```

If you saved the project somewhere else, replace `Desktop\its-not` with the actual path. For example, if it's in your Downloads folder:

```
cd Downloads\its-not
```

**How to tell if it worked:** The text before your cursor should now show the folder name, something like `C:\Users\YourName\Desktop\its-not>`.

### Step 4: Install Dependencies

This project uses a library called `anthropic` to talk to the Claude AI. You need to install it before running the script.

Type this and press **Enter**:

```
pip install -r requirements.txt
```

**What this does in plain English:** `pip` is Python's tool for downloading and installing add-on libraries. The `-r requirements.txt` part says "read the file called requirements.txt and install everything listed in it." In this case, it installs the `anthropic` library, which lets the script communicate with Claude.

You'll see some text scrolling by as it downloads and installs. Wait until you see your cursor blinking again — that means it's done.

### Step 5: Get a Claude API Key

The script needs an API key to communicate with Claude. An API key is like a password that lets the program access the AI service.

1. Go to [console.anthropic.com](https://console.anthropic.com/) in your web browser
2. **Create an account** if you don't have one (click "Sign up" and follow the steps)
3. Once you're logged in, click **"API Keys"** in the left sidebar
4. Click **"Create Key"**
5. Give it a name (anything you want, like "its-not")
6. Click **"Create Key"**
7. **Copy the key** that appears — it starts with `sk-ant-` and is a long string of random characters. Save it somewhere safe (like a text file on your desktop). You won't be able to see it again after you close this page.

**Note:** You'll need to add a payment method and buy some API credits. The script uses the Claude Sonnet model, which costs a small amount per response (fractions of a cent each).

### Step 6: Run the Script

Make sure your terminal is still in the project folder (from Step 3). Type this and press **Enter**:

```
python its_not.py
```

The script will ask you to paste your API key. **Right-click** in the terminal to paste (Ctrl+V doesn't always work in Command Prompt), then press **Enter**.

**Tip:** If you don't want to paste your key every time, you can set it as an environment variable before running the script:

```
set ANTHROPIC_API_KEY=sk-ant-your-key-here
python its_not.py
```

### Step 7: Using the Tool

Once the script is running, here's what to expect:

**The menu:**
```
===================================
        it's not
===================================

Select a question:

  1. What is good for America?
  2. What is America?
  3. Enter your own question

Choice (1/2/3):
```

Type a number and press **Enter** to pick a question, or choose option 3 to write your own.

**Choosing a mode:**
- **Manual mode** — Press **Enter** each time you want a new response. Good for reading each one carefully.
- **Auto mode** — Generates 25 responses in a row with a short pause between each. Good for watching them stream in like a receipt printer.

**While generating:**
- Press **Enter** to generate the next response (Manual) or the next batch of 25 (Auto)
- Type **`b`** and press Enter to go back to the question menu
- Type **`q`** and press Enter to quit

Each response will appear as a line like:

```
it's not the price of insulin at the pharmacy counter
it's not the school lunch debt letters sent home with six-year-olds
it's not the tent city under the overpass on I-10
```

---

## Troubleshooting

### "python is not recognized as an internal or external command"

This means Python wasn't added to your PATH during installation. Two options:

- **Easiest fix:** Uninstall Python (from Windows Settings > Apps), then reinstall it. This time, make sure to check **"Add Python to PATH"** on the first screen of the installer.
- **Alternative:** Try typing `python3` instead of `python`, or `py` instead of `python`.

### "pip is not recognized"

Same PATH issue as above. Try:

```
python -m pip install -r requirements.txt
```

### "No module named 'anthropic'"

You skipped Step 4, or it didn't finish properly. Run the install command again:

```
pip install -r requirements.txt
```

### API key errors ("authentication_error" or "invalid api key")

- Double-check that you copied the full key (it's long — make sure you got it all)
- Make sure there are no extra spaces before or after the key
- If your key is old, go back to [console.anthropic.com](https://console.anthropic.com/) and create a new one

### "Could not connect" or timeout errors

- Check your internet connection
- The Anthropic API might be temporarily down — wait a minute and try again

### The terminal closed immediately after an error

Instead of double-clicking the Python file, always run it from a terminal (Step 2) using `python its_not.py`. That way, if there's an error, you can read it.

### Responses seem slow

Each response requires a round trip to the Claude API. A slight delay (1-2 seconds) is normal. In Auto mode, there's an intentional 1.5-second pause between responses.

---

## Quick Reference (For Returning Users)

```
cd Desktop\its-not
python its_not.py
```

Controls: **Enter** = generate, **b** = back to menu, **q** = quit.
