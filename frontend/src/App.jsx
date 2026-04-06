import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Profile from './pages/Profile';
import Leaderboard from './pages/Leaderboard';
import Locations from './pages/Locations';
import Rewards from './pages/Rewards';

function App() {
  return (
    <div className="app">
      <nav className="navbar">
        <div className="nav-logo">EcoSystem</div>
        <div className="nav-links">
          <Link to="/">Главная</Link>
          <Link to="/locations">Карта</Link>
          <Link to="/leaderboard">Рейтинг</Link>
          <Link to="/rewards">Магазин</Link>
          <Link to="/profile">Профиль</Link>
          <Link to="/login" className="nav-btn">Войти</Link>
        </div>
      </nav>

      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/locations" element={<Locations />} />
          <Route path="/rewards" element={<Rewards />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
