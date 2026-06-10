#!/bin/bash
source venv/Scripts/activate
python currency-manager/app.py &
python data-manager/app.py &
python gateway/app.py &
wait