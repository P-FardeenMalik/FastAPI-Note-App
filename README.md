# Notes App (FastAPI)

## Features
- User registration and login (JWT authentication)
- Create, read, update, delete notes
- SQLite database (can be switched to PostgreSQL)
- Simple, secure API

## API Routes

| Method | Path           | Description           |
|--------|----------------|----------------------|
| POST   | /register      | Register user        |
| POST   | /login         | Login user           |
| POST   | /notes         | Create note          |
| GET    | /notes         | List notes           |
| GET    | /notes/{id}    | Get note by ID       |
| PUT    | /notes/{id}    | Update note by ID    |
| DELETE | /note/{id}     | Delete note by ID    |

## Request/Response Example

**Register/Login Request**
```json
{ "username": "user", "password": "pass" }
```
**Login Response**
```json
{ "access_token": "JWT", "token_type": "bearer" }
```
**Create Note Request**
```json
{ "title": "Title", "content": "Content" }
```
**Note Response**
```json
{ "id": 1, "title": "Title", "content": "Content", "created_at": "...", "updated_at": "..." }
```

## DB Schema

- **User:** id, username, hashed_password
- **Note:** id, title, content, created_at, updated_at

## Auth Choice

- JWT: stateless, secure, widely used for APIs

## Failure Mode & Mitigation

- **Race condition on update:** Use `updated_at` timestamp to check for concurrent edits.

## RAG Pipeline 

- Chunk notes, embed with transformer, store in vector DB, retrieve top-k, prompt LLM, evaluate with