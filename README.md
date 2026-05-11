# Frontend and Backend Communication using AWS EC2

This project demonstrates multiple ways to establish communication between a Frontend application and a Python Flask Backend hosted on AWS EC2 instances.

The project covers:

- Direct Browser to Backend communication
- Nginx Reverse Proxy communication
- Flask Frontend to Flask Backend communication using private IPs

---

# Project Architecture

## 1. Direct Browser → Backend Communication

In this architecture, the frontend directly communicates with the backend using the backend EC2 public IP address.

### Flow

Browser → Frontend → Backend Public IP

### Features

- Simple setup
- Easy for learning and testing
- Backend accessible publicly

### Limitations

- Requires CORS configuration
- Backend publicly exposed
- Less secure for production

---

# 2. Nginx Reverse Proxy Communication

In this architecture, the frontend communicates with Nginx running on the frontend EC2 instance. Nginx internally forwards requests to the backend EC2 private IP.

### Flow

Browser → Frontend EC2 (Nginx) → Backend EC2 Private IP

### Features

- Backend hidden from the public internet
- Secure internal VPC communication
- No CORS issues
- Recommended for production environments

### Benefits

- Improved security
- Better scalability
- Professional deployment architecture

---

# 3. Flask Frontend → Flask Backend Communication

In this architecture, the frontend itself is built using Flask. The frontend Flask server communicates internally with the backend Flask server using private IP communication.

### Flow

Browser → Frontend Flask EC2 → Backend Flask EC2

### Features

- Fully Python-based architecture
- Backend remains private
- No CORS required
- Easier API integration

### Benefits

- Secure internal communication
- Clean microservices architecture
- Ideal for Python applications

---

# AWS Infrastructure

## Frontend EC2

Used for:
- Hosting frontend application
- Running Nginx or Flask frontend server

## Backend EC2

Used for:
- Running Flask backend APIs
- Serving application data

---

# Security Group Configuration

## Frontend Security Group

Allow:
- HTTP (Port 80)
- HTTPS (Port 443 if SSL enabled)

## Backend Security Group

Allow:
- Application Port (Example: 3000)
- Source should only be Frontend EC2 Security Group

---

# Technologies Used

- AWS EC2
- Python Flask
- Nginx
- HTML
- CSS
- JavaScript
- REST APIs

---

# Features

- Modern animated frontend UI
- Secure backend communication
- Private IP communication inside AWS VPC
- Reverse proxy support
- Flask API integration
- Interactive button-based API calls

---

# Production Recommendations

For production deployments:

- Use Nginx Reverse Proxy
- Use Private IP communication
- Use Gunicorn for Flask applications
- Configure SSL using HTTPS
- Use Load Balancer if needed
- Store frontend and backend in private/public subnet architecture

---

# Learning Objectives

This project helps understand:

- Frontend and backend integration
- Flask API development
- Reverse proxy configuration
- Internal VPC communication
- AWS EC2 networking
- Security Group configuration
- Production deployment concepts

---

# Recommended Architecture

| Architecture | Usage |
|---|---|
| Direct Browser → Backend | Learning & Testing |
| Nginx Reverse Proxy | Production Recommended |
| Flask Frontend → Backend | Python-Based Applications |

---

# Conclusion

This project demonstrates how frontend and backend services can communicate securely and efficiently using AWS EC2 instances, Flask APIs, Nginx reverse proxy, and internal private IP communication.

It provides a strong foundation for deploying real-world cloud-native applications and microservices architectures on AWS.
