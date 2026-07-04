@echo off
REM Launch the Streamlit app using the project virtual environment.
cd /d %~dp0
echo Using Python: %~dp0.venv\Scripts\python.exe
".venv\Scripts\python.exe" -c "import sys, sklearn; print('Python:', sys.executable); print('scikit-learn:', sklearn.__version__)"
".venv\Scripts\streamlit.exe" run app.py
pause
