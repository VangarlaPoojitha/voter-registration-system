# 🗳️ Voter Registration System

A simple FastAPI-based voter registration platform with age eligibility checking, password hashing, search, and pagination features.

## Features
- ✅ **Age Eligibility Check** - Only 18+ years allowed
- 🔒 **Password Hashing** - Secure password storage
- 🔍 **Search Functionality** - Search by name or email
- 📄 **Pagination** - Browse voters in pages
- 📊 **Statistics** - Total voters and average age
- 🗂️ **Sorting** - Sort by name, age, or registration date

## Quick Start

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the application:**
```bash
python main.py
```

3. **Open browser:** http://127.0.0.1:8000

## Voter Registration Fields
- Full Name
- Email Address
- Age (must be 18+)
- Phone Number
- Full Address
- Password (securely hashed)

## API Endpoints
- `POST /voters` - Register new voter
- `GET /voters` - Get all voters (with search/pagination)
- `DELETE /voters/{id}` - Delete voter
- `GET /stats` - Get voter statistics

## Database
Uses SQLite database (`voters.db`) - automatically created on first run.

## Security Features
- Age validation (rejects under 18)
- Password hashing with SHA-256
- Email validation
- Unique email constraint