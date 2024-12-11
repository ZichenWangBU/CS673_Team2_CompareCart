import React from "react";
import "../style/Navbar.css";
import logo from "../images/purchase.png";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo-container">
        <img src={logo} alt="CompareCart Logo" className="navbar-logo" />
        <h1 className="navbar-title">CompareCart</h1>
      </div>
      <div className="nav-buttons">
        <button>
          <a href="/">Home</a>
        </button>
        <button>
          <a href="/search">Search</a>
        </button>
        <button>
          <a href="/contact">Contact Us</a>
        </button>
      </div>
    </nav>
  );
};

export default Navbar;

