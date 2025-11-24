
# 🖼️ **Image Metadata Extraction with Python** {#image-metadata-extraction}

---
## 📌 Table of Contents

- [Image Metadata Extraction with Python](#image-metadata-extraction)
- [Introduction to Metadata](#introduction-to-metadata)
- [Understanding EXIF Format](#understanding-exif-format)
- [Python Environment & Required Libraries](#python-environment-and-required-libraries)
- [Extracting EXIF Metadata](#extracting-exif-metadata)
- [Retrieving Specific Fields](#retrieving-specific-fields)
- [Converting GPS to Decimal Degrees](#converting-gps-to-decimal-degrees)
- [Mapping Coordinates with ipyleaflet](#mapping-coordinates-with-ipyleaflet)
- [Images Without Metadata](#images-without-metadata)
- [Removing Metadata](#removing-metadata)


---

# 📘 **Introduction to Metadata** {#introduction-to-metadata}

Metadata is *“data about data”*.  
For images, metadata describes:
- Location where the photo was taken  
- Date & time of capture  
- Camera model & settings  
- GPS coordinates  
- Exposure and brightness data  

Digital cameras and smartphones automatically embed metadata using the **EXIF** standard.

> Example: A selfie contains the exact latitude & longitude of where you took it.

---

# 🗂️ **Understanding EXIF Format** {#understanding-exif-format}

**EXIF (Exchangeable Image File Format)** is the standard for embedding metadata inside image files such as `.jpg`, `.jpeg`, `.tiff`.

### EXIF can store:
- **DateTime**
- **Camera model**
- **Exposure, brightness**
- **GPS information**
- **Orientation, resolution**

When using online-shared images, EXIF is often removed during compression or uploading.

---

# 🐍 **Python Environment & Required Libraries** {#python-environment-and-required-libraries}

Recommended environment: **Google Colab** or **Jupyter Notebook**.

### Required Libraries
```python
pip install ipyleaflet
```

* **Pillow (PIL)** → image processing & EXIF extraction
* **IPython.display** → shows images in notebook
* **ipyleaflet** → interactive maps
* **ExifTags** → dictionary mapping numeric EXIF tags to readable names

---

# 🔍 **Extracting EXIF Metadata** {#extracting-exif-metadata}

### Function to extract metadata

```python
def get_exif(filename):
    exif_data = {}
    image = Image.open(filename)
    info = image._getexif()
    
    if info:
        for tag, value in info.items():
            decoded = ExifTags.TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for gps_tag in value:
                    sub_decoded = ExifTags.GPSTAGS.get(gps_tag, gps_tag)
                    gps_data[sub_decoded] = value[gps_tag]
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value

    return exif_data
```

### Sample usage

```python
exif_data = get_exif("/content/image1.jpg")
print(exif_data)
```

This returns a **dictionary** containing all metadata.

---

# 🕰️ **Retrieving Specific Fields** {#retrieving-specific-fields}

Example: Extracting the **date and time the picture was taken**

```python
exif_data['DateTime']
```

Example output:

```
"2023:02:22 12:37:55"
```

---

# 🧭 **Converting GPS to Decimal Degrees** {#converting-gps-to-decimal-degrees}

EXIF GPS values come as:

* **Degrees**
* **Minutes**
* **Seconds**

But modern systems (OpenStreetMap, Google Maps) require **Decimal Degrees (DD)**.

### Conversion Formula

$$
DD = degrees + \frac{minutes}{60} + \frac{seconds}{3600}
$$

### Python conversion function

```python
def gps_extract(exif_dict):
    gps_metadata = exif_dict['GPSInfo']

    lat_ref_num = 1 if gps_metadata['GPSLatitudeRef'] == 'N' else -1
    lat_list = [float(num) for num in gps_metadata['GPSLatitude']]
    lat_coordinate = (lat_list[0] + lat_list[1]/60 + lat_list[2]/3600) * lat_ref_num

    long_ref_num = 1 if gps_metadata['GPSLongitudeRef'] == 'E' else -1
    long_list = [float(num) for num in gps_metadata['GPSLongitude']]
    long_coordinate = (long_list[0] + long_list[1]/60 + long_list[2]/3600) * long_ref_num

    return (lat_coordinate, long_coordinate)
```

---

# 🗺️ **Mapping Coordinates with ipyleaflet** {#mapping-coordinates-with-ipyleaflet}

### Steps:

1. Convert EXIF GPS to decimal degrees
2. Set the map center
3. Add a marker

### Code:

```python
center = gps_extract(exif_data)

m = Map(center=center, zoom=15)
marker = Marker(location=center, draggable=False)
m.add_layer(marker)
m
```

This plots your photo’s location on an interactive map.

---

# 🖼️ **Images Without Metadata** {#images-without-metadata}

Online images **often have metadata stripped**.

Example:

```python
get_exif("/content/image2.png")
```

Output:

```
{}
```

Reasons:

* Uploaded to web platforms
* Shared multiple times
* Compressed by social media
* Manual metadata removal

---

# 🧹 **Removing Metadata** {#removing-metadata}

### Why remove metadata?

* Privacy
* Prevent tracking
* Avoid leaking location or device information

### Metadata removal with Pillow

```python
img = Image.open('/content/image1.jpg')
img.save('image1_no_metadata.jpg')
get_exif('image1_no_metadata.jpg')
```

New file has **no EXIF data**.

---
