from ultralytics import YOLO
import numpy as np

def main():
    model = YOLO('yolo11n.pt')

    results = model.val(
        data='coco.yaml',
        imgsz=640,
        batch=1,
        device=0,
        save_json=True,
        verbose=True
    )

    print('\n--- YOLOv11n Evaluation Metrics ---')
    print(f"mAP@0.5:0.95: {results.box.map:.4f}")
    print(f"mAP@0.5: {results.box.map50:.4f}")
    print(f"mAP@0.75: {results.box.map75:.4f}")
    print(f"Precision (mean): {results.box.mp:.4f}")
    print(f"Recall (mean): {results.box.mr:.4f}")

    f1_array = results.box.f1
    mean_f1 = np.mean(f1_array) if f1_array.size > 0 else 0.0
    print(f"F1 score (mean): {mean_f1:.4f}")

    print(f"Total Parameters: {sum(p.numel() for p in model.model.parameters())/1e6:.2f}M")
    print(f"Inference Speed (ms/image): {results.speed['inference']:.2f}")
    print(f"Postprocess Speed (ms/image): {results.speed['postprocess']:.2f}")

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
