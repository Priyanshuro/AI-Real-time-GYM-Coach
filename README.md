# AI Gym Trainer 💪

An AI-powered fitness application that uses computer vision to track workout exercises, count repetitions, and provide real-time feedback on exercise performance. The application aims to help users perform workouts more effectively with camera-based exercise monitoring.

## 🚀 Features

- **Real-Time Pose Detection:** Uses MediaPipe and OpenCV to detect human body landmarks.
- **Automatic Rep Counting:** Tracks exercise movements and counts repetitions.
- **Multiple Exercise Detection:** Supports exercises such as squats, push-ups, biceps curls, shoulder presses, and lunges, depending on the implemented detectors.
- **Workout Feedback:** Provides feedback based on detected body positions and movement thresholds.
- **Interactive Web Interface:** Built using Streamlit for a simple and user-friendly experience.
- **Audio Feedback:** Provides voice-based workout feedback if enabled in the application.
- **Workout Tracking:** Uses SQLite for storing application data, if configured.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend / UI:** Streamlit
- **Computer Vision:** OpenCV
- **Pose Estimation:** MediaPipe
- **Numerical Processing:** NumPy
- **Database:** SQLite
- **Version Control:** Git and GitHub

## 📂 Project Structure

```text
AI-Gym-Trainer/
├── core/
├── detectors/
│   ├── squat.py
│   ├── pushup.py
│   ├── biceps_curl.py
│   ├── shoulder_press.py
│   └── lunges.py
├── ml_models/
├── services/
├── static/
├── main.py
├── data.db
├── requirements.txt
└── README.md
```

*Note: The listed detector filenames and features should match the files and functionality actually present in your project.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Replace the placeholders with your actual GitHub repository URL and project folder name.

### 2. Create a Virtual Environment

```bash
python -m venv gym_trainer_env
```

Activate the environment on Windows:

```bash
gym_trainer_env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run main.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

Allow camera access if the application requests it.

## 🏋️ How to Use

1. Start the application using Streamlit.
2. Allow camera access when prompted.
3. Select an available exercise.
4. Position yourself so your body is visible to the camera.
5. Perform the exercise and follow the displayed feedback.
6. Track repetitions and review the feedback provided by the application.

## 🔧 Configuration

- Check `requirements.txt` for the required Python packages.
- Ensure your webcam is connected and accessible.
- Review exercise thresholds in the corresponding detector files if you need to adjust movement detection.
- Ensure database initialization is configured before using features that require SQLite.

## 🔮 Future Enhancements

- More exercise types and improved pose detection.
- Exercise form scoring and posture correction.
- Personalized workout plans.
- Workout history and progress visualization.
- User authentication and personalized profiles.
- Improved voice coaching and performance analytics.

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## 👨‍💻 Author

**Priyanshu Singh**

Computer Science and Engineering

Bundelkhand Institute of Engineering & Technology, Jhansi

## 📄 License

This project is available for educational and personal learning purposes. Add an appropriate open-source license if you intend to distribute it publicly.
