import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../style/HomePage.css";
import welcomeImage from "../images/img-1.png"; // Update path to your image
import reason1 from "../images/compare.png"; // Update path to your image
import reason2 from "../images/Money.png"; // Update path to your image
import reason3 from "../images/aim.png"; // Update path to your image
import reason4 from "../images/featured-04.png"; // Update path to your image

const HomePage = () => {
  const [searchQuery, setSearchQuery] = useState(""); // For capturing search input
  const navigate = useNavigate();

  const handleSearch = (e) => {
    e.preventDefault(); // Prevent default form submission
    if (searchQuery.trim()) {
      navigate(`/search?keyword=${searchQuery.trim()}`); // Redirect to SearchPage with query
    }
  };

  return (
    <div className="home-page">
      {/* Expanded Blue Strip */}
      <div className="welcome-section">
        <div className="content">
          {/* Left Section */}
          <div className="text-section">
            <h1>Welcome to CompareCart</h1>
            <p>
              CompareCart is your one-stop destination to compare prices and
              products across multiple online stores. Save time, save money,
              and shop smarter!
            </p>
            <div className="search-bar">
              <form onSubmit={handleSearch}>
                <input
                  type="text"
                  placeholder="Search for products..."
                  id="searchText"
                  name="searchKeyword"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)} // Update query state
                />
                <button type="submit">Search</button>
              </form>
            </div>
          </div>

          {/* Right Section */}
          <div className="image-section">
            <img src={welcomeImage} alt="Welcome" />
          </div>
        </div>
      </div>

      {/* Section Break */}
      <div className="section-break"></div>

      {/* Why Choose Us Section */}
      <div className="why-choose-us">
        <h2>Why Choose Us?</h2>
        <div className="reasons">
          <div className="reason-box">
            <div className="icon">
              <img src={reason1} alt="Reason 1" />
            </div>
            <h4>Compare prices across multiple platforms</h4>
          </div>
          <div className="reason-box">
            <div className="icon">
              <img src={reason2} alt="Reason 2" />
            </div>
            <h4>Find the best deals and save money</h4>
          </div>
          <div className="reason-box">
            <div className="icon">
              <img src={reason3} alt="Reason 3" />
            </div>
            <h4>Accurate and up-to-date product information</h4>
          </div>
          <div className="reason-box">
            <div className="icon">
              <img src={reason4} alt="Reason 4" />
            </div>
            <h4>User-friendly interface for easy navigation</h4>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;





