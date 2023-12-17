import React, { useState } from "react";
import { Button, Modal, Table } from "react-bootstrap";

const Cake = () => {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <div
      style={{
        padding: "20px",
        display: "flex",
        alignItems: "flex-end",
        flexDirection: "column",
        gap: "10px",
      }}
    >
      <Button variant="primary" style={{ width: "max-content" }}>
        <a
          href="/quan-ly-banh-keo/them-moi"
          style={{ textDecoration: "none", color: "inherit" }}
        >
          Thêm mới
        </a>
      </Button>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Hình ảnh</th>
            <th>Tên sản phẩm</th>
            <th>Giá</th>
            <th>Nhà sản xuất</th>
            <th>Nhà phân phối</th>
            <th>Hash</th>
            <th>Thao tác</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>
              <img src="/sua_co_gai.jpg" alt="" style={{width: '100px'}} />
            </td>
            <td>Bánh chocopike</td>
            <td>25000VNĐ</td>
            <td>Cty Orion</td>
            <td>Đại lý bánh kẹo orion</td>
            <td>jhasdashdhasjwqhewhjdasdjhas</td>
            <td>
              <div style={{ display: "flex", gap: "10px" }}>
                <a
                  href="/quan-ly-banh-keo/1"
                  style={{
                    textDecoration: "none",
                    color: "inherit",
                    cursor: "pointer",
                  }}
                >
                  Xem
                </a>

                <a
                  href="/quan-ly-banh-keo/chinh-sua/1"
                  style={{
                    textDecoration: "none",
                    color: "inherit",
                    cursor: "pointer",
                  }}
                >
                  Sửa
                </a>
                <p
                  style={{
                    cursor: "pointer",
                  }}
                  onClick={handleShow}
                >
                  Xoá
                </p>
              </div>
            </td>
          </tr>
        </tbody>
      </Table>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Xoá bánh kẹo</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          Bạn có chắc chắn muốn xoá bánh kẹo "abc" không ?
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Huỷ
          </Button>
          <Button variant="primary" onClick={handleClose}>
            Xác nhận
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
};

export default Cake;
