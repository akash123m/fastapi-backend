#!/bin/bash

# Force uninstall the broken dummy 'google' package
pip uninstall -y google || true

# Install everything cleanly and explicitly
pip install --no-cache-dir fastapi uvicorn python-dotenv google-generativeai
