# Changelog

All notable changes to this project will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.1.0] - 2025-04-11
### Added
- Initial project structure and README
- UML diagrams created for architecture and workflow
- LICENSE added (CC BY-NC-ND 4.0)
- Changelog markdown created

## [0.2.0] - 2025-04-13 
### Added
- `fetch_from_api.py` to ingest historical and daily price data and fundamentals
- Fundamentals versioning using daily snapshots with change detection
- `upload_to_s3.py` for structured S3 syncing with SHA-256 hash tracking
- Logging of uploaded files to `upload_log.txt`
- Folder structure under `/prices/` and `/fundamentals/`

### Improved
- Replaced redundant `.json` export logic with `.csv` append + dedup
- Switched from filename-based sync to content-aware upload mechanism

### Notes
- All upload logic uses least-privilege IAM user and profile-based auth
