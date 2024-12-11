import React, { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import "../style/SearchPage.css";

const SearchPage = () => {
  const [searchParams] = useSearchParams();
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const query = searchParams.get("keyword");
    if (query) {
      setSearchQuery(query);
      handleSearch(query);
    }
  }, [searchParams]);

  const handleSearch = (query) => {
    fetch(`http://127.0.0.1:5000/api/items/search?keyword=${query}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        setSearchResults(data);
        setError(null);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setError("Error fetching data. Please try again.");
      });
  };

  const handleReset = () => {
    setSearchQuery("");
    setSearchResults([]);
    setError(null);
  };

  return (
    <div className="search-page">
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search for items..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <button onClick={() => handleSearch(searchQuery)}>Search</button>
        <button onClick={handleReset} className="reset-button">
          Reset
        </button>
      </div>
      {error && <p className="error-message">{error}</p>}
      {searchResults.length === 0 && !error && <p>Start searching and discover everything you need in one place!</p>}
      <div className="search-results">
        {searchResults.map((result) => (
          <div key={result.id} className="result-card">
            {result.img_ref && (
              <img
                src={result.img_ref}
                alt={result.title}
                className="result-image"
                onError={(e) => (e.target.style.display = "none")}
              />
            )}
            <h3>{result.title}</h3>
            <p>
              <strong>Store:</strong> {result.store}
            </p>
            <p>
              <strong>Price:</strong> ${result.price.toFixed(2)}
            </p>
            <p>
              <strong>Rating:</strong> {result.star} stars
            </p>
            {result.detail_url && (
              <a href={result.detail_url} target="_blank" rel="noopener noreferrer" className="detail-link">
                View Details
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default SearchPage;
