# Transify
Transportation based bounty hunting system
Transify: Move Green, Earn Clean
Transify is an innovative web application designed to incentivize sustainable public transportation by rewarding users with crypto tokens on the Solana blockchain. It aims to promote eco-friendly commuting habits while providing an interactive and accessible user experience.

Features
Current Core Features:
User Authentication & Profiles:

Separate registration and login flows for Commuters and Transport Operators.



Automatic generation and display of personal QR codes for commuters.

Commuter Dashboard:

Displays user profile information, current points, and total tokens minted.

Interactive Transmi Travel Guide:

An animated chatbot character ("Transmi") providing travel assistance.

Google Maps Integration: Displays a map showing the user's current location.

Speech Recognition: Allows users to speak their destination.

Voice Response (Text-to-Speech): Transmi provides spoken notifications for instructions and checkpoints.

Real-time Location Tracking: Monitors user's proximity to route checkpoints.

Route Suggestions: Provides public transport routes via Google Maps Directions API, considering traffic and feasibility.

Checkpoint Notifications: Automatically notifies the user via voice when they reach a step/checkpoint on their route.

Phantom Wallet connection (frontend only, for status display).

Leaderboard:

A dedicated page displaying users ranked by their accumulated points.

Basic Operator Interface:

A separate registration page for operators.

A placeholder page for operators to scan user QR codes (functionality to be implemented).

Accessibility Enhancements (Ongoing / Planned):
Enhanced audio and haptic feedback for user interactions.

Accessible route planning (data foundation for locations implemented).

Real-time obstacle alerts, "Meet Me" assistance, and other features for disabled users (planned).

Technologies Used
Backend: Django (Python Web Framework)

Frontend: HTML, CSS (Tailwind CSS for utility-first styling), JavaScript

Database: SQLlite 

APIs:

Google Maps Platform APIs (Maps JavaScript API, Geolocation API, Directions API)

Web Speech API (Browser-native for Speech Recognition and Speech Synthesis)

Other Libraries:

qrcode (Python for QR code generation)

html5-qrcode (JavaScript for QR scanning - for operator side)

Phantom Wallet Browser Extension (for Solana wallet interaction)
