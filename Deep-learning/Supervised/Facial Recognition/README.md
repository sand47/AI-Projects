# Dependience 

- Opencv 
- Glib 
- face_recognition library 


# Usage

Create a folder named datasets and add each persons image in it. For better accurary add 200 plus image per each person with different background conditions. 

# Data Preprocessing 

Make sure your image data is not big as you cannot train it thus the resize_image.py code will resize all the image fron the given folder to 640x480 

# Data Collection

```
python data_collect.py --cascade haarcascade_frontalface_default.xml --output dataset/kannan
```
# Training 

```
python encode_faces.py --dataset dataset --encodings encodings.pickle
```

# Inference 

```
python inference_from_image.py --encodings encodings.pickle --image examples/example_01.png
```
