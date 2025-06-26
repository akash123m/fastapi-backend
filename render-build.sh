#!/bin/bash

# Remove any conflicting google package
pip uninstall -y google || true

# Install dependencies explicitly
pip install fastapi uvicorn python-dotenv google-generativeai
