from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

# Initialize the FastAPI app
app = FastAPI()

# --- NEW CORS CONFIGURATION ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ------------------------------

# Loading AI models into memory
try:
    with open('shows_list.pkl', 'rb') as file:
        shows = pickle.load(file)
    with open('similarity_matrix.pkl', 'rb') as file:
        cosine_sim = pickle.load(file)
        
    # Rebuild the lookup dictionary for the API
    indices = pd.Series(shows.index, index=shows['title']).drop_duplicates()
except FileNotFoundError:
    print("Error: Model files not found. Ensure .pkl files are in the same directory.")

class ProfileRequest(BaseModel):
    titles: list[str]

@app.post("/recommend")
def get_recommendations(request: ProfileRequest):
    titles_list = request.titles
    
    # Map titles to row numbers, ignoring any typos or shows not in the dataset
    idx_list = [indices[title] for title in titles_list if title in indices]
    
    if not idx_list:
        raise HTTPException(status_code=404, detail="We couldn't find any of those shows. Check your spelling!")
        
    # Calculate the average vector profile
    profile_scores = cosine_sim[idx_list].mean(axis=0)
    
    # Sort and filter out the inputted shows
    sim_scores = list(enumerate(profile_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    recommended_indices = [i[0] for i in sim_scores if i[0] not in idx_list]
    
    # Grab the top 5 matches
    top_5_matches = recommended_indices[:5]
    
    # Extract titles and convert to a standard Python list for JSON serialization
    recommended_titles = shows['title'].iloc[top_5_matches].tolist()
    
    # Return the clean JSON response
    return {"recommendations": recommended_titles}