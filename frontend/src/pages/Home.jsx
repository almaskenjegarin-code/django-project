import React from 'react';
import { Link } from 'react-router-dom';
import { Leaf, MapPin, Trophy, Gift, ArrowRight } from 'lucide-react';
import './Home.css';

const Home = () => {
    return (
        <div className="home-container">
            {/* Hero Section */}
            <section className="hero">
                <div className="hero-content">
                    <div className="badge">🌱 Эко-революция уже здесь</div>
                    <h1 className="hero-title">
                        Превращайте мусор в <span className="text-gradient">Сокровища</span>
                    </h1>
                    <p className="hero-subtitle">
                        Присоединяйтесь к тысячам пользователей, делающим мир чище.
                        Сортируйте отходы, зарабатывайте Eco-Points и обменивайте их на реальные награды.
                    </p>
                    <div className="hero-actions">
                        <Link to="/register" className="btn btn-primary btn-lg">
                            Начать <ArrowRight size={20} />
                        </Link>
                        <Link to="/locations" className="btn btn-secondary btn-lg">
                            Найти пункты
                        </Link>
                    </div>
                </div>

                {/* Decorative elements */}
                <div className="gradient-blob blob-1"></div>
                <div className="gradient-blob blob-2"></div>
            </section>

            {/* Features Section */}
            <section className="features">
                <h2 className="section-title">Как это работает</h2>
                <div className="features-grid">
                    <div className="feature-card">
                        <div className="feature-icon bg-green">
                            <MapPin size={28} color="white" />
                        </div>
                        <h3>1. Найдите пункт приема</h3>
                        <p>Используйте интерактивную карту для поиска ближайших эко-контейнеров в вашем городе.</p>
                    </div>

                    <div className="feature-card">
                        <div className="feature-icon bg-blue">
                            <Leaf size={28} color="white" />
                        </div>
                        <h3>2. Сдавайте вторсырье</h3>
                        <p>Правильно сортируйте отходы. Пункты приема подтвердят сдачу и начислят баллы.</p>
                    </div>

                    <div className="feature-card">
                        <div className="feature-icon bg-yellow">
                            <Trophy size={28} color="white" />
                        </div>
                        <h3>3. Поднимайтесь в рейтинге</h3>
                        <p>Соревнуйтесь с друзьями и соседями в еженедельной таблице лидеров.</p>
                    </div>

                    <div className="feature-card">
                        <div className="feature-icon bg-purple">
                            <Gift size={28} color="white" />
                        </div>
                        <h3>4. Получайте награды</h3>
                        <p>Тратьте заработанные Eco-Points в нашем магазине на скидки и уникальные товары.</p>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default Home;
