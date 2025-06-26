#!/bin/bash

# Force uninstall the broken dummy 'google' package
pip uninstall -y google || true
pip uninstall google google-api-python-client google-cloud -y
pip install google-generativeai
# Install everything cleanly and explicitly
pip install --no-cache-dir fastapi uvicorn python-dotenv google-generativeai==0.3.2

