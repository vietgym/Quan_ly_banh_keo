import React from 'react'
import NavBar from '../../layouts/UserLayout/NavBar'
import Header from '../../layouts/UserLayout/Header'

const UserLayout = ({children}) => {
  return (
    <div style={{display: 'flex', backgroundColor: '#f9f9f9', minWidth: '100vw', minHeight: '100vh'}}>
      <NavBar />
      <div style={{width: '100%'}}>
        <Header />
        {children}
      </div>
    </div>
  )
}

export default UserLayout
