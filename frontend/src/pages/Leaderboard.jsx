import React from 'react';
import { Trophy, Medal, Award, Search } from 'lucide-react';
import './Leaderboard.css';

const Leaderboard = () => {
    // Mock data representing top users
    const topUsers = [
        { id: 2, rank: 2, name: 'EcoQueen', points: 4200, avatar: 'E' },
        { id: 1, rank: 1, name: 'GreenHero99', points: 5100, avatar: 'G' },
        { id: 3, rank: 3, name: 'PlanetSaver', points: 3850, avatar: 'P' },
    ];

    const otherUsers = [
        { id: 4, rank: 4, name: 'RecycleBot', points: 3200, avatar: 'R' },
        { id: 5, rank: 5, name: 'TreeHugger', points: 2900, avatar: 'T' },
        { id: 6, rank: 6, name: 'OceanCleanup', points: 2850, avatar: 'O' },
        { id: 7, rank: 7, name: 'LeafyGreen', points: 2700, avatar: 'L' },
        { id: 8, rank: 8, name: 'EcoWarrior_99', points: 1250, avatar: 'E', isCurrentUser: true }
    ];

    return (
        <div className="leaderboard-container">
            <div className="leaderboard-header">
                <h1>Глобальный Рейтинг</h1>
                <p>Соревнуйтесь с другими: сортируйте больше всех и займите первое место!</p>

                <div className="search-bar">
                    <Search size={20} className="search-icon" />
                    <input type="text" placeholder="Поиск эко-героев..." />
                </div>
            </div>

            <div className="top-three-podium">
                {topUsers.map((user, index) => (
                    <div key={user.id} className={`podium-stand position-${user.rank}`}>
                        <div className="podium-avatar">
                            <div className="avatar-circle">{user.avatar}</div>
                            {user.rank === 1 && <Trophy className="rank-icon gold" size={28} />}
                            {user.rank === 2 && <Medal className="rank-icon silver" size={24} />}
                            {user.rank === 3 && <Award className="rank-icon bronze" size={24} />}
                        </div>
                        <div className="podium-info">
                            <h3>{user.name}</h3>
                            <p className="points">{user.points} очков</p>
                        </div>
                        <div className={`podium-base base-${user.rank}`}>
                            <span className="rank-number">{user.rank}</span>
                        </div>
                    </div>
                ))}
            </div>

            <div className="leaderboard-list card">
                {otherUsers.map((user) => (
                    <div key={user.id} className={`list-row ${user.isCurrentUser ? 'current-user-row' : ''}`}>
                        <div className="row-rank">
                            <span>{user.rank}</span>
                        </div>
                        <div className="row-user">
                            <div className="small-avatar">{user.avatar}</div>
                            <span className="user-name">{user.name}</span>
                        </div>
                        <div className="row-points">
                            {user.points} очков
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Leaderboard;
