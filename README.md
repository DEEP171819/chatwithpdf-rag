# Chat with PDF using RAG

<div align="center">

## Retrieval-Augmented Generation Application using Local LLMs

A beginner-friendly yet production-structured Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask natural language questions about their content using local Large Language Models powered by Ollama.

---

### Built With

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-Orchestration-green?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-orange?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-LocalLLM-black?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow?style=for-the-badge)

</div>

---

# Table of Contents

- [Introduction](#introduction)
- [Project Objectives](#project-objectives)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [RAG Workflow](#rag-workflow)
- [Project Structure](#project-structure)
- [Installation Guide](#installation-guide)
- [Ollama Setup](#ollama-setup)
- [Running the Application](#running-the-application)
- [How the Project Works](#how-the-project-works)
- [Core Components](#core-components)
- [Example Workflow](#example-workflow)
- [Sample Queries](#sample-queries)
- [Configuration Details](#configuration-details)
- [Error Handling](#error-handling)
- [Future Improvements](#future-improvements)
- [Interview Questions](#interview-questions)
- [Resume Description](#resume-description)
- [License](#license)

---

# Introduction

This project demonstrates a complete Retrieval-Augmented Generation (RAG) pipeline using fully open-source and free technologies.

The application enables users to:

- Upload PDF documents
- Extract and process document text
- Generate semantic embeddings
- Store embeddings in a vector database
- Perform semantic similarity search
- Ask natural language questions
- Generate context-aware answers using a local Large Language Model

The entire system runs locally without requiring any paid APIs or cloud-based AI services.

---

# Project Objectives

The primary objective of this project is to demonstrate understanding of:

- Retrieval-Augmented Generation (RAG)
- Vector embeddings
- Semantic search
- Vector databases
- Local LLM inference
- LangChain orchestration
- PDF document processing
- Streamlit application development

This project is especially suitable for:

- AI/ML beginners
- Portfolio projects
- Internship applications
- GenAI learning
- Resume projects
- Academic demonstrations

---

# Features

## Core Features

- PDF upload interface
- PDF text extraction
- Recursive text chunking
- Semantic embeddings generation
- ChromaDB vector storage
- Semantic similarity search
- Local LLM integration with Ollama
- Question-answering interface
- Fully offline execution
- Persistent vector storage

## Technical Features

- Modular code architecture
- Error handling
- Beginner-friendly implementation
- Lightweight local deployment
- Open-source technology stack
- Persistent vector database
- Scalable project structure

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Streamlit | Frontend interface |
| LangChain | RAG orchestration |
| ChromaDB | Vector database |
| Ollama | Local LLM runtime |
| HuggingFace Embeddings | Semantic embeddings |
| PyPDF | PDF text extraction |
| Sentence Transformers | Embedding generation |

---

# System Architecture

```text
                        ┌─────────────────────┐
                        │     Streamlit UI    │
                        └──────────┬──────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │      LangChain RAG       │
                    │      Orchestration       │
                    └──────────┬───────────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
              ▼                                 ▼
     ┌─────────────────┐              ┌─────────────────┐
     │    ChromaDB     │              │     Ollama      │
     │   Vector Store  │              │    Local LLM    │
     └─────────────────┘              └─────────────────┘

