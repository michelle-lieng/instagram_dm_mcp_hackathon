# 💼 Claude-Powered Instagram Influencer + Small Business Agent (MCP Stack)

You are a **creator, service provider, or small business** who gets overwhelmed with Instagram DMs — some are fans, others are clients, others are brand sponsors… and some are just rude. You also have Notion pages and Google Calendar events to manage.

Instead of doing it all yourself, this Claude agent does it for you.

---

## ⚙️ Tech Stack

This project is built by integrating and extending:

- [`instagram_dm_mcp`](https://github.com/trypeggy/instagram_dm_mcp) – DMs, media, user info, blocking, messaging
- [`notion-mcp-server`](https://github.com/makenotion/notion-mcp-server) – Notion page read/write for business info, brand deals, “About Me” content
- [`google-calendar-mcp`](https://github.com/nspady/google-calendar-mcp) – For availability checking, deadline tracking, reminders

It’s fully Claude-compatible (via Claude Desktop and `stdio` transport).

---

## 👤 Demo Persona: *ShellsLashes*

To show how this works in practice, we created a persona:

> ShellsLashes is a Sydney-based lash artist + beauty influencer. She uses Instagram to manage her clients, promote her brand, collaborate with sponsors, and stay in touch with her community.

## Full demo


---

## 🔥 Core Features & Scenarios (with demo videos)

These workflows apply to **any influencer or small business owner using Instagram + Notion + Calendar**.

### 1. 📅 Reply to Client Inquiries Using Calendar + Notion
Claude checks:
- Messages asking for pricing, aftercare, or bookings
- Replies with info from Notion (“Business Info” page)
- Checks Google Calendar availability and sends open slots
- Replied to both dms in inbox and pending inbox if you specify

### 2. 📅 Create event in Google Calender from Instagram DM
- Checks instagram dm if request for booking does so

### 3. ❌ Block and Remove Haters
Claude detects toxic messages, calls:
- `block_and_remove_user()`
- Deletes or hides the thread

### 4. 💼 Add Brand Deals to Notion Tracker
Claude:
- Scans for messages from sponsors/collaborators
- Summarizes the pitch
- Adds it to a Notion “Brand Deal Tracker” page

### 5. 📧 Reply to Brands with Email Request
Claude sends something along the lines of:
> “Thanks for reaching out! Please email me at shells@lashes.com with your brief + budget 💌”

### 6. 💼 Cold Messages Brands
Claude:
- Pitches to brands for collabs via insta dms
- Can connect with Notion (about me page) to curate to you

### 7. 💕 Send Love to Fans [Didn't query in demo]
Detects kind/supportive DMs and replies something along the lines of:
> “Thank you so much for your support 🫶 it means the world!”

---

## 🧰 Custom Functions Added to `instagram_dm_mcp`

### ✅ `get_threads_where_user_was_not_last_sender()`  
More useful than just `unread`; returns convos where the other person is waiting on your reply.

### ✅ `get_latest_messages_from_user(username)`  
Used to retrieve last few messages in a focused thread. (Less used in final agent, but still included.)

### ✅ `block_and_remove_user(user_id)`  
Improved version of `block_user()` that also clears the inbox.

### ✅ Session Saving & Reuse Logic  
Added `save_session.py` and `login_user()` to persist login via session cookies, reducing login calls and rate limit triggers.

---

## 🐛 Known Issues – Rate Limiting

### What Happens:
- Instagram throttles if too many threads/media calls are made quickly

### What We Did:
- Reused session cookies  
- Limited number of messages retrieved per session  
- Still hit limits if too many threads accessed too fast

---

## ⚙️ Setup Instructions

```bash
# 1. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows

# 2. Set environment variables
export INSTAGRAM_USERNAME="your_username"
export INSTAGRAM_PASSWORD="your_password"

# 3. Install dependencies
pip install -r requirements.txt

# 4. Save Instagram session
python save_session.py

# 5. Follow instructions of each 3 MCP server README's to add to claude

# 6. Open Claude Desktop and start prompting!