import React from "react";
import { Nav, Navbar } from "react-bootstrap";
import { Link, useLocation } from "react-router-dom";

const NavBar = () => {
  const location = useLocation();

  return (
    <Navbar
      bg="light"
      data-bs-theme="light"
      style={{
        backgroundColor: "#fff",
        padding: "20px",
        boxShadow: "rgba(149, 157, 165, 0.2) 0px 2px 3px",
        width: "250px",
        minHeight: "80vh",
        flexDirection: 'column'
      }}
    >
        <Link
          to="/"
          style={{
            textDecoration: "none",
            color: "#333",
            display: "flex",
            alignItems: "center",
            gap: "10px",
            marginBottom: "20px",
          }}
        >
          <img src="/logo.png" alt="logo" />
          <p style={{ fontSize: "18px", fontWeight: 600, margin: 0 }}>Cake Candy</p>
        </Link>
        <Nav
          className="me-auto"
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "5px",
            width: "200px",
          }}
        >
          <Link
            to="/"
            style={
              location.pathname === "/"
                ? {
                    textDecoration: "none",
                    color: "#fff",
                    backgroundColor: "#0d6efd",
                    padding: "10px",
                    borderRadius: "5px",
                  }
                : {
                    textDecoration: "none",
                    color: "#333",
                    padding: "10px",
                    borderRadius: "5px",
                  }
            }
          >
            Quản lý bánh kẹo
          </Link>
          <Link
            to="/thong-tin-tai-khoan"
            style={
              location.pathname === "/thong-tin-tai-khoan"
                ? {
                    textDecoration: "none",
                    color: "#fff",
                    backgroundColor: "#0d6efd",
                    padding: "10px",
                    borderRadius: "5px",
                  }
                : {
                    textDecoration: "none",
                    color: "#333",
                    padding: "10px",
                    borderRadius: "5px",
                  }
            }
          >
            Thông tin tài khoản
          </Link>

          <div
            style={{
              textDecoration: "none",
              color: "#333",
              padding: "10px",
              borderRadius: "5px",
              cursor: "pointer",
            }}
          >
            Đăng xuất
          </div>
        </Nav>
    </Navbar>
  );
};

export default NavBar;
