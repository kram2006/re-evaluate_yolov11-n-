# YOLOv11n Repository

A repository containing the YOLOv11n pretrained model and validation scripts for evaluating object detection performance on the COCO 2017 dataset.

## Overview

This repository includes:
- **yolo11n.pt** — Pretrained YOLOv11n model weights
- **validate_yolov11n.py** — Validation and evaluation script
- **COCO 2017 Dataset** — Images, labels, and annotations (≈56–57 GB)
- **Detection Results** — Output from detection/validation runs
- **Python Virtual Environment** — Pre-configured dependencies

## Repository Structure

```
├── validate_yolov11n.py       # Main validation/evaluation script
├── yolo11n.pt                 # Pretrained model weights
├── datasets/coco/             # COCO 2017 dataset (~56-57 GB)
│   ├── images/
│   │   ├── train2017/         # Training images
│   │   ├── val2017/           # Validation images
│   │   └── test2017/          # Test images (if available)
│   ├── labels/                # Annotation labels
│   └── annotations/
│       └── instances_val2017.json  # COCO evaluation annotations
├── runs/detect/               # Detection/validation output directories
│   └── val/predictions.json   # Example prediction output
├── yolo_env/                  # Python virtual environment
└── README.md                  # This file
```

## COCO 2017 Dataset Information

**Location:** `datasets/coco/`  
**Size:** Approximately 56–57 GB on disk  
**Contents:**
- Training images: `images/train2017/`
- Validation images: `images/val2017/`
- Test images: `images/test2017/` (if present)
- Label files: `labels/` (YOLO format)
- Evaluation annotations: `annotations/instances_val2017.json`
- Split lists: `train2017.txt`, `val2017.txt`, `test-dev2017.txt`

## Managing the Dataset

### When You Can Delete the Dataset

You can safely remove the `datasets/coco/` directory if you have:
- Backed up the annotations folder (`annotations/`) for future COCO evaluations, OR
- Saved prediction JSON files from previous runs (`runs/detect/*/predictions.json`) for re-evaluation

**Note:** COCO evaluation primarily uses annotations and predictions rather than raw images.

### Dataset Removal Options

#### Option 1: Move to External Storage (Recommended)

```powershell
# Create destination folder first
Move-Item -Path .\datasets\coco -Destination D:\backup\coco -Force
```

#### Option 2: Compress to Archive

```powershell
# Creates coco.zip in the current directory
Compress-Archive -Path .\datasets\coco -DestinationPath .\coco.zip -Force
```

#### Option 3: Permanent Deletion

```powershell
# WARNING: This is irreversible. Backup first!
Remove-Item -LiteralPath .\datasets\coco -Recurse -Force
```

Alternative using `rd` command:
```cmd
rd /s /q datasets\coco
```

⚠️ **Warning:** Deletion is permanent unless you have backups or Recycle Bin recovery enabled. Always verify backups before deleting.

## Re-downloading COCO 2017

If you need to restore the dataset, download from the official COCO website:

- **Training images:** http://images.cocodataset.org/zips/train2017.zip
- **Validation images:** http://images.cocodataset.org/zips/val2017.zip
- **Test images:** http://images.cocodataset.org/zips/test2017.zip
- **Annotations:** http://images.cocodataset.org/annotations/annotations_trainval2017.zip

Extract files into `datasets/coco/` to maintain consistent script paths.

## Usage

### 1. Activate the Virtual Environment

**Using PowerShell (Windows):**
```powershell
.\yolo_env\Scripts\Activate.ps1
```

**Using Command Prompt (cmd):**
```cmd
.\yolo_env\Scripts\activate.bat
```

### 2. Run Validation

```powershell
python validate_yolov11n.py
```

**Common arguments:**
- `--data` — Path to dataset (default: `datasets/coco`)
- `--weights` — Path to model weights (default: `yolo11n.pt`)
- See script help for additional options: `python validate_yolov11n.py --help`

### 3. View Results

Validation outputs are saved to `runs/detect/` directory:
- Predictions: `runs/detect/val/predictions.json`
- Metrics and visualizations in respective subdirectories

## Dependencies

- **Python Version:** 3.10+ (from included virtual environment)
- **Environment:** Pre-configured in `yolo_env/`

### Recreate Dependencies

If you need to rebuild the environment:

```powershell
# Activate the virtual environment first
.\yolo_env\Scripts\Activate.ps1

# Generate requirements.txt from current packages
pip freeze > requirements.txt

# Or install from an existing requirements.txt
pip install -r requirements.txt
```

## Evaluation Without Images

If you've deleted the dataset but retained predictions and annotations, you can still:
1. Compute evaluation metrics using `runs/detect/*/predictions.json`
2. Compare predictions against `annotations/instances_val2017.json`
3. Generate COCO evaluation reports without raw images

This is useful for long-term storage and model comparison workflows.

## Next Steps

- Review `validate_yolov11n.py` for available options and customization
- Archive or delete the dataset if disk space is a concern
- Create a `requirements.txt` if you need to share this environment
- Refer to [YOLOv11 Documentation](https://docs.ultralytics.com/models/yolov11/) for advanced usage

---

**Last Updated:** 2026-06-09  
**Model:** YOLOv11n (Nano)  
**Dataset:** COCO 2017 Validation
