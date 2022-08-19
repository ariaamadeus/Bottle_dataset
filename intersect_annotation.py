import os

def intersect(home_path):
    annotations = os.listdir(home_path+"/Annotations")

    for i,annotation in enumerate(annotations):
        annotations[i] = annotations[i][:-4]
    txtann = []
    with open (home_path+"/ImageSets/Main/trainval.txt",'r') as f:
        txtann = f.read().split('\n')[:-1]
    
    newann = [value for value in annotations if value in txtann]

    text = ""
    for ann in newann:
        text += ann
        text += '\n'

    print(text)
    with open (home_path+"/ImageSets/Main/trainval.txt",'w') as f:
        print(text)
        f.write(text)

    #`print(annotations.intersection(ann))

if __name__ == "__main__":
    intersect('.')
