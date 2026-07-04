# IPL Match Prediction Project

## Run the app

Use the project virtual environment and the included Streamlit executable:

```powershell
cd "c:\Users\SANGRAM DAS\OneDrive\Desktop\ipl_match_prediction_project"
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Or use the helper batch file:

```powershell
run_app.bat
```

## Requirements

Dependencies are pinned in `requirements.txt`, including:
- `streamlit==1.58.0`
- `scikit-learn==1.6.1`

These versions match the `pipe.pkl` model and prevent the `_RemainderColsList` pickle loading error.
