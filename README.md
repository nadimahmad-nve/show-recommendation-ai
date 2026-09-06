# AI TV Recommender 📺✨

A full-stack web application that generates highly customised TV show recommendations using natural language processing. By analysing the plot summaries and genres of thousands of shows, this engine builds a unique viewer profile based on your favourite titles and mathematically determines the best matches.

The user interface features a responsive, custom-built cyberpunk dark mode with neon CSS styling.

## Features

*   **Machine Learning Engine:** Utilises TF-IDF vectorisation to convert text descriptions into high-dimensional data, applying cosine similarity to find overlapping themes.
*   **Asynchronous REST API:** Powered by FastAPI for rapid, non-blocking requests between the client and the recommendation model.
*   **Dynamic Frontend:** Built with React (TypeScript) and Vite, featuring controlled components and real-time error handling for a seamless user experience.
*   **Cyberpunk Aesthetic:** Hand-coded CSS featuring glowing text shadows, box-shadow stacking, and infinite keyframe background animations.

## Tech Stack

*   **Frontend:** React (Vite), TypeScript, HTML5, Custom CSS
*   **Backend:** Python, FastAPI, Uvicorn
*   **Data Science:** Pandas, Scikit-learn, Jupyter Notebook

## How It Works

1.  **Data Processing:** The engine ingests a dataset of TV shows and builds a vast vocabulary matrix.
2.  **Vectorisation:** Each show is translated into a numerical array representing the frequency and importance of specific words.
3.  **Profile Generation:** When a user submits a comma-separated list of shows, the backend fetches their respective vectors and calculates a mean "profile" vector.
4.  **Cosine Similarity:** The engine measures the geometric angle between the user's combined profile vector and every other show in the database. The smallest angles yield the closest thematic matches.

## Local Setup & Installation

Because the machine learning models and dependency folders are heavily optimised and large, they are excluded from this repository. You will need to generate the data locally before starting the servers.

### 1. Backend Preparation
Navigate to the backend directory and set up your virtual environment:

```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\Activate.ps1
# On Mac/Linux:
source venv/bin/activate

pip install fastapi uvicorn pandas scikit-learn