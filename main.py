import os
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import google.generativeai as genai
from google.genai import types

# Load environment variables
load_dotenv()

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Gemini API setup
def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set in environment")
    return genai.Client(api_key=api_key)

# Resume context
AKASH_RESUME = """Akash Maity  
AI Engineer | ML Researcher | Data Scientist  
Ghaziabad, India | akashmaity701@gmail.com | +91 7838646805  
LinkedIn: linkedin.com/in/akashmaity | GitHub: github.com/akash123m

🌟 PROFESSIONAL SUMMARY  
AI Engineer & Tech Innovator with hands-on expertise in LLMs, Computer Vision, and Data Science. Adept at using state-of-the-art tools, building automation systems, and integrating APIs across platforms. Known for \"vibe coding\" — rapid, intuitive prototyping using emerging AI technologies. Proven leadership in developer communities, multiple hackathon wins, and project delivery across cloud, ML pipelines, and smart systems. Strong foundation in Python, data handling, and real-world model deployment.

🔧 CORE TECHNICAL SKILLS  
- Programming & Data: Python, SQL, Pandas, NumPy, Excel, Matplotlib, Seaborn  
- ML & Deep Learning: TensorFlow, PyTorch, scikit-learn, YOLOv8, OpenCV, CV/NLP/LLMs  
- AI Tools & APIs: LangChain, Hugging Face, LM Studio, OpenAI, ElevenLabs, Vosk, FastAPI  
- Cloud & Big Data: AWS (EC2, S3, Lambda), Azure ML, Hadoop, Spark  
- DevOps & Platforms: Docker, Git, Jupyter, Postman, VS Code, GitHub  
- Visualization: Tableau, Power BI  
- Workflow Style: Vibe Coding, API Integrations, Rapid Prototyping, Prompt Engineering

🎓 EDUCATION  
B.Tech – Artificial Intelligence & Data Science  
IIMT College of Engineering, 2021 – 2026  

📚 CERTIFICATIONS  
- Deloitte Australia: Data Analytics Simulation – June 2025  
- AWS APAC: Solutions Architecture Virtual Experience – June 2025  

💼 LEADERSHIP & EXPERIENCE  
Tech Lead – GDG On Campus, IIMT | Nov 2024 – Present  
- Directed AI/ML team across multiple projects with 95% timely delivery  
- Led cloud-based big data integrations and real-time ML pipelines  
- Boosted project workflow efficiency by 30% with automation logic  
- Mentored team through workshops; skill uplift of 20%

AI/ML Lead – Google Developer Student Club (GDSC) | Sep 2023 – Oct 2024  
- Delivered high-accuracy NLP and CV models (>90%)  
- Deployed models using Docker and CI/CD with 15% time savings  
- Integrated blockchain for secure AI output tracking  
- Led events that grew participation by 40%

Hackathon Organizer – Mind Installer Hackathon 3.0 | 2025  
- Core team member; coordinated 100+ participants and mentoring sessions  
- Enabled sponsor collaborations and managed real-time judging platforms

🏆 AWARDS & HIGHLIGHTS  
- 🥇 1st Place – IIMT Hackathon  
- 🥈 2nd Place – HackBVP 5.0 (Bharati Vidyapeeth)  
- 🥉 3rd Place – Ideathon @ IILM University  
- 🥉 3rd Place – Auronova Hackathon @ SAIT  

📂 PROJECTS  
🧠 Virtual Assistant – MarY (2025)  
- Created LLM-based desktop assistant using LangChain, voice recognition & APIs  
- Automated 75% of PC-level tasks (file ops, weather, browsing, voice commands)

🧠 BrainWaveController (2024)  
- Built EEG-powered AI system to control devices using brainwaves  
- Achieved 80%+ classification accuracy across signal bands

🧠 Smart Agriculture System (2023)  
- Developed ML model for predictive irrigation using real-time sensor & weather data  
- Reduced water waste by 25% in test deployments

🧠 Duality.AI – Vision Pipeline for XR (2025)  
- Built CV solutions using YOLOv8 + OpenCV on Duality Falcon Cloud  
- Delivered object detection and gesture models for AR/VR/MR scenarios

🧠 Mobile Health Assistant (2023)  
- NLP-powered chatbot for early diagnosis suggestions and symptom logging  
- Delivered 85% prediction accuracy for most common illness categories

🌐 PERSONAL PROJECT STYLE  
- \"Vibe coding\" builds with rapid prototyping  
- Automation systems built using voice + LLM + Python scripting  
- Daily usage of AI APIs (OpenAI, ElevenLabs, Gemini, etc.) for tools & workflows

💬 LANGUAGES & INTERESTS  
- Languages: English, Hindi, Bengali  
- Interests: AI Ethics, Indie Projects, Psychology, Creative Tech Storytelling  
"""

