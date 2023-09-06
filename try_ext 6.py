try:
    f=open("demofile.txt","W")
    try:
        f.write("Los Santos")
    except:
        print("something went wrong")
    finally:
        f.close()
except:
    print("nothing went wrong")