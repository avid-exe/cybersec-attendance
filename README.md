# CyberSec Attendance System

A modern, glassmorphic Flask web application designed for tracking student attendance in the Cybersecurity Department with seamless Google Sheets integration and real-time synchronization.

## 🎯 Purpose

The CyberSec Attendance System is built to streamline the collection and management of student data within the Cybersecurity Department. It provides an intuitive interface for students to record their attendance while automatically syncing all data to Google Sheets for easy access and analysis by department staff.

## ✨ Key Features

### 🎨 Modern UI Design
- **Glassmorphic Interface**: Beautiful, modern design with frosted glass effects that enhance user experience
- **Responsive Layout**: Fully responsive design that works seamlessly across desktop, tablet, and mobile devices
- **Intuitive Navigation**: Clean and simple interface designed specifically for students

### 📊 Data Management
- **Google Sheets Integration**: Automatic synchronization of attendance data to Google Sheets
- **Real-time Sync**: Instant data updates ensure information is always current
- **Persistent Storage**: All attendance records are securely stored and easily accessible

### 🔐 Security & Authentication
- **OAuth2 Authentication**: Secure authentication using OAuth2Client for Google Sheets access
- **Data Privacy**: Student information is handled securely and stored with appropriate permissions

### ⚡ Performance
- **Fast Response Times**: Optimized Flask backend ensures quick data processing
- **Reliable Deployment**: Hosted on Render with Gunicorn for production-grade reliability

## 👥 Target Users

This application is designed primarily for **students** in the Cybersecurity Department who need to:
- Record their attendance for classes and events
- Submit their information quickly and easily
- Access the system from any device

Department staff benefit from:
- Centralized attendance data in Google Sheets
- Real-time visibility of attendance records
- Easy export and analysis capabilities

## 🛠️ Technology Stack

### Frontend
- **HTML5**: Semantic markup for structured content
- **CSS3**: Custom styling with glassmorphism effects

### Backend
- **Python**: Core programming language
- **Flask**: Lightweight web framework for handling routes and requests
- **gspread**: Python library for Google Sheets integration
- **oauth2client**: OAuth 2.0 authentication for Google APIs

### Deployment
- **Gunicorn**: Production-grade WSGI HTTP server
- **Render**: Cloud platform for hosting and deployment

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Google Cloud account with Sheets API enabled
- OAuth2 credentials for Google Sheets access

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cybersec-attendance.git
cd cybersec-attendance
```

2. Install dependencies:
```bash
pip install flask gspread oauth2client gunicorn
```

3. Set up Google Sheets API credentials:
   - Create a project in Google Cloud Console
   - Enable Google Sheets API
   - Download OAuth2 credentials
   - Place credentials file in the project directory

4. Configure environment variables:
```bash
export GOOGLE_SHEETS_CREDENTIALS=path/to/credentials.json
export SPREADSHEET_ID=your_spreadsheet_id
```

5. Run the application:
```bash
# Development
python app.py

# Production
gunicorn app:app
```

## 📱 Usage

1. **Access the Application**: Navigate to the deployment URL
2. **Submit Attendance**: Fill in the required student information fields
3. **Confirm Submission**: Receive confirmation that your data has been recorded
4. **Automatic Sync**: Data is automatically synced to the connected Google Sheet

## 🔧 Configuration

The application can be configured through environment variables or a configuration file:

- `SPREADSHEET_ID`: The ID of your Google Sheet
- `WORKSHEET_NAME`: Name of the specific worksheet (default: 'Sheet1')
- `FLASK_ENV`: Set to 'production' or 'development'

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues, questions, or suggestions, please contact avid.jys@gmail.com

## 🙏 Acknowledgments

- Built for the Cybersecurity Department
- Designed with student experience in mind
- Powered by Google Sheets for seamless data management

---


