from ultralytics import YOLO

# Load a model
model = YOLO('cone-detector.pt') 

while True:
    result = model(source=1, show=True, conf=0.4)
    print(result)