@app.post("/terminal")
async def terminal_query(request: Request):
    data = await request.json()
    user_input = data.get("input", "").strip().lower()

    # Prewritten fallback outputs
    prewritten = {
        "resume": (
            "Akash Maity\nAI Engineer | ML Researcher | Data Scientist\n"
            "Ghaziabad, India | akashmaity701@gmail.com | +91 7838646805\n"
            "LinkedIn: linkedin.com/in/akashmaity | GitHub: github.com/akash123m\n\n"
            "AI Engineer & Tech Innovator specializing in LLMs, Computer Vision, and Data Science.\n"
            "Proven leadership, multiple hackathon wins, and rapid prototyping skills.\n"
        ),
        "skills": (
            "Core Technical Skills:\n"
            "- Python, SQL, Pandas, NumPy, Excel\n"
            "- TensorFlow, PyTorch, scikit-learn, YOLOv8, OpenCV\n"
            "- LangChain, Hugging Face, OpenAI, Gemini, FastAPI\n"
            "- AWS, Azure ML, Docker, Hadoop, Spark\n"
            "- Tableau, Power BI, Git, CI/CD, Postman\n"
        ),
        "projects": (
            "Projects:\n"
            "- Virtual Assistant – MarY: LLM-based desktop assistant (2025)\n"
            "- BrainWaveController: EEG-powered AI device control (2024)\n"
            "- Smart Agriculture System: Predictive irrigation ML (2023)\n"
            "- Duality.AI: Vision pipeline for XR (2025)\n"
            "- Mobile Health Assistant: NLP-powered chatbot (2023)\n"
        ),
        "awards": (
            "Awards & Highlights:\n"
            "- 🥇 1st Place – IIMT Hackathon\n"
            "- 🥈 2nd Place – HackBVP 5.0\n"
            "- 🥉 3rd Place – Ideathon @ IILM University\n"
            "- 🥉 3rd Place – Auronova Hackathon @ SAIT\n"
        ),
        "help": (
            "Available commands:\n"
            "- resume\n- skills\n- projects\n- awards\n- help\n- cloud projects\n- ml projects\n- cv projects\n- nlp llm projects\n- mary\n- brainwavecontroller\n- smart agriculture\n- duality\n- mobile health\n- who are you\n"
        ),
        "akash<": (
            "[AKASH.AI] Akash Maity: AI Engineer, ML Researcher, and Tech Innovator.\n"
            "Specializing in LLMs, Computer Vision, Data Science, and rapid prototyping.\n"
            "Known for 'vibe coding', hackathon wins, and building smart, scalable systems.\n"
            "Contact: akashmaity701@gmail.com | GitHub: akash123m\n"
        ),
        "who are you": (
            "[AKASH.AI] Akash Maity: AI Engineer, ML Researcher, and Tech Innovator.\n"
            "Specializing in LLMs, Computer Vision, Data Science, and rapid prototyping.\n"
            "Known for 'vibe coding', hackathon wins, and building smart, scalable systems.\n"
            "Contact: akashmaity701@gmail.com | GitHub: akash123m\n"
        ),
        "cloud projects": (
            "Cloud & DevOps Projects:\n"
            "- Duality.AI: Vision Pipeline for XR (2025):\n"
            "    • Built CV solutions using YOLOv8 + OpenCV on Duality Falcon Cloud\n"
            "    • Delivered object detection and gesture models for AR/VR/MR scenarios\n"
            "- Smart Agriculture System (2023):\n"
            "    • Developed ML model for predictive irrigation using real-time sensor & weather data\n"
            "    • Reduced water waste by 25% in test deployments\n"
            "- AWS APAC: Solutions Architecture Virtual Experience (2025):\n"
            "    • Cloud architecture, deployment, and best practices\n"
        ),
        "ml projects": (
            "ML/AI Projects:\n"
            "- Virtual Assistant – MarY (2025):\n"
            "    • Created LLM-based desktop assistant using LangChain, voice recognition & APIs\n"
            "    • Automated 75% of PC-level tasks (file ops, weather, browsing, voice commands)\n"
            "- BrainWaveController (2024):\n"
            "    • Built EEG-powered AI system to control devices using brainwaves\n"
            "    • Achieved 80%+ classification accuracy across signal bands\n"
            "- Smart Agriculture System (2023):\n"
            "    • Developed ML model for predictive irrigation using real-time sensor & weather data\n"
            "    • Reduced water waste by 25% in test deployments\n"
        ),
        "cv projects": (
            "Computer Vision Projects:\n"
            "- Duality.AI: Vision Pipeline for XR (2025):\n"
            "    • Built CV solutions using YOLOv8 + OpenCV on Duality Falcon Cloud\n"
            "    • Delivered object detection and gesture models for AR/VR/MR scenarios\n"
            "- BrainWaveController (2024):\n"
            "    • Built EEG-powered AI system to control devices using brainwaves\n"
        ),
        "nlp llm projects": (
            "NLP & LLM Projects:\n"
            "- Virtual Assistant – MarY (2025):\n"
            "    • Created LLM-based desktop assistant using LangChain, voice recognition & APIs\n"
            "    • Automated 75% of PC-level tasks (file ops, weather, browsing, voice commands)\n"
            "- Mobile Health Assistant (2023):\n"
            "    • NLP-powered chatbot for early diagnosis suggestions and symptom logging\n"
            "    • Delivered 85% prediction accuracy for most common illness categories\n"
        ),
        "mary": (
            "🧠 Virtual Assistant – MarY (2025):\n"
            "- Created LLM-based desktop assistant using LangChain, voice recognition & APIs\n"
            "- Automated 75% of PC-level tasks (file ops, weather, browsing, voice commands)\n"
        ),
        "brainwavecontroller": (
            "🧠 BrainWaveController (2024):\n"
            "- Built EEG-powered AI system to control devices using brainwaves\n"
            "- Achieved 80%+ classification accuracy across signal bands\n"
        ),
        "smart agriculture": (
            "🧠 Smart Agriculture System (2023):\n"
            "- Developed ML model for predictive irrigation using real-time sensor & weather data\n"
            "- Reduced water waste by 25% in test deployments\n"
        ),
        "duality": (
            "🧠 Duality.AI – Vision Pipeline for XR (2025):\n"
            "- Built CV solutions using YOLOv8 + OpenCV on Duality Falcon Cloud\n"
            "- Delivered object detection and gesture models for AR/VR/MR scenarios\n"
        ),
        "mobile health": (
            "🧠 Mobile Health Assistant (2023):\n"
            "- NLP-powered chatbot for early diagnosis suggestions and symptom logging\n"
            "- Delivered 85% prediction accuracy for most common illness categories\n"
        ),
    }

    def match_fallback(user_input):
        # Normalize input
        cmd = user_input.strip().lower()
        # Direct match
        if cmd in prewritten:
            return prewritten[cmd]
        # Natural language keyword matching
        if any(word in cmd for word in ["project", "projects", "work", "portfolio", "built", "done"]):
            return prewritten["projects"]
        if any(word in cmd for word in ["certification", "certifications", "certs", "certificate", "courses", "course"]):
            return (
                "Certifications:\n"
                "- Deloitte Australia: Data Analytics Simulation – June 2025\n"
                "- AWS APAC: Solutions Architecture Virtual Experience – June 2025\n"
            )
        if any(word in cmd for word in ["skill", "skills", "technologies", "tech stack", "tools", "proficiencies"]):
            return prewritten["skills"]
        if any(word in cmd for word in ["award", "awards", "achievements", "prizes", "honors", "highlights"]):
            return prewritten["awards"]
        if any(word in cmd for word in ["resume", "cv", "bio", "summary", "profile"]):
            return prewritten["resume"]
        if any(word in cmd for word in ["who are you", "about", "yourself", "akash", "identity", "who is akash"]):
            return prewritten["who are you"]
        if "cloud" in cmd:
            return prewritten["cloud projects"]
        if "ml" in cmd or "machine learning" in cmd:
            return prewritten["ml projects"]
        if "cv" in cmd or "computer vision" in cmd:
            return prewritten["cv projects"]
        if "nlp" in cmd or "llm" in cmd:
            return prewritten["nlp llm projects"]
        if "mary" in cmd:
            return prewritten["mary"]
        if "brainwave" in cmd:
            return prewritten["brainwavecontroller"]
        if "smart agriculture" in cmd:
            return prewritten["smart agriculture"]
        if "duality" in cmd:
            return prewritten["duality"]
        if "mobile health" in cmd:
            return prewritten["mobile health"]
        return None

    try:
        client = get_gemini_client()
        model = "gemini-2.0-flash-lite"  # Use "gemini-1.5-pro-latest" for better results
        contents = [
            types.Content(role="user", parts=[types.Part.from_text(AKASH_RESUME + "\n\n" + user_input)])
        ]
        def stream_response():
            for chunk in client.models.generate_content_stream(
                model=model,
                contents=contents,
            ):
                if hasattr(chunk, "text"):
                    yield chunk.text
        return StreamingResponse(stream_response(), media_type="text/plain")
    except Exception as e:
        # Fallback: stream prewritten output or error
        def fallback_stream():
            output = match_fallback(user_input)
            if output:
                yield output
            else:
                yield ("[AKASH.AI_TERMINAL] Gemini backend unavailable.\n"
                       "Try: resume, skills, projects, awards, help, cloud projects, ml projects, cv projects, nlp llm projects, mary, brainwavecontroller, smart agriculture, duality, mobile health, who are you\n")
        return StreamingResponse(fallback_stream(), media_type="text/plain")

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tryfolio.html"))
    if not os.path.exists(html_path):
        return HTMLResponse("<h1>HTML file not found</h1>", status_code=404)
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read() 
