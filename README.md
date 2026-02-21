# ai-schema-assistant
AI MongoDB Schema Assistant Project

# AI-Powered Schema Design Assistant for MongoDB

## Project Description
The AI-Powered Schema Design Assistant helps developers design optimized MongoDB schemas using natural language input.

The system analyzes entity relationships and suggests collection structures, indexing strategies, and design justification.

---

## Features
- Accepts natural language database design description
- Suggests MongoDB collections structure
- Recommends indexing strategy
- Explains design decisions
- Backend AI microservice architecture

---

## Technology Stack
- Frontend: HTML, JavaScript
- Backend: Node.js, Express.js
- AI Service: Python FastAPI
- API Communication: Axios
- Database Design Logic: Rule-based AI

---

## Project Architecture
User Input → Frontend UI → Node Backend → Python AI Service → Response Display

---

## How to Run Project

### 1. Clone Repository
git clone https://github.com/yourusername/ai-schema-assistant.git

### 2. Install Backend Dependencies
cd backend
npm install

Run backend:
node server.js

### 3. Install AI Service Dependencies
cd ai-service
pip install fastapi uvicorn pydantic

Run AI service:
python -m uvicorn ai_service:app --reload

### 4. Run Frontend
Open `index.html` using Live Server in VS Code.

---

## Future Improvements
- Integration with OpenAI API
- MongoDB Atlas connection
- Schema visualization graphs
- Performance prediction
- Multi-database support

---

## Author
Kosireddy Rishika 
