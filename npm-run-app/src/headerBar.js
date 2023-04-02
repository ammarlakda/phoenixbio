import React from "react";
import logo from "./logo.png"; // import your logo image file here

const HeaderBar = () => {
  return (
    <div style={{ backgroundColor: "rgb(32,33,35)", color: "white", display: "flex", alignItems: "center" }}>
      <img src={logo} alt="Logo" style={{ height: 100, marginLeft: 10 }} /> {/* adjust height and margin as needed */}
      <h1 style={{ paddingRight: 8 }}>Genome Atlas</h1>
      <h1 style={{color: "rgb(33,180,68"}}> Powering your next Genome Search </h1>
    </div>
  );
};

export default HeaderBar;