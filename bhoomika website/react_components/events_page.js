import React from 'react';
import './EventsPage.css'; // Import CSS file

const Navbar = () => {
    return (
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="#" onClick={() => window.history.back()}>Back</a></li>
            </ul>
        </nav>
    );
}

const ImageGrid = ({ images }) => {
    return (
        <div className="image-grid">
            {images.map((image, index) => (
                <div key={index} className="image-item">
                    <img src={image.src} alt={image.alt} />
                    <div className="overlay">
                        <h3>{image.title}</h3>
                        <p>{image.description}</p>
                    </div>
                </div>
            ))}
        </div>
    );
}

const RegisterButton = () => {
    return (
        <button className="register-button">
            <a href="/registration.html">Register</a>
        </button>
    );
}

const EventsPage = () => {
    const images = [
        { src: 'zub.jpg', alt: 'Event 1', title: 'Event 1 Title', description: 'Description of Event 1' },
        // Add more image objects as needed
    ];

    return (
        <div>
            <Navbar />
            <ImageGrid images={images} />
            <RegisterButton />
        </div>
    );
}

export default EventsPage;
