import React from 'react';
import { User, Award, Zap, History, Edit3 } from 'lucide-react';
import './Profile.css';

const Profile = () => {
    // Mock User Data
    const user = {
        username: 'EcoWarrior_99',
        email: 'ecowarrior@example.com',
        level: 5,
        points: 1250,
        rank: 42,
        totalRecycled: 45 // kg
    };

    return (
        <div className="profile-container">
            {/* Header Profile Card */}
            <div className="profile-header-card">
                <div className="profile-avatar-section">
                    <div className="avatar">
                        {user.username.charAt(0)}
                    </div>
                    <div className="profile-info">
                        <h2>{user.username}</h2>
                        <p>{user.email}</p>
                    </div>
                </div>
                <button className="btn btn-secondary btn-edit">
                    <Edit3 size={18} /> Редактировать профиль
                </button>
            </div>

            {/* Stats Grid */}
            <div className="stats-grid">
                <div className="stat-card">
                    <div className="stat-icon bg-green">
                        <Zap size={24} color="white" />
                    </div>
                    <div className="stat-details">
                        <p className="stat-label">Eco-Баллы</p>
                        <p className="stat-value">{user.points}</p>
                    </div>
                </div>

                <div className="stat-card">
                    <div className="stat-icon bg-blue">
                        <Award size={24} color="white" />
                    </div>
                    <div className="stat-details">
                        <p className="stat-label">Текущий рейтинг</p>
                        <p className="stat-value">#{user.rank}</p>
                    </div>
                </div>

                <div className="stat-card">
                    <div className="stat-icon bg-purple">
                        <History size={24} color="white" />
                    </div>
                    <div className="stat-details">
                        <p className="stat-label">Всего сдано (кг)</p>
                        <p className="stat-value">{user.totalRecycled}</p>
                    </div>
                </div>
            </div>

            {/* Recent Activity / Badges */}
            <div className="dashboard-content">
                <div className="activity-feed card">
                    <h3>Последние действия</h3>
                    <ul className="activity-list">
                        <li className="activity-item">
                            <span className="activity-dot bg-green"></span>
                            <div className="activity-text">
                                <p><strong>Сдано 2.5 кг пластика</strong></p>
                                <span className="time">2 часа назад</span>
                            </div>
                            <span className="activity-points">+25 баллов</span>
                        </li>
                        <li className="activity-item">
                            <span className="activity-dot bg-blue"></span>
                            <div className="activity-text">
                                <p><strong>Куплена "Многоразовая кружка"</strong></p>
                                <span className="time">Вчера</span>
                            </div>
                            <span className="activity-points negative">-150 баллов</span>
                        </li>
                        <li className="activity-item">
                            <span className="activity-dot bg-green"></span>
                            <div className="activity-text">
                                <p><strong>Сдано 1.0 кг стекла</strong></p>
                                <span className="time">3 дня назад</span>
                            </div>
                            <span className="activity-points">+10 баллов</span>
                        </li>
                    </ul>
                </div>

                <div className="badges-section card">
                    <h3>Мои достижения</h3>
                    <div className="badges-grid">
                        <div className="badge-item">
                            <div className="badge-icon tier-gold">🥇</div>
                            <p>Герой пластика</p>
                        </div>
                        <div className="badge-item">
                            <div className="badge-icon tier-silver">🥈</div>
                            <p>Мастер стекла</p>
                        </div>
                        <div className="badge-item locked">
                            <div className="badge-icon tier-locked">🔒</div>
                            <p>Спаситель бумаги</p>
                        </div>
                    </div>
                </div>
            </div>
        </div >
    );
};

export default Profile;
