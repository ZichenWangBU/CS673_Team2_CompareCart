import React from "react";
import "./../style/ProductCard.css";

const ProductCard = ({ product }) => {
  return (
    <div className="product-card">
      <div className="product-image-wrapper">
        <img
          src={product.img_ref || "placeholder.jpg"}
          alt={product.title}
          className="product-image"
          onError={(e) => (e.target.src = "placeholder.jpg")}
        />
      </div>
      <div className="product-details">
        <h3 className="product-title">{product.title}</h3>
        <p className="product-store">
          <strong>Store:</strong> {product.store}
        </p>
        <p className="product-price">
          <strong>Price:</strong> ${product.price.toFixed(2)}
        </p>
        <p className="product-rating">
          <strong>Rating:</strong> {product.star} stars
        </p>
        {product.detail_url && (
          <a
            href={product.detail_url}
            target="_blank"
            rel="noopener noreferrer"
            className="product-link"
          >
            View Details
          </a>
        )}
      </div>
    </div>
  );
};

export default ProductCard;
