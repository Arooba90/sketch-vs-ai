# Sketch vs AI 


**Sketch vs AI** is a fun and interactive project where users can draw a sketch in their browser. The sketch is sent to a backend powered by an LLM with vision capabilities (via Ollama), which tries to guess what the sketch represents.


---

## 🚀 Features

-  In-browser canvas for freehand drawing
-  Uploads sketches directly to a FastAPI backend
-  Uses **Ollama** + **LLaVA model** locally for AI vision
-  Returns a fun, intelligent guess based on your drawing
-  No cloud dependencies — everything runs locally!

---

## 🛠️ Tech Stack

| Layer      | Tools                     |
|------------|---------------------------|
| Frontend   | HTML5 Canvas + JavaScript |
| Backend    | Python + FastAPI          |
| AI Model   | LLaVA via [Ollama](https://ollama.com/) |
| Image Prep | Pillow (PNG conversion)   |

---

## 📦 Local Setup

### 1. Clone the repo
<pre>
git clone https://github.com/Arooba90/sketch-vs-ai.git
cd sketch-vs-ai
</pre>

### 2. Install dependencies
<pre>
poetry install
</pre>

### 3. Start Ollama (with LLaVA or BakLLaVA)
<pre>
ollama pull llava
ollama run llava
</pre>

### 4. Run the app
<pre>
uvicorn app.main:app --reload
</pre>

Then visit: http://localhost:8000/ui/

---
## How It Works
1.You draw a sketch in your browser \n
2.The drawing is sent to the /upload-sketch API as a PNG \n
3.The backend encodes the image and sends it to a local Ollama model \n
4.The model returns its best guess \n
5.The frontend displays the result 
