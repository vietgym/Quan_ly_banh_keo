import React from "react";

const CakeInfo = () => {
  return (
    <div style={{ display: "flex", justifyContent: "center", padding: "20px" }}>
      <table
        style={{
          border: "1px solid #000",
          borderCollapse: "separate",
          backgroundColor: "#fff",
        }}
      >
        <tr>
          <td style={{ border: "1px solid #000" }} colspan="2">
            Sữa Tươi Cô Gái Hà Lan
          </td>
        </tr>
        <tr>
          <td colspan="2" style={{ border: "1px solid #000" }}>
            <div
              style={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <img
                src="/sua_co_gai.jpg"
                alt=""
                style={{ width: "300px", height: "400px" }}
              />
              <div style={{ display: "flex", gap: "10px" }}>
                <label
                  style={{
                    fontSize: "30px",
                    padding: "10px",
                    backgroundColor: "#f0f0f0",
                    color: "#476dff",
                  }}
                >
                  180ml
                </label>
                <label
                  style={{
                    fontSize: "30px",
                    padding: "10px",
                    backgroundColor: "#f0f0f0",
                    color: "#476dff",
                  }}
                >
                  Rat It Duong
                </label>
              </div>
            </div>
          </td>
        </tr>
        <tr>
          <td style={{ border: "1px solid #000" }}>Thanh phan Dinh Duong:</td>
          <td style={{ border: "1px solid #000" }}>
            Duong, sua, chat dinh duong
          </td>
        </tr>
        <tr>
          <td style={{ border: "1px solid #000" }}>Lợi ích:</td>
          <td style={{ border: "1px solid #000" }}>Uống vào thông minh</td>
        </tr>
        <tr>
          <td style={{ border: "1px solid #000" }}>trọng Lượng: 180gam</td>
          <td style={{ border: "1px solid #000" }}>Đơn giá: 7000đ</td>
        </tr>
      </table>
    </div>
  );
};

export default CakeInfo;
