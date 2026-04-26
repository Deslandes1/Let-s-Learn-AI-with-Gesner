import streamlit as st
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Let's Learn AI with Gesner",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- PASSWORD PROTECTION ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
    .login-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 20px;
        text-align: center;
        color: white;
    }
    .top-square {
        background: rgba(255,255,255,0.2);
        border-radius: 15px;
        padding: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
    }
    .top-square img {
        width: 40px;
        height: 40px;
        object-fit: contain;
        background: white;
        border-radius: 10px;
        padding: 5px;
    }
    .ai-list {
        background: rgba(0,0,0,0.3);
        border-radius: 15px;
        padding: 0.8rem;
        text-align: left;
        margin-top: 0.5rem;
        font-size: 0.9rem;
    }
    .ai-list h3 {
        margin-top: 0;
        font-size: 1.2rem;
    }
    .ai-list p {
        margin: 3px 0;
    }
    .main-header {
        background: linear-gradient(90deg, #4facfe, #00f2fe);
        padding: 1rem;
        border-radius: 30px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .lesson-card {
        background-color: #f8f9fa;
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .lesson-card:hover { transform: translateY(-5px); }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background-color: #f1f1f1;
        border-radius: 20px;
    }
    .stColumn {
        padding: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN PAGE ----------
def login_page():
    # Main login container with gradient background
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown("<h2>🤖 Let's Learn AI with Gesner</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:0.9rem;'>20 lessons to master the best AI tools</p>", unsafe_allow_html=True)
    
    # Compact top square with working AI symbols
    st.markdown("""
    <div class="top-square">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg" alt="ChatGPT">
        <img src="https://www.gstatic.com/lamda/images/gemini_favicon_197x197_2ef9878c.png" alt="Gemini">
        <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Claude_AI_logo.svg" alt="Claude">
        <img src="https://perplexity.ai/favicon.ico" alt="Perplexity">
        <img src="https://huggingface.co/favicon.ico" alt="Hugging Face">
    </div>
    """, unsafe_allow_html=True)
    
    # List of all 20 AI tools with lesson numbers (two columns)
    ai_tools = [
        "1. ChatGPT", "2. Google Gemini", "3. DeepSeek", "4. Grok", "5. Claude",
        "6. GitHub Copilot", "7. Perplexity AI", "8. Midjourney", "9. DALL‑E 3", "10. Leonardo.ai",
        "11. Runway ML", "12. ElevenLabs", "13. Stable Diffusion", "14. Hugging Face", "15. AutoGPT",
        "16. AgentGPT", "17. LangChain", "18. LlamaIndex", "19. OpenAssistant", "20. Poe"
    ]
    st.markdown('<div class="ai-list"><h3>📚 What you will learn:</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, tool in enumerate(ai_tools):
        if i % 2 == 0:
            col1.markdown(f"✅ {tool}")
        else:
            col2.markdown(f"✅ {tool}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Password login form
    with st.form("login_form"):
        password = st.text_input("🔐 Enter Password", type="password", placeholder="Password: 20082010")
        if st.form_submit_button("✨ Unlock Lessons ✨"):
            if password == "20082010":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Sidebar on login page
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🌐 GlobalInternet.py")
    st.sidebar.markdown("**Gesner Deslandes** – Founder & Python Builder")
    st.sidebar.markdown("📞 (509) 4738-5663")
    st.sidebar.markdown("✉️ deslandes78@gmail.com")
    st.sidebar.markdown("[🌍 Visit our website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app)")

# ---------- LESSONS DATA (20 UNIQUE LESSONS WITH UPDATED IMAGES) ----------
lessons = [
    {
        "title": "Lesson 1: ChatGPT – Your AI Assistant",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/ef/ChatGPT-Logo.svg",
        "text": "**What it does:** ChatGPT by OpenAI is a conversational AI that can answer questions, write code, create content, and more. It supports web browsing, code interpretation, and image generation (DALL-E).\n\n**Setup on Phone:** Download the official ChatGPT app from App Store or Google Play. Sign up with email or Google. Free tier available. For advanced features (GPT-4, plugins), subscribe to ChatGPT Plus ($20/month).\n\n**Setup on Computer:** Visit chat.openai.com. Create an account. Use directly in browser. Install the desktop app (Windows/Mac) for better voice input.",
        "read_aloud": "ChatGPT by OpenAI is a conversational AI that can answer questions, write code, create content, and more. Setup on phone: download the app. On computer: visit the website."
    },
    {
        "title": "Lesson 2: Google Gemini – Multimodal Power",
        "image": "https://www.gstatic.com/lamda/images/gemini_favicon_197x197_2ef9878c.png",
        "text": "**What it does:** Gemini (formerly Bard) is Google's most advanced AI. It understands text, images, audio, and video. Integrated with Google Workspace (Gmail, Docs, Drive).\n\n**Setup on Phone:** Install Google Gemini app (Android) or use Google app on iOS with Gemini enabled. Sign in with Google account.\n\n**Setup on Computer:** Visit gemini.google.com. Sign in. Use directly. For advanced features, subscribe to Gemini Advanced (part of Google One AI Premium).",
        "read_aloud": "Google Gemini is Google's most advanced AI. It understands text, images, audio, and video. Setup: use the app on phone or visit the website on computer."
    },
    {
        "title": "Lesson 3: DeepSeek – The Efficient Coder",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/ec/DeepSeek_logo.svg",
        "text": "**What it does:** DeepSeek is a highly efficient coding and reasoning AI, known for low cost and long context (1 million tokens). Great for programming, math, and technical analysis.\n\n**Setup on Phone:** Use the DeepSeek mobile app (available on official stores) or access via browser at chat.deepseek.com.\n\n**Setup on Computer:** Go to chat.deepseek.com. No login required for basic use. Create account to save chats. Free and open-weight models available.",
        "read_aloud": "DeepSeek is an efficient coding and reasoning AI. Setup: use the mobile app or visit the website. Free to use."
    },
    {
        "title": "Lesson 4: Grok – Witty & Real‑time",
        "image": "https://abs.twimg.com/responsive-web/client-web/icon-ios.77d25eba.png",
        "text": "**What it does:** Grok by xAI (Elon Musk) is designed to be witty, rebellious, and access real‑time X (Twitter) data. It can answer current events with attitude.\n\n**Setup on Phone:** Download the X app (Twitter). Grok is available to X Premium+ subscribers. No standalone app yet.\n\n**Setup on Computer:** Visit x.com, subscribe to Premium+, then access Grok from the sidebar. Real‑time web and X integration.",
        "read_aloud": "Grok by xAI is witty and accesses real‑time X data. Setup requires X Premium+ subscription."
    },
    {
        "title": "Lesson 5: Claude – Safe & Ethical AI",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Claude_AI_logo.svg",
        "text": "**What it does:** Claude by Anthropic focuses on safety, honesty, and helpfulness. Excellent for long documents (100k+ tokens), analysis, and creative writing.\n\n**Setup on Phone:** Download Claude app from App Store (iOS) or use web browser on Android. Sign up with email.\n\n**Setup on Computer:** Visit claude.ai. Free tier available. Pro plan ($20/month) offers more usage and priority access.",
        "read_aloud": "Claude by Anthropic is safe and ethical. Good for long documents. Setup via app or website."
    },
    {
        "title": "Lesson 6: GitHub Copilot – AI Pair Programmer",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0a/GitHub_Copilot_%282025%29.svg",
        "text": "**What it does:** Copilot suggests code and entire functions in real‑time inside VS Code, JetBrains, and other IDEs. Supports many languages.\n\n**Setup on Phone:** No phone IDE currently. Use GitHub Codespaces on mobile browser with Copilot enabled.\n\n**Setup on Computer:** Install VS Code, install Copilot extension, sign in with GitHub account (free for verified students/teachers, $10/month otherwise).",
        "read_aloud": "GitHub Copilot is an AI pair programmer that suggests code inside your editor. Setup via VS Code extension."
    },
    {
        "title": "Lesson 7: Perplexity AI – Search + Answer",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Perplexity_AI_logo.svg",
        "text": "**What it does:** Perplexity is an AI‑powered search engine that gives direct answers with citations. Pro version can search academic papers, YouTube, and use multiple AI models.\n\n**Setup on Phone:** Install Perplexity app. Sign up with Google/Apple.\n\n**Setup on Computer:** Visit perplexity.ai. Free. Pro subscription ($20/month) unlocks more features.",
        "read_aloud": "Perplexity AI is an answer engine with citations. Setup via app or website."
    },
    {
        "title": "Lesson 8: Midjourney – AI Image Generator",
        "image": "https://lobehub.com/icons/midjourney/avatar.svg",
        "text": "**What it does:** Midjourney generates stunning images from text prompts. Runs inside Discord. Known for artistic styles.\n\n**Setup on Phone:** Install Discord, join Midjourney server. Use /imagine command. Free trial limited, then subscription ($10–$120/month).\n\n**Setup on Computer:** Same – use Discord desktop app or web version.",
        "read_aloud": "Midjourney generates images from text prompts inside Discord. Requires subscription after trial."
    },
    {
        "title": "Lesson 9: DALL‑E 3 – OpenAI's Image Creator",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/ef/ChatGPT-Logo.svg",
        "text": "**What it does:** DALL‑E 3 integrated into ChatGPT Plus generates highly accurate images from descriptions. Understands complex prompts.\n\n**Setup on Phone:** Use ChatGPT app (Plus subscription).\n\n**Setup on Computer:** chat.openai.com with Plus account. Describe an image and DALL‑E will create it.",
        "read_aloud": "DALL‑E 3 creates images from text inside ChatGPT Plus. Setup requires ChatGPT subscription."
    },
    {
        "title": "Lesson 10: Leonardo.ai – Free Image Generation",
        "image": "https://leonardo.ai/favicon.ico",
        "text": "**What it does:** Leonardo is a free (daily tokens) image and video generation platform. Many models, fine‑tuning, and canvas editor.\n\n**Setup on Phone:** Use browser on phone, sign up at leonardo.ai.\n\n**Setup on Computer:** Visit leonardo.ai, create account. Free tier gives 150 tokens/day.",
        "read_aloud": "Leonardo.ai offers free image generation daily. Setup via website."
    },
    {
        "title": "Lesson 11: Runway ML – AI Video Editor",
        "image": "https://runwayml.com/favicon.ico",
        "text": "**What it does:** Runway provides AI tools for video editing, green screen removal, text‑to‑video, and motion tracking. Used by filmmakers.\n\n**Setup on Phone:** Runway app for iOS. Sign up.\n\n**Setup on Computer:** Visit runwayml.com. Free tier with limited exports; paid plans start at $12/month.",
        "read_aloud": "Runway ML is an AI video editor. Setup via app or website."
    },
    {
        "title": "Lesson 12: ElevenLabs – Voice Cloning & TTS",
        "image": "https://cdn.simpleicons.org/elevenlabs/000000",
        "text": "**What it does:** ElevenLabs creates realistic text‑to‑speech and voice cloning. Used for audiobooks, dubbing, and AI voiceovers.\n\n**Setup on Phone:** Use browser on phone, sign up at elevenlabs.io. No dedicated app yet.\n\n**Setup on Computer:** Visit elevenlabs.io. Free tier offers 10,000 characters/month. Paid plans start at $5/month.",
        "read_aloud": "ElevenLabs does realistic text‑to‑speech and voice cloning. Setup via website."
    },
    {
        "title": "Lesson 13: Stable Diffusion – Open Source Image Gen",
        "image": "https://cdn.simpleicons.org/stabilityai/000000",
        "text": "**What it does:** Stable Diffusion by Stability AI generates images from text. Can run locally on your own GPU. Many community tools.\n\n**Setup on Phone:** Use free apps like 'DreamStudio' or web demos. For local, needs powerful phone.\n\n**Setup on Computer:** Install Automatic1111 WebUI or ComfyUI. Requires Python and GPU. Or use online free demos (Hugging Face).",
        "read_aloud": "Stable Diffusion is an open‑source image generator. Can run locally or use online demos."
    },
    {
        "title": "Lesson 14: Hugging Face – AI Model Hub",
        "image": "https://huggingface.co/favicon.ico",
        "text": "**What it does:** Hugging Face hosts thousands of free AI models (LLMs, image, audio). Also provides Spaces to run demos and Inference API.\n\n**Setup on Phone:** Use browser to access huggingface.co. Try models on 'Spaces'.\n\n**Setup on Computer:** Create free account. Use 'Inference API' or download models with Transformers library.",
        "read_aloud": "Hugging Face is a hub for free AI models. Setup via website. No installation needed."
    },
    {
        "title": "Lesson 15: AutoGPT – Autonomous AI Agents",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/80/Auto_GPT_Logo.png",
        "text": "**What it does:** AutoGPT is an experimental open‑source agent that can chain LLM calls to achieve goals (e.g., research, code, browse web) autonomously.\n\n**Setup on Phone:** Not recommended. Requires Python and API keys.\n\n**Setup on Computer:** Clone GitHub repo, install Python, get OpenAI API key, run in terminal. Or use web versions (AgentGPT).",
        "read_aloud": "AutoGPT autonomously completes multi‑step tasks. Setup requires Python and API keys."
    },
    {
        "title": "Lesson 16: AgentGPT – Browser Agent",
        "image": "https://agentgpt.com/favicon.ico",
        "text": "**What it does:** AgentGPT is a browser‑based AutoGPT alternative. Define a goal, and it will attempt to achieve it using LLM.\n\n**Setup on Phone:** Use browser on phone, go to agentgpt.com. Requires API key for some features.\n\n**Setup on Computer:** agentgpt.com – sign in, provide OpenAI API key, start an agent. Easy web interface.",
        "read_aloud": "AgentGPT runs autonomous agents in your browser. Setup via website with API key."
    },
    {
        "title": "Lesson 17: LangChain – Build LLM Apps",
        "image": "https://cdn.simpleicons.org/langchain/000000",
        "text": "**What it does:** LangChain is a framework for building applications powered by LLMs – chains, agents, retrieval, memory.\n\n**Setup on Phone:** Not for mobile. Use Replit or GitHub Codespaces on mobile browser.\n\n**Setup on Computer:** Install with pip install langchain. Then integrate with OpenAI, Hugging Face, etc. Great for developers.",
        "read_aloud": "LangChain is a Python framework to build LLM applications. Setup via pip."
    },
    {
        "title": "Lesson 18: LlamaIndex – Data Framework",
        "image": "https://www.llamaindex.ai/favicon.ico",
        "text": "**What it does:** LlamaIndex connects LLMs with your own data (PDFs, databases, APIs). Enables RAG (Retrieval‑Augmented Generation).\n\n**Setup on Phone:** Not suitable. Use cloud notebooks.\n\n**Setup on Computer:** pip install llama-index. Use with OpenAI or local models. Ideal for building Q&A over documents.",
        "read_aloud": "LlamaIndex connects LLMs to your private data. Setup via pip install."
    },
    {
        "title": "Lesson 19: OpenAssistant – Community LLM",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/33/OpenAssistant_logo.svg",
        "text": "**What it does:** OpenAssistant is a free, open‑source chatbot trained by volunteers. Can be run locally or via demo.\n\n**Setup on Phone:** Use browser demo at open-assistant.io.\n\n**Setup on Computer:** Visit open-assistant.io/chat. No login required. For self‑hosting, follow GitHub instructions.",
        "read_aloud": "OpenAssistant is a free community‑built chatbot. Use online demo or self‑host."
    },
    {
        "title": "Lesson 20: Poe – All‑in‑One AI Platform",
        "image": "https://poe.com/favicon.ico",
        "text": "**What it does:** Poe (Platform for Open Exploration) by Quora gives access to ChatGPT, Claude, Gemini, Llama, and more in one interface. Create custom bots.\n\n**Setup on Phone:** Install Poe app (iOS/Android). Sign up. Free tier includes daily messages. Subscription unlocks more.\n\n**Setup on Computer:** Visit poe.com. Free to use. Integrates many models for comparison.",
        "read_aloud": "Poe aggregates multiple AI models in one place. Setup via app or website."
    }
]

# ---------- MAIN PAGE ----------
def main_page():
    # Sidebar branding and logout
    st.sidebar.markdown("## 🌐 GlobalInternet.py")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 👨‍💻 Gesner Deslandes")
    st.sidebar.markdown("📞 (509) 4738-5663")
    st.sidebar.markdown("✉️ deslandes78@gmail.com")
    st.sidebar.markdown("---")
    st.sidebar.markdown("[🌍 Visit our website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app)")
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()
    
    # Main header
    st.markdown('<div class="main-header"><h1>📘 Let\'s Learn AI with Gesner</h1><p>20 Lessons – Master the best AI tools step by step</p></div>', unsafe_allow_html=True)
    
    # Display lessons with image, text, and read-aloud button
    for idx, lesson in enumerate(lessons, 1):
        with st.container():
            st.markdown(f'<div class="lesson-card">', unsafe_allow_html=True)
            col_img, col_text = st.columns([1, 3])
            with col_img:
                st.image(lesson["image"], width=80)
            with col_text:
                st.markdown(f"## {lesson['title']}")
                st.markdown(lesson["text"])
                read_btn = st.button(f"🔊 Read Aloud (Lesson {idx})", key=f"read_{idx}")
                if read_btn:
                    text_to_speak = lesson["read_aloud"].replace('"', '\\"').replace("\n", " ")
                    js_code = f"""
                    <script>
                        var utterance = new SpeechSynthesisUtterance("{text_to_speak}");
                        utterance.lang = "en-US";
                        window.speechSynthesis.cancel();
                        window.speechSynthesis.speak(utterance);
                    </script>
                    """
                    st.components.v1.html(js_code, height=0)
                    st.success("🔊 Now reading aloud... (make sure your device volume is on)")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown(f"""
    <div class="footer">
        <p>© {datetime.now().year} GlobalInternet.py – Built by Gesner Deslandes</p>
        <p>🤖 "Let's Learn AI with Gesner" – Your AI book for the future</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- PAGE ROUTING ----------
if not st.session_state.authenticated:
    login_page()
else:
    main_page()
