***ChatGPT Work Logger Automation System***
1. Project Overview
The ChatGPT Work Logger Automation System is designed to automatically capture project-related work performed through ChatGPT, store it locally, generate professional daily summaries using a Large Language Model (LLM), and automatically update a Google Sheet for daily task tracking.
The system eliminates manual task-sheet preparation by automatically converting technical discussions, implementation work, debugging activities, research efforts, and project planning conversations into structured daily reports.

2. Objective
The objective of this system is to:
1	Capture project-related ChatGPT conversations automatically.
2	Store conversation history locally.
3	Generate professional work summaries.
4	Upload daily work reports into a Google Sheet.
5	Maintain a centralized task tracking mechanism.
6	Reduce manual effort in preparing daily status reports.

3. System Architecture
ChatGPT
   ↓
Chrome Extension
   ↓
Flask Backend API
   ↓
SQLite Database
   ↓
LLM model
   ↓
Daily Report Generator
   ↓
Google Apps Script
   ↓
Google Sheet

4. Component Description
4.1 Chrome Extension
Purpose:
1	Monitors ChatGPT conversations.
2	Extracts project-related messages.
3	Sends conversations to backend.
Functions:
1	Capture conversation content.
2	Filter project-related discussions.
3	Send conversation payload to Flask API.

4.2 Flask Backend
Purpose:
1	Receives conversation data.
2	Stores conversations into SQLite.
Endpoint:
POST /save_chat
Responsibilities:
1	Accept JSON payload.
2	Store timestamp.
3	Store title.
4	Store conversation content.

4.3 SQLite Database
1	Maintain local history.
2	Enable report generation.

4.4 Daily Report Generator
1	Fetch conversations for current day.
2	Remove duplicates.
3	Filter project-specific work.
4	Generate report.
Process:
SQLite
   ↓
Filter Conversations
   ↓
Combine Text
   ↓
Generate Summary

4.5 LLM Summarization Module
Responsibilities:
1	Analyze captured conversations.
2	Generate professional task summaries.
3	Ignore irrelevant discussions.
4	Produce concise work reports.
Output Example:
1. Researched RAG and Hybrid RAG architectures.
2. Evaluated vectorless retrieval approaches.
3. Investigated FAISS indexing methods.
4. Implemented ChatGPT work logging system.

4.6 Google Apps Script
1	Receive task details.
2	Append rows.
3	Maintain reporting format.

4.7 Google Sheet Integration
Example:
Sr No	Task Details	Start Date	End Date	Member
1	Researched Hybrid RAG	2026-06-10	2026-06-10	Pooja

4.8 Windows Task Scheduler
Process:
6 PM
 ↓
scheduler.py
 ↓
daily_report.py
 ↓
Google Sheet Update

7. Features
Implemented:
1	Automatic conversation capture.
2	SQLite storage.
3	Local report generation.
4	LLM summarization.
5	Google Sheet integration.
6	Scheduled execution.
7	Project keyword filtering.

9. Benefits
1	Eliminates manual reporting.
2	Maintains daily project history.
3	Produces professional summaries.
4	Improves task tracking.
5	Supports project documentation.
6	Useful for appraisals and reviews.
7	Provides centralized work monitoring.

9. Conclusion
The ChatGPT Work Logger Automation System successfully automates the complete lifecycle of work tracking by capturing ChatGPT project discussions, storing them locally, generating AI-powered summaries using LLM model, and updating Google Sheets automatically on a scheduled basis. This enables efficient and consistent project documentation with minimal manual effort.
