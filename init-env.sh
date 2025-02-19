#!/bin/bash

echo "Initializing environment variables!"
echo "Creating .env ..."
cp -n sample.env .env
echo "Creating .env.dev ..."
cp -n sample.env .env.dev
echo "Complete."
