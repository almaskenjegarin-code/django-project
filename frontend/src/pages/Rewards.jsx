import React, { useState, useEffect } from 'react';
import { ShoppingBag, Zap, Tag } from 'lucide-react';
import api from '../api';
import './Rewards.css';

const Rewards = () => {
    const [activeTab, setActiveTab] = useState('all');
    const [rewards, setRewards] = useState([]);
    const [userPoints, setUserPoints] = useState(1250); // Still mock for now until Auth is fully wired
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchRewards = async () => {
            try {
                const response = await api.get('rewards/shop/');
                // Transform the backend data 
                const mappedData = response.data.map(item => ({
                    id: item.id,
                    name: item.title,
                    category: 'merch', // hardcoded for demo as category isn't in backend model
                    price: item.cost,
                    image: item.image ? `http://localhost:8000${item.image}` : '🎁',
                    stock: 10, // hardcoded for demo
                }));
                setRewards(mappedData);
            } catch (error) {
                console.error('Error fetching rewards:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchRewards();
    }, []);

    const filteredRewards = activeTab === 'all'
        ? rewards
        : rewards.filter(r => r.category === activeTab);

    return (
        <div className="rewards-container">
            <div className="rewards-header">
                <div className="header-text">
                    <h1>Эко-Магазин</h1>
                    <p>Обменяйте заработанные баллы на эксклюзивные эко-товары и скидки.</p>
                </div>

                <div className="points-balance-card">
                    <div className="balance-icon">
                        <Zap size={28} color="white" />
                    </div>
                    <div className="balance-info">
                        <span className="balance-label">Ваш баланс</span>
                        <span className="balance-amount">{userPoints} баллов</span>
                    </div>
                </div>
            </div>

            <div className="shop-controls">
                <div className="tabs">
                    <button
                        className={`tab ${activeTab === 'all' ? 'active' : ''}`}
                        onClick={() => setActiveTab('all')}
                    >
                        Все товары
                    </button>
                    <button
                        className={`tab ${activeTab === 'merch' ? 'active' : ''}`}
                        onClick={() => setActiveTab('merch')}
                    >
                        Мерч
                    </button>
                    <button
                        className={`tab ${activeTab === 'discount' ? 'active' : ''}`}
                        onClick={() => setActiveTab('discount')}
                    >
                        Скидки
                    </button>
                    <button
                        className={`tab ${activeTab === 'services' ? 'active' : ''}`}
                        onClick={() => setActiveTab('services')}
                    >
                        Услуги
                    </button>
                </div>
            </div>

            <div className="rewards-grid">
                {filteredRewards.map((item) => (
                    <div key={item.id} className={`reward-card ${item.stock === 0 ? 'out-of-stock' : ''}`}>
                        <div className="reward-image">
                            {item.image.startsWith('http') ? (
                                <img src={item.image} alt={item.name} className="emoji-img" style={{ width: '60%', height: '60%', objectFit: 'contain' }} />
                            ) : (
                                <span className="emoji-img">{item.image}</span>
                            )}
                            {item.stock === 0 && <span className="stock-badge sold-out">Раскуплено</span>}
                            {item.stock > 0 && item.stock <= 5 && <span className="stock-badge low-stock">Осталось {item.stock}!</span>}
                        </div>

                        <div className="reward-info">
                            <span className="category-tag"><Tag size={12} /> {item.category === 'merch' ? 'Мерч' : item.category === 'discount' ? 'Скидка' : 'Услуга'}</span>
                            <h3>{item.name}</h3>

                            <div className="reward-footer">
                                <div className={`price ${userPoints >= item.price ? 'affordable' : 'too-expensive'}`}>
                                    <Zap size={16} /> {item.price} баллов
                                </div>

                                <button
                                    className="btn btn-primary"
                                    disabled={item.stock === 0 || userPoints < item.price}
                                >
                                    {item.stock === 0 ? 'Нет в наличии' : 'Купить'}
                                </button>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Rewards;
