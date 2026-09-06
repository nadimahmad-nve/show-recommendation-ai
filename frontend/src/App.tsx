import { useState} from 'react';

function App() {
  const [titleList, setTitleData] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [errorMessage, setErrorMessage] = useState("");

  const handleDiscover = async () => {
    setErrorMessage("");
    setRecommendations([]);

    const formattedTitles = titleList.split(",").map(title => title.trim());
    if (formattedTitles.length === 0) return;

    try {
      const response = await fetch("http://127.0.0.1:8000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titles: formattedTitles }),
      });

      if (!response.ok) {
        throw new Error("Show not found in the database.");
      }

      const data = await response.json();
      setRecommendations(data.recommendations);

    } catch (err: any) {
      setErrorMessage(err.message);
    }
  };

  

  return (
    <div className="app-container">
      <div className="neon-blob blob-blue"></div>
      <div className="neon-blob blob-green"></div>

      <h1 className="neon-title">AI TV Recommender</h1>
      <p style={{ fontWeight: 'bold' }}>Enter show titles separated by commas to build your profile.</p>

      <div className="search-section">
        <input 
          className="neon-input"
          type="text" 
          placeholder="e.g. Stranger Things, Dark" 
          value={titleList}
          onChange={(e) => setTitleData(e.target.value)}
        />
        <button className="neon-button" onClick={handleDiscover}>
          Discover
        </button>
      </div>

      {errorMessage && (
        <p style={{ color: '#ff003c', textShadow: '0 0 8px #ff003c', fontWeight: 'bold' }}>
          {errorMessage}
        </p>
      )}

      {recommendations.length > 0 && (
        <div>
          <h2 className="neon-title">Your Top Matches:</h2>
          <ul className="results-list" >
            {recommendations.map((show, index) => (
              <li key={index} style={{ fontWeight: 'bold' }}>
                {index + 1}. {show}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;