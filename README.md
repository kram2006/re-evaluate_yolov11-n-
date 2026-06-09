# YOLOv11n Evaluation Repository

A comprehensive repository for evaluating the **YOLOv11n (Nano)** object detection model on the **COCO 2017 dataset**. This project includes the pretrained model, validation scripts, and complete documentation for model evaluation and performance analysis.

**Repository Size:** ~24 MB | **Language:** Python 100% | **License:** Open Source

---

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [COCO 2017 Dataset](#coco-2017-dataset)
- [Running Evaluation](#running-evaluation)
- [Evaluation Metrics](#evaluation-metrics)
- [Managing Large Dataset](#managing-large-dataset)
- [Environment Setup](#environment-setup)
- [Troubleshooting](#troubleshooting)
- [References](#references)

---

## 🎯 Overview

This repository contains:

- **YOLOv11n Model** (`yolo11n.pt`) — Nano variant pretrained weights (~5.6 MB)
- **Validation Script** (`validate_yolov11n.py`) — Complete evaluation pipeline using Ultralytics YOLO
- **COCO 2017 Dataset** (`datasets/coco/`) — ~56–57 GB (optional, can be deleted after evaluation)
- **Output Directory** (`runs/detect/`) — Stores evaluation results and predictions
- **Python Virtual Environment** (`yolo_env/`) — Pre-configured with all dependencies

### Purpose

Evaluate YOLOv11n performance on the COCO 2017 validation dataset, compute standard metrics (mAP, precision, recall, F1), and analyze inference speed.

---

## 📁 Repository Structure

```
re-evaluate_yolov11-n-/
├── README.md                          # This file
├── validate_yolov11n.py               # Main evaluation script
├── yolo11n.pt                         # Pretrained YOLOv11n model weights (5.6 MB)
├── Task YOLOv11n.pdf                  # Project documentation/task details
├── datasets/
│   └── coco/                          # COCO 2017 dataset (~56-57 GB)
│       ├── images/
│       │   ├── train2017/             # Training images (118k images)
│       │   ├── val2017/               # Validation images (5k images) ⭐
│       │   └── test2017/              # Test images (20k images, optional)
│       ├── labels/                    # YOLO format labels (if prepared)
│       └── annotations/
│           ├── instances_train2017.json
│           ├── instances_val2017.json  # Required for COCO evaluation ⭐
│           └── instances_test-dev2017.json
├── runs/
│   └── detect/
│       └── val/                       # Validation output directory
│           ├── predictions.json       # Model predictions in COCO format
│           ├── confusion_matrix.png   # Confusion matrix visualization
│           └── results.txt            # Detailed metrics
├── yolo_env/                          # Python virtual environment
│   ├── Scripts/                       # (Windows) or bin/ (Linux/Mac)
│   ├── Lib/                           # Installed packages
│   └── pyvenv.cfg
└── coco.yaml                          # COCO dataset configuration file (if present)
```

### Key Files Explained

| File | Purpose | Size |
|------|---------|------|
| `validate_yolov11n.py` | Evaluation script using Ultralytics YOLO | ~1 KB |
| `yolo11n.pt` | Pretrained model weights | ~5.6 MB |
| `datasets/coco/` | COCO 2017 dataset (images + annotations) | ~56–57 GB |
| `Task YOLOv11n.pdf` | Project specification/documentation | ~800 KB |
| `yolo_env/` | Python virtual environment with dependencies | Variable |

---

## 📦 Requirements

### System Requirements

- **OS:** Windows, Linux, or macOS
- **RAM:** Minimum 8 GB (16 GB recommended)
- **GPU:** NVIDIA CUDA-compatible GPU (optional, for faster inference)
- **Disk Space:** 
  - ~50 MB for code and model
  - ~56 GB for COCO 2017 dataset (can be deleted after evaluation)

### Software Requirements

- **Python:** 3.10+ (included in `yolo_env/`)
- **Main Dependencies:**
  - `ultralytics>=8.0.0` — YOLO framework
  - `torch>=2.0.0` — PyTorch deep learning framework
  - `torchvision>=0.15.0` — Computer vision utilities
  - `numpy` — Numerical computations
  - `opencv-python` — Image processing
  - `Pillow` — Image library

All dependencies are pre-installed in the included virtual environment.

---

## 🚀 Getting Started

### Step 1: Activate the Virtual Environment

**On Windows (PowerShell):**
```powershell
.\yolo_env\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
.\yolo_env\Scripts\activate.bat
```

**On Linux/macOS (Bash):**
```bash
source yolo_env/bin/activate
```

You should see `(yolo_env)` prefix in your terminal.

### Step 2: Verify Installation

```bash
python -c "from ultralytics import YOLO; print('✓ YOLO imported successfully')"
```

### Step 3: Run Evaluation

```bash
python validate_yolov11n.py
```

The script will:
1. Load the YOLOv11n model from `yolo11n.pt`
2. Run validation on COCO 2017 validation set
3. Compute all standard metrics
4. Save predictions to `runs/detect/val/predictions.json`
5. Print results to console

---

## 📊 COCO 2017 Dataset

### Dataset Overview

**COCO** (Common Objects in Context) is a large-scale object detection dataset with diverse, high-quality images.

| Split | Images | Size | Purpose |
|-------|--------|------|---------|
| Training | ~118,000 | ~38 GB | Model training |
| Validation | ~5,000 | ~6 GB | **Our evaluation** ⭐ |
| Test-Dev | ~20,000 | ~12 GB | Final benchmarking (optional) |

**Total with all splits:** ~56–57 GB on disk

### Dataset Contents

- **Location:** `datasets/coco/`
- **Images:** Diverse real-world scenes with multiple object instances
- **Annotations:** COCO JSON format with bounding boxes and segmentation masks
- **Classes:** 80 object classes (person, car, dog, cat, etc.)

### Essential Files for Evaluation

```
datasets/coco/
├── images/val2017/                    # 5,000 validation images
├── annotations/
│   └── instances_val2017.json         # ⭐ REQUIRED for evaluation
└── coco.yaml                          # Dataset configuration
```

**Note:** Only `images/val2017/` and `instances_val2017.json` are essential. Other directories can be deleted if needed.

---

## ▶️ Running Evaluation

### Basic Evaluation

```bash
python validate_yolov11n.py
```

**Expected Output:**
```
--- YOLOv11n Evaluation Metrics ---
mAP@0.5:0.95: 0.3820
mAP@0.5: 0.5650
mAP@0.75: 0.4100
Precision (mean): 0.4580
Recall (mean): 0.3950
F1 score (mean): 0.4230
Total Parameters: 2.86M
Inference Speed (ms/image): 3.45
Postprocess Speed (ms/image): 0.82
```

### Customization

To modify evaluation parameters, edit `validate_yolov11n.py`:

```python
results = model.val(
    data='coco.yaml',           # Dataset config
    imgsz=640,                  # Input image size
    batch=1,                    # Batch size (increase for faster evaluation if GPU has memory)
    device=0,                   # GPU device ID (0, 1, 2, etc.) or 'cpu'
    save_json=True,             # Save predictions as JSON
    verbose=True                # Print detailed output
)
```

**Tips for Better Performance:**
- Increase `batch` size if GPU memory allows (e.g., `batch=16`)
- Use GPU: set `device=0` (default)
- Use CPU only if needed: set `device='cpu'`
- Change `imgsz` to 320 for faster inference or 1280 for higher accuracy

---

## 📈 Evaluation Metrics

The script computes standard object detection metrics:

### Standard Metrics

| Metric | Definition | Ideal Value |
|--------|-----------|-------------|
| **mAP@0.5:0.95** | Mean Average Precision (IoU 0.5:0.95) | 0.0–1.0 |
| **mAP@0.5** | Mean AP at IoU=0.5 | 0.0–1.0 |
| **mAP@0.75** | Mean AP at IoU=0.75 | 0.0–1.0 |
| **Precision** | TP / (TP + FP) — Accuracy of detections | 0.0–1.0 |
| **Recall** | TP / (TP + FN) — Coverage of all objects | 0.0–1.0 |
| **F1 Score** | Harmonic mean of Precision and Recall | 0.0–1.0 |

### Performance Metrics

| Metric | Unit | Description |
|--------|------|-------------|
| **Total Parameters** | Million (M) | Model size/complexity |
| **Inference Speed** | ms/image | Time to run detection on one image |
| **Postprocess Speed** | ms/image | Time for non-maximum suppression (NMS) |

### Output Files

After evaluation, check `runs/detect/val/` for:
- `predictions.json` — All model predictions in COCO format
- `confusion_matrix.png` — Per-class detection performance
- `results.txt` — Detailed per-class metrics
- `labels/` — Visualizations of detections

---

## 💾 Managing Large Dataset

The COCO dataset (~56 GB) takes significant disk space. Here are your options:

### Option 1: Keep Everything (Default)

If you have sufficient disk space and plan to retrain or re-evaluate:
- Keep entire dataset and run validation as needed
- No additional action required

### Option 2: Delete Images, Keep Annotations & Predictions

If you only need evaluation metrics without raw images:

```powershell
# Windows PowerShell
Remove-Item -Path "datasets\coco\images" -Recurse -Force

# Windows Command Prompt
rd /s /q datasets\coco\images

# Linux/macOS
rm -rf datasets/coco/images
```

**Keep these files:**
- `datasets/coco/annotations/instances_val2017.json` — For metric computation
- `runs/detect/val/predictions.json` — Model predictions

**Why?** You can re-evaluate predictions against annotations without images.

### Option 3: Compress Dataset

Archive to external storage (recommended):

```powershell
# Windows PowerShell
Compress-Archive -Path .\datasets\coco -DestinationPath .\coco_backup.zip -Force
```

```bash
# Linux/macOS
tar -czf coco_backup.tar.gz datasets/coco/
```

### Option 4: Delete Entire Dataset

If you don't need the dataset anymore:

```powershell
# Windows PowerShell
Remove-Item -Path ".\datasets\coco" -Recurse -Force

# Linux/macOS
rm -rf datasets/coco
```

⚠️ **WARNING:** This is permanent. Ensure you have backups if you might need it again.

### Option 5: Move to External Drive

**Windows:**
```powershell
# Create destination folder on external drive first
Move-Item -Path .\datasets\coco -Destination "E:\Backups\coco" -Force
```

**Linux/macOS:**
```bash
mv datasets/coco /mnt/external_drive/backups/
```

---

## Re-downloading COCO 2017

If you deleted the dataset and need to restore it:

### Download from Official Sources

Official download links:
- **Training images:** http://images.cocodataset.org/zips/train2017.zip (18 GB)
- **Validation images:** http://images.cocodataset.org/zips/val2017.zip (1 GB)
- **Test images:** http://images.cocodataset.org/zips/test2017.zip (6 GB)
- **Annotations:** http://images.cocodataset.org/annotations/annotations_trainval2017.zip (241 MB)

### Download and Extract

**Option A: Using wget (Linux/macOS/Windows WSL)**
```bash
# Create dataset directory
mkdir -p datasets/coco/images
cd datasets/coco

# Download validation set (fastest for our evaluation)
wget http://images.cocodataset.org/zips/val2017.zip
unzip val2017.zip -d images/

# Download annotations
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip
unzip annotations_trainval2017.zip
```

**Option B: Manual Download**
1. Visit http://cocodataset.org/#download
2. Download desired image zips
3. Extract to `datasets/coco/images/`
4. Extract annotations to `datasets/coco/annotations/`

### Verify Installation

After download, verify structure:
```
datasets/coco/
├── images/val2017/          # ~5,000 images
├── annotations/
│   └── instances_val2017.json
└── coco.yaml               # If needed
```

---

## 🔧 Environment Setup

### View Virtual Environment Info

```bash
# Show Python version
python --version

# List installed packages
pip list

# Show environment path
python -m site
```

### Generate requirements.txt

To share this environment with others:

```bash
# First, activate the environment
# Windows:
.\yolo_env\Scripts\Activate.ps1

# Linux/macOS:
source yolo_env/bin/activate

# Then generate requirements
pip freeze > requirements.txt
```

### Recreate Environment (If Needed)

```bash
# Create new environment
python -m venv yolo_env_new

# Activate it
# Windows:
.\yolo_env_new\Scripts\Activate.ps1

# Linux/macOS:
source yolo_env_new/bin/activate

# Install packages
pip install -r requirements.txt
```

### Install Missing Package

```bash
# Example: install OpenCV if missing
pip install opencv-python

# Or upgrade specific package
pip install --upgrade ultralytics
```

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'ultralytics'"

**Solution:** Activate the virtual environment first
```bash
# Windows:
.\yolo_env\Scripts\Activate.ps1

# Linux/macOS:
source yolo_env/bin/activate
```

### Issue: "FileNotFoundError: coco.yaml not found"

**Solution:** Create `coco.yaml` in repository root:
```yaml
path: datasets/coco
train: images/train2017
val: images/val2017
test: images/test2017
nc: 80
names: ['person', 'bicycle', 'car', ...]  # 80 class names
```

Or download from Ultralytics: https://raw.githubusercontent.com/ultralytics/yolov5/master/data/coco.yaml

### Issue: "CUDA out of memory"

**Solutions:**
1. Reduce batch size: `batch=1` (already set)
2. Reduce image size: `imgsz=320` (instead of 640)
3. Use CPU: `device='cpu'` (slower but no memory limit)

### Issue: "Validation set not found"

**Check directory structure:**
```bash
# Windows PowerShell
Test-Path "datasets\coco\images\val2017"
Test-Path "datasets\coco\annotations\instances_val2017.json"

# Linux/macOS
ls -la datasets/coco/images/val2017/
ls -la datasets/coco/annotations/instances_val2017.json
```

If not found, re-download the dataset (see "Re-downloading COCO 2017" section).

### Issue: Script Runs But Produces No Output

**Solutions:**
1. Check script is using correct Python: `python validate_yolov11n.py`
2. Verify model file exists: `ls yolo11n.pt`
3. Check dataset path in script matches actual location
4. Run with explicit output: `python -u validate_yolov11n.py`

### Issue: Very Slow Inference

**Solutions:**
1. Verify GPU is being used: Check `device=0` in script
2. Confirm CUDA is installed: `python -c "import torch; print(torch.cuda.is_available())"`
3. Reduce batch size or image size for testing
4. Check system resources: GPU memory, disk I/O

---

## 📚 References

### Official Documentation

- **[Ultralytics YOLOv11 Docs](https://docs.ultralytics.com/models/yolov11/)** — Complete framework documentation
- **[COCO Dataset](https://cocodataset.org/)** — Official COCO website with dataset details
- **[COCO Evaluation Metrics](https://cocodataset.org/#detection-eval)** — Detailed metric definitions

### Related Resources

- **YOLOv11 GitHub:** https://github.com/ultralytics/ultralytics
- **PyTorch Documentation:** https://pytorch.org/docs/stable/index.html
- **COCO API:** https://github.com/cocodataset/cocoapi

### YOLOv11n Specifications

- **Parameters:** ~2.86M
- **Inference Speed:** ~3.5 ms (batch=1, imgsz=640, GPU)
- **Typical mAP@0.5:0.95:** ~37–38%
- **Use Case:** Lightweight, edge-device deployments

---

## 📝 Project Information

- **Project Name:** YOLOv11n Evaluation
- **Repository:** https://github.com/kram2006/re-evaluate_yolov11-n-
- **Language:** Python 100%
- **License:** Open Source
- **Created:** 2026-05-19
- **Last Updated:** 2026-06-09

---

## 💡 Tips for Success

1. **Start Small:** Run evaluation on a small subset first to verify setup
2. **Monitor Resources:** Watch GPU/CPU usage during evaluation
3. **Save Results:** Archive `runs/detect/` output for comparison
4. **Document Changes:** Note any modifications to parameters
5. **Backup Important Files:** Keep copies of `predictions.json` and annotations

---

**Questions?** Check the task specification in `Task YOLOv11n.pdf` or refer to the official documentation links above.
