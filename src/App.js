import React from "react";
import { Route, BrowserRouter, Routes } from "react-router-dom";
import UserLayout from "./layouts/UserLayout";
import Cake from "./pages/Cake";
import AddCake from "./pages/AddCake";
import EditCake from "./pages/EditCake";
import EditUser from "./pages/EditUser";
import CakeInfo from "./pages/CakeInfo";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/quan-ly-banh-keo/them-moi"
          element={
            <UserLayout>
              <AddCake />
            </UserLayout>
          }
        />
        <Route
          path="/quan-ly-banh-keo/chinh-sua/:id"
          element={
            <UserLayout>
              <EditCake />
            </UserLayout>
          }
        />

        <Route
          path="/quan-ly-banh-keo/:id"
          element={
            <UserLayout>
              <CakeInfo />
            </UserLayout>
          }
        />

        <Route
          path="/thong-tin-tai-khoan"
          element={
            <UserLayout>
              <EditUser />
            </UserLayout>
          }
        />
        <Route
          index
          path="/"
          element={
            <UserLayout>
              <Cake />
            </UserLayout>
          }
        />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
