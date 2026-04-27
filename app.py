import streamlit as st
from datetime import datetime
import re

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

# ---------- LANGUAGE SELECTION ----------
if "lang" not in st.session_state:
    st.session_state.lang = "en"

def _(key):
    return texts[st.session_state.lang].get(key, key)

# ---------- HELPER: CLEAN TEXT FOR SPEECH ----------
def clean_text_for_speech(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"__(.*?)__", r"\1", text)
    text = re.sub(r"_(.*?)_", r"\1", text)
    text = re.sub(r"\n\s*\n", " ", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# ---------- UI TRANSLATIONS ----------
texts = {
    "en": {
        "app_title": "🤖 Let's Learn AI with Gesner",
        "login_title": "🤖 Let's Learn AI with Gesner",
        "login_sub": "20 lessons to master the best AI tools",
        "what_learn": "📚 What you will learn:",
        "password_label": "🔐 Enter Password",
        "password_placeholder": "Password: 20082010",
        "unlock_button": "✨ Unlock Lessons ✨",
        "incorrect_password": "Incorrect password.",
        "sidebar_company": "🌐 GlobalInternet.py",
        "sidebar_founder": "👨‍💻 Gesner Deslandes – Founder & Python Builder",
        "sidebar_phone": "📞 (509) 4738-5663",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_website": "🌍 Visit our website",
        "logout": "🚪 Logout",
        "jump_to_lesson": "📖 Select Lesson",
        "read_aloud_button": "🔊 Read Aloud (Full Text)",
        "reading_success": "🔊 Now reading the full lesson... (make sure your device volume is on)",
        "main_title": "📘 Let's Learn AI with Gesner",
        "main_sub": "Your selected lesson",
        "footer_text": "Built by Gesner Deslandes – GlobalInternet.py",
        "footer_book": "🤖 'Let's Learn AI with Gesner' – Your AI book for the future",
        "language_selector": "🌐 Language",
        "pricing_title": "💰 Get Lifetime Access",
        "pricing_monthly": "📅 Monthly Subscription\n$29 USD/month",
        "pricing_lifetime": "🏷️ Full Package (One-Time)\n$249 USD\n(Includes Source Code + Email Delivery)",
    },
    "fr": {
        "app_title": "🤖 Apprenons l'IA avec Gesner",
        "login_title": "🤖 Apprenons l'IA avec Gesner",
        "login_sub": "20 leçons pour maîtriser les meilleurs outils d'IA",
        "what_learn": "📚 Ce que vous allez apprendre :",
        "password_label": "🔐 Entrez le mot de passe",
        "password_placeholder": "Mot de passe : 20082010",
        "unlock_button": "✨ Débloquer les leçons ✨",
        "incorrect_password": "Mot de passe incorrect.",
        "sidebar_company": "🌐 GlobalInternet.py",
        "sidebar_founder": "👨‍💻 Gesner Deslandes – Fondateur & Constructeur Python",
        "sidebar_phone": "📞 (509) 4738-5663",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_website": "🌍 Visitez notre site web",
        "logout": "🚪 Déconnexion",
        "jump_to_lesson": "📖 Choisir la leçon",
        "read_aloud_button": "🔊 Lire tout le texte",
        "reading_success": "🔊 Lecture de la leçon complète... (vérifiez le volume)",
        "main_title": "📘 Apprenons l'IA avec Gesner",
        "main_sub": "Votre leçon sélectionnée",
        "footer_text": "Construit par Gesner Deslandes – GlobalInternet.py",
        "footer_book": "🤖 'Apprenons l'IA avec Gesner' – Votre livre IA du futur",
        "language_selector": "🌐 Langue",
        "pricing_title": "💰 Obtenez un accès à vie",
        "pricing_monthly": "📅 Abonnement mensuel\n29 $US/mois",
        "pricing_lifetime": "🏷️ Pack complet (Paiement unique)\n249 $US\n(Code source + livraison par e-mail inclus)",
    },
    "es": {
        "app_title": "🤖 Aprendamos IA con Gesner",
        "login_title": "🤖 Aprendamos IA con Gesner",
        "login_sub": "20 lecciones para dominar las mejores herramientas de IA",
        "what_learn": "📚 Lo que aprenderás:",
        "password_label": "🔐 Ingrese la contraseña",
        "password_placeholder": "Contraseña: 20082010",
        "unlock_button": "✨ Desbloquear lecciones ✨",
        "incorrect_password": "Contraseña incorrecta.",
        "sidebar_company": "🌐 GlobalInternet.py",
        "sidebar_founder": "👨‍💻 Gesner Deslandes – Fundador & Constructor Python",
        "sidebar_phone": "📞 (509) 4738-5663",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_website": "🌍 Visite nuestro sitio web",
        "logout": "🚪 Cerrar sesión",
        "jump_to_lesson": "📖 Seleccionar lección",
        "read_aloud_button": "🔊 Leer texto completo",
        "reading_success": "🔊 Leyendo la lección completa... (verifique el volumen)",
        "main_title": "📘 Aprendamos IA con Gesner",
        "main_sub": "Su lección seleccionada",
        "footer_text": "Construido por Gesner Deslandes – GlobalInternet.py",
        "footer_book": "🤖 'Aprendamos IA con Gesner' – Su libro de IA para el futuro",
        "language_selector": "🌐 Idioma",
        "pricing_title": "💰 Obtén acceso de por vida",
        "pricing_monthly": "📅 Suscripción mensual\n$29 USD/mes",
        "pricing_lifetime": "🏷️ Paquete completo (Pago único)\n$249 USD\n(Incluye código fuente + entrega por correo electrónico)",
    }
}

# ---------- LESSONS DATA (FULL TRANSLATIONS FOR 20 LESSONS) ----------
lessons = {
    "en": [
        {"title": "Lesson 1: ChatGPT – Your AI Assistant", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ef/ChatGPT-Logo.svg", "no_image": False, "text": "**What it does:** ChatGPT by OpenAI is a conversational AI that can answer questions, write code, create content, and more. It supports web browsing, code interpretation, and image generation (DALL-E).\n\n**Setup on Phone:** Download the official ChatGPT app from App Store or Google Play. Sign up with email or Google. Free tier available. For advanced features (GPT-4, plugins), subscribe to ChatGPT Plus ($20/month).\n\n**Setup on Computer:** Visit chat.openai.com. Create an account. Use directly in browser. Install the desktop app (Windows/Mac) for better voice input.", "read_aloud": "ChatGPT by OpenAI is a conversational AI that can answer questions, write code, create content, and more. Setup on phone: download the app. On computer: visit the website."},
        {"title": "Google Gemini – Lesson 2: Google Gemini – Multimodal Power", "image": "", "no_image": True, "text": "**What it does:** Gemini (formerly Bard) is Google's most advanced AI. It understands text, images, audio, and video. Integrated with Google Workspace (Gmail, Docs, Drive).\n\n**Setup on Phone:** Install Google Gemini app (Android) or use Google app on iOS with Gemini enabled. Sign in with Google account.\n\n**Setup on Computer:** Visit gemini.google.com. Sign in. Use directly. For advanced features, subscribe to Gemini Advanced (part of Google One AI Premium).", "read_aloud": "Google Gemini is Google's most advanced AI. It understands text, images, audio, and video. Setup: use the app on phone or visit the website on computer."},
        {"title": "Lesson 3: DeepSeek – The Efficient Coder", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ec/DeepSeek_logo.svg", "no_image": False, "text": "**What it does:** DeepSeek is a highly efficient coding and reasoning AI, known for low cost and long context (1 million tokens). Great for programming, math, and technical analysis.\n\n**Setup on Phone:** Use the DeepSeek mobile app (available on official stores) or access via browser at chat.deepseek.com.\n\n**Setup on Computer:** Go to chat.deepseek.com. No login required for basic use. Create account to save chats. Free and open-weight models available.", "read_aloud": "DeepSeek is an efficient coding and reasoning AI. Setup: use the mobile app or visit the website. Free to use."},
        {"title": "Lesson 4: Grok – Witty & Real‑time", "image": "https://abs.twimg.com/responsive-web/client-web/icon-ios.77d25eba.png", "no_image": False, "text": "**What it does:** Grok by xAI (Elon Musk) is designed to be witty, rebellious, and access real‑time X (Twitter) data. It can answer current events with attitude.\n\n**Setup on Phone:** Download the X app (Twitter). Grok is available to X Premium+ subscribers. No standalone app yet.\n\n**Setup on Computer:** Visit x.com, subscribe to Premium+, then access Grok from the sidebar. Real‑time web and X integration.", "read_aloud": "Grok by xAI is witty and accesses real‑time X data. Setup requires X Premium+ subscription."},
        {"title": "Lesson 5: Claude – Safe & Ethical AI", "image": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Claude_AI_logo.svg", "no_image": False, "text": "**What it does:** Claude by Anthropic focuses on safety, honesty, and helpfulness. Excellent for long documents (100k+ tokens), analysis, and creative writing.\n\n**Setup on Phone:** Download Claude app from App Store (iOS) or use web browser on Android. Sign up with email.\n\n**Setup on Computer:** Visit claude.ai. Free tier available. Pro plan ($20/month) offers more usage and priority access.", "read_aloud": "Claude by Anthropic is safe and ethical. Good for long documents. Setup via app or website."},
        {"title": "Lesson 6: GitHub Copilot – AI Pair Programmer", "image": "https://upload.wikimedia.org/wikipedia/commons/0/0a/GitHub_Copilot_%282025%29.svg", "no_image": False, "text": "**What it does:** Copilot suggests code and entire functions in real‑time inside VS Code, JetBrains, and other IDEs. Supports many languages.\n\n**Setup on Phone:** No phone IDE currently. Use GitHub Codespaces on mobile browser with Copilot enabled.\n\n**Setup on Computer:** Install VS Code, install Copilot extension, sign in with GitHub account (free for verified students/teachers, $10/month otherwise).", "read_aloud": "GitHub Copilot is an AI pair programmer that suggests code inside your editor. Setup via VS Code extension."},
        {"title": "Lesson 7: Perplexity AI – Search + Answer", "image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Perplexity_AI_logo.svg", "no_image": False, "text": "**What it does:** Perplexity is an AI‑powered search engine that gives direct answers with citations. Pro version can search academic papers, YouTube, and use multiple AI models.\n\n**Setup on Phone:** Install Perplexity app. Sign up with Google/Apple.\n\n**Setup on Computer:** Visit perplexity.ai. Free. Pro subscription ($20/month) unlocks more features.", "read_aloud": "Perplexity AI is an answer engine with citations. Setup via app or website."},
        {"title": "Midjourney – Lesson 8: Midjourney – AI Image Generator", "image": "", "no_image": True, "text": "**What it does:** Midjourney generates stunning images from text prompts. Runs inside Discord. Known for artistic styles.\n\n**Setup on Phone:** Install Discord, join Midjourney server. Use /imagine command. Free trial limited, then subscription ($10–$120/month).\n\n**Setup on Computer:** Same – use Discord desktop app or web version.", "read_aloud": "Midjourney generates images from text prompts inside Discord. Requires subscription after trial."},
        {"title": "Lesson 9: DALL‑E 3 – OpenAI's Image Creator", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ef/ChatGPT-Logo.svg", "no_image": False, "text": "**What it does:** DALL‑E 3 integrated into ChatGPT Plus generates highly accurate images from descriptions. Understands complex prompts.\n\n**Setup on Phone:** Use ChatGPT app (Plus subscription).\n\n**Setup on Computer:** chat.openai.com with Plus account. Describe an image and DALL‑E will create it.", "read_aloud": "DALL‑E 3 creates images from text inside ChatGPT Plus. Setup requires ChatGPT subscription."},
        {"title": "Leonardo.ai – Lesson 10: Leonardo.ai – Free Image Generation", "image": "", "no_image": True, "text": "Leonardo.ai: What it does: Leonardo is a free (daily tokens) image and video generation platform. Many models, fine‑tuning, and canvas editor.\n\nSetup on Phone: Use browser on phone, sign up at leonardo.ai.\n\nSetup on Computer: Visit leonardo.ai, create account. Free tier gives 150 tokens/day.", "read_aloud": "Leonardo.ai is a free image generation platform. Setup via website. 150 free tokens daily."},
        {"title": "Runway ML – Lesson 11: Runway ML – AI Video Editor", "image": "", "no_image": True, "text": "Runway ML: What it does: Runway provides AI tools for video editing, green screen removal, text‑to‑video, and motion tracking. Used by filmmakers.\n\nSetup on Phone: Runway app for iOS. Sign up.\n\nSetup on Computer: Visit runwayml.com. Free tier with limited exports; paid plans start at $12/month.", "read_aloud": "Runway ML is an AI video editor. Setup via app or website."},
        {"title": "Lesson 12: ElevenLabs – Voice Cloning & TTS", "image": "https://cdn.simpleicons.org/elevenlabs/000000", "no_image": False, "text": "**What it does:** ElevenLabs creates realistic text‑to‑speech and voice cloning. Used for audiobooks, dubbing, and AI voiceovers.\n\n**Setup on Phone:** Use browser on phone, sign up at elevenlabs.io. No dedicated app yet.\n\n**Setup on Computer:** Visit elevenlabs.io. Free tier offers 10,000 characters/month. Paid plans start at $5/month.", "read_aloud": "ElevenLabs does realistic text‑to‑speech and voice cloning. Setup via website."},
        {"title": "Stable Diffusion – Lesson 13: Stable Diffusion – Open Source Image Gen", "image": "", "no_image": True, "text": "Stable Diffusion: What it does: Stable Diffusion by Stability AI generates images from text. Can run locally on your own GPU. Many community tools.\n\nSetup on Phone: Use free apps like 'DreamStudio' or web demos. For local, needs powerful phone.\n\nSetup on Computer: Install Automatic1111 WebUI or ComfyUI. Requires Python and GPU. Or use online free demos (Hugging Face).", "read_aloud": "Stable Diffusion is an open‑source image generator. Can run locally or use online demos."},
        {"title": "Lesson 14: Hugging Face – AI Model Hub", "image": "https://huggingface.co/favicon.ico", "no_image": False, "text": "**What it does:** Hugging Face hosts thousands of free AI models (LLMs, image, audio). Also provides Spaces to run demos and Inference API.\n\n**Setup on Phone:** Use browser to access huggingface.co. Try models on 'Spaces'.\n\n**Setup on Computer:** Create free account. Use 'Inference API' or download models with Transformers library.", "read_aloud": "Hugging Face is a hub for free AI models. Setup via website. No installation needed."},
        {"title": "Lesson 15: AutoGPT – Autonomous AI Agents", "image": "https://upload.wikimedia.org/wikipedia/commons/8/80/Auto_GPT_Logo.png", "no_image": False, "text": "**What it does:** AutoGPT is an experimental open‑source agent that can chain LLM calls to achieve goals (e.g., research, code, browse web) autonomously.\n\n**Setup on Phone:** Not recommended. Requires Python and API keys.\n\n**Setup on Computer:** Clone GitHub repo, install Python, get OpenAI API key, run in terminal. Or use web versions (AgentGPT).", "read_aloud": "AutoGPT autonomously completes multi‑step tasks. Setup requires Python and API keys."},
        {"title": "AgentGPT – Lesson 16: AgentGPT – Browser Agent", "image": "", "no_image": True, "text": "AgentGPT: What it does: AgentGPT is a browser‑based AutoGPT alternative. Define a goal, and it will attempt to achieve it using LLM.\n\nSetup on Phone: Use browser on phone, go to agentgpt.com. Requires API key for some features.\n\nSetup on Computer: agentgpt.com – sign in, provide OpenAI API key, start an agent. Easy web interface.", "read_aloud": "AgentGPT runs autonomous agents in your browser. Setup via website with API key."},
        {"title": "Lesson 17: LangChain – Build LLM Apps", "image": "https://cdn.simpleicons.org/langchain/000000", "no_image": False, "text": "**What it does:** LangChain is a framework for building applications powered by LLMs – chains, agents, retrieval, memory.\n\n**Setup on Phone:** Not for mobile. Use Replit or GitHub Codespaces on mobile browser.\n\n**Setup on Computer:** Install with pip install langchain. Then integrate with OpenAI, Hugging Face, etc. Great for developers.", "read_aloud": "LangChain is a Python framework to build LLM applications. Setup via pip."},
        {"title": "Lesson 18: LlamaIndex – Data Framework", "image": "https://www.llamaindex.ai/favicon.ico", "no_image": False, "text": "**What it does:** LlamaIndex connects LLMs with your own data (PDFs, databases, APIs). Enables RAG (Retrieval‑Augmented Generation).\n\n**Setup on Phone:** Not suitable. Use cloud notebooks.\n\n**Setup on Computer:** pip install llama-index. Use with OpenAI or local models. Ideal for building Q&A over documents.", "read_aloud": "LlamaIndex connects LLMs to your private data. Setup via pip install."},
        {"title": "OpenAssistant – Lesson 19: OpenAssistant – Community LLM", "image": "", "no_image": True, "text": "OpenAssistant: What it does: OpenAssistant is a free, open‑source chatbot trained by volunteers. Can be run locally or via demo.\n\nSetup on Phone: Use browser demo at open-assistant.io.\n\nSetup on Computer: Visit open-assistant.io/chat. No login required. For self‑hosting, follow GitHub instructions.", "read_aloud": "OpenAssistant is a free community‑built chatbot. Use online demo or self‑host."},
        {"title": "Lesson 20: Poe – All‑in‑One AI Platform", "image": "https://poe.com/favicon.ico", "no_image": False, "text": "**What it does:** Poe (Platform for Open Exploration) by Quora gives access to ChatGPT, Claude, Gemini, Llama, and more in one interface. Create custom bots.\n\n**Setup on Phone:** Install Poe app (iOS/Android). Sign up. Free tier includes daily messages. Subscription unlocks more.\n\n**Setup on Computer:** Visit poe.com. Free to use. Integrates many models for comparison.", "read_aloud": "Poe aggregates multiple AI models in one place. Setup via app or website."}
    ],
    "fr": [
        {"title": "Leçon 1 : ChatGPT – Votre assistant IA", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ef/ChatGPT-Logo.svg", "no_image": False, "text": "**Ce qu'il fait :** ChatGPT d'OpenAI est une IA conversationnelle qui peut répondre aux questions, écrire du code, créer du contenu, etc. Il prend en charge la navigation Web, l'interprétation de code et la génération d'images (DALL-E).\n\n**Installation sur téléphone :** Téléchargez l'application officielle ChatGPT sur l'App Store ou Google Play. Inscrivez-vous avec un e-mail ou Google. Niveau gratuit disponible. Pour les fonctionnalités avancées (GPT-4, plugins), abonnez-vous à ChatGPT Plus (20 $/mois).\n\n**Installation sur ordinateur :** Rendez-vous sur chat.openai.com. Créez un compte. Utilisez directement dans le navigateur. Installez l'application de bureau (Windows/Mac) pour une meilleure entrée vocale.", "read_aloud": "ChatGPT d'OpenAI est une IA conversationnelle qui peut répondre aux questions, écrire du code et créer du contenu. Installation : téléchargez l'application sur téléphone ou visitez le site web sur ordinateur."},
        {"title": "Google Gemini – Leçon 2 : Google Gemini – Puissance multimodale", "image": "", "no_image": True, "text": "**Ce qu'il fait :** Gemini (anciennement Bard) est l'IA la plus avancée de Google. Il comprend le texte, les images, l'audio et la vidéo. Intégré à Google Workspace (Gmail, Docs, Drive).\n\n**Installation sur téléphone :** Installez l'application Google Gemini (Android) ou utilisez l'application Google sur iOS avec Gemini activé. Connectez-vous avec votre compte Google.\n\n**Installation sur ordinateur :** Rendez-vous sur gemini.google.com. Connectez-vous. Utilisez directement. Pour les fonctionnalités avancées, abonnez-vous à Gemini Advanced (inclus dans Google One AI Premium).", "read_aloud": "Google Gemini est l'IA la plus avancée de Google. Il comprend le texte, les images, l'audio et la vidéo. Installation : utilisez l'application sur téléphone ou visitez le site web sur ordinateur."},
        {"title": "Leçon 3 : DeepSeek – Le codeur efficace", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ec/DeepSeek_logo.svg", "no_image": False, "text": "**Ce qu'il fait :** DeepSeek est une IA de codage et de raisonnement très efficace, connue pour son faible coût et son long contexte (1 million de tokens). Idéal pour la programmation, les mathématiques et l'analyse technique.\n\n**Installation sur téléphone :** Utilisez l'application mobile DeepSeek (disponible sur les magasins officiels) ou accédez via le navigateur à chat.deepseek.com.\n\n**Installation sur ordinateur :** Rendez-vous sur chat.deepseek.com. Aucune connexion requise pour une utilisation de base. Créez un compte pour sauvegarder les discussions. Modèles gratuits et open‑weight disponibles.", "read_aloud": "DeepSeek est une IA de codage et de raisonnement efficace. Installation : utilisez l'application mobile ou visitez le site web. Gratuit."},
        {"title": "Leçon 4 : Grok – Spirituel et temps réel", "image": "https://abs.twimg.com/responsive-web/client-web/icon-ios.77d25eba.png", "no_image": False, "text": "**Ce qu'il fait :** Grok par xAI (Elon Musk) est conçu pour être spirituel, rebelle et accéder aux données X (Twitter) en temps réel. Il peut répondre à l'actualité avec attitude.\n\n**Installation sur téléphone :** Téléchargez l'application X (Twitter). Grok est disponible pour les abonnés X Premium+. Pas d'application autonome pour l'instant.\n\n**Installation sur ordinateur :** Rendez-vous sur x.com, abonnez-vous à Premium+, puis accédez à Grok depuis la barre latérale. Intégration web et X en temps réel.", "read_aloud": "Grok par xAI est spirituel et accède aux données X en temps réel. L'installation nécessite un abonnement X Premium+."},
        {"title": "Leçon 5 : Claude – IA sûre et éthique", "image": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Claude_AI_logo.svg", "no_image": False, "text": "**Ce qu'il fait :** Claude d'Anthropic se concentre sur la sécurité, l'honnêteté et la serviabilité. Excellent pour les longs documents (100 000+ tokens), l'analyse et l'écriture créative.\n\n**Installation sur téléphone :** Téléchargez l'application Claude sur l'App Store (iOS) ou utilisez le navigateur web sur Android. Inscrivez-vous avec un e-mail.\n\n**Installation sur ordinateur :** Rendez-vous sur claude.ai. Niveau gratuit disponible. Le plan Pro (20 $/mois) offre plus d'utilisation et un accès prioritaire.", "read_aloud": "Claude d'Anthropic est sûre et éthique. Idéal pour les longs documents. Installation via application ou site web."},
        {"title": "Leçon 6 : GitHub Copilot – Programmeur pair IA", "image": "https://upload.wikimedia.org/wikipedia/commons/0/0a/GitHub_Copilot_%282025%29.svg", "no_image": False, "text": "**Ce qu'il fait :** Copilot suggère du code et des fonctions entières en temps réel dans VS Code, JetBrains et d'autres IDE. Prend en charge de nombreux langages.\n\n**Installation sur téléphone :** Pas d'IDE sur téléphone actuellement. Utilisez GitHub Codespaces sur le navigateur mobile avec Copilot activé.\n\n**Installation sur ordinateur :** Installez VS Code, installez l'extension Copilot, connectez-vous avec votre compte GitHub (gratuit pour les étudiants/enseignants vérifiés, 10 $/mois sinon).", "read_aloud": "GitHub Copilot est un programmeur pair IA qui suggère du code dans votre éditeur. Installation via l'extension VS Code."},
        {"title": "Leçon 7 : Perplexity AI – Recherche + Réponse", "image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Perplexity_AI_logo.svg", "no_image": False, "text": "**Ce qu'il fait :** Perplexity est un moteur de recherche alimenté par l'IA qui donne des réponses directes avec des citations. La version Pro peut rechercher des articles académiques, YouTube et utiliser plusieurs modèles d'IA.\n\n**Installation sur téléphone :** Installez l'application Perplexity. Inscrivez-vous avec Google/Apple.\n\n**Installation sur ordinateur :** Rendez-vous sur perplexity.ai. Gratuit. L'abonnement Pro (20 $/mois) débloque plus de fonctionnalités.", "read_aloud": "Perplexity AI est un moteur de réponse avec citations. Installation via application ou site web."},
        {"title": "Midjourney – Leçon 8 : Midjourney – Générateur d'images IA", "image": "", "no_image": True, "text": "**Ce qu'il fait :** Midjourney génère des images époustouflantes à partir de descriptions textuelles. Fonctionne dans Discord. Connu pour ses styles artistiques.\n\n**Installation sur téléphone :** Installez Discord, rejoignez le serveur Midjourney. Utilisez la commande /imagine. Essai gratuit limité, puis abonnement (10–120 $/mois).\n\n**Installation sur ordinateur :** Même chose – utilisez l'application de bureau Discord ou la version web.", "read_aloud": "Midjourney génère des images à partir de texte dans Discord. Nécessite un abonnement après l'essai."},
        {"title": "Leçon 9 : DALL‑E 3 – Créateur d'images d'OpenAI", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ef/ChatGPT-Logo.svg", "no_image": False, "text": "**Ce qu'il fait :** DALL‑E 3 intégré à ChatGPT Plus génère des images très précises à partir de descriptions. Comprend les requêtes complexes.\n\n**Installation sur téléphone :** Utilisez l'application ChatGPT (abonnement Plus).\n\n**Installation sur ordinateur :** chat.openai.com avec compte Plus. Décrivez une image et DALL‑E la créera.", "read_aloud": "DALL‑E 3 crée des images à partir de texte dans ChatGPT Plus. Nécessite un abonnement ChatGPT."},
        {"title": "Leonardo.ai – Leçon 10 : Leonardo.ai – Génération d'images gratuite", "image": "", "no_image": True, "text": "Leonardo.ai : Ce qu'il fait : Leonardo est une plateforme gratuite (jetons quotidiens) de génération d'images et de vidéos. De nombreux modèles, affinage et éditeur canvas.\n\nInstallation sur téléphone : Utilisez le navigateur sur téléphone, inscrivez-vous sur leonardo.ai.\n\nInstallation sur ordinateur : Rendez-vous sur leonardo.ai, créez un compte. Le niveau gratuit donne 150 jetons/jour.", "read_aloud": "Leonardo.ai est une plateforme gratuite de génération d'images. Installation via site web. 150 jetons gratuits par jour."},
        {"title": "Runway ML – Leçon 11 : Runway ML – Éditeur vidéo IA", "image": "", "no_image": True, "text": "Runway ML : Ce qu'il fait : Runway fournit des outils IA pour le montage vidéo, la suppression de fond vert, la vidéo à partir de texte et le suivi de mouvement. Utilisé par les cinéastes.\n\nInstallation sur téléphone : Application Runway pour iOS. Inscrivez-vous.\n\nInstallation sur ordinateur : Rendez-vous sur runwayml.com. Niveau gratuit avec exportations limitées ; les plans payants commencent à 12 $/mois.", "read_aloud": "Runway ML est un éditeur vidéo IA. Installation via application ou site web."},
        {"title": "Leçon 12 : ElevenLabs – Clonage vocal et TTS", "image": "https://cdn.simpleicons.org/elevenlabs/000000", "no_image": False, "text": "**Ce qu'il fait :** ElevenLabs crée une synthèse vocale réaliste et un clonage de voix. Utilisé pour les livres audio, le doublage et les voix off IA.\n\n**Installation sur téléphone :** Utilisez le navigateur sur téléphone, inscrivez-vous sur elevenlabs.io. Pas d'application dédiée pour l'instant.\n\n**Installation sur ordinateur :** Rendez-vous sur elevenlabs.io. Le niveau gratuit offre 10 000 caractères/mois. Les plans payants commencent à 5 $/mois.", "read_aloud": "ElevenLabs fait de la synthèse vocale réaliste et du clonage de voix. Installation via site web."},
        {"title": "Stable Diffusion – Leçon 13 : Stable Diffusion – Générateur d'images open source", "image": "", "no_image": True, "text": "Stable Diffusion : Ce qu'il fait : Stable Diffusion par Stability AI génère des images à partir de texte. Peut fonctionner localement sur votre propre GPU. De nombreux outils communautaires.\n\nInstallation sur téléphone : Utilisez des applications gratuites comme 'DreamStudio' ou des démos web. Pour une utilisation locale, besoin d'un téléphone puissant.\n\nInstallation sur ordinateur : Installez Automatic1111 WebUI ou ComfyUI. Nécessite Python et un GPU. Ou utilisez des démos gratuites en ligne (Hugging Face).", "read_aloud": "Stable Diffusion est un générateur d'images open source. Peut fonctionner localement ou utiliser des démos en ligne."},
        {"title": "Leçon 14 : Hugging Face – Hub de modèles IA", "image": "https://huggingface.co/favicon.ico", "no_image": False, "text": "**Ce qu'il fait :** Hugging Face héberge des milliers de modèles d'IA gratuits (LLM, image, audio). Fournit également des Spaces pour exécuter des démos et une API d'inférence.\n\n**Installation sur téléphone :** Utilisez le navigateur pour accéder à huggingface.co. Essayez les modèles dans 'Spaces'.\n\n**Installation sur ordinateur :** Créez un compte gratuit. Utilisez l'API d'inférence ou téléchargez des modèles avec la bibliothèque Transformers.", "read_aloud": "Hugging Face est un hub de modèles IA gratuits. Installation via site web. Pas d'installation nécessaire."},
        {"title": "Leçon 15 : AutoGPT – Agents IA autonomes", "image": "https://upload.wikimedia.org/wikipedia/commons/8/80/Auto_GPT_Logo.png", "no_image": False, "text": "**Ce qu'il fait :** AutoGPT est un agent open‑source expérimental qui peut enchaîner des appels LLM pour atteindre des objectifs (recherche, code, navigation web) de manière autonome.\n\n**Installation sur téléphone :** Non recommandé. Nécessite Python et des clés API.\n\n**Installation sur ordinateur :** Clonez le dépôt GitHub, installez Python, obtenez une clé API OpenAI, exécutez dans le terminal. Ou utilisez les versions web (AgentGPT).", "read_aloud": "AutoGPT accomplit des tâches multi‑étapes de manière autonome. L'installation nécessite Python et des clés API."},
        {"title": "AgentGPT – Leçon 16 : AgentGPT – Agent navigateur", "image": "", "no_image": True, "text": "AgentGPT : Ce qu'il fait : AgentGPT est une alternative à AutoGPT basée sur le navigateur. Définissez un objectif, et il tentera de l'atteindre en utilisant un LLM.\n\nInstallation sur téléphone : Utilisez le navigateur sur téléphone, allez sur agentgpt.com. Nécessite une clé API pour certaines fonctionnalités.\n\nInstallation sur ordinateur : agentgpt.com – connectez-vous, fournissez votre clé API OpenAI, lancez un agent. Interface web facile.", "read_aloud": "AgentGPT exécute des agents autonomes dans votre navigateur. Installation via site web avec clé API."},
        {"title": "Leçon 17 : LangChain – Construire des applications LLM", "image": "https://cdn.simpleicons.org/langchain/000000", "no_image": False, "text": "**Ce qu'il fait :** LangChain est un framework pour construire des applications alimentées par LLM – chaînes, agents, récupération, mémoire.\n\n**Installation sur téléphone :** Pas pour mobile. Utilisez Replit ou GitHub Codespaces sur navigateur mobile.\n\n**Installation sur ordinateur :** Installez avec pip install langchain. Ensuite intégrez avec OpenAI, Hugging Face, etc. Idéal pour les développeurs.", "read_aloud": "LangChain est un framework Python pour construire des applications LLM. Installation via pip."},
        {"title": "Leçon 18 : LlamaIndex – Framework de données", "image": "https://www.llamaindex.ai/favicon.ico", "no_image": False, "text": "**Ce qu'il fait :** LlamaIndex connecte les LLM à vos propres données (PDF, bases de données, API). Permet le RAG (Retrieval‑Augmented Generation).\n\n**Installation sur téléphone :** Non adapté. Utilisez des notebooks cloud.\n\n**Installation sur ordinateur :** pip install llama-index. Utilisez avec OpenAI ou des modèles locaux. Idéal pour construire des Q&A sur des documents.", "read_aloud": "LlamaIndex connecte les LLM à vos données privées. Installation via pip install."},
        {"title": "OpenAssistant – Leçon 19 : OpenAssistant – LLM communautaire", "image": "", "no_image": True, "text": "OpenAssistant : Ce qu'il fait : OpenAssistant est un chatbot gratuit et open‑source entraîné par des bénévoles. Peut être exécuté localement ou via une démo.\n\nInstallation sur téléphone : Utilisez la démo du navigateur sur open-assistant.io.\n\nInstallation sur ordinateur : Rendez-vous sur open-assistant.io/chat. Aucune connexion requise. Pour l'auto‑hébergement, suivez les instructions GitHub.", "read_aloud": "OpenAssistant est un chatbot communautaire gratuit. Utilisez la démo en ligne ou auto‑hébergez."},
        {"title": "Leçon 20 : Poe – Plateforme IA tout‑en‑un", "image": "https://poe.com/favicon.ico", "no_image": False, "text": "**Ce qu'il fait :** Poe (Platform for Open Exploration) par Quora donne accès à ChatGPT, Claude, Gemini, Llama, etc. dans une seule interface. Créez des bots personnalisés.\n\n**Installation sur téléphone :** Installez l'application Poe (iOS/Android). Inscrivez-vous. Le niveau gratuit inclut des messages quotidiens. L'abonnement débloque plus.\n\n**Installation sur ordinateur :** Rendez-vous sur poe.com. Gratuit. Intègre de nombreux modèles pour comparaison.", "read_aloud": "Poe agrège plusieurs modèles d'IA en un seul endroit. Installation via application ou site web."}
    ],
    "es": [
        {"title": "Lección 1: ChatGPT – Tu asistente IA", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ef/ChatGPT-Logo.svg", "no_image": False, "text": "**Lo que hace:** ChatGPT de OpenAI es una IA conversacional que puede responder preguntas, escribir código, crear contenido y más. Admite navegación web, interpretación de código y generación de imágenes (DALL-E).\n\n**Configuración en el teléfono:** Descargue la aplicación oficial de ChatGPT desde App Store o Google Play. Regístrese con correo electrónico o Google. Nivel gratuito disponible. Para funciones avanzadas (GPT-4, plugins), suscríbase a ChatGPT Plus ($20/mes).\n\n**Configuración en la computadora:** Visite chat.openai.com. Cree una cuenta. Úselo directamente en el navegador. Instale la aplicación de escritorio (Windows/Mac) para una mejor entrada de voz.", "read_aloud": "ChatGPT de OpenAI es una IA conversacional que puede responder preguntas, escribir código y crear contenido. Configuración: descargue la aplicación en el teléfono o visite el sitio web en la computadora."},
        {"title": "Google Gemini – Lección 2: Google Gemini – Potencia multimodal", "image": "", "no_image": True, "text": "**Lo que hace:** Gemini (anteriormente Bard) es la IA más avanzada de Google. Comprende texto, imágenes, audio y video. Integrado con Google Workspace (Gmail, Docs, Drive).\n\n**Configuración en el teléfono:** Instale la aplicación Google Gemini (Android) o use la aplicación Google en iOS con Gemini habilitado. Inicie sesión con su cuenta de Google.\n\n**Configuración en la computadora:** Visite gemini.google.com. Inicie sesión. Úselo directamente. Para funciones avanzadas, suscríbase a Gemini Advanced (parte de Google One AI Premium).", "read_aloud": "Google Gemini es la IA más avanzada de Google. Comprende texto, imágenes, audio y video. Configuración: use la aplicación en el teléfono o visite el sitio web en la computadora."},
        {"title": "Lección 3: DeepSeek – El codificador eficiente", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ec/DeepSeek_logo.svg", "no_image": False, "text": "**Lo que hace:** DeepSeek es una IA de codificación y razonamiento altamente eficiente, conocida por su bajo costo y contexto largo (1 millón de tokens). Ideal para programación, matemáticas y análisis técnico.\n\n**Configuración en el teléfono:** Use la aplicación móvil DeepSeek (disponible en tiendas oficiales) o acceda a través del navegador a chat.deepseek.com.\n\n**Configuración en la computadora:** Vaya a chat.deepseek.com. No se requiere inicio de sesión para uso básico. Cree una cuenta para guardar chats. Modelos gratuitos y de peso abierto disponibles.", "read_aloud": "DeepSeek es una IA de codificación y razonamiento eficiente. Configuración: use la aplicación móvil o visite el sitio web. Gratis."},
        {"title": "Lección 4: Grok – Ingenioso y en tiempo real", "image": "https://abs.twimg.com/responsive-web/client-web/icon-ios.77d25eba.png", "no_image": False, "text": "**Lo que hace:** Grok de xAI (Elon Musk) está diseñado para ser ingenioso, rebelde y acceder a datos de X (Twitter) en tiempo real. Puede responder a eventos actuales con actitud.\n\n**Configuración en el teléfono:** Descargue la aplicación X (Twitter). Grok está disponible para suscriptores de X Premium+. Aún no hay aplicación independiente.\n\n**Configuración en la computadora:** Visite x.com, suscríbase a Premium+, luego acceda a Grok desde la barra lateral. Integración web y X en tiempo real.", "read_aloud": "Grok de xAI es ingenioso y accede a datos de X en tiempo real. La configuración requiere suscripción a X Premium+."},
        {"title": "Lección 5: Claude – IA segura y ética", "image": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Claude_AI_logo.svg", "no_image": False, "text": "**Lo que hace:** Claude de Anthropic se centra en la seguridad, honestidad y utilidad. Excelente para documentos largos (100k+ tokens), análisis y escritura creativa.\n\n**Configuración en el teléfono:** Descargue la aplicación Claude desde App Store (iOS) o use el navegador web en Android. Regístrese con correo electrónico.\n\n**Configuración en la computadora:** Visite claude.ai. Nivel gratuito disponible. El plan Pro ($20/mes) ofrece más uso y acceso prioritario.", "read_aloud": "Claude de Anthropic es segura y ética. Buena para documentos largos. Configuración mediante aplicación o sitio web."},
        {"title": "Lección 6: GitHub Copilot – Programador par IA", "image": "https://upload.wikimedia.org/wikipedia/commons/0/0a/GitHub_Copilot_%282025%29.svg", "no_image": False, "text": "**Lo que hace:** Copilot sugiere código y funciones completas en tiempo real dentro de VS Code, JetBrains y otros IDE. Admite muchos lenguajes.\n\n**Configuración en el teléfono:** Actualmente no hay IDE para teléfono. Use GitHub Codespaces en el navegador móvil con Copilot habilitado.\n\n**Configuración en la computadora:** Instale VS Code, instale la extensión Copilot, inicie sesión con su cuenta de GitHub (gratis para estudiantes/profesores verificados, $10/mes de lo contrario).", "read_aloud": "GitHub Copilot es un programador par IA que sugiere código dentro de su editor. Configuración mediante extensión de VS Code."},
        {"title": "Lección 7: Perplexity AI – Búsqueda + Respuesta", "image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Perplexity_AI_logo.svg", "no_image": False, "text": "**Lo que hace:** Perplexity es un motor de búsqueda impulsado por IA que ofrece respuestas directas con citas. La versión Pro puede buscar artículos académicos, YouTube y usar múltiples modelos de IA.\n\n**Configuración en el teléfono:** Instale la aplicación Perplexity. Regístrese con Google/Apple.\n\n**Configuración en la computadora:** Visite perplexity.ai. Gratis. La suscripción Pro ($20/mes) desbloquea más funciones.", "read_aloud": "Perplexity AI es un motor de respuestas con citas. Configuración mediante aplicación o sitio web."},
        {"title": "Midjourney – Lección 8: Midjourney – Generador de imágenes IA", "image": "", "no_image": True, "text": "**Lo que hace:** Midjourney genera imágenes impresionantes a partir de indicaciones de texto. Funciona dentro de Discord. Conocido por sus estilos artísticos.\n\n**Configuración en el teléfono:** Instale Discord, únase al servidor de Midjourney. Use el comando /imagine. Prueba gratuita limitada, luego suscripción ($10–$120/mes).\n\n**Configuración en la computadora:** Igual – use la aplicación de escritorio de Discord o la versión web.", "read_aloud": "Midjourney genera imágenes a partir de texto dentro de Discord. Requiere suscripción después de la prueba."},
        {"title": "Lección 9: DALL‑E 3 – Creador de imágenes de OpenAI", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ef/ChatGPT-Logo.svg", "no_image": False, "text": "**Lo que hace:** DALL‑E 3 integrado en ChatGPT Plus genera imágenes muy precisas a partir de descripciones. Comprende indicaciones complejas.\n\n**Configuración en el teléfono:** Use la aplicación ChatGPT (suscripción Plus).\n\n**Configuración en la computadora:** chat.openai.com con cuenta Plus. Describa una imagen y DALL‑E la creará.", "read_aloud": "DALL‑E 3 crea imágenes a partir de texto dentro de ChatGPT Plus. Requiere suscripción a ChatGPT."},
        {"title": "Leonardo.ai – Lección 10: Leonardo.ai – Generación de imágenes gratuita", "image": "", "no_image": True, "text": "Leonardo.ai: Lo que hace: Leonardo es una plataforma gratuita (fichas diarias) de generación de imágenes y videos. Muchos modelos, ajuste fino y editor de lienzo.\n\nConfiguración en el teléfono: Use el navegador en el teléfono, regístrese en leonardo.ai.\n\nConfiguración en la computadora: Visite leonardo.ai, cree una cuenta. El nivel gratuito ofrece 150 fichas/día.", "read_aloud": "Leonardo.ai es una plataforma gratuita de generación de imágenes. Configuración mediante sitio web. 150 fichas gratuitas al día."},
        {"title": "Runway ML – Lección 11: Runway ML – Editor de video IA", "image": "", "no_image": True, "text": "Runway ML: Lo que hace: Runway proporciona herramientas de IA para edición de video, eliminación de fondo verde, texto a video y seguimiento de movimiento. Utilizado por cineastas.\n\nConfiguración en el teléfono: Aplicación Runway para iOS. Regístrese.\n\nConfiguración en la computadora: Visite runwayml.com. Nivel gratuito con exportaciones limitadas; los planes de pago comienzan en $12/mes.", "read_aloud": "Runway ML es un editor de video IA. Configuración mediante aplicación o sitio web."},
        {"title": "Lección 12: ElevenLabs – Clonación de voz y TTS", "image": "https://cdn.simpleicons.org/elevenlabs/000000", "no_image": False, "text": "**Lo que hace:** ElevenLabs crea una síntesis de voz realista y clonación de voz. Se utiliza para audiolibros, doblaje y locuciones IA.\n\n**Configuración en el teléfono:** Use el navegador en el teléfono, regístrese en elevenlabs.io. Aún no hay aplicación dedicada.\n\n**Configuración en la computadora:** Visite elevenlabs.io. El nivel gratuito ofrece 10,000 caracteres/mes. Los planes de pago comienzan en $5/mes.", "read_aloud": "ElevenLabs hace una síntesis de voz realista y clonación de voz. Configuración mediante sitio web."},
        {"title": "Stable Diffusion – Lección 13: Stable Diffusion – Generador de imágenes de código abierto", "image": "", "no_image": True, "text": "Stable Diffusion: Lo que hace: Stable Diffusion de Stability AI genera imágenes a partir de texto. Puede ejecutarse localmente en su propia GPU. Muchas herramientas comunitarias.\n\nConfiguración en el teléfono: Use aplicaciones gratuitas como 'DreamStudio' o demostraciones web. Para uso local, se necesita un teléfono potente.\n\nConfiguración en la computadora: Instale Automatic1111 WebUI o ComfyUI. Requiere Python y GPU. O use demostraciones gratuitas en línea (Hugging Face).", "read_aloud": "Stable Diffusion es un generador de imágenes de código abierto. Puede ejecutarse localmente o usar demostraciones en línea."},
        {"title": "Lección 14: Hugging Face – Centro de modelos IA", "image": "https://huggingface.co/favicon.ico", "no_image": False, "text": "**Lo que hace:** Hugging Face alberga miles de modelos de IA gratuitos (LLM, imagen, audio). También proporciona Spaces para ejecutar demostraciones y una API de inferencia.\n\n**Configuración en el teléfono:** Use el navegador para acceder a huggingface.co. Pruebe modelos en 'Spaces'.\n\n**Configuración en la computadora:** Cree una cuenta gratuita. Use la 'API de inferencia' o descargue modelos con la biblioteca Transformers.", "read_aloud": "Hugging Face es un centro de modelos de IA gratuitos. Configuración mediante sitio web. No se necesita instalación."},
        {"title": "Lección 15: AutoGPT – Agentes IA autónomos", "image": "https://upload.wikimedia.org/wikipedia/commons/8/80/Auto_GPT_Logo.png", "no_image": False, "text": "**Lo que hace:** AutoGPT es un agente experimental de código abierto que puede encadenar llamadas LLM para lograr objetivos (investigación, código, navegación web) de forma autónoma.\n\n**Configuración en el teléfono:** No recomendado. Requiere Python y claves API.\n\n**Configuración en la computadora:** Clone el repositorio de GitHub, instale Python, obtenga una clave API de OpenAI, ejecute en la terminal. O use versiones web (AgentGPT).", "read_aloud": "AutoGPT completa tareas de múltiples pasos de forma autónoma. La configuración requiere Python y claves API."},
        {"title": "AgentGPT – Lección 16: AgentGPT – Agente de navegador", "image": "", "no_image": True, "text": "AgentGPT: Lo que hace: AgentGPT es una alternativa a AutoGPT basada en navegador. Defina un objetivo e intentará alcanzarlo usando un LLM.\n\nConfiguración en el teléfono: Use el navegador en el teléfono, vaya a agentgpt.com. Requiere clave API para algunas funciones.\n\nConfiguración en la computadora: agentgpt.com – inicie sesión, proporcione su clave API de OpenAI, inicie un agente. Interfaz web fácil.", "read_aloud": "AgentGPT ejecuta agentes autónomos en su navegador. Configuración mediante sitio web con clave API."},
        {"title": "Lección 17: LangChain – Construir aplicaciones LLM", "image": "https://cdn.simpleicons.org/langchain/000000", "no_image": False, "text": "**Lo que hace:** LangChain es un framework para construir aplicaciones impulsadas por LLM – cadenas, agentes, recuperación, memoria.\n\n**Configuración en el teléfono:** No para móviles. Use Replit o GitHub Codespaces en el navegador móvil.\n\n**Configuración en la computadora:** Instale con pip install langchain. Luego integre con OpenAI, Hugging Face, etc. Ideal para desarrolladores.", "read_aloud": "LangChain es un framework de Python para construir aplicaciones LLM. Configuración mediante pip."},
        {"title": "Lección 18: LlamaIndex – Framework de datos", "image": "https://www.llamaindex.ai/favicon.ico", "no_image": False, "text": "**Lo que hace:** LlamaIndex conecta LLMs con sus propios datos (PDF, bases de datos, API). Permite RAG (Generación Aumentada por Recuperación).\n\n**Configuración en el teléfono:** No adecuado. Use cuadernos en la nube.\n\n**Configuración en la computadora:** pip install llama-index. Use con OpenAI o modelos locales. Ideal para construir Q&A sobre documentos.", "read_aloud": "LlamaIndex conecta LLMs a sus datos privados. Configuración mediante pip install."},
        {"title": "OpenAssistant – Lección 19: OpenAssistant – LLM comunitario", "image": "", "no_image": True, "text": "OpenAssistant: Lo que hace: OpenAssistant es un chatbot gratuito y de código abierto entrenado por voluntarios. Se puede ejecutar localmente o mediante demostración.\n\nConfiguración en el teléfono: Use la demostración del navegador en open-assistant.io.\n\nConfiguración en la computadora: Visite open-assistant.io/chat. No se requiere inicio de sesión. Para autoalojamiento, siga las instrucciones de GitHub.", "read_aloud": "OpenAssistant es un chatbot comunitario gratuito. Use la demostración en línea o autoalójelo."},
        {"title": "Lección 20: Poe – Plataforma IA todo en uno", "image": "https://poe.com/favicon.ico", "no_image": False, "text": "**Lo que hace:** Poe (Platform for Open Exploration) de Quora brinda acceso a ChatGPT, Claude, Gemini, Llama y más en una sola interfaz. Cree bots personalizados.\n\n**Configuración en el teléfono:** Instale la aplicación Poe (iOS/Android). Regístrese. El nivel gratuito incluye mensajes diarios. La suscripción desbloquea más.\n\n**Configuración en la computadora:** Visite poe.com. Gratis. Integra muchos modelos para comparación.", "read_aloud": "Poe agrega múltiples modelos de IA en un solo lugar. Configuración mediante aplicación o sitio web."}
    ]
}

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
    .ai-list {
        background: rgba(0,0,0,0.3);
        border-radius: 15px;
        padding: 0.8rem;
        text-align: left;
        margin: 1rem 0;
        font-size: 0.9rem;
    }
    .ai-list h3 {
        margin-top: 0;
        font-size: 1.2rem;
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
        scroll-margin-top: 80px;
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
    .pricing-box {
        background-color: #1e3c72;
        color: white;
        border-radius: 15px;
        padding: 0.8rem;
        margin: 0.5rem 0;
        text-align: center;
    }
    .pricing-box h4 {
        margin: 0 0 0.3rem 0;
        font-size: 1rem;
    }
    .pricing-box p {
        margin: 0;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN PAGE ----------
def login_page():
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown(f"<h2>{_('login_title')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:0.9rem;'>{_('login_sub')}</p>", unsafe_allow_html=True)
    
    ai_names = [
        "ChatGPT", "Google Gemini", "DeepSeek", "Grok", "Claude",
        "GitHub Copilot", "Perplexity AI", "Midjourney", "DALL‑E 3", "Leonardo.ai",
        "Runway ML", "ElevenLabs", "Stable Diffusion", "Hugging Face", "AutoGPT",
        "AgentGPT", "LangChain", "LlamaIndex", "OpenAssistant", "Poe"
    ]
    st.markdown(f'<div class="ai-list"><h3>{_("what_learn")}</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, name in enumerate(ai_names):
        if i % 2 == 0:
            col1.markdown(f"✅ {name}")
        else:
            col2.markdown(f"✅ {name}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    with st.form("login_form"):
        password = st.text_input(_("password_label"), type="password", placeholder=_("password_placeholder"))
        if st.form_submit_button(_("unlock_button")):
            if password == "20082010":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error(_("incorrect_password"))
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### {_('sidebar_company')}")
    st.sidebar.markdown(f"**{_('sidebar_founder')}**")
    st.sidebar.markdown(_("sidebar_phone"))
    st.sidebar.markdown(_("sidebar_email"))
    st.sidebar.markdown(f"[{_('sidebar_website')}](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app)")

# ---------- MAIN PAGE ----------
def main_page():
    lang_map = {"English": "en", "Français": "fr", "Español": "es"}
    selected_lang = st.sidebar.selectbox(_("language_selector"), list(lang_map.keys()), index=["en","fr","es"].index(st.session_state.lang))
    st.session_state.lang = lang_map[selected_lang]
    
    st.sidebar.markdown(f"## {_('sidebar_company')}")
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**{_('sidebar_founder')}**")
    st.sidebar.markdown(_("sidebar_phone"))
    st.sidebar.markdown(_("sidebar_email"))
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"[{_('sidebar_website')}](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app)")
    st.sidebar.markdown("---")
    
    st.sidebar.markdown(f"### {_('pricing_title')}")
    st.sidebar.markdown(f"""
    <div class="pricing-box">
        <h4>📅 {_('pricing_monthly')}</h4>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown(f"""
    <div class="pricing-box">
        <h4>🏷️ {_('pricing_lifetime')}</h4>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    if st.sidebar.button(_("logout")):
        st.session_state.authenticated = False
        st.rerun()
    
    current_lessons = lessons[st.session_state.lang]
    lesson_titles = [f"{i+1}. {l['title'][:60]}" for i, l in enumerate(current_lessons)]
    selected_idx = st.sidebar.selectbox(_("jump_to_lesson"), range(len(current_lessons)), format_func=lambda i: lesson_titles[i], index=0)
    
    st.markdown(f'<div class="main-header"><h1>{_("main_title")}</h1><p>{_("main_sub")}</p></div>', unsafe_allow_html=True)
    
    lesson = current_lessons[selected_idx]
    with st.container():
        st.markdown(f'<div class="lesson-card">', unsafe_allow_html=True)
        if lesson.get("no_image", False):
            st.markdown(f"## {lesson['title']}")
            st.markdown(lesson["text"])
            if st.button(f"{_('read_aloud_button')} ({selected_idx+1})", key=f"read_{selected_idx}"):
                full_text = clean_text_for_speech(lesson["text"])
                escaped_text = full_text.replace('"', '\\"').replace("\n", " ").replace("'", "\\'")
                st.components.v1.html(f"""
                <script>
                    var utterance = new SpeechSynthesisUtterance("{escaped_text}");
                    utterance.lang = "{st.session_state.lang}";
                    window.speechSynthesis.cancel();
                    window.speechSynthesis.speak(utterance);
                </script>
                """, height=0)
                st.success(_("reading_success"))
        else:
            col_img, col_text = st.columns([1, 3])
            with col_img:
                if lesson["image"]:
                    st.image(lesson["image"], width=80)
            with col_text:
                st.markdown(f"## {lesson['title']}")
                st.markdown(lesson["text"])
                if st.button(f"{_('read_aloud_button')} ({selected_idx+1})", key=f"read_{selected_idx}"):
                    full_text = clean_text_for_speech(lesson["text"])
                    escaped_text = full_text.replace('"', '\\"').replace("\n", " ").replace("'", "\\'")
                    st.components.v1.html(f"""
                    <script>
                        var utterance = new SpeechSynthesisUtterance("{escaped_text}");
                        utterance.lang = "{st.session_state.lang}";
                        window.speechSynthesis.cancel();
                        window.speechSynthesis.speak(utterance);
                    </script>
                    """, height=0)
                    st.success(_("reading_success"))
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="footer">
        <p>© {datetime.now().year} {_('footer_text')}</p>
        <p>{_('footer_book')}</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- ROUTING ----------
if not st.session_state.authenticated:
    login_page()
else:
    main_page()
