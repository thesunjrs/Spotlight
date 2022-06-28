"""This program copies Microsoft Spotlight Images directly to Spotlight
                    Directory in Pictures Directory.

                    - Written from Scratch by
                            Gagan Gulyani

"""


try:
    
    import os
    import os.path
    import shutil
    import time

    try:
        from PIL import Image

    except ImportError:
        print ("\nInstall Pillow Image Library to run the Script")

    src=os.path.expanduser("~")+r"\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
    src=src.replace("\\","/")
    dest=os.path.expanduser("~")+"\\Pictures\\Spotlight"


    if not os.path.exists(dest):
        os.makedirs(dest)
    if not os.path.exists(f"{dest}/Portraits"):
        os.makedirs(f"{dest}/Portraits")

    count_existing=count_new=0

    for i in os.listdir(src):
        current_image = f"{src}/{i}"
        portrait = f"{dest}/Portraits/{i}"
        landscape = f"{dest}/{i}"

        im = Image.open(current_image)
        width, height = im.size

        if (
            os.path.exists(portrait)
            or os.path.exists(landscape)
            or os.path.exists(f"{portrait}.jpg")
            or os.path.exists(f"{landscape}.jpg")
        ):
            count_existing+=1

        elif width in [1920, 1080]:
                
            if width<height:
                print(f"\nTransfering {i} of dimensions {width}x{height} in {dest}/Portraits")
                shutil.copy2(current_image, f"{dest}/Portraits")
                print("Size :",os.path.getsize(portrait))
                os.rename(portrait, f"{portrait}.jpg")

            else:
                print(f"\nTransfering {i} of dimensions {width}x{height} in {dest}")
                shutil.copy2(current_image,dest)
                print ("Size :",os.path.getsize(landscape))
                os.rename(landscape, f"{landscape}.jpg")

            count_new+=1

    print(
        "*" * 35
        + f"\n{count_existing} image(s) already exists.\n\n{count_new} New images copied in Spotlight Directory."
    )

    print ("\nOperation Completed Successfully!\n"+"*"*35)


except Exception as e:
    logs=os.path.expanduser("~")+"\\Pictures\\Spotlight\\logs.txt"

    if os.path.exists(logs):
        f=open(logs,"a")
    else:
        f=open(logs,"a")
        f.write("="*75+"\n\nError Logs of the Wallpaper Setter by GG\n\n"+"="*75+"\n")

    t = f'\nDate : {time.strftime("%H:%M:%S", time.gmtime())}\nTime : {time.strftime("%d-%m-%Y", time.gmtime())}'


    report = "="*75+"\n\n"+t+"\n\n"+"Error Message : "+str(e)+"\n\n"+"="*75+"\n"+"\n"+"="*15+"Finished"+"="*15+"\n"

    print (report)

    f.write(report)

    f.close()
    

