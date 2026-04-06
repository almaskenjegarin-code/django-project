import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Mail, Lock, LogIn } from 'lucide-react';
import './Auth.css';

const Login = () => {
    const [formData, setFormData] = useState({ email: '', password: '' });

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Login attempt:', formData);
        // TODO: Connect to Django API
    };

    return (
        <div className="auth-container">
            <div className="auth-card">
                <div className="auth-header">
                    <h2>С возвращением</h2>
                    <p>Войдите в эко-аккаунт, чтобы продолжить получать баллы.</p>
                </div>

                <form onSubmit={handleSubmit} className="auth-form">
                    <div className="input-group">
                        <Mail className="input-icon" size={20} />
                        <input
                            type="email"
                            placeholder="Электронная почта"
                            value={formData.email}
                            onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                            required
                        />
                    </div>

                    <div className="input-group">
                        <Lock className="input-icon" size={20} />
                        <input
                            type="password"
                            placeholder="Пароль"
                            value={formData.password}
                            onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                            required
                        />
                    </div>

                    <div className="auth-actions">
                        <label className="remember-me">
                            <input type="checkbox" /> Запомнить меня
                        </label>
                        <a href="#" className="forgot-password">Забыли пароль?</a>
                    </div>

                    <button type="submit" className="btn btn-primary btn-full">
                        <LogIn size={20} /> Войти
                    </button>
                </form>

                <div className="auth-footer">
                    Нет аккаунта? <Link to="/register">Зарегистрироваться</Link>
                </div>
            </div>
        </div>
    );
};

export default Login;
