# Installation Guide

This guide will help you install CDE550-sim on your system.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/Nsfr750/CDE550-sim.git
cd CDE550-sim
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python main.py --version
```

## Updating

To update to the latest version:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## Troubleshooting

If you encounter any issues during installation, please check the [Troubleshooting Guide](./troubleshooting.md) or [open an issue](https://github.com/Nsfr750/CDE550-sim/issues).
