#!/bin/bash

# Build des images
docker image build ./Authentication -t authentication_test:latest
docker image build ./Authorization -t authorization_test:latest
docker image build ./Content -t content_test:latest

# Lancement du docker-compose
docker-compose up -d --build
