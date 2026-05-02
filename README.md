# API Load Testing with Python (Threading)

This project is a simple load testing tool built in Python using threading, designed to evaluate the performance and limits of a Django REST API developed as part of a personal SaaS inventory system.

## ⚠️ Disclaimer
This project is for educational and testing purposes only.  
It is intended to be used only on systems owned or authorized by the developer.  
No malicious use is intended.

---

## 🧠 Context

I developed a SaaS inventory system using:

- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication

This tool is used to analyze how the API behaves under concurrent requests and stress conditions.

---

## 🚀 Testing Methods

### 🔹 GET Requests
Used to test read performance and response time of API endpoints under concurrent access.

### 🔹 POST Requests
Used to evaluate how the system handles concurrent creation of resources in the database.

---

## 🧵 Concurrency

The tests simulate multiple users using Python threading to generate simultaneous requests.

---

## 🎯 Goal

- Measure API stability under load
- Detect performance bottlenecks
- Observe behavior under concurrent usage
- Improve backend robustness
