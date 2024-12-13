import settings

if __name__ == '__main__':
    if settings.distro_select():
        print(f"Distro {settings.distro_select()}!")
    else:
        print(f"some text")

