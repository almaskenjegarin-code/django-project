import React, { useState } from 'react';
import { Map as MapIcon, Filter, Navigation, Info } from 'lucide-react';
import './Locations.css';

const Locations = () => {
    const [activeFilter, setActiveFilter] = useState('all');

    // Mock data for locations
    const locations = [
        { id: 1, name: 'Central Park Bin', type: 'plastic', distance: '0.8 km', active: true },
        { id: 2, name: 'Downtown Recycling Center', type: 'all', distance: '2.1 km', active: true },
        { id: 3, name: 'Westside Glass Collection', type: 'glass', distance: '3.5 km', active: false },
        { id: 4, name: 'University Paper Bin', type: 'paper', distance: '1.2 km', active: true },
    ];

    const filteredLocations = activeFilter === 'all'
        ? locations
        : locations.filter(loc => loc.type === activeFilter || loc[`accepts_${activeFilter}`]);

    return (
        <div className="locations-container">
            <div className="locations-header">
                <h1>Найти эко-контейнеры</h1>
                <p>Найдите ближайшие пункты приема для сдачи отсортированных отходов.</p>
            </div>

            <div className="locations-layout">
                <div className="sidebar">
                    <div className="filters card">
                        <h3>Фильтры</h3>
                        <div className="filter-chips">
                            <button
                                className={`chip ${activeFilter === 'all' ? 'active' : ''}`}
                                onClick={() => setActiveFilter('all')}
                            >
                                Все пункты
                            </button>
                            <button
                                className={`chip ${activeFilter === 'plastic' ? 'active' : ''}`}
                                onClick={() => setActiveFilter('plastic')}
                            >
                                Пластик
                            </button>
                            <button
                                className={`chip ${activeFilter === 'glass' ? 'active' : ''}`}
                                onClick={() => setActiveFilter('glass')}
                            >
                                Стекло
                            </button>
                            <button
                                className={`chip ${activeFilter === 'paper' ? 'active' : ''}`}
                                onClick={() => setActiveFilter('paper')}
                            >
                                Макулатура
                            </button>
                        </div>
                    </div>

                    <div className="location-list card">
                        <h3>Поблизости <span className="badge-count">{locations.length}</span></h3>
                        <div className="list-items">
                            {locations.map((loc) => (
                                <div key={loc.id} className="loc-card">
                                    <div className="loc-info">
                                        <h4>{loc.name}</h4>
                                        <p className="loc-meta">
                                            <span className={`status-dot ${loc.active ? 'active' : 'inactive'}`}></span>
                                            {loc.active ? 'Доступно' : 'Заполнен / Ремонт'} • {loc.distance}
                                        </p>
                                    </div>
                                    <button className="btn-icon">
                                        <Navigation size={18} />
                                    </button>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>

                <div className="map-view card">
                    {/* Placeholder for 2GIS Map */}
                    <div className="map-placeholder">
                        <MapIcon size={64} className="map-icon-bg" />
                        <p>Здесь будет интерактивная карта 2GIS</p>
                        <button className="btn btn-primary">
                            <Navigation size={18} /> Включить геолокацию
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Locations;
