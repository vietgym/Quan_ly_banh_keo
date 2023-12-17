import React from "react";
import { Button } from "react-bootstrap";

const Header = () => {
  return (
    <div
      style={{
        width: "100%",
        padding: "10px 20px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
      }}
    >
      <Button variant="outline-primary">
        Kết nối metamask
      </Button>

      <div style={{display: 'flex', alignItems: 'center', gap: '10px'}}>
        <p style={{margin: 0, fontWeight: 600}}>Lê hoàng long</p>
        <img src= "/logo.png" alt = "" style={{width: '45px', height: '45px', borderRadius: '50%'}}/>
      </div>
    </div>
  );
};

export default Header;
