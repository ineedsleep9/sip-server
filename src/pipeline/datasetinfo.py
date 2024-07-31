import json

eval_file = './src/pipeline/dataset.json'
data = []

fallcnt = 0
adlcnt = 0

for i in range(1, 71):
    groundtruth = ''
    add = ''
    file_path = "./data/Annotation_files/video_(" + str(i) + ").txt"

    with open(file_path, "r") as f:
        s = f.readlines()

    try:
        if 'Fall' in s[0]:
            groundtruth = "Fall"
        elif('ADL' in s[0] or int(s[0]) == 0):
            groundtruth = "ADL"
        else:
            groundtruth = "Fall"
    except:
        groundtruth = "ADL"

    if(groundtruth == "Fall"):
        fallcnt += 1
    else:
        adlcnt += 1

    start = -1
    end = -1
    try:
        if(groundtruth == 'Fall'):
            if(s[0] == 'Fall\n'):
                start = int(s[1][:-1])
                end = int(s[2][:-1])
            else:
                start = int(s[0][:-1])
                end = int(s[1][:-1])
    except:
        start = -1
        end = -1

    f.close()
    
    dict1 = {
        "id": i,
        "filepath": file_path,
        "location": "Coffee Room",
        "original_location": "Le2i Dataset",
        "groundtruth": groundtruth,
        "fall_start_frame": start,
        "fall_end_frame": end,
        "point_of_view": "Wall-Mounted Camera",
        "action": groundtruth
    }

    data.append(dict1)

for i in range(71, 131):
    groundtruth = ''
    add = ''
    file_path = "./data/Annotation_files/video_(" + str(i) + ").txt"

    with open(file_path, "r") as f:
        s = f.readlines()

    try:
        if 'Fall' in s[0]:
            groundtruth = "Fall"
        elif('ADL' in s[0] or int(s[0]) == 0):
            groundtruth = "ADL"
        else:
            groundtruth = "Fall"
    except:
        groundtruth = "ADL"

    if(groundtruth == "Fall"):
        fallcnt += 1
    else:
        adlcnt += 1
    start = -1
    end = -1
    try:
        if(groundtruth == 'Fall'):
            if(s[0] == 'Fall\n'):
                start = int(s[1][:-1])
                end = int(s[2][:-1])
            else:
                start = int(s[0][:-1])
                end = int(s[1][:-1])
    except:
        start = -1
        end = -1

    f.close()
    
    dict1 = {
        "id": i,
        "filepath": file_path,
        "location": "Home",
        "original_location": "Le2i Dataset",
        "groundtruth": groundtruth,
        "fall_start_frame": start,
        "fall_end_frame": end,
        "point_of_view": "Wall-Mounted Camera",
        "action": groundtruth
    }

    data.append(dict1)

for i in range(131, 191):
    groundtruth = ''
    file_path = "./data/Annotation_files/video_(" + str(i) + ").txt"

    with open(file_path, "r") as f:
        s = f.readlines()

    pov = 'Camera 1 (Birds\' Eye View)'
    if(i % 2 == 1):
        pov = 'Camera 0 (Side/Front/Ground Level View)'

    try:
        if 'Fall' in s[0]:
            groundtruth = "Fall"
        elif('ADL' in s[0] or int(s[0]) == 0):
            groundtruth = "ADL"
        else:
            groundtruth = "Fall"
    except:
        groundtruth = "ADL"
    
    if(groundtruth == 'ADL'):
        start = -1
        end = -1
    else:
        start = None
        end = None
    
    f.close()

    dict1 = {
        "id": i,
        "filepath": file_path,
        "location": "Workspace",
        "original_location": "UR Dataset",
        "groundtruth": groundtruth,
        "fall_start_frame": start,
        "fall_end_frame": end,
        "point_of_view": pov,
        "action": groundtruth
    }

    data.append(dict1)

for i in range(191, 231):
    groundtruth = ''
    file_path = "./data/Annotation_files/video_(" + str(i) + ").txt"

    with open(file_path, "r") as f:
        s = f.readlines()

    pov = 'Camera 1 (Birds\' Eye View)'
    if(i % 2 == 1):
        pov = 'Camera 0 (Side/Front/Ground Level View)'

    try:
        if 'Fall' in s[0]:
            groundtruth = "Fall"
        elif('ADL' in s[0] or int(s[0]) == 0):
            groundtruth = "ADL"
        else:
            groundtruth = "Fall"
    except:
        groundtruth = "ADL"

    if(groundtruth == 'ADL'):
        start = -1
        end = -1
    else:
        start = None
        end = None

    f.close()

    dict1 = {
        "id": i,
        "filepath": file_path,
        "location": "Workspace",
        "original_location": "UR Dataset",
        "groundtruth": groundtruth,
        "fall_start_frame": start,
        "fall_end_frame": end,
        "point_of_view": pov,
        "action": groundtruth
    }

    data.append(dict1)

for i in range(231, 281):
    groundtruth = ''
    file_path = "./data/Annotation_files/video_(" + str(i) + ").txt"
    subject = i % 10
    if(subject == 0):
        subject = 10

    with open(file_path, "r") as f:
        s = f.readlines()
    
    act = 'Backwards Fall'

    if(i > 240):
        act = 'Forward Fall'
    if(i > 250):
        act = 'Left Fall'
    if(i > 260):
        act = 'Right Fall'
    if(i > 270):
        act = 'Sitting Fall'

    try:
        if 'Fall' in s[0]:
            groundtruth = "Fall"
        elif('ADL' in s[0] or int(s[0]) == 0):
            groundtruth = "ADL"
        else:
            groundtruth = "Fall"
    except:
        groundtruth = "ADL"

    if(groundtruth == 'ADL'):
        start = -1
        end = -1
    else:
        start = None
        end = None

    f.close()

    dict1 = {
        "id": i,
        "filepath": file_path,
        "location": "Room",
        "person": "Subject " + str(subject),
        "original_location": "CAUCAFall Dataset",
        "groundtruth": groundtruth,
        "fall_start_frame": start,
        "fall_end_frame": end,
        "point_of_view": "Wall-Mounted Camera",
        "action": act
    }

    data.append(dict1)

for i in range(281, 331):
    groundtruth = ''
    file_path = "./data/Annotation_files/video_(" + str(i) + ").txt"
    subject = i % 10
    if(subject == 0):
        subject = 10
    
    with open(file_path, "r") as f:
        s = f.readlines()

    act = 'Hop'

    if(i > 290):
        act = 'Kneel'
    if(i > 300):
        act = 'Pick Up Object'
    if(i > 310):
        act = 'Sit Down'
    if(i > 320):
        act = 'Walk'

    try:
        if 'Fall' in s[0]:
            groundtruth = "Fall"
        elif('ADL' in s[0] or int(s[0]) == 0):
            groundtruth = "ADL"
        else:
            groundtruth = "Fall"
    except:
        groundtruth = "ADL"

    if(groundtruth == 'ADL'):
        start = -1
        end = -1
    else:
        start = None
        end = None

    f.close()

    dict1 = {
        "id": i,
        "filepath": file_path,
        "location": "Room",
        "person": "Subject " + str(subject),
        "original_location": "CAUCAFall Dataset",
        "groundtruth": groundtruth,
        "fall_start_frame": start,
        "fall_end_frame": end,
        "point_of_view": "Wall-Mounted Camera",
        "action": act
    }

    data.append(dict1)

with open(eval_file, 'w') as outfile:
    json.dump(data, outfile, indent=4)